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

main code that runs the experimental setup is `main.ipynb` (located in `source_code/`).
The repository layout is:

.
├── README.md
├── Report.pdf
├── presentation.pptx
├── source_code/
│   ├── ImageNet.yaml          # Dataset / experiment configuration
│   ├── main.ipynb             # Notebook that runs experiments
│   ├── map.txt                # ImageNet class index → label mapping
│   └── utils.py               # Helper functions (label conversion, etc.)
└── .gitignore

For more details, you can read our [project report](./Report.pdf).