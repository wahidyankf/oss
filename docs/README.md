# OSS Monorepo Documentation

Welcome to the comprehensive documentation for the OSS monorepo. This documentation follows the [Diátaxis framework](./explanation/diataxis-framework.md) to help you find exactly what you need.

## 🧭 Quick Navigation Guide

- **New to the project?** → Start with [Tutorials](./tutorials/)
- **Have a specific task?** → Use [How-To Guides](./how-to/)
- **Need details?** → Check [Reference](./reference/)
- **Want to understand why?** → Read [Explanation](./explanation/)

## 📚 Documentation Structure

Our documentation is organized into four distinct types, each serving a specific purpose:

### 🎓 [Tutorials](./tutorials/)

**Learning-oriented** guides that take you by the hand through a series of steps.

- [Getting Started](./tutorials/getting-started.md) - Your first steps with the monorepo

### 🛠️ [How-To Guides](./how-to/)

**Task-oriented** instructions for achieving specific goals.

- [Add a New Project](./how-to/add-new-project.md) - Steps to add new applications
- [Development Workflow](./how-to/development-workflow.md) - Day-to-day development practices
- [Run Tests](./how-to/run-tests.md) - Testing across different projects
- [Troubleshoot Issues](./how-to/troubleshoot-issues.md) - Common problems and solutions

### 📖 [Reference](./reference/)

**Information-oriented** descriptions of the system.

- [Commands](./reference/commands.md) - Complete command reference
- [Code Style](./reference/code-style.md) - Coding standards and conventions
- [Technology Stack](./reference/technology-stack.md) - Technologies and tools used
- [Nx Projects](./reference/nx-projects.md) - Nx-integrated project details
- [Standalone Projects](./reference/standalone-projects.md) - Independent application details

### 💡 [Explanation](./explanation/)

**Understanding-oriented** discussions of concepts and decisions.

- [Design Decisions](./explanation/design-decisions.md) - Key architectural choices
- [Monorepo Structure](./explanation/monorepo-structure.md) - Why we organize code this way

## 🚀 Quick Links

### Project-Specific Documentation

Each project has its own README with detailed information:

**Nx-Integrated Applications:**

- [next-hello](../apps/next-hello/README.md) - Next.js template application

**Standalone Applications:**

- [wahidyankf-web](../apps-standalone/wahidyankf-web/README.md) - Personal portfolio website
- [ayokoding-web](../apps-standalone/ayokoding-web/README.md) - Educational platform
- [analisapasar-web](../apps-standalone/analisapasar-web/README.md) - Market analysis platform
- [python-mastery](../apps-standalone/python-mastery/README.md) - Python learning resources
- [wahidyankf-e2e](../apps-standalone/wahidyankf-e2e/README.md) - E2E testing suite

## 🎯 Project Overview

This monorepo houses multiple interconnected projects:

1. **Educational Resources**: AyoKoding platform for learning software engineering
2. **Professional Portfolio**: Personal website showcasing professional experience
3. **Learning Materials**: Comprehensive Python mastery curriculum
4. **Market Analysis**: Platform for market analysis content (in development)
5. **Infrastructure**: Shared tooling and templates

## 🔧 Key Technologies

- **Monorepo Management**: Nx
- **Node Version**: 22.20.0 (Volta)
- **Frontend**: Next.js, Hugo
- **Languages**: TypeScript, JavaScript, Python
- **Testing**: Jest, Playwright, Vitest
- **Styling**: Tailwind CSS

## 📖 Getting Help

- For setup issues, see [Getting Started](./tutorials/getting-started.md)
- For common problems, check [Troubleshooting](./how-to/troubleshoot-issues.md)
- For specific project questions, refer to individual project READMEs
