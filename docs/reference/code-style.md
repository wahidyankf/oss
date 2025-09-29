# Code Style Guide

This guide defines the coding standards and style conventions for the OSS monorepo.

## General Principles

1. **Consistency**: Follow existing patterns in the codebase
2. **Clarity**: Write code that is easy to understand
3. **Simplicity**: Prefer simple solutions over clever ones
4. **Documentation**: Comment complex logic and document APIs

## Automated Formatting

All code is automatically formatted on commit using:

- **Prettier**: JavaScript, TypeScript, JSON, Markdown
- **Black**: Python files

### Manual Formatting

```bash
# Format all JS/TS files
prettier --write "**/*.{js,jsx,ts,tsx,json,md}"

# Format Python files
black . --quiet
```

## JavaScript/TypeScript

### Language Features

- Use TypeScript for all new code
- Target ES2017+ features
- Prefer `const` over `let`, avoid `var`
- Use optional chaining (`?.`) and nullish coalescing (`??`)

### Naming Conventions

```typescript
// Constants: UPPER_SNAKE_CASE
const MAX_RETRIES = 3;
const API_BASE_URL = 'https://api.example.com';

// Variables and functions: camelCase
const userName = 'John';
const getUserData = () => {};

// Classes and types: PascalCase
class UserService {}
interface UserData {}
type UserRole = 'admin' | 'user';

// Private methods: prefix with underscore
class Service {
  private _internalMethod() {}
}

// React components: PascalCase
const UserProfile = () => {};

// Files: kebab-case for utils, PascalCase for components
// user-utils.ts
// UserProfile.tsx
```

### React/Next.js

#### Component Structure

```typescript
// 1. Imports
import React, { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import styles from './Component.module.css'

// 2. Types/Interfaces
interface ComponentProps {
  title: string
  onAction: () => void
}

// 3. Component definition
export const Component: React.FC<ComponentProps> = ({ title, onAction }) => {
  // 4. Hooks
  const [state, setState] = useState(false)
  const router = useRouter()

  // 5. Effects
  useEffect(() => {
    // Effect logic
  }, [dependency])

  // 6. Handlers
  const handleClick = () => {
    onAction()
  }

  // 7. Render
  return (
    <div className={styles.container}>
      <h1>{title}</h1>
      <button onClick={handleClick}>Action</button>
    </div>
  )
}
```

#### Hooks Usage

```typescript
// Custom hooks in separate files
// hooks/useUser.ts
export const useUser = () => {
  const [user, setUser] = useState(null)
  // Hook logic
  return { user, setUser }
}

// Use early returns
const Component = () => {
  const { data, loading } = useData()

  if (loading) return <Spinner />
  if (!data) return <Empty />

  return <Content data={data} />
}
```

### TypeScript Best Practices

```typescript
// Prefer interfaces for objects
interface User {
  id: string;
  name: string;
  email?: string; // Optional property
}

// Use type for unions and aliases
type Status = 'pending' | 'active' | 'inactive';
type ID = string | number;

// Avoid any, use unknown when needed
const processData = (data: unknown) => {
  if (typeof data === 'string') {
    // Type narrowed to string
  }
};

// Use generics for reusable code
const getValue = <T>(key: string, defaultValue: T): T => {
  return localStorage.getItem(key) ?? defaultValue;
};

// Const assertions for literal types
const config = {
  api: 'https://api.example.com',
  timeout: 5000,
} as const;
```

## Python Style

### PEP 8 Compliance

All Python code follows PEP 8, enforced by Black:

```python
# Naming conventions
MODULE_CONSTANT = 42

class UserService:  # PascalCase for classes
    def __init__(self):
        self.user_count = 0  # snake_case for attributes

    def get_user_data(self):  # snake_case for methods
        pass

    def _internal_method(self):  # prefix _ for internal
        pass

# Function definitions
def calculate_total(
    items: List[Item],
    tax_rate: float = 0.1,
    discount: Optional[float] = None
) -> float:
    """Calculate total with tax and optional discount.

    Args:
        items: List of items to calculate
        tax_rate: Tax rate to apply (default: 0.1)
        discount: Optional discount percentage

    Returns:
        Total amount after tax and discount
    """
    subtotal = sum(item.price for item in items)
    if discount:
        subtotal *= (1 - discount)
    return subtotal * (1 + tax_rate)
```

### Type Hints

```python
from typing import List, Dict, Optional, Union, Callable

# Use type hints for clarity
def process_users(users: List[Dict[str, str]]) -> List[str]:
    return [user['name'] for user in users]

# Complex types
UserData = Dict[str, Union[str, int, List[str]]]
Callback = Callable[[str], None]

# Optional types
def find_user(user_id: str) -> Optional[User]:
    # Returns User or None
    pass
```

## CSS/Styling

### Tailwind CSS

```jsx
// Component-specific styles
<div className="flex flex-col space-y-4 p-6">
  <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Title</h1>
</div>;

// Reusable style constants
const buttonStyles = {
  primary: 'bg-blue-500 hover:bg-blue-600 text-white',
  secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-900',
};

// Using clsx for conditional classes
import clsx from 'clsx';

<button
  className={clsx(
    'px-4 py-2 rounded',
    isActive ? 'bg-blue-500' : 'bg-gray-200',
  )}
/>;
```

### CSS Modules (when used)

```scss
/* Component.module.css */
.container {
  display: flex;
  flex-direction: column;
  gap: 1rem;

  &:hover {
    background-color: var(--hover-bg);
  }
}

.title {
  font-size: 2rem;
  font-weight: bold;

  @media (max-width: 768px) {
    font-size: 1.5rem;
  }
}
```

## JSON Configuration

### package.json

Always include the JSON Schema reference for better editor support:

```json
{
  "$schema": "https://json.schemastore.org/package",
  "name": "your-package",
  "version": "1.0.0"
}
```

This provides:

- IntelliSense/autocomplete in supported editors
- Validation of required and optional fields
- Type information for property values
- Documentation on hover

### tsconfig.json

Similarly for TypeScript configuration:

```json
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "compilerOptions": {
    // Configuration options
  }
}
```

## Markdown

### Documentation Structure

````markdown
# Main Title

Brief introduction paragraph.

## Table of Contents

- [Section 1](#section-1)
- [Section 2](#section-2)

## Section 1

### Subsection

Content with **bold** and _italic_ text.

```bash
# Code blocks with language specified
npm install
```
````

### Lists

1. Ordered item
2. Another item
   - Nested unordered
   - Another nested

### Links and Images

[Link text](https://example.com)
![Alt text](./images/image.png)

```

## Git Commits

### Message Format
```

type(scope): subject

[optional body]

[optional footer]

````

### Examples
```bash
# Good commit messages
git commit -m "feat(auth): add social login support"
git commit -m "fix(ui): correct button alignment on mobile"
git commit -m "docs: update API documentation"
git commit -m "refactor(api): extract validation logic"

# With body
git commit -m "feat(payment): integrate Stripe checkout

This adds Stripe checkout integration with support for:
- One-time payments
- Subscription management
- Webhook handling

Closes #123"
````

## Comments and Documentation

### JavaScript/TypeScript

```typescript
/**
 * Calculate the discounted price.
 * @param price - Original price
 * @param discount - Discount percentage (0-100)
 * @returns Discounted price
 * @example
 * calculateDiscount(100, 20) // returns 80
 */
function calculateDiscount(price: number, discount: number): number {
  // Ensure discount is within valid range
  const validDiscount = Math.max(0, Math.min(100, discount));
  return price * (1 - validDiscount / 100);
}

// TODO: Implement caching mechanism
// FIXME: Handle edge case for negative values
// NOTE: This is a temporary workaround
```

### Python

```python
def process_data(data: List[Dict]) -> Dict[str, Any]:
    """Process raw data and return summary statistics.

    This function takes raw data and calculates various
    statistics including mean, median, and standard deviation.

    Args:
        data: List of dictionaries containing numerical data

    Returns:
        Dictionary containing summary statistics

    Raises:
        ValueError: If data is empty or invalid

    Example:
        >>> data = [{'value': 1}, {'value': 2}, {'value': 3}]
        >>> result = process_data(data)
        >>> print(result['mean'])
        2.0
    """
    if not data:
        raise ValueError("Data cannot be empty")

    # Implementation here
    pass
```

## File Organization

### Next.js Projects

```
src/
├── app/
│   ├── (routes)/
│   ├── layout.tsx
│   └── page.tsx
├── components/
│   ├── common/
│   ├── features/
│   └── ui/
├── hooks/
├── lib/
│   ├── api/
│   └── utils/
└── types/
```

### Python Projects

```
project/
├── src/
│   ├── __init__.py
│   ├── models/
│   ├── services/
│   └── utils/
├── tests/
│   ├── unit/
│   └── integration/
└── docs/
```

## Linting Rules

### ESLint Configuration

Key rules enforced:

- No console logs in production
- Prefer const assertions
- No unused variables
- Consistent return statements
- Exhaustive deps in hooks

### Python Linting

- Line length: 88 characters (Black default)
- Import sorting: alphabetical
- Docstring presence for public methods
- Type hints encouraged

## Accessibility

```jsx
// Always include proper ARIA labels
<button
  aria-label="Close dialog"
  onClick={handleClose}
>
  <CloseIcon />
</button>

// Semantic HTML
<nav aria-label="Main navigation">
  <ul role="list">
    <li><a href="/">Home</a></li>
  </ul>
</nav>

// Form accessibility
<label htmlFor="email">Email Address</label>
<input
  id="email"
  type="email"
  required
  aria-describedby="email-error"
/>
<span id="email-error" role="alert">
  Please enter a valid email
</span>
```

## Performance Considerations

```typescript
// Memoize expensive computations
const expensiveValue = useMemo(() => {
  return computeExpensiveValue(data)
}, [data])

// Debounce user input
const debouncedSearch = useMemo(
  () => debounce(handleSearch, 300),
  [handleSearch]
)

// Lazy load components
const HeavyComponent = lazy(() => import('./HeavyComponent'))

// Optimize re-renders
const ChildComponent = memo(({ data }) => {
  return <div>{data}</div>
})
```
