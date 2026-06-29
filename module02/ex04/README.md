# my_minipack

A lightweight Python packaging exercise developed as part of the **42 AI Machine Learning Bootcamp** (Module 02, Exercise 04). This project demonstrates modern Python packaging standards utilizing `pyproject.toml` (PEP 621 compliance) and automated build distribution scripting.

---

## 📦 Project Overview

`my_minipack` consolidates useful utility modules developed throughout the bootcamp into a single, cohesive, and distributable Python library. The package consists of two primary submodules:

* **`my_minipack.progress`**: A custom terminal-based progress tracker loop (originally featured in Module 00, Ex 10 as `loading.py`).
* **`my_minipack.logger`**: A decorative execution-time logging utility designed to benchmark functions seamlessly (originally featured in Module 02, Ex 02).

---

## 🛠️ Package Architecture

The project directory is self-contained and structured specifically to satisfy strict installation metadata hooks and backward compatibility constraints:

```text
ex04/
├── build.sh             # Automation script to upgrade tools, compile, and install
├── LICENSE              # Copyleft GNU General Public License v3 (GPLv3)
├── pyproject.toml       # Modern build-system configuration and project metadata
├── README.md            # Project documentation
└── my_minipack/         # Core package source directory
    ├── __init__.py      # Package initialization hook (intentionally empty)
    ├── logger.py        # Function logging decorators
    └── progress.py      # Terminal progress visualization utilities
```

---

## 🚀 Building the Package

The configuration workspace includes a bash script (`build.sh`) designed to automate the entire distribution setup pipeline. Running this script ensures that your build environment tools are fully updated before generating distribution bundles.

### Setup and Compilation

1. Grant execution permissions to the build script:
   ```bash
   chmod +x build.sh
   ```

2. Execute the compilation pipeline inside your active virtual or Conda environment:
   ```bash
   ./build.sh
   ```

Running this script clears out legacy cache files, safely upgrades `pip`, `setuptools`, and `wheel`, and populates a new local `dist/` directory containing two distinct build targets:
* A compressed source distribution archiver: `my_minipack-1.0.0.tar.gz`
* A pre-compiled binary wheel archive: `my_minipack-1.0.0-py3-none-any.whl`

---

## 💾 Installation Options

Once compiled, this package can be installed locally via `pip` using either of the built distribution files located inside the `dist/` workspace. Both of the following commands are fully supported:

#### Option A: Installing via the Source Distribution (.tar.gz)
```bash
pip install ./dist/my_minipack-1.0.0.tar.gz
```

#### Option B: Installing via the Pre-compiled Binary Wheel (.whl)
```bash
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
```

---

## 📋 Verification & Metadata Inspection

To confirm that the package has successfully integrated into your active workspace and is reporting correct regulatory compliance data, check your local index using the extended verbose flag:

```bash
pip show -v my_minipack
```

### Target Output Integrity
The package metadata is specifically engineered to guarantee perfect alignment with evaluation grading metrics:

```text
Name: my-minipack
Version: 1.0.0
Summary: Howto create a package in python.
Home-page: None
Author: erik
Author-email: erik@student.42.fr
License: GPLv3
Location: /home/user/.../site-packages
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 3 - Alpha
  Intended Audience :: Developers
  Intended Audience :: Students
  Topic :: Education
  Topic :: HowTo
  Topic :: Package
  License :: OSI Approved :: GNU General Public License v3 (GPLv3)
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3 :: Only
```

---

## 🐍 Usage Examples

Once installed, the modules can be cleanly imported into any external python script inside your environment using the standard dot-notation syntax:

### 1. Utilizing the Progress Bar Component
```python
import my_minipack.progress
import time

listy = range(1000)
ret = 0
for elem in my_minipack.progress.ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
```

### 2. Utilizing the Decorative Execution Logger
```python
import my_minipack.logger
import random

@my_minipack.logger.log
def add_water(water_level):
    return water_level + random.randint(1, 10)

# Executes and logs timestamp data to machine.log automatically
add_water(42)
```