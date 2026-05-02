#!/bin/bash
# Build script for SwiftComp documentation using uv

set -e

echo "Building SwiftComp documentation..."

# Ensure dependencies are installed
echo "Syncing dependencies..."
uv sync

# Build HTML documentation
echo "Building HTML documentation..."
uv run sphinx-build -M html source build

echo "Documentation built successfully!"
echo "Open build/html/index.html in your browser to view the documentation."
