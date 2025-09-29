# Development Workflow

This guide outlines the recommended development workflow for contributing to the OSS monorepo.

## Branch Strategy

### Main Branch

- `main`: Production-ready code
- Protected branch with required checks
- Direct commits not allowed

### Feature Branches

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or for different types
git checkout -b fix/bug-description
git checkout -b docs/documentation-update
git checkout -b refactor/code-improvement
```

## Development Cycle

### 1. Start with Latest Code

```bash
# Ensure you're on main
git checkout main

# Pull latest changes
git pull origin main

# Create your branch
git checkout -b feature/new-feature
```

### 2. Make Changes

#### For Nx-Integrated Projects

```bash
# Start development server
npx nx serve next-hello

# Run tests in watch mode
npx nx test next-hello --watch

# Check affected projects
npx nx affected:test
npx nx affected:build
```

#### For Standalone Projects

```bash
# Navigate to project
cd apps-standalone/wahidyankf-web

# Run development server
npm run dev

# Run tests
npm test
```

### 3. Code Quality Checks

Before committing, ensure code quality:

```bash
# Format code (automatic on commit)
npm run format  # If available in project

# Or manually
prettier --write .
black . --quiet  # For Python files

# Run linting
npx nx lint next-hello  # For Nx projects
npm run lint  # For standalone projects

# Type checking
npx nx typecheck next-hello
npm run typecheck  # If available
```

### 4. Commit Changes

#### Commit Message Format

```bash
# Format: type(scope): subject

# Examples:
git commit -m "feat(wahidyankf-web): add dark mode toggle"
git commit -m "fix(ayokoding): correct navigation links"
git commit -m "docs: update getting started guide"
git commit -m "refactor(python-mastery): reorganize module structure"
```

#### Types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks
- `build`: Build system changes
- `ci`: CI/CD changes
- `perf`: Performance improvements
- `revert`: Reverting previous commits

### 5. Push and Create PR

```bash
# Push your branch
git push -u origin feature/your-feature-name

# Create PR using GitHub CLI
gh pr create --title "feat: add new feature" --body "Description of changes"

# Or create via GitHub web interface
```

## Working with Multiple Projects

### Check Affected Projects

```bash
# See which projects are affected by your changes
npx nx affected:graph

# Run tests only for affected projects
npx nx affected:test

# Build affected projects
npx nx affected:build
```

### Running Multiple Dev Servers

```bash
# Terminal 1: Next.js app
npm run wahidyankf-web:dev

# Terminal 2: Hugo site
npm run ayokoding-web:dev

# Terminal 3: Run tests in watch mode
cd apps-standalone/wahidyankf-web && npm run test:unit:watch
```

## Git Hooks

Automatic checks run via Husky:

### Pre-commit

- Formats staged files with Prettier (JS/TS)
- Formats Python files with Black
- Prevents commits with linting errors

### Commit-msg

- Validates commit message format
- Ensures conventional commits

### Pre-push

- Runs tests for affected projects
- Ensures builds pass
- Only runs on main branch pushes

## Debugging

### VS Code Debugging

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: debug",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev",
      "cwd": "${workspaceFolder}/apps-standalone/wahidyankf-web"
    },
    {
      "name": "Jest: debug tests",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/.bin/jest",
      "args": ["--runInBand"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen"
    }
  ]
}
```

### Browser DevTools

1. Next.js apps: Use React Developer Tools
2. Hugo sites: Standard browser DevTools
3. Enable source maps in development

## Best Practices

### 1. Small, Focused Commits

- One logical change per commit
- Easy to review and revert
- Clear commit messages

### 2. Test Before Push

```bash
# Run all tests locally
npm run test:all

# Or for specific project
npm test
```

### 3. Keep Dependencies Updated

```bash
# Check for updates
npm outdated

# Update carefully
npm update package-name
```

### 4. Document Your Changes

- Update relevant README files
- Add JSDoc comments for complex functions
- Update this documentation if needed

### 5. Clean Up

```bash
# After PR is merged
git checkout main
git pull origin main
git branch -d feature/your-feature-name
```

## Troubleshooting Common Issues

### Merge Conflicts

```bash
# Update your branch with latest main
git checkout main
git pull origin main
git checkout feature/your-branch
git rebase main

# Resolve conflicts
# Then continue
git rebase --continue
```

### Failed Hooks

If git hooks fail:

```bash
# Bypass hooks (use sparingly)
git commit --no-verify

# Fix issues and amend
git commit --amend
```

### Build Failures

```bash
# Clean and rebuild
npx nx reset  # Clear Nx cache
rm -rf node_modules
npm install
```

## Continuous Integration

When you push:

1. GitHub Actions run (if configured)
2. Tests execute for affected projects
3. Build verification
4. PR checks must pass before merge

## Getting Help

- Check project-specific READMEs
- Review [Troubleshooting Guide](./troubleshoot-issues.md)
- Ask in PR comments
- Check existing issues
