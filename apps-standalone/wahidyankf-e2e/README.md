# WahidyanKF E2E Tests

End-to-end testing suite for WahidyanKF applications, built with [Playwright](https://playwright.dev/).

## Overview

This package contains end-to-end tests for:

- WahidyanKF Web (`apps/wahidyankf-web`)
- Future WahidyanKF applications

The tests are based on specifications defined in:

- `features/app/wahidyankf-web`
- Future WahidyanKF application specifications

## Getting Started

1. Install dependencies:

```bash
npm install
```

2. Install Playwright browsers:

```bash
npx playwright install
```

## Running Tests

### All Tests

```bash
npm run test
```

### Specific Test File

```bash
npx playwright test tests/example.spec.ts
```

### With UI Mode

```bash
npm run test:ui
```

## Test Structure

```
wahidyankf-e2e/
├── tests/                 # Main test directory
│   ├── example.spec.ts   # Example test file
│   └── ...              # Other test files
└── playwright.config.ts  # Playwright configuration
```

## Writing Tests

1. Tests should be organized to match the feature specifications in the `features/` directory
2. Follow Playwright's best practices for writing tests:
   - Use page objects when appropriate
   - Keep tests independent
   - Clean up test data
   - Use appropriate assertions

## Configuration

The test configuration is defined in `playwright.config.ts` and includes:

- Browser configurations
- Test timeouts
- Parallel execution settings
- Reporter settings

## CI/CD Integration

Tests can be run in CI/CD pipelines using Playwright's Docker images or GitHub Actions.
