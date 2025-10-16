# OSS Monorepo

A hybrid monorepo combining Nx-integrated and standalone applications for web development, educational content, and E2E testing.

## Quick Start

```bash
# Clone and install
git clone https://github.com/wahidyankf/oss.git
cd oss
npm install

# Verify setup
npm run doctor

# Development
npx nx serve next-hello              # Nx-integrated app
npm run wahidyankf-web:dev          # Standalone Next.js
npm run ayokoding-web:dev           # Standalone Hugo

# Quality checks
npm run test:all                     # All tests
npm run typecheck                    # TypeScript validation
npm run build                        # Build all projects
```

## Documentation

📚 **[Complete Documentation](docs/README.md)** - Comprehensive guides using Diátaxis framework

**Quick Links**:

- [Getting Started Guide](docs/tutorials/getting-started.md) - Detailed setup instructions
- [Development Workflow](docs/how-to/development-workflow.md) - Daily development tasks
- [Common Commands](docs/reference/commands.md) - Full command reference
- [Architecture Overview](docs/explanation/monorepo-structure.md) - Design decisions
- [Technology Stack](docs/reference/technology-stack.md) - Complete tech stack details
- [Troubleshooting](docs/how-to/troubleshoot-issues.md) - Common issues and solutions

## Project Structure

```
oss/
├── apps/                   # Nx-integrated applications
│   └── next-hello/         # Next.js app with Nx tooling
├── apps-standalone/        # Standalone applications
│   ├── ayokoding-web/      # Hugo educational platform
│   ├── analisapasar-web/   # Hugo market analysis site
│   ├── wahidyankf-web/     # Next.js portfolio
│   ├── wahidyankf-e2e/     # Playwright E2E tests
│   └── python-mastery/     # Python curriculum
├── docs/                   # Documentation (Diátaxis framework)
├── plans/                  # Implementation plans
└── specs/                  # Gherkin specifications
```

See [docs/explanation/monorepo-structure.md](docs/explanation/monorepo-structure.md) for detailed structure explanation.

## Tech Stack

**Core**: Node.js 22.20.0 (Volta), npm 11.1.0, TypeScript, Nx
**Frontend**: Next.js, Tailwind CSS, Hugo
**Testing**: Vitest, Playwright
**Formatting**: Prettier (JS/TS/Gherkin), ruff (Python)

See [docs/reference/technology-stack.md](docs/reference/technology-stack.md) for complete details.

## Contributing

See [docs/how-to/development-workflow.md](docs/how-to/development-workflow.md) for detailed contribution guidelines.

**Quick steps**:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit using conventional format: `type(scope): subject`
4. Ensure quality checks pass: `npm run test:all`
5. Push and open a Pull Request

**Commit format**: Use [conventional commits](https://www.conventionalcommits.org/) - `type(scope): description`
**Git hooks**: Pre-commit formatting, commit message validation, pre-push testing (automatic via Husky)

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Wahidyan Kresna Fridayoka - [@wahidyankf](https://github.com/wahidyankf)

Project Link: [https://github.com/wahidyankf/oss](https://github.com/wahidyankf/oss)
