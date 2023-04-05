# Basic Anaconda Notes
Ned Lecky
Ctl-k, v to open preview to the side in VSCode

## Shorter Prompt Control
  * Use "prompt $g " before activating your env and you won't have a 2-foot long prompt
  * Use "prompt" to get the default prompt back!

## Basic Commands
```
conda env list
conda create -n YourEnvironment python=3.6
conda activate YourEnvironment
conda deactivate
```

## Environment Control
```
conda create -n YourEnvironment python=3.6
conda activate YourEnvironment 
conda remove -n YourEnvironment --all
```

# Class 1
## Minimal setup for code
Running 3/27/2023
* python 3.10.10
* pytorch 1.12.1 torchvision 0.13.1
* pygame 2.3.0
* pymunk 5.7.0
```
conda create -n intel
conda activate intel
pip install torchvision
pip install pygame
pip install pymunk==5.7.0
```

# Class 2
## Minimal setup for code
Running 4/4/2023
* python 3.10.10
* pytorch 1.12.1 torchvision 0.13.1
```
conda create -n intel2
conda activate intel2
conda install numpy scipy matplotlib
pip install torch
pip install pygame
#pip install pylab
#pip install glob
```
