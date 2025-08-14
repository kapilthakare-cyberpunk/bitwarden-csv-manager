#!/bin/bash

# Build script for Bitwarden CSV Manager

echo "Building Bitwarden CSV Manager..."

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Install build dependencies
echo "Installing build dependencies..."
pip install --upgrade build twine

# Build the package
echo "Building package..."
python -m build

echo "Build complete! Package files are in the 'dist/' directory."
echo ""
echo "To install locally:"
echo "pip install dist/bitwarden_csv_manager-1.0.0-py3-none-any.whl"
echo ""
echo "To upload to PyPI (if configured):"
echo "twine upload dist/*"
