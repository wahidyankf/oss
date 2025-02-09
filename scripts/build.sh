#!/bin/bash
set -e

# Create public directory if it doesn't exist
mkdir -p apps/next-hello/public

# Copy favicon.ico if it exists
if [ -f apps/next-hello/public/favicon.ico ]; then
  cp apps/next-hello/public/favicon.ico apps/next-hello/public/favicon.ico.bak
fi

# Run the build
npx nx build next-hello

# Restore favicon.ico if it was backed up
if [ -f apps/next-hello/public/favicon.ico.bak ]; then
  mv apps/next-hello/public/favicon.ico.bak apps/next-hello/public/favicon.ico
fi
