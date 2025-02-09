#!/bin/bash
set -e

# Change to the project root
cd apps/next-hello

# Install dependencies
npm install

# Build the project
next build

# Return to root directory
cd ../..
