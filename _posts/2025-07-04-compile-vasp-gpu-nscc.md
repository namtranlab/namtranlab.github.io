---
layout: distill
title: How to compile VASP GPU (v6.4.0) on NSCC
description: Instruction for compiling vasp gpu on NSCC
tags: Tutorial
giscus_comments: true
date: 2025-05-4
featured: true
thumbnail: https://github.com/deepmodeling/deepmd-kit/raw/master/doc/_static/logo.svg
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
  - name: Load libs
    # if a section has subsections, you can add them as follows:
    # subsections:
    #   - name: Example Child Subsection 1
    #   - name: Example Child Subsection 2
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


## Load libs

Assume the vasp source was downloaded in extracted in $HOME/vasp.6.4.0_gpu

Clean all loaded modules.

``` shell
module purge
```

Load intel mkl lib.

All packages from intel oneapi can be found in ```/app/apps/oneapi/```

In this tutorial we will use version 2022.1.2

``` shell
source /app/apps/oneapi/2022.1.2/mkl/2022.0.2/env/vars.sh
```

Next we need to load the compiler and libs from nvidia hpc skl (nvhpc).

Create a file named ```vasp_nv``` and put it under the vasp source code folder.

Different of nvhpc can be found at ```/app/apps/nvhpc/```. In this tutorial we will use version 22.5 with cuda version of 11.7

```bash
#%Module1.0

# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

conflict nvidia
conflict nvhpc
conflict nvhpc-nompi
conflict nvhpc-byo-compiler

set nvhome /app/apps/nvhpc/22.5
set target Linux_x86_64
set version 22.5

set nvcudadir $nvhome/$target/$version/cuda
set nvcompdir $nvhome/$target/$version/compilers
set nvmathdir $nvhome/$target/$version/math_libs
set nvcommdir $nvhome/$target/$version/comm_libs

setenv NVHPC $nvhome
setenv NVHPC_ROOT $nvhome/$target/$version
setenv CC $nvcompdir/bin/nvc
setenv CXX $nvcompdir/bin/nvc++
setenv FC $nvcompdir/bin/nvfortran
setenv F90 $nvcompdir/bin/nvfortran
setenv F77 $nvcompdir/bin/nvfortran
setenv CPP cpp

prepend-path PATH $nvcudadir/bin
prepend-path PATH $nvcompdir/bin
prepend-path PATH $nvcommdir/mpi/bin
prepend-path PATH $nvcompdir/extras/qd/bin

prepend-path LD_LIBRARY_PATH $nvcudadir/lib64
prepend-path LD_LIBRARY_PATH $nvcudadir/extras/CUPTI/lib64
prepend-path LD_LIBRARY_PATH $nvcompdir/extras/qd/lib
prepend-path LD_LIBRARY_PATH $nvcompdir/lib
prepend-path LD_LIBRARY_PATH $nvmathdir/lib64
prepend-path LD_LIBRARY_PATH $nvcommdir/mpi/lib
prepend-path LD_LIBRARY_PATH $nvcommdir/nccl/lib
prepend-path LD_LIBRARY_PATH $nvcommdir/nvshmem/lib

prepend-path CPATH $nvmathdir/include
prepend-path CPATH $nvcommdir/mpi/include
prepend-path CPATH $nvcommdir/nccl/include
prepend-path CPATH $nvcommdir/nvshmem/include
prepend-path CPATH $nvcompdir/extras/qd/include/qd

prepend-path MANPATH $nvcompdir/man

setenv OPAL_PREFIX $nvcommdir/mpi

setenv NVHPC_PATH               $env(NVHPC_ROOT)
setenv NVHPC_VERSION            $version

setenv CRAY_NVIDIA_PREFIX       $env(NVHPC_ROOT)
setenv CRAY_NVIDIA_VERSION      $version
 

setenv OMP_NUM_THREADS 16
setenv OMP_STACKSIZE 512m
setenv OMP_PLACES cores
setenv OMP_PROC_BIND close


module-whatis "Nvidia HPC Compilers"
```

Then load the packages by:

```bash
module load $HOME/vasp.6.4.0_gpu/vasp_nv
```

***

## Modify the makefile

Modify the makefile.include as follow.

```bash
# Default precompiler options
CPP_OPTIONS = -DHOST=\"LinuxNV\" \
              -DMPI -DMPI_INPLACE -DMPI_BLOCK=8000 -Duse_collective \
              -DscaLAPACK \
              -DCACHE_SIZE=4000 \
              -Davoidalloc \
              -Dvasp6 \
              -Duse_bse_te \
              -Dtbdyn \
              -Dqd_emulate \
              -Dfock_dblbuf \
              -D_OPENMP \
              -D_OPENACC \
              -DUSENCCL \
              -DUSENCCLP2P

CPP         = nvfortran -Mpreprocess -Mfree -Mextend -E $(CPP_OPTIONS) $*$(FUFFIX)  > $*$(SUFFIX)

# N.B.: you might need to change the cuda-version here
#       to one that comes with your NVIDIA-HPC SDK
FC          = mpif90 -acc -gpu=cc60,cc70,cc80,cuda11.7 -mp
FCL         = mpif90 -acc -gpu=cc60,cc70,cc80,cuda11.7 -mp -c++libs

FREE        = -Mfree

FFLAGS      = -Mbackslash -Mlarge_arrays

OFLAG       = -fast

DEBUG       = -Mfree -O0 -traceback

OBJECTS     = fftmpiw.o fftmpi_map.o fftw3d.o fft3dlib.o

LLIBS       = -cudalib=cublas,cusolver,cufft,nccl -cuda

# Redefine the standard list of O1 and O2 objects
SOURCE_O1  := pade_fit.o minimax_dependence.o
SOURCE_O2  := pead.o

# For what used to be vasp.5.lib
CPP_LIB     = $(CPP)
FC_LIB      = nvfortran
CC_LIB      = nvc -w
CFLAGS_LIB  = -O
FFLAGS_LIB  = -O1 -Mfixed
FREE_LIB    = $(FREE)

OBJECTS_LIB = linpack_double.o

# For the parser library
CXX_PARS    = nvc++ --no_warnings

##
## Customize as of this point! Of course you may change the preceding
## part of this file as well if you like, but it should rarely be
## necessary ...
##
# When compiling on the target machine itself , change this to the
# relevant target when cross-compiling for another architecture
VASP_TARGET_CPU ?= -tp host
FFLAGS     += $(VASP_TARGET_CPU)

# Specify your NV HPC-SDK installation (mandatory)
#... first try to set it automatically
NVROOT      =$(shell which nvfortran | awk -F /compilers/bin/nvfortran '{ print $$1 }')

# If the above fails, then NVROOT needs to be set manually
#NVHPC      ?= /opt/nvidia/hpc_sdk
#NVVERSION   = 21.11
#NVROOT      = $(NVHPC)/Linux_x86_64/$(NVVERSION)

## Improves performance when using NV HPC-SDK >=21.11 and CUDA >11.2
#OFLAG_IN   = -fast -Mwarperf
#SOURCE_IN  := nonlr.o

# Software emulation of quadruple precsion (mandatory)
QD         ?= $(NVROOT)/compilers/extras/qd
LLIBS      += -L$(QD)/lib -lqdmod -lqd
INCS       += -I$(QD)/include/qd

# Intel MKL for FFTW, BLAS, LAPACK, and scaLAPACK
MKLROOT    ?= /path/to/your/mkl/installation
LLIBS_MKL   = -Mmkl -L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64
INCS       += -I$(MKLROOT)/include/fftw

# Use a separate scaLAPACK installation (optional but recommended in combination with OpenMPI)
# Comment out the two lines below if you want to use scaLAPACK from MKL instead
#SCALAPACK_ROOT ?= /opt/nvidia/hpc_sdk/Linux_x86_64/23.11/comm_libs/12.3/hpcx/hpcx-2.16/ompi
#LLIBS_MKL   = -L$(SCALAPACK_ROOT)/lib -lscalapack -Mmkl


LLIBS      += $(LLIBS_MKL)
```

***

## Installtion

Then install the vasp package with:

```bash
make DEPS=1 -j4 all
```

***

## Vasp script

The bash script to run vasp can be set as follow.

```bash
#!/bin/bash
#PBS -N JOB_NAME
#PBS -q normal
#PBS -P PROJECT_ID
#PBS -l select=1:ncpus=64:ngpus=4
#PBS -l walltime=24:00:00
#PBS -j oe

# Change directory to the one where the job was submitted
idir=${PBS_O_WORKDIR}
cd $idir/$target

# Set scratch environment
module purge

source /app/apps/oneapi/2022.1.2/mkl/2022.0.2/env/vars.sh
module load $HOME/vasp.6.4.0_gpu/vasp_nv

# VASP path
vasp_exe=$HOME/vasp.6.4.0_gpu/bin/vasp_std

time mpirun -np 4 --mca btl '^openib' --map-by ppr:4:node:PE=16 --bind-to core $vasp_exe > print-out
```