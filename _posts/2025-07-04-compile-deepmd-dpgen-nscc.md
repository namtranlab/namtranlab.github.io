---
layout: distill
title: Step-by-Step Guide to Compile DeepMD-kit and DPGEN on NSCC
description: Instruction for compiling deepmd-kit and dpgen on NSCC
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
  - name: Related resource 
    # if a section has subsections, you can add them as follows:
    # subsections:
    #   - name: Example Child Subsection 1
    #   - name: Example Child Subsection 2
  - name: DeepMD-kit Installation
  - name: DPGEN Installation


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

## Related resource 

- DeepMD-kit GitHub:  
    [https://github.com/deepmodeling/deepmd-kit](https://github.com/deepmodeling/deepmd-kit)
- DeepModeling:  
    [https://deepmodeling.com](https://deepmodeling.com/)
- Instruction:  
    [https://www.bohrium.com/notebooks/16449433825](https://www.bohrium.com/notebooks/16449433825)

***

## DeepMD-kit Installation

### 1. Download the installation package

``` shell
wget [https://github.com/deepmodeling/deepmd-kit/releases/download/v3.0.1/deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh.0](https://github.com/deepmodeling/deepmd-kit/releases/download/v3.0.1/deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh.0)  
wget [https://github.com/deepmodeling/deepmd-kit/releases/download/v3.0.1/deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh.1](https://github.com/deepmodeling/deepmd-kit/releases/download/v3.0.1/deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh.1)  
```

### 2. Merge installation files

``` shell
cat deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh.0 \  
deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh.1 > \  
deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh  

```

### 3. Execute installation script

```
sh deepmd-kit-3.0.1-cuda126-Linux-x86_64.sh  
```

The software will as you where to install the binary.

### 4. Environment variable configuration

```bash
source /root/deepmd-kit/bin/activate /root/deepmd-kit
```
You have to put the above command to your bash script.

***

## DPGEN Installation

### 1. Download dp-gen from github link below

The current version is v0.13.1.

```shell
https://github.com/deepmodeling/dpgen
```

### 2. Edit the code for MAGMON and PLUS U

Modify the ```make_vasp_incar``` function in dpgen/generator/run.py as follow.

```python
def make_vasp_incar(jdata, filename):
    if "fp_incar" in jdata.keys():
        fp_incar_path = jdata["fp_incar"]
        assert os.path.exists(fp_incar_path)
        fp_incar_path = os.path.abspath(fp_incar_path)
        fr = open(fp_incar_path)
        incar = fr.read()
        ### adding magmom or plus U
        
        if "fp_incar_magom" in jdata:
            fp_incar_magmom = jdata["fp_incar_magom"]
            poscar_file = open(os.path.abspath("POSCAR"))
            poscar_data = poscar_file.readlines()
            elements_order = [ele.strip() for ele in poscar_data[5].split()]
            element_counts = [ele.strip() for ele in poscar_data[6].split()]
            magmom = "MAGMOM ="
            for idx, element in enumerate(elements_order):
                mag = fp_incar_magmom[element]
                magmom = magmom + " " + element_counts[idx] + "*" + str(mag)
        incar = incar + "\n" + magmom

        
        if "fp_incar_plus_u" in jdata:
            fp_incar_plus_u = jdata["fp_incar_plus_u"]
            poscar_file = open(os.path.abspath("POSCAR"))
            poscar_data = poscar_file.readlines()
            elements_order = [ele.strip() for ele in poscar_data[5].split()]
            total_added_u = 0
            max_ul = 0
            ldaul = "LDAUL ="
            ldauu = "LDAUU ="
            ldauj = "LDAUJ ="
            for element in elements_order:
                ul = fp_incar_plus_u[element]['ul']
                if ul>max_ul: max_ul = ul
                ldaul = ldaul + " " + str(ul)
                uu = fp_incar_plus_u[element]['uu']
                ldauu = ldauu + " " + str(uu)
                total_added_u +=uu
                uj = fp_incar_plus_u[element]['uj']
                ldauj = ldauj + " " + str(uj)
                total_added_u +=uj

            if total_added_u > 0:
                incar = incar + "\n" + "LDAU = .TRUE."
                incar = incar + "\n" + ldaul
                incar = incar + "\n" + ldauu
                incar = incar + "\n" + ldauj
                if max_ul > 2:
                    incar = incar + "\n" + "LMAXMIX = 6"
                else:
                    incar = incar + "\n" + "LMAXMIX = 4"

        ### end of adding magmon or plus U
        fr.close()
    elif "user_fp_params" in jdata.keys():
        incar = write_incar_dict(jdata["user_fp_params"])
    else:
        incar = make_vasp_incar_user_dict(jdata["fp_params"])
    
    with open(filename, "w") as fp:
        fp.write(incar)
    return incar
```

When running dpgen the following tags (```fp_incar_magom``` and ```fp_incar_plus_u```) with informattion about initial MAGMON or Plus+U should be added.

For example:

```json
.......
"fp_incar": "./INCAR",
'fp_incar_magom': {'C': 0,  
                    'Ce': 3,     
                    'O': 0, 
                    'Ti': 3,
                    'Pd': 3,
                    'H': 0},
'fp_incar_plus_u': {'C': {'ul':-1, 'uu': 0.00, 'uj': 0.00},  
                    'Ce': {'ul':3, 'uu': 5.50, 'uj': 1.00},     
                    'O': {'ul':-1, 'uu': 0.00, 'uj': 0.00}, 
                    'Ti': {'ul':2, 'uu': 5.50, 'uj': 1.00},
                    'Pd': {'ul':-1, 'uu': 0.00, 'uj': 0.00}, 
                    'H': {'ul':-1, 'uu': 0.00, 'uj': 0.00},
                    }
```

### 3. Install the package

Create an environment (tested with python version 3.11.7)

```shell
python3 -m venv dpgen_env
```

Activate the environment.
```shell
source /home/users/ntu/vannamtr/dpgen_env/bin/activate
```
You must add the above command to your bash script

Then install the package with

```shell
pip install ./dpgen
```

To test if the installation is successful, you may execute

```shell
dpgen -h
```

Note: The above tutorial should work on NCI as well.