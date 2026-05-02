# swiftcomp-doc

SwiftComp documentation

## Setup with uv

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Installation

1. Install uv:
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Or with pip
   pip install uv
   ```

2. Install project dependencies:
   ```bash
   uv sync
   ```

3. Activate the virtual environment:
   ```bash
   # On Unix/Linux/macOS
   source .venv/bin/activate

   # On Windows
   .venv/Scripts/activate.ps1
   ```

### Building Documentation

Build the documentation using the provided scripts or direct uv commands:

```bash
# Using the build script (recommended)
scripts/build.bat    # On Windows
scripts/build.sh     # On Unix/Linux/macOS

# Or using direct uv commands
uv run sphinx-build -M html source build    # Build HTML documentation
uv run sphinx-build -M clean source build   # Clean build directory

# Serve docs locally on http://localhost:8000
uv run python -m http.server 8000 --directory build/html

# Or using traditional make commands (if make is available)
make html
make clean
```

### Development

Install development dependencies:
```bash
uv sync --extra dev
```

Run development tools:
```bash
# Format code
uv run black .

# Sort imports
uv run isort .

# Lint code
uv run flake8 .
```
