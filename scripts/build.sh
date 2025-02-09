#!/bin/bash
set -e

# Create public directory if it doesn't exist
mkdir -p apps/ayokoding-web/public

# Copy favicon.ico if it exists
if [ -f apps/ayokoding-web/public/favicon.ico ]; then
  cp apps/ayokoding-web/public/favicon.ico apps/ayokoding-web/public/favicon.ico.bak
fi

# Run the build
npx nx build ayokoding-web

# Restore favicon.ico if it was backed up
if [ -f apps/ayokoding-web/public/favicon.ico.bak ]; then
  mv apps/ayokoding-web/public/favicon.ico.bak apps/ayokoding-web/public/favicon.ico
fi
