---
layout: distill
title: Step-by-Step Compilation of VASP (CPU) Incorporating Grand-Canonical Methods on NSCC
description: Instruction for compiling vasp cpu with grand-canonical approach on NSCC
tags: Tutorial
giscus_comments: true
date: 2025-05-4
featured: true
thumbnail: https://cmp.univie.ac.at/fileadmin/_processed_/csm_vasp_logo_3956c6ee63.png
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

Clean all loaded modules and load intel oneapi packages.

``` bash
module purge
source /app/apps/oneapi/2022.1.2/setvars.sh
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

FC          = mpiifort -qopenmp
FCL         = mpiifort

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
CC_LIB      = icc
CFLAGS_LIB  = -O
FFLAGS_LIB  = -O1
FREE_LIB    = $(FREE)

OBJECTS_LIB = linpack_double.o

# For the parser library
CXX_PARS    = icpc
LLIBS       = -lstdc++

##
## Customize as of this point! Of course you may change the preceding
## part of this file as well if you like, but it should rarely be
## necessary ...
##

# When compiling on the target machine itself, change this to the
# relevant target when cross-compiling for another architecture
VASP_TARGET_CPU ?= -march=core-avx2
FFLAGS     += $(VASP_TARGET_CPU)

# Intel MKL (FFTW, BLAS, LAPACK, and scaLAPACK)
# (Note: for Intel Parallel Studio's MKL use -mkl instead of -qmkl)
FCL        += -qmkl
MKLROOT    ?= /path/to/your/mkl/installation
LLIBS      += -L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_intelmpi_lp64
INCS        =-I$(MKLROOT)/include/fftw
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

#PBS -N CPU-vasp
#PBS -q normal
#PBS -P personal-vannamtr
#PBS -l select=1:ncpus=128:mpiprocs=64:mem=420G
#PBS -l walltime=1:00:00
#PBS -j oe

# Change directory to the one where the job was submitted
idir=${PBS_O_WORKDIR}
cd $idir
# Set scratch environment

module purge
source /app/apps/oneapi/2022.1.2/setvars.sh

EXECROOT=/home/users/ntu/vannamtr/vasp.6.4.0_cp_cpu/intel_omp

MPIFLAGS='-genv I_MPI_PIN_DOMAIN=omp -genv I_MPI_PIN=yes -genv OMP_NUM_THREADS=4 -genv OMP_STACKSIZE=512m -genv OMP_PLACES=cores -genv OMP_PROC_BIND=close'

time mpirun $MPIFLAGS $EXECROOT/vasp_std > print-out

echo $(date) $PBS_JOBNAME ${PBS_O_WORKDIR} >> ~/LOG
```