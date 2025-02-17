#!/bin/bash
set -e

# Install Hugo
wget https://github.com/gohugoio/hugo/releases/download/v0.134.3/hugo_extended_0.134.3_Linux-64bit.tar.gz
tar -xzf hugo_extended_0.134.3_Linux-64bit.tar.gz
chmod +x hugo

# Build the site
./hugo

# Verify build
ls -l public
