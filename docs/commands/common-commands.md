# Common Commands Reference

Quick reference for frequently used commands across the monorepo.

## Global Commands (from root)

### Setup and Installation

```bash
# Initial setup (installs dependencies and git hooks)
npm install

# Verify environment setup
npm run doctor

# Manually set up git hooks
npm run prepare
```

### Development Servers

```bash
# Nx-integrated apps
npx nx serve next-hello

# Standalone apps
npm run wahidyankf-web:dev     # Next.js portfolio
npm run ayokoding-web:dev      # Hugo educational site
npm run analisapasar-web:dev   # Hugo market analysis
```

### Building

```bash
# Build all projects
npm run build

# Build Nx projects
npx nx build next-hello
npx nx run-many --target=build

# Build standalone projects
npm run build:standalone       # All standalone
npm run wahidyankf-web:build  # Specific project
```

### Testing

```bash
# Run all tests
npm run test:all

# Test Nx projects
npx nx test next-hello
npx nx affected:test          # Only affected

# Test standalone projects
npm run test:all:standalone
```

## Nx Commands

### Project Management

```bash
# View dependency graph
npx nx graph

# View affected projects
npx nx affected:graph

# List all projects
npx nx list

# Show project details
npx nx show project next-hello
```

### Running Tasks

```bash
# Run single target
npx nx build next-hello
npx nx test next-hello
npx nx lint next-hello

# Run multiple projects
npx nx run-many --target=build --projects=proj1,proj2
npx nx run-many --target=test --all

# Run for affected only
npx nx affected:build
npx nx affected:test
npx nx affected:lint
```

### Cache Management

```bash
# Clear Nx cache
npx nx reset

# Run without cache
npx nx build next-hello --skip-nx-cache

# View cache status
npx nx report
```

## Git Commands

### Branching

```bash
# Create feature branch
git checkout -b feature/description
git checkout -b fix/bug-description
git checkout -b docs/update-description

# Update branch with latest main
git checkout main
git pull origin main
git checkout feature/branch
git rebase main
```

### Committing

```bash
# Stage and commit with conventional message
git add .
git commit -m "feat(scope): add new feature"
git commit -m "fix: resolve navigation bug"
git commit -m "docs: update README"

# Amend last commit
git commit --amend

# Interactive rebase
git rebase -i HEAD~3
```

### GitHub CLI

```bash
# Create pull request
gh pr create --title "feat: add feature" --body "Description"

# List PRs
gh pr list

# Check PR status
gh pr status
```

## Project-Specific Commands

### wahidyankf-web (Next.js)

```bash
cd apps-standalone/wahidyankf-web

# Development
npm run dev              # Start dev server
npm run build           # Production build
npm start               # Start production server

# Testing
npm test                # Run unit tests
npm run test:unit:watch # Watch mode
npm run test:e2e        # Playwright tests
npm run test:e2e:watch  # Playwright UI mode

# Code quality
npm run lint            # ESLint
npm run format          # Prettier
npm run typecheck       # TypeScript
```

### ayokoding-web / analisapasar-web (Hugo)

```bash
cd apps-standalone/ayokoding-web

# Development
hugo server             # Dev server with drafts
hugo server -D          # Include draft content
npm run dev             # Using npm script

# Content management
hugo new content/en/learn/topic.md    # English content
hugo new content/id/belajar/topik.md  # Indonesian content

# Building
hugo                    # Build site
hugo --minify          # Minified build
npm run build          # Using npm script
./build.sh             # Custom build script
```

### python-mastery (Python)

```bash
cd apps-standalone/python-mastery

# Environment setup
pyenv local 3.13.2      # Set Python version
python -m venv venv     # Create virtual env
source venv/bin/activate # Activate (Unix)
venv\Scripts\activate   # Activate (Windows)

# Development
python main.py          # Run main script
python -m pytest        # Run tests
python -m pytest -v     # Verbose tests

# Code quality
black .                 # Format code
pylint src/            # Lint code
```

### wahidyankf-e2e (Playwright)

```bash
cd apps-standalone/wahidyankf-e2e

# Setup
npx playwright install  # Install browsers

# Testing
npm test                # Run all tests
npx playwright test     # Run all tests
npx playwright test --ui # Interactive UI
npx playwright test --headed # See browser

# Specific tests
npx playwright test home.spec.ts
npx playwright test --grep "navigation"

# Debugging
npx playwright test --debug
npx playwright codegen localhost:3000
```

## Development Utilities

### Code Formatting

```bash
# Format all JavaScript/TypeScript
prettier --write "**/*.{js,jsx,ts,tsx,json,md}"

# Format Python files
black . --quiet

# Check formatting without changing
prettier --check .
black . --check
```

### Dependency Management

```bash
# Check outdated packages
npm outdated

# Update dependencies
npm update              # Update to latest minor
npm install pkg@latest  # Update to latest major

# Audit for vulnerabilities
npm audit
npm audit fix
```

### Environment Variables

```bash
# Create local env file
cp .env.example .env.local

# Using direnv
direnv allow
direnv reload
```

## Troubleshooting Commands

### Clear Caches

```bash
# Clear all caches
npx nx reset                    # Nx cache
rm -rf .next                   # Next.js cache
rm -rf node_modules/.cache     # General cache
rm -rf resources/_gen          # Hugo cache
```

### Reinstall Dependencies

```bash
# Clean reinstall
rm -rf node_modules package-lock.json
npm install

# For Python
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Debug Information

```bash
# System information
node --version
npm --version
hugo version
python --version

# Project information
npx nx report
npm list --depth=0
```

## Quick Command Aliases

Add to your shell profile (.bashrc, .zshrc):

```bash
# Navigation
alias oss='cd ~/path/to/oss'
alias ossweb='cd ~/path/to/oss/apps-standalone/wahidyankf-web'

# Common commands
alias nxs='npx nx serve'
alias nxb='npx nx build'
alias nxt='npx nx test'
alias nxa='npx nx affected'

# Development
alias dev-web='npm run wahidyankf-web:dev'
alias dev-ayo='npm run ayokoding-web:dev'
alias test-all='npm run test:all'
```

## VS Code Tasks

Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Dev: wahidyankf-web",
      "type": "npm",
      "script": "wahidyankf-web:dev",
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Test: All",
      "type": "npm",
      "script": "test:all",
      "group": "test"
    }
  ]
}
```

Run with: `Cmd/Ctrl + Shift + P` > "Tasks: Run Task"
