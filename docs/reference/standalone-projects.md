# Standalone Projects

This document covers projects in the `apps-standalone/` directory that operate independently of the Nx monorepo structure.

## Overview

Standalone projects maintain their independence for various reasons:

- Different build systems (e.g., Hugo)
- Legacy codebases not yet migrated
- Experimental projects
- Projects with conflicting dependencies
- External deployment requirements

## Project Directory

### 1. wahidyankf-web

**Type**: Next.js Application

**Purpose**: Professional portfolio website showcasing Wahidyan Kresna Fridayoka's experience

**Key Features**:

- Modern Next.js 14 with App Router
- Advanced CV search functionality
- Dark/light theme support
- SEO optimized
- Google Analytics integration

**Tech Stack**:

- Next.js 14.2.13
- TypeScript
- Tailwind CSS
- Vitest for testing
- Playwright for E2E

**Commands**:

```bash
cd apps-standalone/wahidyankf-web
npm install
npm run dev      # Start dev server
npm run build    # Production build
npm run test     # Run tests
npm run lint     # Lint code
```

### 2. ayokoding-web

**Type**: Hugo Static Site

**Purpose**: Bilingual educational platform for software engineering content

**Key Features**:

- Indonesian and English content
- Documentation-style layout
- YouTube integration (@AyoKoding channel)
- SEO optimized static site
- Hextra theme customization

**Tech Stack**:

- Hugo (latest)
- Markdown content
- Hextra documentation theme
- Multilingual support

**Commands**:

```bash
cd apps-standalone/ayokoding-web
npm run dev     # Hugo development server
npm run build   # Build static site
hugo new content/en/learn/new-topic.md  # Create content
```

### 3. analisapasar-web

**Type**: Hugo Static Site

**Purpose**: Market analysis platform (in development)

**Key Features**:

- Bilingual support (ID/EN)
- Documentation structure
- Hextra theme
- Template for market analysis content

**Tech Stack**:

- Hugo (latest)
- Hextra theme
- Markdown

**Commands**:

```bash
cd apps-standalone/analisapasar-web
npm run dev     # Development server
npm run build   # Production build
```

### 4. python-mastery

**Type**: Python Learning Repository

**Purpose**: Comprehensive Python learning curriculum from basics to advanced topics

**Key Features**:

- 32 structured topics
- Code examples for each concept
- Progressive difficulty
- Professional development topics

**Structure**:

```
python-mastery/
├── 01-fundamentals/
├── 02-intermediate-python/
├── 03-advanced-python/
└── 04-professional-development/
```

**Setup**:

```bash
cd apps-standalone/python-mastery
pyenv local 3.13.2
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 5. wahidyankf-e2e

**Type**: Playwright E2E Test Suite

**Purpose**: End-to-end testing for wahidyankf-web deployment

**Key Features**:

- Cross-browser testing
- Mobile viewport testing
- Component and page tests
- Visual regression capability

**Test Structure**:

```
tests/
├── components/
│   ├── navigation.spec.ts
│   └── theme.spec.ts
└── pages/
    ├── cv.spec.ts
    ├── home.spec.ts
    └── personal-projects.spec.ts
```

**Commands**:

```bash
cd apps-standalone/wahidyankf-e2e
npx playwright install  # Install browsers
npm test               # Run all tests
npx playwright test --ui  # Interactive mode
npx playwright codegen    # Generate test code
```

## Development Workflows

### Running Standalone Projects

From the root directory:

```bash
# Next.js projects
npm run wahidyankf-web:dev
npm run wahidyankf-web:build

# Hugo projects
npm run ayokoding-web:dev
npm run ayokoding-web:build
npm run analisapasar-web:dev
npm run analisapasar-web:build

# Build all standalone projects
npm run build:standalone
```

### Project-Specific Development

#### Hugo Projects

1. **Content Creation**:

   ```bash
   cd apps-standalone/ayokoding-web
   hugo new content/en/learn/new-topic.md
   hugo new content/id/belajar/topik-baru.md
   ```

2. **Theme Customization**:

   - Modify `hugo.yaml` for configuration
   - Override theme files in `layouts/`
   - Add custom CSS in `assets/`

3. **Build Process**:
   ```bash
   ./build.sh  # Custom build script
   # or
   hugo --minify
   ```

#### Next.js Projects

1. **Component Development**:

   ```bash
   # Run dev server with hot reload
   npm run dev

   # Run tests in watch mode
   npm run test:unit:watch
   ```

2. **API Routes**:

   - Located in `src/app/api/`
   - Follow Next.js 14 App Router conventions

3. **Styling**:
   - Tailwind CSS utilities
   - Component variants with CVA
   - Dark mode support

#### Python Projects

1. **Running Examples**:

   ```bash
   cd 01-fundamentals/01-syntax-semantics-environment
   python main.py
   ```

2. **Testing**:
   ```bash
   python -m pytest
   python -m pytest -v  # Verbose
   python -m pytest --cov=.  # With coverage
   ```

## Deployment

### Vercel (Next.js)

**wahidyankf-web**:

```json
// vercel.json
{
  "git": {
    "deploymentEnabled": {
      "main": false
    }
  }
}
```

Deploy command:

```bash
cd apps-standalone/wahidyankf-web && npm run build
```

### Static Hosting (Hugo)

**ayokoding-web / analisapasar-web**:

1. **Build**:

   ```bash
   npm run build
   # Output in public/ directory
   ```

2. **Deploy Options**:
   - Netlify (netlify.toml configured)
   - GitHub Pages
   - Vercel
   - Any static host

### E2E Testing in CI

```yaml
# Example GitHub Actions
- name: Run E2E tests
  run: |
    cd apps-standalone/wahidyankf-e2e
    npx playwright install
    npm test
```

## Maintenance

### Dependency Updates

Each project manages its own dependencies:

```bash
# Check outdated packages
cd apps-standalone/project-name
npm outdated

# Update dependencies
npm update  # Minor updates
npm install package@latest  # Major updates
```

### Version Management

- Node/npm versions managed by Volta
- Python version in `.python-version`
- Hugo version in build scripts

### Common Tasks

1. **Adding Git Hooks** (project-specific):

   ```bash
   cd apps-standalone/wahidyankf-web
   npm run prepare  # Sets up Husky
   ```

2. **Formatting**:

   ```bash
   # JavaScript/TypeScript
   prettier --write .

   # Python
   black .
   ```

3. **Linting**:

   ```bash
   # Next.js projects
   npm run lint

   # Python
   pylint src/
   ```

## Migration Path to Nx

### Candidates for Migration

1. **wahidyankf-web**: Good candidate

   - Already uses Next.js
   - Standard structure
   - Would benefit from shared dependencies

2. **wahidyankf-e2e**: Possible candidate
   - Could test multiple apps
   - Shared test utilities

### Challenges for Migration

1. **Hugo Projects**: Difficult

   - Different build system
   - No Nx executor for Hugo
   - Would need custom executor

2. **Python Projects**: Complex
   - Different runtime
   - Virtual environment requirements
   - Different dependency management

## Best Practices

### 1. Consistent Node Versions

All projects include:

```json
"volta": {
  "node": "22.20.0",
  "npm": "11.1.0"
}
```

### 2. Shared Git Hooks

Root-level Husky configuration applies to all:

- Pre-commit: Formatting
- Commit-msg: Conventional commits
- Pre-push: Tests (when applicable)

### 3. Documentation

Each project should maintain:

- README.md with setup instructions
- Architecture decisions
- Deployment documentation

### 4. Testing Strategy

- Unit tests co-located with code
- E2E tests in separate project
- Coverage goals documented

## Troubleshooting

### Hugo Build Issues

```bash
# Clear Hugo cache
rm -rf resources/_gen
hugo --cleanDestinationDir
```

### Next.js Issues

```bash
# Clear Next.js cache
rm -rf .next
npm run build
```

### Python Environment

```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
