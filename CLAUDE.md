# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Overview

This is a hybrid monorepo with both Nx-integrated and standalone applications. For comprehensive documentation, see the `/docs` directory.

## Key Documentation

- **[Documentation Index](/docs/README.md)** - Start here for all documentation
- **[Getting Started](/docs/development/getting-started.md)** - Environment setup
- **[Common Commands](/docs/commands/common-commands.md)** - Quick command reference
- **[Architecture](/docs/architecture/)** - Design decisions and structure

## Essential Commands

```bash
# Setup
npm install              # Install deps and git hooks
npm run doctor          # Verify environment

# Development (from root)
npx nx serve next-hello            # Nx app
npm run wahidyankf-web:dev         # Standalone Next.js
npm run ayokoding-web:dev          # Standalone Hugo

# Testing
npm run test:all                   # All tests
npx nx affected:test              # Only affected Nx projects

# Build
npm run build                      # All projects
npx nx affected:build             # Only affected
```

## Project Types

### Nx-Integrated (`apps/`)

- Use `npx nx <command> <project>`
- Benefit from caching and affected commands
- See: [Nx-Integrated Projects Guide](/docs/projects/nx-integrated.md)

### Standalone (`apps-standalone/`)

- Have their own package.json and build process
- Use npm scripts from root or navigate to project
- See: [Standalone Projects Guide](/docs/projects/standalone.md)

## Important Notes

1. **Node/npm versions**: Managed by Volta (22.20.0/11.1.0)
2. **Commit format**: `type(scope): subject` (conventional commits)
3. **Code formatting**: Automatic via git hooks (Prettier/Black)
4. **Python projects**: Use pyenv and virtual environments
5. **E2E tests**: Located in separate `wahidyankf-e2e` project

## When Working on Tasks

1. **Research first**: Use search/grep tools to understand the codebase
2. **Check project README**: Each project has specific instructions
3. **Run tests**: Ensure changes don't break existing functionality
4. **Follow conventions**: Match existing code style and patterns
5. **Lint and typecheck**: Run `npx nx lint <project>` for specific projects and `npm run typecheck` for all Nx projects

## Troubleshooting

If you encounter issues, check:

- [Troubleshooting Guide](/docs/guides/troubleshooting.md)
- Project-specific README files
- Run `npm run doctor` for environment issues

## Project-Specific Details

For detailed information about each project:

- [next-hello](/apps/next-hello/README.md)
- [wahidyankf-web](/apps-standalone/wahidyankf-web/README.md)
- [ayokoding-web](/apps-standalone/ayokoding-web/README.md)
- [analisapasar-web](/apps-standalone/analisapasar-web/README.md)
- [python-mastery](/apps-standalone/python-mastery/README.md)
- [wahidyankf-e2e](/apps-standalone/wahidyankf-e2e/README.md)
