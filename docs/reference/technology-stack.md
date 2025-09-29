# Technology Stack

This document details all technologies, frameworks, and tools used across the monorepo.

## Core Technologies

### Version Management

- **Volta**: Node.js version manager
  - Node.js: 22.20.0
  - npm: 11.1.0
- **pyenv**: Python version management
  - Python: 3.13.2 (for python-mastery)

### Monorepo Management

- **Nx**: 20.x
  - Workspace orchestration
  - Build caching
  - Affected commands
  - Dependency graph visualization

### Frontend Frameworks

#### React-based

- **Next.js**: 14.x - 15.x
  - wahidyankf-web: 14.2.13
  - next-hello: 15.1.6
- **React**: 18.x
- **React DOM**: 18.x

#### Static Site Generators

- **Hugo**: Latest
  - ayokoding-web
  - analisapasar-web
  - Uses Hextra theme

### Languages

- **TypeScript**: 5.4.2
- **JavaScript**: ES2017+
- **Python**: 3.13.2
- **Go**: (for Hugo development)

### Styling

- **Tailwind CSS**: 3.x - 4.x
- **PostCSS**: 8.x
- **Autoprefixer**: 10.x
- **CSS Modules**: For component-scoped styles
- **Tailwind Merge**: Utility for merging Tailwind classes
- **class-variance-authority**: For component variants

### Testing

#### Unit Testing

- **Jest**: 29.x
- **Vitest**: 0.31.x (wahidyankf-web)
- **Testing Library**:
  - React: 14.x - 16.x
  - Jest DOM: 5.x - 6.x

#### E2E Testing

- **Playwright**: 1.48.x
  - Multiple browser support
  - Mobile viewport testing

#### Python Testing

- **pytest**: For python-mastery project

### Code Quality

#### Linting

- **ESLint**: 8.x
- **eslint-config-next**: For Next.js projects

#### Formatting

- **Prettier**: 2.x - 3.x
  - JavaScript/TypeScript
  - Markdown
  - JSON/YAML
- **Black**: Latest
  - Python code formatting

#### Git Hooks

- **Husky**: 9.x
- **lint-staged**: 13.x - 15.x
- **commitlint**: 19.x
  - Conventional commits enforcement

### Build Tools

- **Webpack**: (via Next.js)
- **Vite**: 4.x (for Vitest)
- **Babel**: 7.x
  - Various presets and plugins
- **TypeScript Compiler**: Via ts-node

### Development Tools

- **nodemon**: For development servers
- **ts-node**: TypeScript execution
- **identity-obj-proxy**: CSS module mocking

### UI Libraries

- **Lucide React**: Icon library
- **React Icons**: Additional icons
- **tailwindcss-animate**: Animation utilities

### Analytics & SEO

- **@next/third-parties**: Google Analytics integration
- **Google Tag Manager**: Via Next.js integration

### Documentation

- **Markdown**: Primary documentation format
- **Hugo Hextra Theme**: Documentation theme
- **CommonMark**: Markdown specification

## Technology Choices by Project

### wahidyankf-web

- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Vitest for testing
- Playwright for E2E

### ayokoding-web

- Hugo static site generator
- Hextra theme
- Multilingual support (ID/EN)
- GitHub Pages compatible

### python-mastery

- Python 3.13.2
- Virtual environments via pyenv
- Black for formatting
- pytest for testing

### next-hello

- Next.js 15 (latest)
- TypeScript
- Jest for testing
- Nx integration

## Version Pinning Strategy

1. **Exact Versions**: For critical dependencies
2. **Minor Version Ranges**: For stable packages
3. **Volta**: Ensures consistent Node/npm versions
4. **Lock Files**: Both package-lock.json and go.sum

## Future Technology Considerations

- Migration to Nx for all projects
- Shared component library
- Unified testing strategy
- Container orchestration
- CI/CD pipeline improvements
