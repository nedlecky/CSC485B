# Basic Anaconda Notes
Ned Lecky
Ctl-k, v to open preview to the side in VSCode

## Shorter Prompt Control
  * Use "prompt $g " before activating your env and you won't have a 2-foot long prompt
  * Use "prompt" to get the default prompt back!

## Basic Commands
conda env list
conda create -n YourEnvironment python=3.6
conda activate YourEnvironment
conda deactivate

## Environment Control
conda create -n YourEnvironment python=3.6
conda activate YourEnvironment 
conda remove -n YourEnvironment --all

# Intel Game Env Setup
  * Note using Python 3.6 and Pymunk < 6.00 are required
conda create -n intel_game_env python=3.6
conda activate intel_game_env

conda install pytorch-cpu -c pytorch 

pip install cython
pip install torchvision
pip install pygame
pip install pymunk==5.7.0

