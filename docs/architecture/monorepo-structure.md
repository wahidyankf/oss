# Monorepo Structure

This document explains the organization and structure of the OSS monorepo.

## Overview

The monorepo uses a hybrid approach, combining Nx-managed applications with standalone projects that are difficult to integrate or experimental.

## Directory Structure

```
oss/
├── apps/                    # Nx-integrated applications
│   └── next-hello/         # Template Next.js application
├── apps-standalone/         # Independent applications
│   ├── ayokoding-web/      # Hugo-based educational platform
│   ├── analisapasar-web/   # Hugo-based market analysis site
│   ├── wahidyankf-web/     # Next.js personal portfolio
│   ├── wahidyankf-e2e/     # Playwright E2E test suite
│   └── python-mastery/     # Python learning curriculum
├── docs/                    # Comprehensive documentation
└── scripts/                 # Build and utility scripts
    ├── doctor.js           # Environment health check
    └── prepare.js          # Git hooks setup

Note: Additional directories (libs/, tools/, apps/web-e2e/) are planned for future development.
```

## Nx-Integrated vs Standalone

### Nx-Integrated Applications (`apps/`)

- Managed by Nx workspace configuration
- Share dependencies and configurations
- Can reference shared libraries
- Benefit from Nx's caching and affected commands
- Currently includes:
  - `next-hello`: A minimal Next.js template

### Standalone Applications (`apps-standalone/`)

These applications maintain their independence for various reasons:

1. **Different Build Systems**: Hugo-based sites use a different build process
2. **Legacy Projects**: Existing projects not yet migrated
3. **Experimental**: Projects in early development
4. **Different Dependencies**: Projects with conflicting dependency requirements

Current standalone applications:

- `ayokoding-web`: Hugo static site generator with custom theme
- `analisapasar-web`: Hugo-based market analysis platform
- `wahidyankf-web`: Next.js 14 with specific configurations
- `wahidyankf-e2e`: Playwright tests targeting external deployment
- `python-mastery`: Python educational content with its own environment

## Shared Configuration

Despite the separation, all projects share:

1. **Node Version**: Managed by Volta (22.20.0)
2. **Git Hooks**: Husky for pre-commit and pre-push checks
3. **Code Formatting**: Prettier for JS/TS, Black for Python
4. **Commit Standards**: Conventional commits enforced

## Future Migration Path

The goal is to gradually integrate more standalone applications into the Nx workspace as:

- Build processes are standardized
- Dependencies are aligned
- Shared code is extracted into libraries

## Benefits of This Structure

1. **Flexibility**: Different projects can use appropriate tools
2. **Gradual Migration**: No need for big-bang migrations
3. **Independence**: Projects can be developed/deployed separately
4. **Shared Standards**: Common development practices across all projects
5. **Monorepo Benefits**: Where applicable, projects share configs and dependencies
