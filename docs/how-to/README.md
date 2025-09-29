# How-To Guides

**Task-oriented instructions** for accomplishing specific goals in the project.

## What are How-To Guides?

How-to guides are recipes for solving specific problems. They:

- Assume some knowledge and experience
- Provide step-by-step instructions
- Focus on results, not concepts
- Address real-world tasks

Think of how-to guides as recipes in a cookbook - they tell you exactly what to do to achieve a specific result.

## Available Guides

### Project Management

- [Add a New Project](./add-new-project.md) - Steps to add applications to the monorepo

### Development

- [Development Workflow](./development-workflow.md) - Day-to-day development practices
- [Run Tests](./run-tests.md) - Testing across different project types

### Troubleshooting

- [Troubleshoot Issues](./troubleshoot-issues.md) - Common problems and solutions

## Common Tasks Quick Reference

### Starting Development

```bash
npm install
npm run doctor
npx nx serve <project-name>
```

### Running Tests

```bash
npm run test:all
npx nx affected:test
```

### Building Projects

```bash
npm run build
npx nx build <project-name>
```

## How to Use These Guides

1. **Identify your goal** - What do you want to achieve?
2. **Find the right guide** - Use the categories above
3. **Follow the steps** - Complete each step in order
4. **Adapt as needed** - Adjust for your specific situation

## Can't Find What You Need?

- Check [Reference](../reference/) for detailed information
- Read [Explanation](../explanation/) to understand the why
- Review [Tutorials](../tutorials/) if you need to learn basics
