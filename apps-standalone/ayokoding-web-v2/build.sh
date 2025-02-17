#!/bin/bash
set -e

# Ensure we're in the correct directory
cd "$(dirname "$0")"

# Check if Hugo is already installed
if ! command -v hugo &> /dev/null; then
    echo "Hugo not found, installing..."
    
    # Determine the appropriate Hugo download URL
    HUGO_VERSION="0.134.3"
    HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
    
    # Create a local bin directory if it doesn't exist
    mkdir -p "$HOME/bin"
    
    # Download Hugo using curl
    curl -L -o hugo.tar.gz "$HUGO_URL"
    
    # Extract Hugo to the local bin directory
    tar -xzf hugo.tar.gz -C "$HOME/bin"
    
    # Make Hugo executable
    chmod +x "$HOME/bin/hugo"
    
    # Add local bin to PATH if not already there
    if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
        export PATH="$HOME/bin:$PATH"
    fi
    
    # Cleanup
    rm hugo.tar.gz
fi

# Verify Hugo installation
hugo version

# Build the site
hugo

# Verify build output
if [ -d "public" ]; then
    echo "Build successful. Contents of public directory:"
    ls -l public
else
    echo "Error: Public directory not created"
    exit 1
fi
