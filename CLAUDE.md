# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a monorepo containing multiple applications, libraries, and tools. It uses Nx for monorepo management and includes both integrated and standalone applications.

### Repository Structure

- `apps/` - Nx-integrated applications
  - `next-hello` - Main Next.js web application
  - `web-e2e` - End-to-end tests for web application
- `apps-standalone/` - Applications not yet integrated with Nx
  - `ayokoding-web` - Hugo-based multilingual website (ID/EN)
  - `analisapasar-web` - Hugo-based market analysis website
  - `wahidyankf-web` - Personal Next.js website
  - `wahidyankf-e2e` - Playwright E2E tests
  - `python-mastery` - Python learning materials and examples
- `libs/` - Shared libraries and components
- `scripts/` - Utility scripts for project management

## Development Commands

### Monorepo (Nx) Applications

```bash
# Development server
npx nx serve next-hello

# Build application
npx nx build next-hello

# Run tests
npx nx test next-hello

# Type checking
npx nx typecheck next-hello

# Run multiple targets across all projects
npx nx run-many --target=test
npx nx run-many --target=typecheck
npx nx run-many --target=build
```

### Standalone Applications

```bash
# Next.js App (wahidyankf-web)
npm run wahidyankf-web:dev      # Development server
npm run wahidyankf-web:build    # Production build
cd apps-standalone/wahidyankf-web && npm run test:unit  # Unit tests
cd apps-standalone/wahidyankf-web && npm run test:e2e   # E2E tests

# Hugo Apps (ayokoding-web, analisapasar-web)
npm run ayokoding-web:dev       # Hugo development server
npm run ayokoding-web:build     # Hugo production build
npm run analisapasar-web:dev    # Hugo development server
npm run analisapasar-web:build  # Hugo production build

# All standalone builds
npm run build:standalone
```

### Testing

```bash
# Run all tests (monorepo + standalone)
npm run test:all

# Run only standalone tests
npm run test:all:standalone

# Run E2E tests for wahidyankf-web
cd apps-standalone/wahidyankf-web && npm run test:e2e
cd apps-standalone/wahidyankf-web && npm run test:e2e:watch  # Interactive UI
```

### Code Quality

```bash
# Linting and formatting handled by Git hooks
# Manual formatting
prettier --write .      # JavaScript/TypeScript files
black --quiet .        # Python files

# Type checking
npm run typecheck      # All Nx projects
```

### Python Development

For Python projects in `apps-standalone/python-mastery`:

```bash
# Activate virtual environment
pyenv activate interview-learn-private

# Install dependencies
pip install -r requirements.txt

# Run Python scripts
python main.py

# Run tests
python -m pytest
```

## Architecture Overview

### Technology Stack

- **Monorepo Management**: Nx
- **Node Version**: 22.20.0 (managed by Volta)
- **npm Version**: 11.1.0 (managed by Volta)
- **Frontend Frameworks**:
  - Next.js 14.x/15.x for React applications
  - Hugo for static sites
- **Styling**: Tailwind CSS
- **Testing**:
  - Jest + Testing Library for unit tests
  - Playwright for E2E tests
  - Vitest for wahidyankf-web
- **Languages**: TypeScript, JavaScript, Python
- **Code Quality**: Prettier, ESLint, Black (Python)

### Key Architectural Decisions

1. **Hybrid Monorepo Structure**: Uses Nx for integrated apps while maintaining standalone apps that are difficult to integrate or experimental
2. **Multiple Build Systems**: Hugo for static sites, Next.js for React apps
3. **Volta for Node Management**: Ensures consistent Node/npm versions across all projects
4. **Git Hooks with Husky**: Automatic formatting and commit message validation

## Commit Message Convention

Follows conventional commits with these types:

- `build`: Build system changes
- `chore`: Maintenance tasks
- `ci`: CI/CD changes
- `docs`: Documentation
- `feat`: New features
- `fix`: Bug fixes
- `perf`: Performance improvements
- `refactor`: Code restructuring
- `revert`: Reverting commits
- `style`: Code style changes
- `test`: Test additions/changes

Format: `type(scope): subject` (sentence-case subject, max 72 chars)

## Important Configuration Files

- `nx.json` - Nx workspace configuration
- `commitlint.config.js` - Commit message rules
- `.nvmrc` / package.json volta - Node version specification
- `tsconfig.base.json` - Shared TypeScript configuration
- Individual `package.json` files in standalone apps for specific configurations

## Development Workflow

1. **Before starting**: Run `npm install` to set up dependencies and Git hooks
2. **Health check**: Run `npm run doctor` to verify environment setup
3. **Choose workspace**: Work in either Nx-integrated apps or standalone apps
4. **Follow conventions**: Code style is enforced via Git hooks
5. **Test before commit**: Pre-push hooks run tests for affected projects

## Special Notes

- The `prepare` script ensures Git hooks are executable
- Python files are formatted with Black on commit
- Standalone Hugo apps have their own build scripts (build.sh)
- E2E tests use Playwright with multiple browser configurations
- The repository supports multilingual content (EN/ID) in Hugo sites
