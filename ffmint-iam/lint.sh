#!/bin/bash
set -e

APP_DIR="app/"
TESTS_DIR="tests/"
MAX_LINE_LENGTH=88
VENV_DIR=".venv"

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Set PYTHONPATH so pylint and others can find your code
export PYTHONPATH="$(pwd)/$APP_DIR"

run_lint() {
  echo "--- Running Code Quality Checks (Linting & Formatting) ---"

  # Use the installed tools inside the venv
  isort "$APP_DIR" "$TESTS_DIR"
  black "$APP_DIR" "$TESTS_DIR" --line-length="$MAX_LINE_LENGTH"
  ruff check "$APP_DIR" "$TESTS_DIR" --fix --line-length="$MAX_LINE_LENGTH"
  flake8 "$APP_DIR" "$TESTS_DIR" --max-line-length="$MAX_LINE_LENGTH"
  pylint "$APP_DIR" "$TESTS_DIR" --max-line-length="$MAX_LINE_LENGTH"
  mypy "$APP_DIR" "$TESTS_DIR"

  echo "--- Code Quality Checks Complete ---"
}

run_test() {
  echo "--- Running Tests ---"
  pytest "$TESTS_DIR"
  echo "--- Testing Complete ---"
}

if [ -z "$1" ]; then
  echo "Usage: $0 [lint|test]"
  exit 1
fi

case "$1" in
  lint) run_lint ;;
  test) run_test ;;
  *)
    echo "Invalid option $1"
    exit 1
    ;;
esac
