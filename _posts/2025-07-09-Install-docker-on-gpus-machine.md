---
layout: distill
title: Installing Docker on a GPU Machine
description: Step-by-step Instruction for compiling Docker on a GPU Machine
tags: Tutorial
giscus_comments: true
date: 2025-05-8
featured: true
thumbnail: https://miro.medium.com/v2/resize:fit:720/format:webp/1*9-EDiPjlvT_cwAzRkmTubg.png
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
  - name: Install Docker from a package
    # if a section has subsections, you can add them as follows:
    # subsections:
    #   - name: Example Child Subsection 1
    #   - name: Example Child Subsection 2
  - name: Installing the NVIDIA Container Toolkit
  - name: Configuring Docker
  - name: How to run


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


## Install Docker from a package

1. Go to https://download.docker.com/linux/debian/dists/.

2. Select your Debian version in the list.

3. Go to pool/stable/ and select the applicable architecture (amd64, armhf, arm64, or s390x).

4. Download the following deb files for the Docker Engine, CLI, containerd, and Docker Compose packages:

  - containerd.io_<version>_<arch>.deb
  - docker-ce_<version>_<arch>.deb
  - docker-ce-cli_<version>_<arch>.deb
  - docker-buildx-plugin_<version>_<arch>.deb
  - docker-compose-plugin_<version>_<arch>.deb

5. Install the .deb packages. Update the paths in the following example to where you downloaded the Docker packages.

``` shell
sudo dpkg -i ./containerd.io_<version>_<arch>.deb
sudo dpkg -i ./docker-ce_<version>_<arch>.deb
...
```
6. Verify that the installation is successful by running the hello-world image

``` shell
 sudo service docker start
 sudo docker run hello-world
```
***

## Installing the NVIDIA Container Toolkit

1. Configure the production repository:

``` shell
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

2. Update the packages list from the repository:

``` shell
sudo apt-get update
```

3. Install the NVIDIA Container Toolkit packages:

``` shell
export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
  sudo apt-get install -y \
      nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```
***

## Configuring Docker

1. Create the docker group (if it doesn’t exist)

Check if a docker group exist using
``` shell
getent group docker
```

If it does not exist, then create a new group

``` shell
sudo groupadd docker
```

2. Add your user to the group

``` shell
sudo usermod -aG docker nam
```

3. Configure the container runtime by using the nvidia-ctk command:

``` shell
sudo nvidia-ctk runtime configure --runtime=docker
```

The nvidia-ctk command modifies the /etc/docker/daemon.json file on the host. The file is updated so that Docker can use the NVIDIA Container Runtime.


4. Restart the Docker daemon:

``` shell
sudo systemctl restart docker
```

5. Run a sample CUDA container:

``` shell
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

## How to run

``` shell
docker run -it --rm \
  --gpus all  \
  --runtime=nvidia \
  registry.bohrium.dp.tech/dptech/dp/native/prod-759944/deepmd:dEdN /bin/bash
```