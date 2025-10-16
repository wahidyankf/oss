# CLAUDE.md

Guidance for Claude Code when working in this hybrid monorepo (Nx-integrated + standalone projects).

## Documentation

**Start here**: [docs/README.md](docs/README.md) - Complete documentation using Diátaxis framework

**AI Assistant Rules**: [docs/explanation/conventions/ai-assistant-rules.md](docs/explanation/conventions/ai-assistant-rules.md) - **MANDATORY** rules for AI assistants

**Quick Links**:

- [Getting Started](docs/tutorials/getting-started.md) - Environment setup
- [Common Commands](docs/reference/commands.md) - Command reference
- [Development Workflow](docs/how-to/development-workflow.md) - Daily development tasks
- [Troubleshooting](docs/how-to/troubleshoot-issues.md) - Common issues

## Essential Commands

```bash
# Setup & Validation
npm install              # Install deps and git hooks
npm run doctor          # Verify environment

# Quality Checks (MANDATORY before commits)
npm run test:all        # All tests
npm run typecheck       # TypeScript validation
npm run build          # Build all projects

# Development
npx nx serve <project>           # Nx-integrated apps
npm run <project>:dev           # Standalone apps

# Testing (Nx projects)
npx nx test <project>           # Single project
npx nx affected:test           # Only affected
```

## Project Structure

- **Nx-integrated** (`apps/`): Use `npx nx <command> <project>` - [Details](docs/reference/nx-projects.md)
- **Standalone** (`apps-standalone/`): Use npm scripts - [Details](docs/reference/standalone-projects.md)
- **Project READMEs**: Each project has specific instructions in its README.md

## Key Conventions

- **Versions**: Volta manages Node 22.20.0 / npm 11.1.0
- **Python**: pyenv with `wkf-oss` environment
- **Commits**: Conventional format `type(scope): subject`
- **Formatting**: Automatic via git hooks (Prettier for JS/TS/Gherkin, ruff for Python)
- **Documentation**: Follow Diátaxis framework (tutorials/how-to/reference/explanation)

## Working on Tasks

1. Check [AI Assistant Rules](docs/explanation/conventions/ai-assistant-rules.md) first
2. Read project-specific README.md
3. Run quality checks before committing
4. See [docs/](docs/) for comprehensive guidance
