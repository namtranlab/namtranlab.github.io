---
layout: distill
title: Configuration of a Small-Scale High-Performance Computing System – Part I
description: High-Performance Computing Setup – Part I - Network File System and Module Management Configuration
tags: Tutorial
giscus_comments: true
date: 2025-05-2
featured: true
thumbnail: https://as2.ftcdn.net/v2/jpg/04/45/36/25/1000_F_445362578_bfhBkRNUmuZUzi8ur1lNHZwvs7hC2alD.jpg
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
  - name: Config NFS
    # if a section has subsections, you can add them as follows:
    # subsections:
    #   - name: Example Child Subsection 1
    #   - name: Example Child Subsection 2
  - name: Config SLURMN
  - name: Module system

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

## Config NFS

Install ```nfs-kernel-server``` on your head node and ```nfs-common``` on your compute node.

For head node
```bash
apt install nfs-kernel-server
```
For compute node
```bash
apt install nfs-common
```

Configure the shared dir from your head node by modifying ```/etc/exportfs```.

```bash
/opt 192.168.1.0/24(ro,sync,no_subtree_check)
/home 192.168.1.0/24(rw,sync,no_subtree_check)
/scratch 192.168.1.0/24(rw,sync,no_subtree_check)
```
Run the following command to make the settings take effect.

```bash
/sbin/exportfs -ra
``` 


Mount the shared dir in compute node.

```bash
mount j35a:/opt /opt
mount j35a:/home /home 
mount j35a:/scratch /scratch 
```

Setup auto mount by editing ```/etc/fstab```.

On head node we need to auto mount the external hard drive to ```scratch``` folders.
UUID of the external hard drive can be found using ```lsblk -f /dev/sda1```.
```bash
# written by chenxi, for /scratch dirctory
UUID=fd2391a4-72ca-4926-bd1c-8bd0d44a4448 /scratch ext4 defaults 0 2
# written by chenxi, for scratch2
UUID=2cf23a6c-2524-4fa1-963e-4d3465b99008 /scratch2 ext4 defaults 0 2
```

On compute nodes we need to auto mount the shared dirs (opt, home and scratch) from head node (ip:192.168.1.1)
```bash
192.168.1.1:/opt /opt nfs defaults,_netdev 0 0
192.168.1.1:/home /home nfs defaults,_netdev 0 0
192.168.1.1:/scratch /scratch nfs defaults,_netdev 0 0
```


Add user with user id and the same group id. This has to be done on very node (head node an compute nodes)

```bash
/sbin/adduser -u 1002 chenxi
/sbin/adduser -u 1003 nam
/sbin/adduser -u 1004 jianghong

/sbin/adduser -u 1005 guanming
/sbin/adduser -u 1006 chengxi
/sbin/adduser -u 1007 ningwen

/sbin/adduser -u 1008 junbo
/sbin/adduser -u 1009 haoyang
/sbin/adduser -u 1010 choi
```

Create a dir in shared /scratch links for every user and give them permision. This only need to be done on head node.

Example.

```bash
cd /scratch
mkdir chenxi
chown chenxi:chenxi ./chenxi
ln -s /scratch/chenxi /home/chenxi/scratch
```

***


## Config SLURM 

Install slurm using the following command on both head node and compute nodes.
```bash
```sudo apt-get install slurm-wlm```
```

Check slurm status. On head node we need both ```slurmctld``` and ```slurmd```. On compute node we only need ```slurmd``` to run
```bash
sudo systemctl status slurmctld
sudo systemctl status slurmd
```

If not running we can start using
```bash
sudo systemctl start slurmctld
sudo systemctl start slurmd
```

You may want Slurm to auto-start after reboot
```bash
sudo systemctl enable slurmctld
sudo systemctl enable slurmd
```

Edit ```/etc/slurm/slurm.conf``` as following
```bash
ClusterName=LiCPU
ControlMachine=j35a

SlurmUser=slurm
SlurmctldPort=6817
SlurmdPort=6818
AuthType=auth/munge

StateSaveLocation=/var/log/slurm/slurmctld
SlurmdSpoolDir=/var/log/slurm/slurmd
SlurmctldPidFile=/var/log/slurm/slurmctld.pid
SlurmdPidFile=/var/log/slurm/slurmd.pid

ReturnToService=2
ProctrackType=proctrack/linuxproc

SlurmctldLogFile=/var/log/slurm/slurmctld.log
SlurmdLogFile=/var/log/slurm/slurmd.log
GresTypes=cpu

TaskPlugin=task/cgroup

SelectType=select/cons_res
SelectTypeParameters=CR_Core_Memory

NodeName=j35a  NodeAddr=192.168.1.1  Sockets=2 CoresPerSocket=42 ThreadsPerCore=2 RealMemory=500000 State=UNKNOWN
NodeName=j35b  NodeAddr=192.168.1.2  Sockets=2 CoresPerSocket=48 ThreadsPerCore=2 RealMemory=500000 State=UNKNOWN
PartitionName=Normal Nodes=ALL Default=YES MaxTime=INFINITE State=UP OverSubscribe=NO
```

Make sure all the files mentioned in slurm.conf editable by the user 'slurm'. User slurm will be automatically created when install slurm.

Create/edit the ```/etc/slurm/cgroup.conf``` as following.
```bash
CgroupAutomount=no
ConstrainCores=yes
ConstrainRAMSpace=yes
##TaskAffinity=yes
ConstrainDevices=no
```
***

## Module system

Install environment-modules on your head node.

```bash
sudo apt-get install environment-modules
source /usr/share/modules/init/bash >> /etc/profile
export MODULEPATH=$MODULEPATH:/opt/module_file/
```