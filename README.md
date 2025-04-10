# OSS Monorepo

## Overview

This monorepo is a comprehensive development workspace that includes multiple applications, libraries, and tools. It provides a flexible and scalable approach to managing different projects and standalone applications.

## Project Structure

```
oss/
├── apps/
│   ├── next-hello/   # Main Next.js web application integrated into the monorepo
│   └── web-e2e/      # End-to-end tests for the web application
├── apps-standalone/  # Apps that are hard/not yet integrated to the monorepo
│   ├── ayokoding-web/  # Standalone version of the web application
│   ├── wahidyankf-e2e/  # End-to-end testing environment
│   └── wahidyankf-web/  # Personal web application
├── libs/             # Shared libraries and components
│   └── ...           # Reusable code and shared utilities
├── scripts/          # Utility scripts for project management
└── tools/            # Development and build tools
```

### Folder Descriptions

#### Apps

- `next-hello`: The primary web application integrated into the monorepo
- `web-e2e`: End-to-end testing suite for the web application

#### Apps-Standalone

The `apps-standalone` folder is used for applications that are:

- Difficult to integrate into the monorepo
- Experimental projects
- Not yet ready for full monorepo integration
- Maintained separately from the main monorepo workflow

Current standalone applications:

- `ayokoding-web`: Standalone version of the web application
- `wahidyankf-e2e`: End-to-end testing environment
- `wahidyankf-web`: Personal web application

#### Libs

Shared libraries and components that can be used across different applications in the monorepo.

## Tech Stack

- **Framework**: Next.js
- **Monorepo Management**: Nx
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Python Formatting**: Black
- **Node Version Management**: nvm (via .nvmrc)
- **Testing**:
  - Unit Testing: Jest
  - E2E Testing: Playwright
- **Code Formatting**: Prettier
- **Git Hooks**: Husky

## Getting Started

### Prerequisites

- Node.js (version 20.x or later)
- npm (version 9.x or later)
- Nx CLI

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/wahidyankf/ayokoding.git
   cd ayokoding
   ```

2. Install dependencies
   ```bash
   npm install
   ```

### Development

#### Monorepo Applications

- Start the main application:

  ```bash
  npx nx serve next-hello
  ```

- Build for production:
  ```bash
  npx nx build next-hello
  ```

#### Standalone Applications

- Start the standalone web application:

  ```bash
  npm run ayokoding-web:dev
  ```

- Build standalone web application:
  ```bash
  npm run ayokoding-web:build
  ```

### Testing

- Run all tests (including standalone and monorepo applications):

  ```bash
  npm run test:all
  ```

- Run standalone application tests:
  ```bash
  npm run test:all:standalone
  ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Git Hooks

The project uses Husky for Git hooks with automated setup:

```bash
npm run prepare
```

Hooks include:

- `pre-commit`: Runs lint-staged (Prettier for JS/TS, Black for Python)
- `commit-msg`: Validates commit messages
- `pre-push`: Runs tests and builds affected projects

The prepare script ensures all hooks are executable.

## Project Health Checks

The project includes automated checks to ensure proper setup:

### Doctor Script

```bash
npm run doctor
```

Checks:

- Required tools (nvm, black)
- Node version matches .nvmrc

### Pre-install Checks

Automatically runs during `npm install` to verify:

- Correct Node version
- Required tools are installed

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Wahid Yankfi - [Your Email or Social Media]

Project Link: [https://github.com/wahidyankf/oss](https://github.com/wahidyankf/oss)
