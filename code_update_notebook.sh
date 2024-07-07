#!/bin/bash

# Function to update conda
update_conda() {
    echo "Updating conda..."
    conda update conda -y
}

# Function to update Anaconda
update_anaconda() {
    echo "Updating Anaconda..."
    conda update anaconda -y
}

# Function to update Jupyter Notebook
update_jupyter_notebook() {
    echo "Updating Jupyter Notebook..."
    conda update jupyter -y
}

# Function to update all conda packages
update_all_conda_packages() {
    echo "Updating all conda packages..."
    conda update --all -y
}

# Function to update Visual Studio Code
update_vscode() {
    echo "Updating Visual Studio Code..."
    brew update
    brew upgrade --cask visual-studio-code
}

# Function to update VS Code Jupyter extension
update_vscode_jupyter_extension() {
    echo "Updating VS Code Jupyter extension..."
    code --install-extension ms-toolsai.jupyter --force
}

# Main function to run all updates
main() {
    update_conda
    update_anaconda
    update_jupyter_notebook
    update_all_conda_packages
    update_vscode
    update_vscode_jupyter_extension
    echo "Update complete!"
}

# Run the main function
main
