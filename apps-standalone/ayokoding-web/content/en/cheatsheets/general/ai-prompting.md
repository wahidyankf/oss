---
title: 'AI Prompting'
date: 2025-03-18T07:36:00+07:00
draft: false
weight: 2
---

## Core Prompting Principles

### Clarity & Specificity

- **Be explicit**: State exactly what you want rather than implying it
- **Define parameters**: Specify format, length, tone, audience, and purpose
- **Set constraints**: Establish boundaries for what is and isn't needed
- **Use concrete language**: Avoid vague terms like "good" or "better"

### Context Management

- **Provide relevant background**: Include necessary context but avoid overwhelming
- **Establish knowledge scope**: Indicate what the AI should assume you know
- **Consider prompt length**: Balance comprehensive information with conciseness

### Instruction Framing

- **Sequence multi-part tasks**: Number steps for complex instructions
- **Use imperative verbs**: Start with action words like "Analyze," "Create," "Compare"

## Prompt Structure Techniques

### Role & Persona Assignment

- **Expert framing**: "As an expert in [domain]..."
- **Audience specification**: "Explain this to me as if I'm a [profession/age/knowledge level]"
- **Contextual roles**: "You are a [role], and I am a [role]"
- **Skill emphasis**: "Focus on your capabilities in [specific area]"

### Format Control

- **Template providing**: "Use this format: [template]"
- **Output structure**: "Structure your response as: [structure]"
- **Section requests**: "Include these sections: [list of sections]"

### Response Shaping

- **Length indication**: "Provide a [brief/comprehensive] explanation in approximately [X] words"
- **Depth setting**: "Explore this at a [basic/intermediate/advanced] level"
- **Style direction**: "Write in a [formal/conversational/technical] style"
- **Example inclusion**: "Include [number] examples to illustrate each point"

## Task-Specific Strategies

### Creative Writing

- **Character development**: "Create a character with these traits: [traits]"
- **Setting parameters**: "The story takes place in [setting] during [time period]"
- **Genre adherence**: "Write in the style of [genre/author]"

### Analysis & Explanation

- **Comparative framework**: "Compare and contrast [X] and [Y] based on [criteria]"
- **Multi-perspective analysis**: "Analyze this from [perspective A], [perspective B], and [perspective C]"

### Technical Content

- **Precision guidance**: "Use standard terminology from [field/domain]"
- **Accuracy emphasis**: "Ensure all information is technically accurate and up-to-date"
- **Complexity calibration**: "Explain at the level of someone with [background/experience]"

### Decision Support

- **Criteria definition**: "Evaluate options based on these criteria: [criteria]"
- **Alternatives request**: "Provide [number] alternatives with pros and cons"

## Advanced Techniques

### Chain-of-Thought Prompting

- **Reasoning request**: "Walk through your reasoning step by step"
- **Verbalized thinking**: "Think aloud as you solve this problem"
- **Process breakdown**: "Break down the process into discrete steps"
- **Logic tracing**: "Trace your logical progression from premises to conclusion"

### Few-Shot Learning

- **Example provision**: Provide 2-3 examples of desired input-output pairs
- **Pattern demonstration**: "Here are examples of the pattern I want you to follow: [examples]"
- **Consistency modeling**: Ensure examples demonstrate consistent formats and styles

### Self-Reflection & Refinement

- **Verification request**: "Verify your answer by checking if [condition]"
- **Improvement iteration**: "Refine your initial response by addressing these aspects: [aspects]"

## Common Pitfalls & Troubleshooting

### Vagueness Problems

- **Symptom**: Generic, shallow, or overly broad responses
- **Solution**: Add specific parameters, constraints, and evaluation criteria
- **Example fix**: Change "Write about climate change" to "Analyze three specific technological solutions to climate change, evaluating each based on cost, scalability, and time to implementation"

### Accuracy Issues

- **Solution**: Request source citations or explanations of confidence levels

### Verbosity Problems

- **Symptom**: Overly long, repetitive responses with low information density
- **Solution**: Specify word count, request conciseness, ask for key points only
- **Example fix**: Add "Limit your response to 300 words, focusing only on the most essential information"

### Tone Misalignment

- **Symptom**: Responses that don't match desired formality, technicality, or style
- **Solution**: Explicitly specify tone, provide examples of desired style
- **Example fix**: Add "Use a conversational tone suitable for a high school student, avoiding jargon and complex terminology"

## Optimization Techniques

### Iterative Refinement

- **Start broad**: Begin with a general prompt, then refine based on responses
- **Targeted feedback**: Provide specific feedback on what aspects need improvement
- **Incremental changes**: Modify one aspect at a time to isolate effects
- **Response evaluation**: Rate response quality to guide improvements

### System vs. User Messages

- **System messages**: Use for persistent instructions that apply to entire conversation
- **User messages**: Use for specific requests and content in the current exchange
- **Hybrid approach**: Combine persistent instructions with specific requests

### Evaluation Methods

- **Output quality check**: "Evaluate your response against these criteria: [criteria]"
