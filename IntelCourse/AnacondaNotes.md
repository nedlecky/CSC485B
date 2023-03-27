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

# Make course code run- minimal
Running 3/27/2023
* python 3.10.10
* pytorch 1.12.1 torchvision 0.13.1
* pygame 2.3.0
* pymunk 5.7.0
```
conda create -n nn2
conda activate nn2
pip install torchvision
pip install pygame
pip install pymunk==5.7.0
```