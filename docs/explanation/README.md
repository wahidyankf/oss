# Explanation

**Understanding-oriented discussions** that clarify and illuminate particular topics.

## What is Explanation Documentation?

Explanation documentation provides context and discusses topics at a higher level. It:

- Deepens understanding of concepts
- Discusses alternatives and trade-offs
- Connects different parts of the system
- Explains the "why" behind decisions

Think of explanations as conversations with an expert - they share insights, discuss options, and help you understand not just what, but why.

## Available Explanations

### Documentation & Architecture

- [Diátaxis Framework](./diataxis-framework.md) - Understanding our documentation approach
- [Design Decisions](./design-decisions.md) - Key architectural choices and their rationale
- [Monorepo Structure](./monorepo-structure.md) - Why we organize code this way

## Key Concepts Explained

### Why a Monorepo?

This repository uses a monorepo structure to:

- Share code and configurations
- Ensure consistency across projects
- Simplify dependency management
- Enable atomic changes across projects

### Why Hybrid Architecture?

We combine Nx-integrated and standalone projects because:

- Different projects have different needs
- Gradual migration is less disruptive
- Some tools (like Hugo) work better standalone
- Flexibility for experimentation

### Why These Technologies?

Our technology choices reflect:

- **Performance**: Fast builds and runtime
- **Developer Experience**: Good tooling and ecosystem
- **Flexibility**: Ability to use best tool for each job
- **Maintainability**: Long-term sustainability

## How to Read Explanations

1. **Start with curiosity** - Come with questions
2. **Read for understanding** - Not for immediate action
3. **Consider alternatives** - Think about trade-offs
4. **Connect concepts** - See the bigger picture

## Related Documentation

- Apply knowledge with [How-To Guides](../how-to/)
- Find specifics in [Reference](../reference/)
- Learn basics in [Tutorials](../tutorials/)
