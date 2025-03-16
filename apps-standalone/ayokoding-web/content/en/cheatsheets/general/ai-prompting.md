---
title: 'ChatGPT'
date: 2025-03-16T07:20:00+07:00
draft: false
---

# ChatGPT

Here is the list of possible prompts that you can use in ChatGPT. To use this, you can substitute `{{}}` with what you need.

## Learning

### List of essentials topics

```yaml
- Give the list of the most important topics to learn, use the Pareto principle, and smooth the learning curve. Format the result as the list in markdown format, and make a heading for each topic.
  - {{topic}} essentials
- Get straight to the point, skip the Pareto principle section/intro
- Add the further readings section with links (if available), and ensure it includes all the items.
```

### List of 3-level topics

```yaml
- Give the list of the most important topics to learn with its subtopics, use the Pareto principle, and smoothen its learning curve. Format the result as the list in markdown format, and make a heading for each topic.
  - essentials, intermediate, and advanced topics of {{topic}}
- Get straight to the point, skip the Pareto principle section/intro
- Add the further readings section with links (if available), and ensure it includes all the items.
```

### Topic details

```yaml
- Teach me about this topic, consider the Pareto principles, and don't forget to make the explanation comprehensive and give many examples. Format the result in markdown format.
  - {{topic}}
- Get straight to the point, skip the Pareto principle section/intro
- Add the further readings section with links (if available), and ensure it includes all the items.
- Make the title H1
```

### Explain Like I am 5 Years Old

```clojure
Explain Like I am 5 years old and dumb about this {{topic}}: {{subtopic}}.

Also, give the benefits and downsides of this approach and further readings.

Format the result in markdown, with H1 as the title.
```
