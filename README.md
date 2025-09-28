# OSS Monorepo

## Overview

This monorepo is a comprehensive development workspace that includes multiple applications, libraries, and tools. It provides a flexible and scalable approach to managing different projects and standalone applications.

## Project Structure

```
oss/
├── apps/
│   └── next-hello/         # Main Next.js web application integrated into the monorepo
├── apps-standalone/        # Apps that are hard/not yet integrated to the monorepo
│   ├── ayokoding-web/      # Hugo-based educational platform
│   ├── analisapasar-web/   # Hugo-based market analysis site
│   ├── wahidyankf-web/     # Next.js personal portfolio
│   ├── wahidyankf-e2e/     # Playwright E2E test suite
│   └── python-mastery/     # Python learning curriculum
├── docs/                   # Comprehensive documentation
└── scripts/                # Utility scripts for project management
```

### Folder Descriptions

#### Apps

- `next-hello`: The primary web application integrated into the monorepo

#### Apps-Standalone

The `apps-standalone` folder is used for applications that are:

- Difficult to integrate into the monorepo
- Experimental projects
- Not yet ready for full monorepo integration
- Maintained separately from the main monorepo workflow

Current standalone applications:

- `ayokoding-web`: Hugo-based educational platform (ID/EN)
- `analisapasar-web`: Hugo-based market analysis site
- `wahidyankf-web`: Next.js personal portfolio website
- `wahidyankf-e2e`: Playwright E2E test suite
- `python-mastery`: Python learning curriculum

#### Docs

Comprehensive documentation for the entire monorepo, including architecture, development guides, and troubleshooting.

## Tech Stack

- **Framework**: Next.js
- **Monorepo Management**: Nx
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Python Formatting**: Black
- **Node Version Management**: Volta (22.20.0)
- **Testing**:
  - Unit Testing: Jest
  - E2E Testing: Playwright
- **Code Formatting**: Prettier
- **Git Hooks**: Husky

## Getting Started

### Prerequisites

- Node.js 22.20.0 (managed by Volta)
- npm 11.1.0 (managed by Volta)
- Nx CLI (optional - can use npx)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/wahidyankf/oss.git
   cd oss
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

- Required tools (volta, black)
- Node version matches Volta configuration

### Pre-install Checks

Automatically runs during `npm install` to verify:

- Correct Node version
- Required tools are installed

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Wahidyan Kresna Fridayoka - [@wahidyankf](https://github.com/wahidyankf)

Project Link: [https://github.com/wahidyankf/oss](https://github.com/wahidyankf/oss)
