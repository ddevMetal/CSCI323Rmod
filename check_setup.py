#!/usr/bin/env python3
"""
Validation script to check if all required dependencies are installed correctly.
Run this script before starting the lab to ensure your environment is ready.
"""

import sys

def check_imports():
    """Check if all required packages can be imported."""
    errors = []
    
    packages = {
        'torch': 'PyTorch',
        'torchvision': 'torchvision',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'jupyter': 'Jupyter',
    }
    
    print("Checking dependencies...\n")
    
    for package, name in packages.items():
        try:
            module = __import__(package)
            version = getattr(module, '__version__', 'unknown')
            print(f"✓ {name:15s} installed (version: {version})")
        except ImportError:
            print(f"✗ {name:15s} NOT FOUND")
            errors.append(name)
    
    return errors

def check_cuda():
    """Check if CUDA is available for GPU acceleration."""
    try:
        import torch
        if torch.cuda.is_available():
            print(f"\n✓ CUDA is available (GPU: {torch.cuda.get_device_name(0)})")
            print(f"  PyTorch will use GPU acceleration")
        else:
            print(f"\n⚠ CUDA not available - will use CPU")
            print(f"  Training will be slower but still functional")
    except Exception as e:
        print(f"\n⚠ Could not check CUDA: {e}")

def main():
    print("=" * 60)
    print("CSCI323 ML Lab Environment Validation")
    print("=" * 60 + "\n")
    
    errors = check_imports()
    check_cuda()
    
    print("\n" + "=" * 60)
    if errors:
        print(f"✗ Setup incomplete! Missing: {', '.join(errors)}")
        print("\nPlease install missing packages:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    else:
        print("✓ All dependencies are installed correctly!")
        print("✓ You're ready to start the lab!")
        print("\nRun: jupyter notebook")
    print("=" * 60)

if __name__ == "__main__":
    main()
