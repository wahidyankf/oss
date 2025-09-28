#!/bin/bash

# Build script for all projects in the monorepo

echo "Building OSS monorepo projects..."

# Build Nx-integrated projects
echo "Building Nx projects..."
npx nx run-many --target=build

# Build standalone projects
echo "Building standalone projects..."
npm run build:standalone

echo "Build complete!"