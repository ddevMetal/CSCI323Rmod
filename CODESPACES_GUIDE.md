# Quick Start Guide for GitHub Codespaces

## Yes, you can run this notebook on GitHub Codespaces! 🚀

This repository is fully configured to work with GitHub Codespaces. Here's how:

### Step-by-Step Instructions:

1. **Launch Codespace:**
   - Go to the repository on GitHub
   - Click the green **"<> Code"** button
   - Select the **"Codespaces"** tab
   - Click **"Create codespace on main"**

2. **Automatic Setup:**
   - Codespaces will automatically:
     - Set up Python 3.11 environment
     - Install PyTorch, torchvision, and all required libraries
     - Configure Jupyter notebook support in VS Code
   - Wait 2-3 minutes for the initial setup

3. **Open and Run the Notebook:**
   - In the VS Code file explorer, click on `cifar10_cnn_vs_dnn_v2.ipynb`
   - When prompted, select the Python 3.11 kernel
   - Run cells using:
     - **Shift + Enter** to run a single cell
     - **Run All** button in the toolbar to execute all cells

### What's Included:

✅ PyTorch 2.0+ with CPU support  
✅ torchvision for CIFAR-10 dataset  
✅ NumPy and Matplotlib for data processing and visualization  
✅ Jupyter notebook environment  
✅ VS Code extensions for Python and Jupyter  

### Advantages of Using Codespaces:

- **No Local Setup**: Everything runs in the cloud
- **Consistent Environment**: Same setup for everyone
- **Free Tier Available**: GitHub provides free Codespaces hours
- **VS Code Interface**: Full IDE experience in your browser
- **Easy Sharing**: Share your running Codespace with others

### Note:

The notebook was originally designed for Google Colab, but it works perfectly in Codespaces without any modifications! The code is compatible with both platforms.

### Troubleshooting:

If you encounter any issues:
- Make sure the kernel is selected (Python 3.11)
- Restart the kernel if needed: Click the "Restart" button in the notebook toolbar
- Check that all dependencies installed correctly by running `pip list` in a terminal

Happy coding! 🎉
