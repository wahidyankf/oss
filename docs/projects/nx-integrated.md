# Nx-Integrated Projects

This document covers projects that are fully integrated into the Nx monorepo structure.

## Overview

Nx-integrated projects benefit from:

- Shared dependencies and configurations
- Build caching and incremental builds
- Affected commands for targeted operations
- Consistent tooling across projects
- Dependency graph visualization

## Current Projects

### next-hello

**Location**: `apps/next-hello`

**Purpose**: Template Next.js application demonstrating Nx integration

**Key Features**:

- Next.js 15.x with App Router
- TypeScript configuration
- Jest testing setup
- Tailwind CSS integration
- Basic API route example

**Commands**:

```bash
# Development
npx nx serve next-hello

# Build
npx nx build next-hello

# Test
npx nx test next-hello

# Lint
npx nx lint next-hello

# Type checking
npx nx typecheck next-hello
```

**Project Configuration**:

- Config: `apps/next-hello/project.json`
- Extends base TypeScript config
- Custom Jest configuration
- Tailwind CSS setup

### Future Projects

**web-e2e**: Planned E2E test suite for Nx-integrated applications (not yet created)

## Working with Nx

### Understanding the Dependency Graph

```bash
# View project dependencies
npx nx graph

# View affected projects
npx nx affected:graph
```

### Running Affected Commands

Nx can determine which projects are affected by your changes:

```bash
# Test only affected projects
npx nx affected:test

# Build only affected projects
npx nx affected:build

# Run any target on affected projects
npx nx affected --target=lint
```

### Parallel Execution

Nx automatically runs tasks in parallel when possible:

```bash
# Run build for all projects
npx nx run-many --target=build

# Run specific projects in parallel
npx nx run-many --target=test --projects=next-hello,web-e2e
```

## Adding New Nx Projects

### Generate a New Application

```bash
# Generate Next.js app
npx nx g @nx/next:application my-app

# Generate React app
npx nx g @nx/react:application my-react-app

# Generate Node app
npx nx g @nx/node:application my-api
```

### Generate a Library

```bash
# Generate TypeScript library
npx nx g @nx/js:library my-lib

# Generate React component library
npx nx g @nx/react:library ui-components

# Generate Node library
npx nx g @nx/node:library api-interfaces
```

## Project Structure

### Standard Nx Application Structure

```
apps/next-hello/
├── src/
│   ├── app/           # Next.js app directory
│   │   ├── layout.tsx
│   │   └── page.tsx
│   └── test-setup.ts  # Jest setup
├── public/            # Static assets
├── project.json       # Nx project configuration
├── tsconfig.json      # TypeScript config
├── tsconfig.spec.json # Test TypeScript config
├── jest.config.js     # Jest configuration
└── next.config.js     # Next.js configuration
```

### Project Configuration (project.json)

```json
{
  "$schema": "../../node_modules/nx/schemas/project-schema.json",
  "sourceRoot": "apps/next-hello/src",
  "projectType": "application",
  "targets": {
    "build": {
      "executor": "@nx/next:build",
      "options": {
        "outputPath": "dist/apps/next-hello"
      }
    },
    "serve": {
      "executor": "@nx/next:server",
      "options": {
        "buildTarget": "next-hello:build",
        "dev": true
      }
    },
    "test": {
      "executor": "@nx/jest:jest",
      "options": {
        "jestConfig": "apps/next-hello/jest.config.js"
      }
    }
  }
}
```

## Shared Libraries (Future)

Note: The `libs/` directory is planned for future development. When implemented, it will allow:

### Creating Shared Code

```bash
# Generate a utility library (when libs/ is created)
npx nx g @nx/js:library utils

# Use in your app
import { formatDate } from '@ayokoding/utils'
```

### Planned Library Types

1. **Feature Libraries**: Complete features with UI and logic
2. **UI Libraries**: Shared components and design system
3. **Data Access Libraries**: API clients and state management
4. **Utility Libraries**: Common functions and helpers

## Build and Deployment

### Building for Production

```bash
# Build single project
npx nx build next-hello

# Build all projects
npx nx run-many --target=build

# Build with custom configuration
npx nx build next-hello --configuration=production
```

### Output Structure

Builds are output to:

```
dist/
└── apps/
    └── next-hello/
        ├── .next/     # Next.js build output
        └── public/    # Static assets
```

## Caching

### Local Caching

Nx caches build outputs and test results:

```bash
# Clear cache
npx nx reset

# Run with cache disabled
npx nx build next-hello --skip-nx-cache
```

### Cache Location

- Default: `node_modules/.cache/nx`
- Configurable in `nx.json`

## Best Practices

### 1. Use Nx Generators

Always use Nx generators for consistency:

```bash
npx nx g @nx/react:component Button --project=ui-lib
```

### 2. Enforce Module Boundaries

Configure import restrictions in `.eslintrc.json`:

```json
{
  "@nx/enforce-module-boundaries": [
    "error",
    {
      "depConstraints": [
        {
          "sourceTag": "type:app",
          "onlyDependOnLibsWithTags": ["type:feature", "type:ui", "type:util"]
        }
      ]
    }
  ]
}
```

### 3. Keep Project Size Manageable

- Split large apps into libraries
- Use lazy loading for features
- Keep build times under 2 minutes

### 4. Consistent Naming

- Apps: `feature-name-app`
- Libraries: `feature-name-lib`
- E2E: `feature-name-e2e`

## Troubleshooting

### Common Issues

1. **Module not found**

   ```bash
   # Regenerate TypeScript paths
   npx nx reset
   npm install
   ```

2. **Cache issues**

   ```bash
   npx nx reset
   rm -rf node_modules/.cache
   ```

3. **Dependency conflicts**
   ```bash
   # Check why a dependency is included
   npm ls package-name
   ```

## Future Plans

1. **More Applications**: Migrate standalone apps to Nx
2. **Shared Libraries**: Extract common code
3. **Custom Generators**: Project-specific templates
4. **CI/CD Integration**: Nx Cloud for distributed caching
