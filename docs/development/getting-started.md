# Getting Started

This guide will help you set up the OSS monorepo development environment.

## Prerequisites

### Required Software

1. **Git**: Version control

   ```bash
   git --version  # Should be 2.x or higher
   ```

2. **Volta**: Node.js version management

   ```bash
   # Install Volta
   curl https://get.volta.sh | bash

   # Verify installation
   volta --version
   ```

3. **Python** (for Python projects and Black formatter):

   ```bash
   # Install pyenv (macOS/Linux)
   curl https://pyenv.run | bash

   # Install Python 3.13.2
   pyenv install 3.13.2
   ```

4. **Black** (Python formatter):

   ```bash
   pip install black
   ```

5. **Hugo** (for static sites):

   ```bash
   # macOS
   brew install hugo

   # Or download from https://gohugo.io/
   ```

### Recommended Software

- **VS Code**: With recommended extensions
- **GitHub CLI**: For PR creation
- **direnv**: For environment variables

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/wahidyankf/oss.git
cd oss
```

### 2. Install Dependencies

```bash
# Volta will automatically use correct Node version
npm install
```

This will:

- Install all npm dependencies
- Set up Git hooks via Husky
- Run the doctor script to verify environment

### 3. Verify Setup

```bash
# Run health check
npm run doctor

# Run a simple build
npm run next-hello:build
```

## Project-Specific Setup

### Next.js Applications

```bash
# wahidyankf-web
cd apps-standalone/wahidyankf-web
npm install
npm run dev  # Starts on http://localhost:3000

# next-hello
npm run next-hello:dev  # From root directory
```

### Hugo Sites

```bash
# ayokoding-web
cd apps-standalone/ayokoding-web
hugo server  # Starts on http://localhost:1313

# Or from root
npm run ayokoding-web:dev
```

### Python Projects

```bash
# python-mastery
cd apps-standalone/python-mastery
pyenv local 3.13.2  # Set Python version
python -m venv venv  # Create virtual environment

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### E2E Tests

```bash
cd apps-standalone/wahidyankf-e2e
npm install
npx playwright install  # Install browsers
npm run test:e2e
```

## Environment Variables

### Development Environment

Create `.env.local` files for projects that need them:

```bash
# apps-standalone/wahidyankf-web/.env.local
NEXT_PUBLIC_GA_ID=your-google-analytics-id
NEXT_PUBLIC_GTM_ID=your-google-tag-manager-id
```

### Using direnv (Recommended)

```bash
# Install direnv
brew install direnv  # macOS

# Create .envrc
echo 'export PROJECT_ENV="development"' > .envrc
direnv allow
```

## IDE Setup

### VS Code Extensions

Recommended extensions:

- ESLint
- Prettier
- Tailwind CSS IntelliSense
- TypeScript and JavaScript Language Features
- Python
- Hugo Language and Syntax Support
- Nx Console

### Settings

Create `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "typescript.tsdk": "node_modules/typescript/lib"
}
```

## Common Issues

### Node Version Mismatch

**Problem**: Node version doesn't match requirements

**Solution**: Ensure Volta is properly installed and restart terminal

```bash
volta install node@22.20.0
volta install npm@11.1.0
```

### Permission Errors

**Problem**: Permission denied when running scripts

**Solution**: Make scripts executable

```bash
chmod +x scripts/*.js
npm run prepare  # Re-run hook setup
```

### Hugo Build Failures

**Problem**: Hugo command not found

**Solution**: Install Hugo for your platform

```bash
# Verify Hugo installation
hugo version
```

## Next Steps

1. Read the [Development Workflow](./development-workflow.md)
2. Check project-specific READMEs
3. Review [Code Style](./code-style.md) guidelines
4. Set up your [Testing](./testing.md) environment
