# CSCI323 Machine Learning Lab

This repository contains the machine learning lab exercises for CSCI323. The lab focuses on comparing Convolutional Neural Networks (CNN) and Deep Neural Networks (DNN) using the CIFAR-10 dataset.

## Lab Contents

- **cifar10_cnn_vs_dnn_v2.ipynb**: Main notebook comparing CNN vs DNN performance on CIFAR-10

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/ddevMetal/CSCI323Rmod.git
cd CSCI323Rmod
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Lab

1. Launch Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `cifar10_cnn_vs_dnn_v2.ipynb` in your browser

3. Follow the instructions in the notebook and execute each cell sequentially

## Lab Objectives

Students will:
1. Understand how input images are handled differently in CNN vs DNN
2. Learn the training loop for both CNN and DNN models
3. Compare the performance of CNN vs DNN on image classification
4. Analyze how loss changes across epochs for both models

## Assignment Submission

- Export to PDF: File → Print → Save as PDF (entire notebook)
- Filename: Lab1_UOWID.pdf
- Deadline: 26 Oct 2025, 11:55 pm (2 attempts max)

## Requirements

- PyTorch >= 2.0.0
- torchvision >= 0.15.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- jupyter >= 1.0.0

## Notes

- The notebook will automatically download the CIFAR-10 dataset on first run
- Training may take several minutes depending on your hardware
- GPU acceleration is optional but recommended for faster training