#!/bin/bash
set -e

# Check if Hugo is already installed
if ! command -v hugo &> /dev/null; then
    echo "Hugo not found, installing..."
    
    # Determine the appropriate Hugo download URL
    HUGO_VERSION="0.134.3"
    HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
    
    # Download Hugo using curl
    curl -L -o hugo.tar.gz "$HUGO_URL"
    
    # Extract Hugo
    tar -xzf hugo.tar.gz
    
    # Move Hugo to a directory in PATH
    sudo mv hugo /usr/local/bin/hugo
    
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
