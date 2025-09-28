# next-hello

A minimal Next.js application template integrated with Nx monorepo management.

## Overview

This project serves as a template and example of how to integrate Next.js applications within an Nx workspace. It demonstrates the basic setup and configuration needed for Nx-managed Next.js projects.

## Tech Stack

- **Framework**: Next.js 15.1.6
- **Language**: TypeScript 5.4.2
- **Styling**: Tailwind CSS 4.x
- **Testing**: Jest with React Testing Library
- **Monorepo**: Nx

## Getting Started

### Prerequisites

- Node.js 22.20.0 (managed by Volta)
- npm 11.1.0
- Nx CLI (optional, can use npx)

### Development

From the repository root:

```bash
# Start development server
npx nx serve next-hello
# or
npm run next-hello:dev

# The app will be available at http://localhost:3000
```

### Building

```bash
# Build for production
npx nx build next-hello
# or
npm run next-hello:build

# Output will be in dist/apps/next-hello
```

### Testing

```bash
# Run unit tests
npx nx test next-hello
# or
npm run next-hello:test

# Run tests in watch mode
npx nx test next-hello --watch

# Run tests with coverage
npx nx test next-hello --coverage
```

### Type Checking

```bash
# Run TypeScript type checking
npx nx typecheck next-hello
```

## Project Structure

```
next-hello/
├── src/
│   ├── app/                 # Next.js App Router
│   │   ├── api/             # API routes
│   │   │   └── hello/
│   │   ├── global.css      # Global styles
│   │   ├── layout.tsx      # Root layout
│   │   └── page.tsx        # Home page
│   └── test-setup.ts       # Jest configuration
├── public/                  # Static assets
├── project.json             # Nx project configuration
├── jest.config.js           # Jest configuration
├── next.config.js           # Next.js configuration
├── tsconfig.json            # TypeScript configuration
└── tsconfig.spec.json       # TypeScript test configuration
```

## Configuration

### Nx Integration

This project is configured in `project.json` with the following targets:

- `build`: Production build
- `serve`: Development server
- `lint`: ESLint checking
- `test`: Jest unit tests

### TypeScript

Extends the base TypeScript configuration from the monorepo root with Next.js specific settings.

### Tailwind CSS

Configured with the monorepo's shared Tailwind configuration, using the latest v4 approach.

## API Routes

Example API route available at `/api/hello`:

```typescript
// GET /api/hello
// Returns: { name: 'John Doe' }
```

## Extending This Template

### Adding Components

```bash
# Generate a new component
npx nx g @nx/react:component MyComponent --project=next-hello
```

### Adding Pages

Create new files in `src/app/` following Next.js App Router conventions:

```typescript
// src/app/about/page.tsx
export default function AboutPage() {
  return <div>About Page</div>
}
```

### Adding Libraries

This project can import shared libraries from the monorepo:

```typescript
import { someUtil } from '@ayokoding/shared-utils';
```

## Deployment

The build output can be deployed to any platform that supports Next.js:

```bash
# Build the application
npx nx build next-hello

# The output in dist/apps/next-hello can be deployed
```

## Troubleshooting

### Module Resolution Issues

If you encounter module resolution errors:

```bash
npx nx reset
npm install
```

### Port Conflicts

The default port is 3000. To use a different port:

```bash
PORT=3001 npx nx serve next-hello
```

## Related Documentation

- [Nx-Integrated Projects Guide](/docs/projects/nx-integrated.md)
- [Common Commands Reference](/docs/commands/common-commands.md)
- [Troubleshooting Guide](/docs/guides/troubleshooting.md)
