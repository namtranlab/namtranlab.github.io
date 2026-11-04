---
layout: distill
title: Step-by-Step Compilation of VASP (CPU) Incorporating Grand-Canonical Methods on NSCC
description: Instruction for compiling vasp cpu with grand-canonical approach on NSCC
tags: Tutorial
giscus_comments: true
date: 2025-05-4
featured: true
thumbnail: https://github.com/yuanyue-liu-group/CP-VASP/blob/main/CP-VASP.jpg
images:
  lightbox2: true
  photoswipe: true
  spotlight: true
  venobox: true

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU


toc:
  - name: Download packages
    # if a section has subsections, you can add them as follows:
    # subsections:
    #   - name: Example Child Subsection 1
    #   - name: Example Child Subsection 2
  - name: Patch VASPSOL
  - name: Patch VASP-CP
  - name: Load libs
  - name: Modify the makefile
  - name: Installtion
  - name: Vasp script

_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }

---

## Download packages
Assume the vasp source code was downloaded in extracted in ```$HOME/vasp.6.4.0_cp_cpu```

You need the patch ```VASPSOL``` for ```VASP.6.3.0``` and ```VASP-CP```. Those patches can be found in the links below.

- VASPSol:  
    [https://github.com/henniggroup/VASPsol/issues/64](https://github.com/henniggroup/VASPsol/issues/64)

```bash
solvation.F
VASPsol_VASP630.patch
```

- VASP-CP:  
    [https://github.com/yuanyue-liu-group/CP-VASP/](https://github.com/yuanyue-liu-group/CP-VASP/)

```bash
cp-vaspsol.patch
```
***

## Patch VASPSOL

Copy ```solvation.F and VASPsol_VASP630.patch``` to ```src``` folder of vasp source code

```bash
cp solvation.F $HOME/vasp.6.4.0_cp_cpu/src
cp VASPsol_VASP630.patch $HOME/vasp.6.4.0_cp_cpu/src
```
Then execute the patch.

```bash
patch -p0 < VASPsol_VASP630.patch
```
***

## Patch VASP-CP

Copy ```cp-vaspsol.patch``` to ```src``` folder of vasp source code

```bash
cp cp-vaspsol.patch $HOME/vasp.6.4.0_cp_cpu/src
```

Then execute the patch.

```bash
patch -p0 < cp-vaspsol++.patch
```
***

## Load libs

Clean all loaded modules and swap PrgEnv from cray to intel. Default the __MKL__ environment variable __MKLROOT__ will be setup by module file "mkl". The module "mkl" has several version. You can switch it and find the best one for you. Here choose the default version of mkl, which is 2024.0. 

``` bash
module swap PrgEnv-cray PrgEnv-intel
module swap intel intel/2022.1.0
module load mkl
module load cray-hdf5
```
***

## Modify the makefile

Modify the makefile.include as follow.

```bash
# Default precompiler options
CPP_OPTIONS = -DHOST=\"LinuxIFC\" \
              -DMPI -DMPI_BLOCK=8000 -Duse_collective \
              -DscaLAPACK \
              -DCACHE_SIZE=4000 \
              -Davoidalloc \
              -Dvasp6 \
              -Duse_bse_te \
              -Dtbdyn \
              -Dfock_dblbuf \
              -D_OPENMP \
              -Dsol_compat

CPP         = fpp -f_com=no -free -w0  $*$(FUFFIX) $*$(SUFFIX) $(CPP_OPTIONS)

FC          = ftn -qopenmp
FCL         = ftn

FREE        = -free -names lowercase

FFLAGS      = -assume byterecl -w

OFLAG       = -O2
OFLAG_IN    = $(OFLAG)
DEBUG       = -O0

OBJECTS     = fftmpiw.o fftmpi_map.o fftw3d.o fft3dlib.o
OBJECTS_O1 += fftw3d.o fftmpi.o fftmpiw.o
OBJECTS_O2 += fft3dlib.o

# For what used to be vasp.5.lib
CPP_LIB     = $(CPP)
FC_LIB      = $(FC)
CC_LIB      = cc
CFLAGS_LIB  = -O
FFLAGS_LIB  = -O1
FREE_LIB    = $(FREE)

OBJECTS_LIB = linpack_double.o

# For the parser library
CXX_PARS    = CC
LLIBS       = -lstdc++

##
## Customize as of this point! Of course you may change the preceding
## part of this file as well if you like, but it should rarely be
## necessary ...
##

# When compiling on the target machine itself, change this to the
# relevant target when cross-compiling for another architecture
# -xHost will show error for vm or the amd cpu.
FFLAGS     += -O3

# Intel MKL (FFTW, BLAS, LAPACK, and scaLAPACK)
# (Note: for Intel Parallel Studio's MKL use -mkl instead of -qmkl)
FCL        += -qmkl
MKLROOT    ?= /app/apps/oneapi/2024.0/mkl/2024.0
LLIBS      += -L$(MKLROOT)/lib -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_lp64 -liomp5 -lpthread -lm -ldl
# If compile with GNU, use this MKL link flags
#  LLIBS      +=  -m64  -L${MKLROOT}/lib -lmkl_scalapack_lp64 -Wl,--no-as-needed -lmkl_cdft_core -lmkl_intel_lp64 -lmkl_gnu_thread -lmkl_core -lmkl_blacs_intelmpi_lp64 -lgomp -lpthread -lm -ldl
INCS        =-I$(MKLROOT)/include/fftw

# HDF5-support (optional but strongly recommended)
CPP_OPTIONS+= -DVASP_HDF5
HDF5_ROOT  ?= /opt/cray/pe/hdf5/1.12.1.1/INTEL/19.0/lib
LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
INCS       += -I$(HDF5_ROOT)/include

# For the VASP-2-Wannier90 interface (optional)
#CPP_OPTIONS    += -DVASP2WANNIER90
#WANNIER90_ROOT ?= /path/to/your/wannier90/installation
#LLIBS          += -L$(WANNIER90_ROOT)/lib -lwannier

# For the fftlib library (experimental)
#CPP_OPTION += -Dsysv
#FCL         = mpif90 fftlib.o -qmkl
#CXX_FFTLIB  = icpc -qopenmp -std=c++11 -DFFTLIB_USE_MKL -DFFTLIB_THREADSAFE
#INCS_FFTLIB = -I./include -I$(MKLROOT)/include/fftw
#LIBS       += fftlib
```
***

## Installtion

Then install the vasp package with the command below. Remember to change ```N``` in the command.

```bash
make DEPS=1 -jN all
```
***

## Vasp script

The bash script to run vasp can be set as follow.

```bash
#!/bin/bash

#PBS -P <project_id>
#PBS -q normal
#PBS -l select=1:ncpus=128:mem=440gb:mpiprocs=128:ompthreads=1
#PBS -l walltime=24:00:00
#PBS -j oe
#PBS -N <job_name>

cd $PBS_O_WORKDIR

module swap PrgEnv-cray PrgEnv-intel
module swap intel intel/2022.1.0
module load mkl
module load cray-hdf5

export PATH=/path/to/my/vasp/bin:$PATH

mpirun -np 128 --cpu-bind depth -d 1 vasp_std > print-out
```