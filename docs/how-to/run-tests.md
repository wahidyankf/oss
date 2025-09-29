# Testing Strategy

This document outlines the testing approach across different projects in the monorepo.

## Overview

The monorepo uses multiple testing frameworks suited to each project's needs:

- **Jest**: Default for Nx-integrated projects
- **Vitest**: Used in wahidyankf-web for better Vite integration
- **Playwright**: End-to-end testing across all web projects
- **pytest**: Python project testing

## Running Tests

### All Projects

```bash
# Run all tests, typechecks, and builds across the monorepo
npm run test:all  # Runs: tests + typecheck + build for all projects

# Build all standalone projects (misleading name - this only builds)
npm run test:all:standalone  # Actually runs build:standalone
```

### Nx-Integrated Projects

```bash
# Run tests for a specific project
npx nx test next-hello

# Run tests in watch mode
npx nx test next-hello --watch

# Run tests for affected projects only
npx nx affected:test

# Run with coverage
npx nx test next-hello --coverage
```

### Standalone Projects

#### wahidyankf-web (Vitest)

```bash
cd apps-standalone/wahidyankf-web

# Run unit tests
npm run test:unit

# Watch mode
npm run test:unit:watch

# With UI
npx vitest --ui
```

#### Python Mastery

```bash
cd apps-standalone/python-mastery

# Run all tests
python -m pytest

# Run specific test file
python -m pytest test_main.py

# Verbose output
python -m pytest -v

# With coverage
python -m pytest --cov=.
```

## Test Organization

### Unit Tests

#### TypeScript/JavaScript Projects

```
├── component.tsx
├── component.test.tsx  # Co-located test file
└── component.spec.tsx  # Alternative naming
```

Example test structure:

```typescript
// component.test.tsx
import { render, screen } from '@testing-library/react'
import { Component } from './component'

describe('Component', () => {
  it('should render correctly', () => {
    render(<Component />)
    expect(screen.getByText('Hello')).toBeInTheDocument()
  })

  it('should handle user interaction', async () => {
    // Test implementation
  })
})
```

#### Python Projects

```
├── module.py
└── test_module.py  # Test file with test_ prefix
```

Example test:

```python
# test_module.py
import pytest
from module import function_to_test

def test_function_behavior():
    result = function_to_test(input_data)
    assert result == expected_output

def test_function_raises_error():
    with pytest.raises(ValueError):
        function_to_test(invalid_input)
```

### Integration Tests

For API routes and page components:

```typescript
// app/api/hello/route.test.ts
import { GET } from './route';

describe('/api/hello', () => {
  it('should return correct response', async () => {
    const response = await GET();
    const data = await response.json();
    expect(data).toEqual({ message: 'Hello World' });
  });
});
```

### E2E Tests (Playwright)

```bash
cd apps-standalone/wahidyankf-e2e

# Run all E2E tests
npm run test:e2e

# Run in UI mode
npm run test:e2e:watch

# Run specific test file
npx playwright test tests/pages/home.spec.ts

# Run in headed mode (see browser)
npx playwright test --headed

# Run only in Chrome
npx playwright test --project=chromium
```

Example E2E test:

```typescript
// tests/pages/home.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Home Page', () => {
  test('should load and display content', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Welcome/);
    await expect(page.locator('h1')).toContainText('Hello');
  });

  test('should navigate to about page', async ({ page }) => {
    await page.goto('/');
    await page.click('text=About');
    await expect(page).toHaveURL('/about');
  });
});
```

## Testing Best Practices

### 1. Test Structure

- **Arrange**: Set up test data and environment
- **Act**: Execute the function/interaction
- **Assert**: Verify the outcome

### 2. Test Naming

```typescript
// Good test names
it('should return user data when valid ID is provided');
it('should throw error when user ID is invalid');
it('should update cache after successful API call');

// Avoid vague names
it('works correctly'); // Too vague
it('test user'); // Not descriptive
```

### 3. Test Coverage

#### Viewing Coverage

```bash
# Jest projects
npx nx test project-name --coverage

# Vitest projects
npx vitest run --coverage

# Python projects
pytest --cov=. --cov-report=html
```

#### Coverage Goals

- Aim for 80%+ coverage
- Focus on critical paths
- Don't test implementation details
- Test edge cases and error conditions

### 4. Mocking

#### Jest/Vitest

```typescript
// Mock external modules
jest.mock('@/lib/api', () => ({
  fetchData: jest.fn(() => Promise.resolve({ data: 'mocked' })),
}));

// Mock environment variables
process.env.NEXT_PUBLIC_API_URL = 'http://test.api';
```

#### Python

```python
from unittest.mock import patch, Mock

@patch('module.external_service')
def test_with_mock(mock_service):
    mock_service.return_value = {'status': 'success'}
    result = function_using_service()
    assert result == expected
```

### 5. Testing React Components

```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react'

// Prefer queries in this order:
// 1. getByRole
// 2. getByLabelText
// 3. getByPlaceholderText
// 4. getByText
// 5. getByTestId (last resort)

test('form submission', async () => {
  render(<ContactForm />)

  // Fill form
  fireEvent.change(screen.getByLabelText('Email'), {
    target: { value: 'test@example.com' }
  })

  // Submit
  fireEvent.click(screen.getByRole('button', { name: 'Submit' }))

  // Wait for async action
  await waitFor(() => {
    expect(screen.getByText('Success!')).toBeInTheDocument()
  })
})
```

## CI/CD Integration

### Pre-push Hook

Tests run automatically before push:

```bash
# .husky/pre-push
npm run test:push
```

### GitHub Actions

Tests run on pull requests:

```yaml
# .github/workflows/test.yml
jobs:
  test:
    steps:
      - run: npm ci
      - run: npm run test:all
```

## Debugging Tests

### Jest/Vitest

```bash
# Run single test file
npx jest path/to/test.ts

# Run tests matching pattern
npx jest --testNamePattern="should render"

# Debug in VS Code
# Add breakpoint and use Jest runner extension
```

### Playwright

```bash
# Debug mode
npx playwright test --debug

# Generate test code
npx playwright codegen localhost:3000

# View test report
npx playwright show-report
```

## Performance Testing

### Vitest Benchmarks

```typescript
import { bench, describe } from 'vitest';

describe('Performance', () => {
  bench('array sort', () => {
    const arr = Array.from({ length: 1000 }, () => Math.random());
    arr.sort();
  });
});
```

### Lighthouse CI

```bash
# Run Lighthouse tests
npx lhci autorun
```

## Common Testing Patterns

### Testing Async Code

```typescript
// Using async/await
test('async operation', async () => {
  const result = await fetchData()
  expect(result).toBeDefined()
})

// Testing loading states
test('shows loading state', async () => {
  render(<DataComponent />)
  expect(screen.getByText('Loading...')).toBeInTheDocument()
  await waitFor(() => {
    expect(screen.queryByText('Loading...')).not.toBeInTheDocument()
  })
})
```

### Testing Errors

```typescript
test('handles errors gracefully', async () => {
  // Mock error
  mockFetch.mockRejectedValue(new Error('Network error'))

  render(<DataComponent />)

  await waitFor(() => {
    expect(screen.getByText('Error loading data')).toBeInTheDocument()
  })
})
```

### Testing Hooks

```typescript
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter';

test('useCounter hook', () => {
  const { result } = renderHook(() => useCounter());

  expect(result.current.count).toBe(0);

  act(() => {
    result.current.increment();
  });

  expect(result.current.count).toBe(1);
});
```

## Troubleshooting

### Common Issues

1. **Module not found errors**

   - Check tsconfig paths
   - Verify jest.config moduleNameMapper

2. **Timeout errors**

   - Increase timeout: `jest.setTimeout(10000)`
   - Check for missing async/await

3. **Flaky tests**

   - Use waitFor for async operations
   - Avoid fixed timeouts
   - Mock external dependencies

4. **Coverage gaps**
   - Check coverage reports
   - Add tests for error cases
   - Test edge conditions
