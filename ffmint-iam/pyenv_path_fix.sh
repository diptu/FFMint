#!/bin/bash

# --- Script Start ---
echo "--- pyenv PATH Fix Script ---"
echo "This script will attempt to fix pyenv PATH issues in your shell configuration."
echo "It will make a backup of your current config file before making changes."

# Determine the shell
SHELL_NAME=$(basename "$SHELL")
SHELL_CONFIG_FILE=""
BREW_SHELLENV_LINE='eval "$(/opt/homebrew/bin/brew shellenv)"'

if [[ "$SHELL_NAME" == "zsh" ]]; then
    SHELL_CONFIG_FILE="$HOME/.zshrc"
elif [[ "$SHELL_NAME" == "bash" ]]; then
    SHELL_CONFIG_FILE="$HOME/.bash_profile"
    # For Bash, .bashrc might also be relevant if .bash_profile sources it
    # For simplicity, we'll focus on .bash_profile first as it's for login shells
else
    echo "Error: Unsupported shell: $SHELL_NAME"
    echo "This script currently supports 'zsh' and 'bash'."
    exit 1
fi

echo "Detected shell: $SHELL_NAME"
echo "Targeting configuration file: $SHELL_CONFIG_FILE"

if [[ ! -f "$SHELL_CONFIG_FILE" ]]; then
    echo "Warning: Configuration file '$SHELL_CONFIG_FILE' not found. Creating it."
    touch "$SHELL_CONFIG_FILE"
fi

# Create a backup of the original config file
BACKUP_FILE="${SHELL_CONFIG_FILE}.bak_$(date +%Y%m%d%H%M%S)"
cp "$SHELL_CONFIG_FILE" "$BACKUP_FILE"
echo "Backup created at: $BACKUP_FILE"

# pyenv initialization lines
PYENV_SETUP_LINES=(
    '# --- pyenv setup by pyenv_path_fix.sh script ---'
    'export PYENV_ROOT="$HOME/.pyenv"'
    'export PATH="$PYENV_ROOT/bin:$PATH"'
    'eval "$(pyenv init --path)"'
    'eval "$(pyenv init -)"'
    '# --- end pyenv setup ---'
)

# Function to add lines if not present
add_lines_if_missing() {
    local file="$1"
    local lines=("${!2}") # Indirect expansion to get the array
    local added=false

    for line in "${lines[@]}"; do
        # Check if line already exists (ignoring comments from our setup)
        if ! grep -qF "${line}" "$file"; then
            echo "$line" >> "$file"
            added=true
        fi
    done
    if [[ "$added" == "true" ]]; then
        echo "Added missing pyenv setup lines to $file."
    else
        echo "pyenv setup lines already present in $file."
    fi
}

# Function to check if a block of lines exists in the file
contains_block() {
    local file="$1"
    local pattern_start="$2"
    local pattern_end="$3"
    grep -qF "$pattern_start" "$file" && grep -qF "$pattern_end" "$file"
}

# Check for Homebrew shellenv and ensure it's before pyenv
if ! grep -qF "$BREW_SHELLENV_LINE" "$SHELL_CONFIG_FILE"; then
    echo "Homebrew 'brew shellenv' line not found. Adding it."
    echo "$BREW_SHELLENV_LINE" >> "$SHELL_CONFIG_FILE"
    echo "Added Homebrew 'brew shellenv' to $SHELL_CONFIG_FILE."
fi

# Check if pyenv block is present
if contains_block "$SHELL_CONFIG_FILE" "${PYENV_SETUP_LINES[0]}" "${PYENV_SETUP_LINES[${#PYENV_SETUP_LINES[@]}-1]}"; then
    echo "Existing pyenv setup block found. Checking order..."
    # A simple way to check order: ensure pyenv start is after brew shellenv if both exist
    if grep -nF "$BREW_SHELLENV_LINE" "$SHELL_CONFIG_FILE" > /dev/null && \
       grep -nF "${PYENV_SETUP_LINES[0]}" "$SHELL_CONFIG_FILE" > /dev/null; then

        BREW_LINE_NUM=$(grep -nF "$BREW_SHELLENV_LINE" "$SHELL_CONFIG_FILE" | cut -d: -f1)
        PYENV_START_NUM=$(grep -nF "${PYENV_SETUP_LINES[0]}" "$SHELL_CONFIG_FILE" | cut -d: -f1)

        if (( BREW_LINE_NUM > PYENV_START_NUM )); then
            echo "Homebrew 'brew shellenv' is after pyenv. Reordering for optimal PATH."
            # Remove pyenv block and re-add at end
            sed -i.tmp '/# --- pyenv setup by pyenv_path_fix.sh script ---/,/# --- end pyenv setup ---/d' "$SHELL_CONFIG_FILE"
            add_lines_if_missing "$SHELL_CONFIG_FILE" PYENV_SETUP_LINES[@]
        else
            echo "Homebrew 'brew shellenv' is correctly before pyenv setup."
        fi
    fi
else
    echo "pyenv setup block not found. Adding it to the end of $SHELL_CONFIG_FILE."
    add_lines_if_missing "$SHELL_CONFIG_FILE" PYENV_SETUP_LINES[@]
fi

echo ""
echo "Configuration file '$SHELL_CONFIG_FILE' has been updated."
echo "You might need to reload your shell for changes to take effect."
read -p "Do you want to reload your current shell now? (y/N): " reload_confirm
if [[ "$reload_confirm" =~ ^[Yy]$ ]]; then
    echo "Reloading shell..."
    exec "$SHELL"
else
    echo "Please close your terminal and open a new one, or run 'source $SHELL_CONFIG_FILE'."
fi

echo "--- Script Finished ---"
