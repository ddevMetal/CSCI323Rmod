# CSCI323Rmod

## Running the Notebook on GitHub Codespaces

This repository is configured to work with GitHub Codespaces, allowing you to run the `cifar10_cnn_vs_dnn_v2.ipynb` notebook directly in your browser without any local setup.

### How to Use Codespaces:

1. **Open in Codespaces:**
   - Click the green "Code" button at the top of this repository
   - Select "Codespaces" tab
   - Click "Create codespace on main" (or your current branch)

2. **Wait for Setup:**
   - Codespaces will automatically build the environment
   - All dependencies (PyTorch, torchvision, numpy, matplotlib, Jupyter) will be installed automatically
   - This may take a few minutes on first launch

3. **Open the Notebook:**
   - Once the environment is ready, navigate to `cifar10_cnn_vs_dnn_v2.ipynb` in the file explorer
   - Click on the file to open it
   - VS Code will prompt you to select a kernel - choose the Python 3.11 kernel

4. **Run the Notebook:**
   - You can now run all cells in the notebook
   - Use Shift+Enter to run individual cells
   - Or use "Run All" from the notebook toolbar

### Alternative: Running Locally

If you prefer to run locally, install the dependencies:

```bash
pip install -r requirements.txt
```

Then open the notebook with Jupyter:

```bash
jupyter notebook cifar10_cnn_vs_dnn_v2.ipynb
```

### Note on Google Colab

The notebook was originally designed for Google Colab, but all features work identically in Codespaces.