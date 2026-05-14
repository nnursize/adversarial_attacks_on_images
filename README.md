Adversarial Attacks on Images

This repository contains code and notebooks for adversarial attack experiments on ImageNet.

required libraries:

torch
torchvision
matplotlib
numpy
statsmodels
scipy
tqdm
pyyaml

-> pip install torch torchvision matplotlib numpy statsmodels scipy tqdm pyyaml

main code that runs the experimental setup is main.ipynb
given three helper files are needed to run main.ipynb notebook
.
├── ImageNet.yaml          # Dataset / experiment configuration
├── map.txt                # ImageNet class index → label mapping
├── utils.py               # Helper functions (label conversion, etc.)

For more details, you can read our [project report](./Report.pdf).