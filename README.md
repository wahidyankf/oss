# Ayokoding Monorepo

## Project Overview

This is a Next.js monorepo built with Nx, designed to provide a scalable and maintainable web application architecture.

## Tech Stack

- **Framework**: Next.js
- **Monorepo Management**: Nx
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Testing**:
  - Unit Testing: Jest
  - E2E Testing: Playwright
- **Code Formatting**: Prettier
- **Git Hooks**: Husky

## Project Structure

```
ayokoding/
├── apps/
│   ├── ayokoding-web/   # Main Next.js web application
│   └── web-e2e/         # End-to-end tests for the web application
├── libs/                # Shared libraries and components
```

## Getting Started

### Prerequisites

- Volta (recommended for managing Node.js and npm versions)
- Node.js (v20.11.0 LTS)
- npm (v10.2.4)

### Installing Volta

Volta simplifies Node.js version management:

1. Install Volta:

   ```bash
   curl https://get.volta.sh | bash
   ```

2. Install and use the project's Node.js version:
   ```bash
   volta install node@20.11.0
   volta use node@20.11.0
   ```

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

### Running the Application

- Start development server:

  ```bash
  npx nx serve ayokoding-web
  ```

- Build for production:

  ```bash
  npx nx build ayokoding-web
  ```

- Run tests:
  ```bash
  npx nx test ayokoding-web
  npx nx e2e web-e2e
  ```

## Code Formatting and Git Hooks

This project uses Prettier for consistent code formatting and Husky for Git hooks.

### Pre-commit Formatting

Before each commit, the pre-commit hook will automatically format the following file types:

- JavaScript/TypeScript (`.js`, `.jsx`, `.ts`, `.tsx`)
- Markdown (`.md`)
- JSON (`.json`)
- HTML (`.html`)

This ensures consistent code style across the project. No manual formatting is required.

### Manual Formatting

To manually format files, run:

```bash
npx prettier --write .
```

## Contributing

### Conventional Commits

This project uses Conventional Commits for commit messages. The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### Commit Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semi-colons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks, build changes
- `perf`: Performance improvements
- `ci`: CI/CD pipeline changes
- `build`: Build system changes
- `revert`: Reverting previous commits

#### Example Commit Messages

```
feat(web): add login functionality

fix(api): resolve authentication error

docs: update README with new setup instructions

chore: upgrade dependencies
```

Commit messages are automatically validated by commitlint to ensure consistency.

### Steps to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [Your Email]

Project Link: [https://github.com/yourusername/ayokoding](https://github.com/yourusername/ayokoding)
