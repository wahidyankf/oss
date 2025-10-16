# Documentation Audit Protocol

Guidelines for auditing and maintaining documentation quality in any repository. This protocol ensures documentation stays accurate, up-to-date, and properly organized according to the Diátaxis framework.

## Core Principles

### No Fictional Content

**This is repository documentation, not creative writing.** Documentation must contain only factual, technical information that can be verified in the codebase. Eliminate all:

- Made-up API endpoints that don't exist in the code
- Fictional business processes and workflows
- Speculative features or capabilities not implemented
- Imaginary integrations and partnerships
- Business jargon and marketing language
- Social impact claims and business value propositions

Document only what exists, for example: Maven modules, database schemas, configuration files, actual commands, real file paths, and implemented technical functionality.

### Implementation Accuracy

Documentation must always reflect the current implementation, not aspirational or planned features. Every command example, file path, and configuration snippet should work exactly as documented. The goal is eliminating the gap between what the docs say and what the code actually does.

## Audit Areas

### Links & References

All documentation links must be functional and point to current resources. Internal links should use correct relative paths that work from their document location. External links should point to current, accessible resources - not deprecated or moved pages. File paths mentioned in documentation must exist in the repository structure.

Use WebFetch tool to validate external URLs and ensure they contain current, accurate information. For framework documentation links, verify they point to the correct version and haven't been restructured.

**Audit checklist:**

- [ ] All internal markdown links work
- [ ] External URLs return 200 (not 404) - verify with WebFetch
- [ ] File paths in docs actually exist
- [ ] Code examples reference real files
- [ ] External documentation links point to current versions

### Commands & Examples

Every command example in documentation should work when executed in the current repository state. Commands should include necessary directory context and use current syntax. Port numbers, service endpoints, and environment variables must match the actual development setup.

**Audit checklist:**

- [ ] All command examples actually work
- [ ] Commands include necessary directory context
- [ ] Port numbers match current services
- [ ] Environment variables are correct

### Implementation Alignment

Documentation must describe the system as it currently exists, not as it was planned or might be in the future. Version numbers should match package manifests, configuration examples should mirror actual config files, and architectural descriptions should reflect the current codebase structure.

Use WebSearch and WebFetch tools to research current best practices and verify that documented approaches align with latest framework recommendations. Check if newer versions are available and if migration guides exist.

**Audit checklist:**

- [ ] Technology versions match package.json
- [ ] Node/npm versions match Volta config (22.20.0/11.1.0)
- [ ] Configuration examples match actual config files
- [ ] Architecture descriptions reflect current implementation (hybrid monorepo: Nx + standalone)
- [ ] No references to removed/deprecated features
- [ ] Best practices align with current framework recommendations - research with WebSearch
- [ ] Nx project paths use `apps/` directory
- [ ] Standalone project paths use `apps-standalone/` directory

### Content Completeness

Essential documentation should exist for all major components and workflows. Directories should have README files explaining their purpose. Setup guides need troubleshooting sections for common issues. Tutorials should include clear prerequisites.

**Audit checklist:**

- [ ] **No fictional content**: All content is factual and verifiable in codebase
- [ ] **No made-up APIs**: All documented endpoints exist in actual code
- [ ] **No speculative features**: Only document implemented functionality
- [ ] All directories have README.md files
- [ ] Setup guides have troubleshooting sections
- [ ] Tutorials include prerequisites
- [ ] How-to guides have complete examples

### Diátaxis Framework Compliance

Documentation should follow the four-category Diátaxis structure to serve different user needs effectively. Each document type has a specific purpose and should not mix concerns. Tutorials teach newcomers, how-to guides solve specific problems, reference materials provide lookup information, and explanations offer understanding.

**The four types:**

- **Tutorials**: Learning-oriented, assume no knowledge, provide complete working examples
- **How-to guides**: Task-oriented, step-by-step problem solving, assume some experience
- **Reference**: Information lookup, factual descriptions, organized for quick access
- **Explanations**: Understanding-oriented, context and background, discuss alternatives

**Audit checklist:**

- [ ] All docs follow Diátaxis structure: docs/tutorials/, docs/how-to/, docs/reference/, docs/explanation/
- [ ] No mixing of types (tutorials don't explain concepts, how-tos don't teach basics)
- [ ] Cross-references between types are clear and appropriate
- [ ] Each category has a README.md index file

## Validation Protocol

### Manual Testing

- Test every command example in the documentation
- Verify all file paths exist in the repository
- Check external links are accessible
- Validate configuration examples against actual config files

### Content Review

- **Search for fictional content**: Made-up APIs, business processes, speculative features
- **Verify all technical claims**: Every API endpoint, configuration option, and feature must exist in code
- **Remove business jargon**: Focus on technical facts, not marketing language
- Search for placeholder content (TODO, FIXME, "Coming soon")
- Look for hardcoded URLs and outdated port references
- Check for inconsistent terminology across documents
- Verify examples reflect current implementation
- Use WebSearch to validate technical information and ensure accuracy
- Use WebFetch to verify external resources are current and accessible

## Implementation Protocol

1. **Scan**: Use checklist to identify issues systematically
2. **Verify**: Test all examples and references against current codebase
3. **Fix**: Update documentation to match current implementation
4. **Validate**: Ensure fixes are accurate and complete

## Documentation Improvement Recommendations

After completing the audit, apply these common fix patterns based on your findings:

### Links

- Fix broken relative paths to match actual file structure
- Update external URLs that return 404
- Ensure cross-references point to correct sections

### Commands

- Update command examples to match current project structure
- Add directory context where commands need to be run
- Fix outdated CLI syntax and deprecated flags

### Versions

- Align documented versions with package.json/pom.xml
- Update framework versions in examples
- Correct runtime requirements

### Content

- Add missing Prerequisites sections to tutorials
- Include Troubleshooting sections in how-to guides
- Complete incomplete code examples
- Fill gaps where directories lack README files

### Diátaxis Compliance

- Move conceptual explanations from tutorials to explanation/
- Move step-by-step instructions from explanation to how-to/
- Move lookup information from tutorials to reference/
- Ensure tutorials focus on learning, not achieving real goals
- Ensure how-to guides solve specific problems without teaching concepts

## Success Criteria

- **Zero fictional content** - all information verifiable in codebase
- Zero broken links
- All commands work
- Versions match implementation
- Complete user workflows
- Proper Diátaxis categorization

## This Repository Specifics

**Technology Stack:**

- Package manager: npm (not yarn/pnpm)
- Version management: Volta (Node 22.20.0, npm 11.1.0)
- Monorepo structure: Hybrid (Nx + standalone projects)
- Nx projects: `apps/` directory
- Standalone projects: `apps-standalone/` directory
- Documentation: `docs/` with Diátaxis structure
- Formatting: Prettier (JS/TS/JSON/YAML/Gherkin), ruff (Python)

**Key Commands to Verify in Docs:**

```bash
npm install              # Setup
npm run doctor          # Environment check
npm run test:all        # Full validation
npm run typecheck       # Type checking
npx nx <command> <project>  # Nx commands
npm run <project>:dev       # Standalone dev servers
```

**Common Documentation Locations:**

- Getting started: `docs/tutorials/getting-started.md`
- Commands reference: `docs/reference/commands.md`
- Architecture: `docs/explanation/monorepo-structure.md`
- Project guides: `docs/reference/nx-projects.md`, `docs/reference/standalone-projects.md`
