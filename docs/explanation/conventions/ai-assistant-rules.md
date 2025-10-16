# AI Assistant Rules

This document defines the conventions and rules that AI assistants
must follow when developing in software development repositories.
These rules ensure consistency, quality, and adherence to project standards
**across all programming languages and technology stacks**.

**Application Scope:** These conventions apply differently based on the
architecture and maturity of different parts of a repository:

- **New Development & Modern Services**: Full adherence to all patterns
- **Legacy/Existing Systems**: Gradual adoption where appropriate
- **Enterprise Monoliths**: May use traditional patterns (e.g., JUnit instead of BDD)

**Exception Policy:** These conventions can only be overridden when explicitly
instructed by the human developer or project supervisor. All exceptions must
be documented and justified.

## Core Testing Rules

### 1. Strict Mocking vs Real API Policy

**E2E Tests (End-to-End Test Projects) - NO MOCKING**

- ❌ **NEVER use mocks** in E2E test projects
- ✅ **Always use real API calls** and external connections
- ✅ Tests must connect to actual running services
- ✅ Use real HTTP requests, database connections, file systems
- ✅ Black-box testing only - no knowledge of internals
- ✅ Test complete workflows from external perspective

**All Other Tests - ALWAYS MOCK**

- ✅ **Always use mocks** for external dependencies
- ❌ **NEVER make real API calls** in unit/integration tests
- ✅ Mock HTTP requests, database calls, file system operations
- ✅ Focus on isolated component testing
- ✅ Use your language's standard mocking libraries

**Universal Examples (Language Agnostic):**

```pseudo
❌ BAD: Real API call in unit test
TEST "should fetch user data":
  response = HTTP_CLIENT.get(BACKEND_URL + "/api/v1/users/123")
  ASSERT(response.status == 200)

✅ GOOD: Mocked API call in unit test
TEST "should fetch user data":
  MOCK_HTTP_CLIENT.setup_response(status=200, body={id: 123, name: "John"})
  response = API_SERVICE.get_user(123)
  ASSERT(response.name == "John")

✅ GOOD: Real API call in E2E test (Backend API)
SCENARIO "backend service is available":
  response = REAL_HTTP_CLIENT.get(BACKEND_URL + "/api/v1/users/123")
  ASSERT(response.status_ok())

✅ GOOD: Real API call in E2E test (GraphQL API)
SCENARIO "graphql service is available":
  response = REAL_HTTP_CLIENT.post(GRAPHQL_URL + "/graphql")
  ASSERT(response.status_ok())
```

### 2. Service Management Policy

**NEVER run services yourself** - The human developer will manage all service
lifecycle:

- ❌ Don't start backend servers (any language: `PROJECT_DEV_COMMAND`,
  `BUILD_TOOL_RUN_COMMAND`, `RUNTIME_START_COMMAND`, etc.)
- ❌ Don't stop or restart services
- ❌ Don't modify service configurations to make tests pass
- ✅ Assume services are already running when needed
- ✅ Use service wait utilities to verify availability
- ✅ Provide clear error messages if services are unavailable

**Universal Pattern:**

```pseudo
FUNCTION ensure_services_ready():
  FOR EACH service IN required_services:
    IF NOT wait_for_service(service.url, timeout=30):
      THROW Error(service.name + " not available - please start it first")
```

## Quality Assurance Rules

### 3. Mandatory Command Validation

After any code changes, **ALL command patterns must pass**:

```bash
# This Repository: Full validation
npm run test:all        # Runs all tests, typechecking, and builds
npm run typecheck       # TypeScript type checking for all Nx projects
npm run build          # Build all projects (Nx and standalone)

# Nx-specific commands (for apps/ projects)
npx nx test <project>       # Run tests for specific Nx project
npx nx lint <project>       # Lint specific Nx project
npx nx typecheck <project>  # Typecheck specific Nx project
npx nx affected:test        # Test only affected projects
npx nx affected:build       # Build only affected projects

# Standalone projects (apps-standalone/)
npm run <project>:test      # Test standalone project
npm run <project>:dev       # Run standalone project
npm run <project>:build     # Build standalone project

# Format checking (automatic via git hooks)
prettier --write <file>     # Format JS/TS/JSON/YAML/Gherkin files
ruff format <file>          # Format Python files
```

**Universal Requirements:**

- ✅ All tests must pass consistently (no flaky tests)
- ✅ All linting must pass (language-specific linters)
- ✅ All type checking must pass (if applicable to language)
- ✅ All formatting must be correct (language-specific formatters)
- ❌ Zero tolerance for intermittent failures

### 4. Specification Update Policy

**Minimize spec changes** - Only update specifications when:

- ✅ Explicitly requested by the human developer
- ✅ Absolutely unavoidable for functionality
- ✅ Fixing critical bugs that require behavior changes
- ❌ **NEVER** change specs to make tests pass more easily
- ❌ **NEVER** change specs to avoid implementation complexity

### 5. Git Commit Standards

**NEVER commit code changes unless explicitly instructed:**

- ❌ **NEVER commit code automatically** after making changes
- ❌ **NEVER assume code changes should be committed**
- ✅ **ONLY commit when explicitly asked** by the user
- ✅ **Ask for permission** before committing if unclear
- ✅ **Documentation-only changes** can be committed without explicit
  instruction

**NEVER bypass validation** when committing or pushing:

- ❌ **NEVER use `--no-verify`** flag
- ❌ **NEVER skip pre-commit hooks**
- ❌ **NEVER skip pre-push hooks**
- ✅ **ALWAYS fix errors** identified by hooks
- ✅ **ALWAYS run affected commands** before pushing
- ✅ Address root causes, not symptoms

**Universal Pattern:**

```pseudo
# ❌ BAD: Bypassing validation (any tech stack)
GIT_PUSH("--no-verify")

# ✅ GOOD: Fix the actual issues (this repository)
prettier --write . && npm run test:all  # Fix formatting and run all checks
npm run typecheck && npm run build      # Verify types and builds pass
git push
```

### 6. No Shortcuts Policy

**Fix problems properly** - Never take shortcuts:

- ❌ Don't disable linting rules to make code pass
- ❌ Don't weaken type checking (TypeScript, Java, Python type hints)
- ❌ Don't ignore test failures
- ❌ Don't comment out failing tests
- ❌ Don't change static analysis rules to avoid errors
- ✅ **ALWAYS fix root cause** of problems
- ✅ **ALWAYS maintain code quality standards**
- ✅ **ALWAYS preserve existing rules** unless explicitly told otherwise

**Universal Examples:**

```pseudo
❌ BAD: Disabling rules to avoid work (any language)
DISABLE_LINTER_RULE("next-line")           // Scripted languages
SUPPRESS_WARNINGS("all")                   // Compiled languages
IGNORE_TYPE_CHECK()                        // Type-checked languages
DISABLE_ANALYSIS_TOOLS("all")             // Static analysis tools

✅ GOOD: Properly fixing the issue (language-appropriate solutions)
- DEFINE_PROPER_TYPES_AND_INTERFACES()
- HANDLE_ERRORS_EXPLICITLY(try_catch=true)
- FOLLOW_LANGUAGE_IDIOMS_AND_BEST_PRACTICES()
```

## Development Process Rules

### 7. Think Ultra Hard Policy

Before implementing any solution:

- 🧠 **Analyze the full problem** scope
- 🧠 **Consider all edge cases** and implications
- 🧠 **Plan the implementation** thoroughly
- 🧠 **Review existing patterns** in the codebase
- 🧠 **Be patient** with complex problems
- 🧠 **Use search and fetch tools** for understanding
- 🧠 **Consider language-specific best practices**

### 8. Environment Configuration

**GitHub Integration Configuration:**

When working with GitHub-related tasks (creating PRs, fetching repository information, etc.), you may need a GitHub token for authentication. The token is configured as follows:

- **Location**: GITHUB_TOKEN is available in `.env.local` file at the root of this repository
- **Usage**: Source the environment variable when needed: `GITHUB_TOKEN`
- **Security**: The `.env.local` file is in `.gitignore` and safe for secrets
- **Setup**: If the token is missing, refer to `.env.example` for the expected format

**Universal Pattern:**

```pseudo
# When GitHub API access is needed
IF GitHub API interaction required:
  token = READ_ENV_VAR("GITHUB_TOKEN")
  IF token IS NULL OR EMPTY:
    THROW_ERROR("GITHUB_TOKEN not found in .env.local - check .env.example for setup")
  USE_TOKEN_FOR_GITHUB_API(token)
```

### 9. Research and Information Gathering Policy

**🔍 MANDATORY: Use web search and fetch tools liberally** - This is REQUIRED,
not optional:

- ✅ **ALWAYS use WebSearch** to research current technology trends and best
  practices
- ✅ **ALWAYS use WebFetch** to get official documentation and guides
- ✅ **ALWAYS use Playwright MCP tools** for examining web interfaces when working with running services
- ✅ **Feel free to use these tools EXTENSIVELY** - use them as much as needed
  for thorough understanding
- ✅ **Verify information** from authoritative sources before implementation
- ✅ **Check for latest versions** and breaking changes
- ✅ **Research language-specific patterns** and community standards
- ✅ **Think ultra hard** before implementing - thorough research is MANDATORY
  part of this process
- ❌ **NEVER assume** knowledge is current without verification
- ✅ **Use search tools proactively** - don't wait to be stuck, research upfront

**Mandatory Research Requirements:**

- **ALWAYS research** before implementing new libraries, frameworks, or patterns
- **ALWAYS verify** current best practices for the technology stack in use
- **ALWAYS check** for breaking changes and version compatibility
- **ALWAYS consult** official documentation and authoritative sources
- **ALWAYS use** WebSearch and WebFetch tools when implementing unfamiliar
  features
- **ALWAYS use** Playwright MCP tools when examining running services or web interfaces
- **NEVER implement** based on outdated or assumed knowledge without
  verification

**Universal Examples:**

```pseudo
✅ GOOD: Research before implementing (any technology)
- WEB_SEARCH("[LIBRARY_NAME] [YEAR] best practices [FRAMEWORK]")
- WEB_FETCH(OFFICIAL_DOCUMENTATION_URL)
- MCP_PLAYWRIGHT_TOOLS(examine running services, web interfaces)
- CHECK_COMMUNITY_PATTERNS_AND_EXAMPLES()
- VERIFY_CURRENT_API_AND_BREAKING_CHANGES()

❌ BAD: Implementing without research
- USE_OUTDATED_PATTERNS_FROM_MEMORY()
- SKIP_VERIFICATION_OF_CURRENT_SYNTAX()
- MISS_LATEST_FEATURES_AND_OPTIMIZATIONS()
- IGNORE_RUNNING_SERVICE_INTERFACES()
```

### 10. Testing Strategy Enforcement

**For Modern Applications & New Development:**

**Maintain clear separation** between test types:

| Test Type   | Location Pattern                              | Mocking     | External Calls | Purpose                    | Source      |
| ----------- | --------------------------------------------- | ----------- | -------------- | -------------------------- | ----------- |
| BDD         | `tests/bdd/`, `src/test/bdd/`, `specs/`       | ✅ Required | ❌ Never       | Behavior specification     | `features/` |
| Unit        | `tests/`, `__tests__/`, `src/test/`           | ✅ Required | ❌ Never       | Component isolation        | N/A         |
| Integration | `tests/integration/`, `src/test/integration/` | ✅ Allowed  | ❌ Never       | Module integration         | N/A         |
| E2E         | `apps-standalone/wahidyankf-e2e/`             | ❌ Never    | ✅ Required    | System behavior validation | N/A         |

**This Repository**: E2E tests are in `apps-standalone/wahidyankf-e2e/`. BDD support prepared in `specs/` directory (Gherkin formatting ready via prettier-plugin-gherkin).

**BDD Test Architecture (Modern Services):**

- **BDD Tests consume feature files from `features/`** - Single source of truth
  for behavior
- **E2E BDD uses real API calls** - Full system validation with no mocking against running services
- **App BDD uses mocking** - Fast behavior testing with isolated dependencies
- **Unit/Integration tests avoid duplicating BDD scenarios** - Focus on
  technical implementation details not covered by BDD

**BDD Implementation Strategy (vitest-cucumber):**

For projects using vitest-cucumber, follow the **proven systematic methodology** that achieved 655 tests with 100% pass rate:

- ✅ **Use Error-Driven Development**: `Framework Error → Implement Exact Step → Run Test → Repeat`
- ✅ **Leverage Zero Tolerance Policy**: vitest-cucumber requires ALL feature file steps to be implemented - use this as your implementation guide
- ✅ **Implement Steps Exactly**: Step definitions must match feature file text precisely (no regex, no approximation)
- ✅ **Separate E2E and Unit Concerns**: Same feature files, different execution contexts
  - **Unit tests**: Mock all external dependencies in BeforeEachScenario
  - **E2E tests**: Use real filesystem/API calls, no mocking
- ✅ **Use Systematic Progression**: Each test run reveals the next missing step to implement
- ✅ **Batch Similar Steps**: For scenarios with many file/output verification steps, use efficient forEach patterns
- ✅ **Ensure Test Isolation**: Always use BeforeEachScenario with `vi.clearAllMocks()` and proper setup

**📚 BDD Resources:**

**Note**: This repository has Gherkin formatting support (`prettier-plugin-gherkin`) and a `specs/` directory prepared for future BDD implementation. BDD frameworks like vitest-cucumber can be added when needed. See the agent `gherkin-spec-writer` for creating feature files.

**MANDATORY: When implementing BDD tests with vitest-cucumber:**

- ❌ **NEVER** guess at step implementations - let framework errors guide you
- ❌ **NEVER** skip steps or use approximations - exact matching required
- ❌ **NEVER** mix mocked and real execution in same test type
- ✅ **ALWAYS** use the error-driven systematic approach
- ✅ **ALWAYS** achieve 100% pass rate for both test suites (unit + E2E)
- ✅ **ALWAYS** consult the comprehensive guides for complex scenarios

**Traditional Test Architecture (Enterprise/Legacy Systems):**

- **Unit tests with JUnit/TestNG** - Standard enterprise testing patterns
- **Integration tests** - Component and service integration validation
- **End-to-end tests** - Full workflow validation
- **Follow existing project conventions** - Maintain consistency with established patterns

**BDD Test Responsibilities:**

| Test Type       | Covers                                                | Avoids                                       |
| --------------- | ----------------------------------------------------- | -------------------------------------------- |
| **BDD Tests**   | User scenarios, business rules, acceptance criteria   | Technical implementation details, edge cases |
| **Unit Tests**  | Edge cases, error handling, internal logic not in BDD | Business scenarios already covered by BDD    |
| **Integration** | Module interactions not covered by BDD scenarios      | Full workflow testing (leave to BDD/E2E)     |

**Universal Test Organization Patterns:**

```pseudo
Scripted Languages (JavaScript/TypeScript, etc.):
  - BDD: TEST_DIR/bdd/*.EXTENSION, tests/bdd/*.spec.EXTENSION
  - Unit: TEST_DIR/, *.test.EXTENSION, *.spec.EXTENSION, src/**/*.test.EXTENSION
  - E2E: e2e/, tests/e2e/, E2E_FRAMEWORK_DIR/

Compiled Languages (Java, C#, etc.):
  - BDD: src/test/bdd/, src/test/resources/features/
  - Unit: src/test/LANGUAGE/, *Test.EXTENSION, *Tests.EXTENSION
  - Integration: src/test/LANGUAGE/, *IT.EXTENSION, *IntegrationTest.EXTENSION

General Pattern:
  - Adapt directory structures to project conventions
  - Follow language-specific naming patterns
  - Maintain clear separation between test types
```

### 11. Documentation Maintenance

**ALWAYS update related documentation** when making changes:

- ✅ **Update documentation files** when behavior changes
- ✅ **Update module-specific docs** when requirements change
- ✅ **Update READMEs** when setup or usage changes
- ✅ **Add examples** for complex scenarios
- ✅ **Maintain consistency** with existing docs
- ✅ **Follow Diátaxis framework** for categorization (tutorials, how-to guides, reference, explanation)

**Never forget documentation updates** - they are as important as code changes.

### 12. Plans Convention

**Follow structured implementation planning** when working with plans:

- ✅ **Use 4-document structure** - README.md, requirements.md, tech-docs.md, delivery.md
- ✅ **Design for single PR implementation** - Complete atomic changes only
- ✅ **Focus on technical content** - No project management content (timelines, metrics, business value)
- ✅ **Include comprehensive Gherkin** - All acceptance criteria in requirements.md
- ✅ **Reference plans directory** - `plans/in-progress--feature-name/requirements.md#section`
- ❌ **NEVER include** - Time estimates, success metrics, risk assessments, deployment requirements
- ❌ **NEVER create complex rollback procedures** - Simple PR revert only

**This Repository**: Plans directory structure available at `/plans/`. Use agents `plan-writer` and `plan-auditor` for creating and validating plans.

## Error Handling Standards

### 13. Comprehensive Error Messages

Provide actionable error information regardless of language:

**Universal Pattern:**

```pseudo
❌ BAD: Vague error (any language)
THROW_ERROR("Test failed")
RAISE_EXCEPTION("Error")
PANIC("Failed")

✅ GOOD: Actionable error with context (language-appropriate)
THROW_ERROR(
  "API test failed: Expected status 200 but got " + actual_status + "\n" +
  "URL: " + api_client.base_url + "/api/v1/users\n" +
  "Response: " + response_body + "\n" +
  "Ensure the backend service is running on the expected port"
)
```

### 14. Service Dependency Clarity

Make service requirements explicit across all languages:

**Universal Pattern:**

```pseudo
FUNCTION require_running_services():
  services = [
    {name: "Backend API", url: "http://localhost:PORT_1"},
    {name: "GraphQL API", url: "http://localhost:PORT_2"},
    {name: "Frontend App", url: "http://localhost:PORT_3"}
  ]
  // Adapt PORT_1, PORT_2, PORT_3 to actual project ports

  FOR EACH service IN services:
    TRY:
      HTTP_CHECK(service.url)
    CATCH error:
      THROW_ERROR(
        service.name + " is not running at " + service.url + ". " +
        "Please start it before running E2E tests."
      )
```

## Validation Checklist

Before completing any development task, verify:

**Testing Strategy (Modern Services):**

- [ ] BDD tests consume feature files from `features/` (single source of truth)
- [ ] BDD tests use mocking in apps, real calls in E2E projects
- [ ] Unit/Integration tests avoid duplicating BDD scenarios
- [ ] All tests use appropriate mocking strategy for their type
- [ ] No real API calls in unit/integration/BDD tests (except E2E)
- [ ] No mocking in E2E tests

**Testing Strategy (Traditional/Enterprise Systems):**

- [ ] Unit tests follow existing framework patterns (JUnit, TestNG, etc.)
- [ ] Integration tests validate component interactions
- [ ] All tests use appropriate mocking strategy for their type
- [ ] No real API calls in unit/integration tests
- [ ] E2E tests may use real services where appropriate
- [ ] Follow established project testing conventions

**Quality Gates:**

- [ ] All quality checks pass consistently for the project's tech stack
- [ ] All BDD, unit, and integration tests pass
- [ ] No shortcuts taken in implementation
- [ ] No linting/type-check rules weakened
- [ ] Specifications updated only when necessary

**Documentation & Process:**

- [ ] **Documentation files updated** when behavior changes
- [ ] **Module-specific docs updated** when requirements change
- [ ] **READMEs updated** when setup or usage changes
- [ ] Git hooks respected (no `--no-verify`)
- [ ] Error messages are actionable
- [ ] Service dependencies are clear
- [ ] Language-specific best practices followed

## Universal Application

This convention applies to all technology stacks in any repository:

**Language Categories:**

- **Scripted Languages**: Dynamic languages with interpreters (JavaScript, TypeScript, etc.)
- **Compiled Languages**: Static compilation required (Java, C#, Go, etc.)
- **Build-System Languages**: Languages with complex build pipelines

**Universal Tool Categories:**

- **Package Managers**: Dependency management systems
- **Build Tools**: Compilation and bundling systems
- **Test Frameworks**: Unit, integration, and E2E testing tools
- **Quality Tools**: Linters, formatters, type checkers
- **Development Servers**: Local development environments

## Quick Reference Commands

**This Repository - Essential Commands:**

```bash
# Setup
npm install              # Install dependencies and setup git hooks
npm run doctor          # Verify environment (Node, npm versions)

# Quality checks
npm run test:all        # Full validation: tests + typecheck + build
npm run typecheck       # TypeScript checking (all Nx projects)
npm run build          # Build all projects

# Development (from root)
npx nx serve next-hello            # Nx app
npm run wahidyankf-web:dev         # Standalone Next.js
npm run ayokoding-web:dev          # Standalone Hugo

# Nx-specific (apps/ directory)
npx nx test <project>              # Run tests
npx nx lint <project>              # Lint code
npx nx affected:test              # Only affected projects
npx nx affected:build             # Only affected projects

# Formatting (handled by git hooks automatically)
prettier --write <file>            # JS/TS/JSON/YAML/Gherkin
ruff format <file>                 # Python

# Environment
# - Node: 22.20.0 (managed by Volta)
# - npm: 11.1.0 (managed by Volta)
# - Package manager: npm (not yarn/pnpm)
```

## Related Documentation

- Documentation Audit Protocol - Systematic documentation maintenance
- Testing Philosophy - Why we test this way
- Testing Guides - Practical testing implementation
- Code Quality Standards - Quality principles and practices

## Enforcement

These rules are **non-negotiable** for AI assistants across all technology
stacks. Violations should be treated as bugs and fixed immediately. When in
doubt, ask the human developer for clarification rather than making assumptions
that might violate these conventions.

The principles remain constant - only the implementation details change with
different technologies.
