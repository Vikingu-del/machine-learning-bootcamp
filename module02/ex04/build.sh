#!/bin/bash
set -e

# Upgrade the tools and install the modern build wrapper
python -m pip install --upgrade pip setuptools wheel build

# Compile the package cleanly using the pyproject.toml instructions
python -m build

# Install it locally
python -m pip install .
