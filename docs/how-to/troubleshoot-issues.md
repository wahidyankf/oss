# Troubleshooting Guide

Common issues and their solutions across the monorepo.

## General Issues

### Node Version Mismatch

**Symptoms**:

- `npm install` fails
- "Engine incompatible" errors
- Different behavior between developers

**Solution**:

```bash
# Ensure Volta is installed
volta --version

# If not installed
curl https://get.volta.sh | bash

# Restart terminal and try again
npm install
```

**Alternative (without Volta)**:

```bash
# Check required version
cat package.json | grep "node"
# Should show: "node": "22.20.0"

# Install correct version with nvm
nvm install 22.20.0
nvm use 22.20.0
```

### Permission Errors

**Symptoms**:

- "Permission denied" when running scripts
- Git hooks not executing
- Build scripts failing

**Solution**:

```bash
# Fix script permissions
chmod +x scripts/*.js
chmod +x scripts/*.sh

# Fix git hooks
npm run prepare

# If still failing
rm -rf .husky
npm run prepare
```

### Dependency Installation Failures

**Symptoms**:

- `npm install` hangs or fails
- Package conflicts
- Peer dependency warnings

**Solution**:

```bash
# Clean install
rm -rf node_modules package-lock.json
npm cache clean --force
npm install

# If specific package fails
npm install problematic-package --legacy-peer-deps
```

## Nx-Specific Issues

### Nx Commands Not Working

**Symptoms**:

- "nx: command not found"
- "Cannot find module '@nx/workspace'"

**Solution**:

```bash
# Install Nx globally (optional)
npm install -g nx

# Or use npx (recommended)
npx nx --version

# Reset Nx
npx nx reset
npm install
```

### Nx Cache Issues

**Symptoms**:

- Old build outputs served
- Changes not reflected
- "Cache hit" for modified code

**Solution**:

```bash
# Clear Nx cache
npx nx reset

# Clear all caches
rm -rf node_modules/.cache
rm -rf .nx

# Run without cache
npx nx build project-name --skip-nx-cache
```

### Affected Commands Not Detecting Changes

**Symptoms**:

- `nx affected:test` runs nothing
- Changes not detected between commits

**Solution**:

```bash
# Ensure you're comparing correct branches
git fetch origin main
npx nx affected:test --base=origin/main --head=HEAD

# Check git status
git status

# Verify Nx sees changes
npx nx affected:graph --base=origin/main
```

## Next.js Issues

### Build Failures

**Symptoms**:

- "Module not found" errors
- Type errors during build
- "Cannot find module 'next/server'"

**Solution**:

```bash
# Clear Next.js cache
rm -rf .next

# Reinstall Next.js
npm uninstall next
npm install next@14.2.13  # Or appropriate version

# Check TypeScript config
npx tsc --noEmit
```

### Development Server Issues

**Symptoms**:

- Port already in use
- Hot reload not working
- Styles not updating

**Solution**:

```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Or use different port
next dev -p 3001

# For hot reload issues
rm -rf .next
npm run dev
```

### Tailwind CSS Not Working

**Symptoms**:

- Styles not applied
- Classes not generated
- Dark mode not working

**Solution**:

```bash
# Check Tailwind config
cat tailwind.config.js

# Ensure content paths are correct
# Should include: './src/**/*.{js,ts,jsx,tsx}'

# Rebuild
rm -rf .next
npm run dev
```

## Hugo Issues

### Hugo Command Not Found

**Symptoms**:

- "hugo: command not found"
- Build scripts failing

**Solution**:

```bash
# Install Hugo (macOS)
brew install hugo

# Install Hugo (Linux)
sudo snap install hugo

# Or download from https://gohugo.io/

# Verify installation
hugo version
```

### Theme Not Loading

**Symptoms**:

- Blank pages
- "Theme not found" errors
- Broken layouts

**Solution**:

```bash
# Check theme installation
cd apps-standalone/ayokoding-web
ls themes/

# If missing, check hugo.yaml
cat hugo.yaml | grep theme

# Update theme
cd themes/hextra
git pull origin main
```

### Content Not Appearing

**Symptoms**:

- New content not showing
- Multilingual content missing
- Draft content not visible

**Solution**:

```bash
# Include drafts in development
hugo server -D

# Check content front matter
# Ensure draft: false for production

# Check language configuration
cat hugo.yaml | grep defaultContentLanguage
```

## Python Issues

### Virtual Environment Problems

**Symptoms**:

- "No module named" errors
- Wrong Python version
- pip install failures

**Solution**:

```bash
# Check Python version
python --version

# Set correct version with pyenv
pyenv install 3.13.2
pyenv local 3.13.2

# Recreate virtual environment
rm -rf venv
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Black Formatting Errors

**Symptoms**:

- Git commit fails
- "Black not found" errors
- Formatting conflicts

**Solution**:

```bash
# Install Black globally
pip install black

# Or in virtual environment
source venv/bin/activate
pip install black

# Format manually
black . --quiet
```

## Testing Issues

### Jest Test Failures

**Symptoms**:

- "Cannot find module" in tests
- Transform errors
- Unexpected token errors

**Solution**:

```bash
# Clear Jest cache
npx jest --clearCache

# Check Jest config
cat jest.config.js

# Run with no cache
npx jest --no-cache

# Debug specific test
npx jest path/to/test --verbose
```

### Playwright Issues

**Symptoms**:

- Browser launch failures
- Timeout errors
- "Executable doesn't exist"

**Solution**:

```bash
# Install browsers
npx playwright install

# Install with dependencies (Linux)
npx playwright install --with-deps

# Run specific browser
npx playwright test --project=chromium

# Increase timeout
npx playwright test --timeout=60000
```

### Vitest Not Working

**Symptoms**:

- Configuration errors
- Module resolution issues
- UI mode not opening

**Solution**:

```bash
# Check Vitest version
npx vitest --version

# Run with specific config
npx vitest --config vitest.config.ts

# Clear cache and retry
rm -rf node_modules/.vite
npm run test
```

## Git Issues

### Pre-commit Hook Failures

**Symptoms**:

- Commits blocked
- Formatting not applied
- "husky - pre-commit hook exited with code 1"

**Solution**:

```bash
# Run formatters manually
prettier --write .
black . --quiet

# Bypass hooks (emergency only)
git commit --no-verify -m "message"

# Reinstall hooks
rm -rf .husky
npm run prepare
```

### Merge Conflicts in Lock Files

**Symptoms**:

- package-lock.json conflicts
- Dependency version mismatches

**Solution**:

```bash
# Delete and regenerate
git checkout main -- package-lock.json
npm install
git add package-lock.json

# Or accept incoming and reinstall
git checkout --theirs package-lock.json
npm install
```

## Build & Deployment Issues

### Production Build Failures

**Symptoms**:

- Build works locally but fails in CI
- Environment variable errors
- Memory errors

**Solution**:

```bash
# Check environment variables
cp .env.example .env.local

# Increase Node memory
export NODE_OPTIONS="--max-old-space-size=4096"
npm run build

# Build with verbose logging
NEXT_PUBLIC_DEBUG=true npm run build
```

### Vercel Deployment Issues

**Symptoms**:

- Build fails on Vercel
- Wrong Node version
- Missing dependencies

**Solution**:

1. Check `vercel.json` configuration
2. Ensure Node version matches:
   ```json
   {
     "engines": {
       "node": "22.x"
     }
   }
   ```
3. Check build command in Vercel dashboard

## Performance Issues

### Slow Development Server

**Symptoms**:

- Long startup times
- Slow hot reload
- High memory usage

**Solution**:

```bash
# Limit file watching
# Add to next.config.js:
module.exports = {
  watchOptions: {
    ignored: /node_modules/,
  },
}

# Clear caches
rm -rf .next
rm -rf node_modules/.cache

# Use turbo mode (Next.js)
next dev --turbo
```

### Slow Test Execution

**Symptoms**:

- Tests take too long
- Timeout errors
- Memory issues

**Solution**:

```bash
# Run tests in parallel
npx jest --maxWorkers=4

# Run only changed tests
npx jest -o

# Skip heavy tests in watch mode
npx jest --watch --testPathIgnorePatterns="e2e"
```

## Getting Help

### Debug Information

Gather this information when reporting issues:

```bash
# System info
uname -a              # OS info
node --version       # Node version
npm --version        # npm version
npx nx report        # Nx environment

# Project state
git status
git log --oneline -5
npm list --depth=0
```

### Logs Location

- Nx logs: `node_modules/.cache/nx`
- Next.js logs: `.next/trace`
- npm logs: `~/.npm/_logs/`

### Community Resources

1. **Project Issues**: [GitHub Issues](https://github.com/wahidyankf/oss/issues)
2. **Nx Community**: [Nx Discord](https://go.nx.dev/community)
3. **Next.js**: [Next.js Discord](https://nextjs.org/discord)
4. **Hugo**: [Hugo Forums](https://discourse.gohugo.io/)
