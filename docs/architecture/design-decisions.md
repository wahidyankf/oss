# Design Decisions

This document captures key architectural and design decisions made for this monorepo.

## 1. Hybrid Monorepo Approach

**Decision**: Use both Nx-integrated and standalone applications.

**Rationale**:

- Allows gradual migration to monorepo structure
- Accommodates projects with different build systems (Hugo vs Next.js)
- Provides flexibility for experimental projects
- Avoids big-bang migrations that could disrupt development

**Trade-offs**:

- (+) Flexibility and gradual adoption
- (+) Projects can maintain their optimal tooling
- (-) Some duplication of configuration
- (-) Less benefit from shared dependencies

## 2. Volta for Node Version Management

**Decision**: Migrated from nvm to Volta for Node.js version management.

**Rationale**:

- Automatic version switching
- Better Windows support
- Faster than nvm
- Includes npm version pinning
- Per-project configuration via package.json

**Implementation**:

```json
"volta": {
  "node": "22.20.0",
  "npm": "11.1.0"
}
```

## 3. Multiple Testing Frameworks

**Decision**: Allow different testing frameworks per project.

**Current Setup**:

- Jest: Nx-integrated apps
- Vitest: wahidyankf-web
- Playwright: E2E testing
- pytest: Python projects

**Rationale**:

- Each project can use the most suitable testing framework
- Vitest offers better performance for Vite-based projects
- Existing projects don't need migration

## 4. Hugo for Content Sites

**Decision**: Use Hugo for content-heavy websites (ayokoding, analisapasar).

**Rationale**:

- Excellent performance for static sites
- Built-in multilingual support
- Simple content management via Markdown
- No JavaScript required for basic functionality
- Great for SEO

**Trade-offs**:

- (+) Blazing fast static sites
- (+) Simple deployment
- (-) Limited interactivity without additional JS
- (-) Different toolchain from React apps

## 5. Conventional Commits

**Decision**: Enforce conventional commits across all projects.

**Format**: `type(scope): subject`

**Types**:

- feat, fix, docs, style, refactor, test, chore, build, ci, perf, revert

**Rationale**:

- Automated changelog generation
- Clear commit history
- Enables semantic versioning
- Better collaboration

## 6. Git Hooks Strategy

**Decision**: Use Husky with lint-staged for automated checks.

**Hooks**:

- **pre-commit**: Format code (Prettier, Black)
- **commit-msg**: Validate commit message
- **pre-push**: Run tests for affected projects

**Rationale**:

- Maintains code quality
- Prevents broken commits
- Reduces CI failures
- Immediate feedback to developers

## 7. Standalone E2E Tests

**Decision**: Keep E2E tests as a separate project.

**Rationale**:

- Can test deployed applications
- Independent test execution
- Different dependencies from main apps
- Can test across multiple projects

## 8. Multilingual Support Strategy

**Decision**: Built-in i18n for content sites, English-only for portfolio.

**Implementation**:

- Hugo's native i18n for ayokoding/analisapasar
- Single language for wahidyankf-web (professional audience)

**Rationale**:

- Educational content needs local language support
- Professional portfolio targets international audience
- Reduces complexity where not needed

## 9. CSS Strategy

**Decision**: Tailwind CSS as the primary styling solution.

**Rationale**:

- Consistent design system
- Rapid development
- Small production bundles
- Good IDE support
- Works well with component libraries

**Exceptions**:

- Hugo themes may use their own CSS
- Legacy projects during migration

## 10. Documentation Approach

**Decision**: Comprehensive documentation in `/docs` with project-specific READMEs.

**Structure**:

- `/docs`: Architecture and guides
- Project READMEs: Specific setup and commands
- CLAUDE.md: AI assistant guidance

**Rationale**:

- Centralized architecture documentation
- Project-specific details stay with code
- Easy navigation and discovery
- Supports AI-assisted development

## Future Decisions to Make

1. **Shared Component Library**: When to extract common UI components
2. **CI/CD Strategy**: GitHub Actions vs other platforms
3. **Deployment Strategy**: Vercel, Netlify, or self-hosted
4. **State Management**: For complex applications
5. **API Strategy**: GraphQL vs REST for future services
6. **Monitoring**: Error tracking and analytics approach
