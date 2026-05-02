@echo off
REM Build script for SwiftComp documentation using uv

echo Building SwiftComp documentation...

REM Ensure dependencies are installed
echo Syncing dependencies...
uv sync
if errorlevel 1 (
    echo Failed to sync dependencies
    exit /b 1
)

REM Build HTML documentation
echo Building HTML documentation...
uv run sphinx-build -M html source build
if errorlevel 1 (
    echo Failed to build documentation
    exit /b 1
)

echo Documentation built successfully!
echo Open build\html\index.html in your browser to view the documentation.
