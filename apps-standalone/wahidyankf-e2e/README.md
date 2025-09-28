# wahidyankf-e2e

End-to-end test suite for wahidyankf-web using Playwright, ensuring the portfolio website functions correctly across different browsers and devices.

## Overview

This project contains comprehensive E2E tests for the wahidyankf-web portfolio website, testing critical user journeys, UI components, and cross-browser compatibility.

## Features

- **Cross-browser Testing**: Chrome, Firefox, Safari, Edge
- **Mobile Testing**: iOS and Android viewports
- **Visual Regression**: Screenshot comparisons
- **Parallel Execution**: Fast test runs
- **CI/CD Ready**: GitHub Actions integration

## Tech Stack

- **Test Framework**: Playwright 1.48.x
- **Language**: TypeScript
- **Test Runner**: Playwright Test
- **Assertions**: Playwright's built-in expects

## Getting Started

### Prerequisites

- Node.js 22.20.0 (managed by Volta)
- npm 11.1.0

### Installation

```bash
# Navigate to project
cd apps-standalone/wahidyankf-e2e

# Install dependencies
npm install

# Install Playwright browsers
npx playwright install
# or with system dependencies (Linux)
npx playwright install --with-deps
```

### Running Tests

```bash
# Run all tests
npm test
# or
npx playwright test

# Run tests in headed mode (see browser)
npx playwright test --headed

# Run tests in UI mode (interactive)
npm run test:e2e:watch
# or
npx playwright test --ui

# Run specific test file
npx playwright test tests/pages/home.spec.ts

# Run tests in specific browser
npx playwright test --project=chromium
npx playwright test --project=firefox
npx playwright test --project=webkit
```

## Test Structure

```
wahidyankf-e2e/
├── tests/
│   ├── components/         # Component-level tests
│   │   ├── navigation.spec.ts
│   │   └── theme.spec.ts
│   └── pages/              # Page-level tests
│       ├── cv.spec.ts
│       ├── home.spec.ts
│       └── personal-projects.spec.ts
├── playwright.config.ts    # Playwright configuration
└── package.json
```

### Test Categories

#### Component Tests

- **Navigation**: Mobile/desktop menu functionality
- **Theme Toggle**: Dark/light mode switching
- **Search**: Search functionality and filtering

#### Page Tests

- **Home Page**: Content loading, layout, CTAs
- **CV Page**: Search, filtering, content display
- **Projects Page**: Project cards, links, descriptions

## Configuration

### playwright.config.ts

```typescript
export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://127.0.0.1:3000',
    trace: 'on-first-retry',
  },
  projects: [
    // Desktop browsers
    { name: 'chromium', use: devices['Desktop Chrome'] },
    { name: 'firefox', use: devices['Desktop Firefox'] },
    { name: 'webkit', use: devices['Desktop Safari'] },
    // Mobile browsers
    { name: 'Mobile Chrome', use: devices['Pixel 5'] },
    { name: 'Mobile Safari', use: devices['iPhone 12'] },
  ],
});
```

## Writing Tests

### Basic Test Structure

```typescript
import { test, expect } from '@playwright/test';

test.describe('Feature Name', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should do something', async ({ page }) => {
    // Arrange
    const button = page.locator('button[aria-label="Submit"]');

    // Act
    await button.click();

    // Assert
    await expect(page).toHaveURL('/success');
    await expect(page.locator('h1')).toContainText('Success');
  });
});
```

### Testing Best Practices

1. **Use Semantic Selectors**

   ```typescript
   // Good
   page.getByRole('button', { name: 'Submit' });
   page.getByLabel('Email address');

   // Avoid
   page.locator('.btn-primary');
   page.locator('#email');
   ```

2. **Wait for Stability**

   ```typescript
   await page.waitForLoadState('networkidle');
   await expect(locator).toBeVisible();
   ```

3. **Test User Journeys**
   ```typescript
   test('complete user flow', async ({ page }) => {
     // Navigate
     await page.goto('/');

     // Interact
     await page.click('text=View CV');

     // Search
     await page.fill('[placeholder="Search"]', 'React');

     // Verify results
     await expect(page.locator('.result')).toContainText('React');
   });
   ```

## Debugging

### Debug Mode

```bash
# Run in debug mode
npx playwright test --debug

# Debug specific test
npx playwright test test-file.spec.ts --debug
```

### Generate Tests

```bash
# Open codegen tool
npx playwright codegen localhost:3000

# Record actions and generate code
```

### View Test Report

```bash
# After test run
npx playwright show-report

# Opens HTML report in browser
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: E2E Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: volta-cli/action@v4

      - name: Install dependencies
        run: |
          cd apps-standalone/wahidyankf-e2e
          npm ci

      - name: Install Playwright
        run: npx playwright install --with-deps

      - name: Run E2E tests
        run: npm test

      - uses: actions/upload-artifact@v3
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
```

## Advanced Features

### Visual Testing

```typescript
test('visual regression', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveScreenshot('homepage.png');
});
```

### API Mocking

```typescript
test('with mocked API', async ({ page }) => {
  await page.route('**/api/data', (route) => {
    route.fulfill({ json: { mocked: true } });
  });

  await page.goto('/');
  // Test with mocked data
});
```

### Accessibility Testing

```typescript
test('accessibility', async ({ page }) => {
  await page.goto('/');
  const accessibilitySnapshot = await page.accessibility.snapshot();
  expect(accessibilitySnapshot).toBeTruthy();
});
```

## Troubleshooting

### Common Issues

1. **Browser Installation**

   ```bash
   # Reinstall browsers
   npx playwright install --force
   ```

2. **Timeout Errors**

   ```typescript
   // Increase timeout for slow operations
   test.setTimeout(60000);
   await page.goto('/', { timeout: 30000 });
   ```

3. **Flaky Tests**
   - Use `waitForLoadState`
   - Add explicit waits
   - Check for race conditions

### Environment Variables

```bash
# .env.test
BASE_URL=http://localhost:3000
TIMEOUT=30000
HEADLESS=true
```

## Scripts

```bash
npm test                  # Run all tests
npm run test:headed       # Run with browser visible
npm run test:debug        # Debug mode
npm run test:report       # Generate and open report
npm run test:codegen      # Open test generator
```

## Best Practices

1. **Keep Tests Independent**: Each test should run in isolation
2. **Use Page Objects**: For complex pages, create page object models
3. **Parallel Execution**: Leverage Playwright's parallel capabilities
4. **Meaningful Names**: Descriptive test and describe block names
5. **Avoid Hard Waits**: Use Playwright's auto-waiting features

## Related Documentation

- [Playwright Documentation](https://playwright.dev)
- [wahidyankf-web README](../wahidyankf-web/README.md)
- [Testing Strategy Guide](/docs/development/testing.md)
- [Troubleshooting Guide](/docs/guides/troubleshooting.md)

## License

MIT License - see the [LICENSE](LICENSE) file for details.
