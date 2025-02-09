#!/bin/bash
set -e

# Change to the project root
cd apps/ayokoding-web

# Install dependencies
npm install

# Build the project
next build

# Return to root directory
cd ../..
