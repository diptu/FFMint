#!/bin/bash

set -e

VENV_DIR=".venv"

echo "🔁 Resetting Python environment..."

# Step 1: Remove old virtual environment if it exists
if [ -d "$VENV_DIR" ]; then
  echo "🧹 Removing existing virtual environment at '$VENV_DIR'..."
  rm -rf "$VENV_DIR"
else
  echo "ℹ️ No existing virtual environment found at '$VENV_DIR'."
fi

# Step 2: Create new virtual environment
echo "🌱 Creating new virtual environment..."
uv venv "$VENV_DIR"

# Step 3: Activate the virtual environment
echo "🐍 Activating new virtual environment..."
source "$VENV_DIR/bin/activate"

# Step 4: Install ALL dependencies from pyproject.toml
echo "📦 Installing all dependencies from pyproject.toml..."
uv pip install --no-cache-dir ".[dev]"

echo "✅ Environment reset and all dependencies installed successfully."
