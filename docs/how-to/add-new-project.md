# Adding a New Project

This guide explains how to add new projects to the monorepo, either as Nx-integrated or standalone.

## Decision Tree

Before adding a project, consider:

```
Is it a JavaScript/TypeScript project?
│
├─ No → Add as Standalone
│
└─ Yes → Will it use React/Next.js/Node?
         │
         ├─ No → Add as Standalone
         │
         └─ Yes → Does it need special build process?
                  │
                  ├─ Yes → Add as Standalone
                  │
                  └─ No → Add as Nx-integrated
```

## Adding an Nx-Integrated Project

### 1. Generate with Nx

#### Next.js Application

```bash
# Generate Next.js app
npx nx g @nx/next:application my-new-app \
  --directory=apps/my-new-app \
  --style=css \
  --appDir=true

# With options
npx nx g @nx/next:application my-new-app \
  --tags="type:app,scope:public" \
  --unitTestRunner=jest \
  --e2eTestRunner=none
```

#### React Application

```bash
npx nx g @nx/react:application my-react-app \
  --directory=apps/my-react-app \
  --routing=true \
  --style=css
```

#### Node/Express API

```bash
npx nx g @nx/node:application my-api \
  --directory=apps/my-api \
  --framework=express
```

#### Library (Future)

Note: The `libs/` directory doesn't exist yet. To create libraries:

```bash
# First create the libs directory
mkdir -p libs

# Then generate libraries
# UI component library
npx nx g @nx/react:library ui-components \
  --directory=libs/ui-components \
  --component=false \
  --publishable

# Utility library
npx nx g @nx/js:library utils \
  --directory=libs/utils \
  --unitTestRunner=jest
```

### 2. Configure Project

#### Update project.json

```json
{
  "$schema": "../../node_modules/nx/schemas/project-schema.json",
  "sourceRoot": "apps/my-new-app/src",
  "projectType": "application",
  "tags": ["type:app", "scope:public"],
  "targets": {
    "build": {
      "executor": "@nx/next:build",
      "options": {
        "outputPath": "dist/apps/my-new-app"
      },
      "configurations": {
        "production": {
          "optimization": true
        }
      }
    },
    "serve": {
      "executor": "@nx/next:server",
      "options": {
        "buildTarget": "my-new-app:build:development"
      }
    },
    "lint": {
      "executor": "@nx/linter:eslint",
      "options": {
        "lintFilePatterns": ["apps/my-new-app/**/*.{ts,tsx,js,jsx}"]
      }
    },
    "test": {
      "executor": "@nx/jest:jest",
      "options": {
        "jestConfig": "apps/my-new-app/jest.config.js"
      }
    }
  }
}
```

### 3. Add to Root Scripts

Update root `package.json`:

```json
{
  "scripts": {
    "my-new-app:dev": "nx serve my-new-app",
    "my-new-app:build": "nx build my-new-app",
    "my-new-app:test": "nx test my-new-app"
  }
}
```

### 4. Configure TypeScript

Extend base configuration:

```json
// apps/my-new-app/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "jsx": "preserve"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

## Adding a Standalone Project

### 1. Create Project Structure

```bash
# Create directory
mkdir -p apps-standalone/my-standalone-app
cd apps-standalone/my-standalone-app

# Initialize project
npm init -y

# Add Volta configuration
npm pkg set volta.node="22.20.0"
npm pkg set volta.npm="11.1.0"
```

### 2. Install Dependencies

#### For Next.js

```bash
npm install next react react-dom
npm install -D typescript @types/react @types/node
npm install -D eslint eslint-config-next
npm install -D tailwindcss postcss autoprefixer
```

#### For Hugo

```bash
# Hugo doesn't need npm dependencies
# Just create hugo site
hugo new site . --force
```

#### For Python

```bash
# Create requirements.txt
echo "pytest>=7.0.0" > requirements.txt
echo "black>=22.0.0" >> requirements.txt

# Create .python-version
echo "3.13.2" > .python-version
```

### 3. Add Standard Files

#### README.md

````markdown
# My Standalone App

Description of the project.

## Setup

```bash
npm install
```
````

## Development

```bash
npm run dev
```

## Testing

```bash
npm test
```

## Build

```bash
npm run build
```

```

#### .gitignore
```

# Dependencies

node_modules/
venv/
**pycache**/

# Build outputs

.next/
dist/
build/
public/ # For Hugo

# Environment

.env.local
.env\*.local

# IDE

.vscode/
.idea/

# OS

.DS_Store
Thumbs.db

````

### 4. Configure Scripts

#### package.json scripts
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest",
    "format": "prettier --write ."
  }
}
````

### 5. Add to Root Scripts

Update root `package.json`:

```json
{
  "scripts": {
    "my-standalone:dev": "cd apps-standalone/my-standalone-app && npm run dev",
    "my-standalone:build": "cd apps-standalone/my-standalone-app && npm run build",
    "build:standalone": "npm run ayokoding-web:build && npm run analisapasar-web:build && npm run wahidyankf-web:build && npm run my-standalone:build"
  }
}
```

## Integration Steps

### 1. Update Documentation

1. Add to `/docs/reference/standalone-projects.md` or `/docs/reference/nx-projects.md`
2. Update main README.md project list
3. Create project-specific README.md

### 2. Configure Git Hooks

For standalone projects with own package.json:

```bash
cd apps-standalone/my-project
npm install -D husky lint-staged
npm pkg set scripts.prepare="husky install"
npm run prepare
```

### 3. Set Up Testing

#### Jest Configuration

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
};
```

#### Vitest Configuration

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: './src/test/setup.ts',
  },
});
```

### 4. Add to CI/CD

If using GitHub Actions:

```yaml
# .github/workflows/ci.yml
jobs:
  test-my-app:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: volta-cli/action@v4
      - run: npm ci
      - run: npm run my-app:test
      - run: npm run my-app:build
```

## Project Templates

### Next.js Template Structure

```
my-next-app/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   └── lib/
├── public/
├── package.json
├── tsconfig.json
├── next.config.js
├── tailwind.config.js
└── README.md
```

### Hugo Template Structure

```
my-hugo-site/
├── archetypes/
├── content/
│   ├── en/
│   └── id/
├── layouts/
├── static/
├── themes/
├── hugo.yaml
├── package.json
└── README.md
```

### Python Template Structure

```
my-python-project/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
├── .python-version
├── pyproject.toml
└── README.md
```

## Best Practices

### 1. Naming Conventions

- Use kebab-case for project names
- Suffix with project type: `-web`, `-api`, `-lib`
- Be descriptive but concise

### 2. Dependencies

- Pin major versions in package.json
- Use exact versions for critical dependencies
- Regular updates with testing

### 3. Configuration

- Extend shared configs where possible
- Document any special requirements
- Keep configuration files at project root

### 4. Documentation

- Always include README.md
- Document setup steps
- Include architecture decisions
- Add usage examples

### 5. Testing

- Set up tests from the start
- Aim for 80%+ coverage
- Include in CI/CD pipeline

## Checklist

- [ ] Project structure created
- [ ] Dependencies installed
- [ ] Volta configuration added
- [ ] Scripts configured in package.json
- [ ] Added to root package.json scripts
- [ ] README.md created
- [ ] Added to documentation
- [ ] Git hooks configured
- [ ] Tests set up
- [ ] Added to CI/CD
- [ ] First commit made
