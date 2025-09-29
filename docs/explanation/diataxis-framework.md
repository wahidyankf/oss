# Diátaxis Framework: A Systematic Approach to Documentation

Diátaxis is a comprehensive framework for organizing technical documentation
that divides content into four distinct types based on user needs: tutorials,
how-to guides, reference materials, and explanations. Developed by Daniele
Procida, this framework addresses three core documentation challenges: content
(what to write), style (how to write it), and architecture (how to organize
it).[1][2][3]

## **What is Diátaxis?**

The framework operates on two fundamental axes that create a systematic
relationship between different documentation types:[2]

**Theory vs. Practice Axis**: Distinguishes between theoretical knowledge
(understanding concepts) and practical application (performing tasks)

**Study vs. Application Axis**: Separates learning-oriented content from
work-oriented content

These axes create four quadrants, each serving specific user needs:[1][2]

```
                          ┌─────────────────────────────────┐
                          │    PRACTICAL STEPS              │
                          │  (When we're coding)            │
                          ├────────────────┬────────────────┤
                          │   TUTORIALS    │   HOW-TO       │
                          │                │   GUIDES       │
   LEARNING               │ "Take my hand" │ "Achieve goal" │    DOING
   (Acquisition)          │                │                │    (Application)
                          ├────────────────┼────────────────┤
                          │  EXPLANATION   │   REFERENCE    │
                          │                │                │
                          │ "Here's why"   │ "Look it up"   │
                          ├────────────────┴────────────────┤
                          │    THEORETICAL KNOWLEDGE        │
                          │  (When we're studying)          │
                          └─────────────────────────────────┘
```

- **Tutorials**: Learning-oriented, practical content that guides users through
  hands-on exercises
- **How-to Guides**: Problem-oriented, practical directions for accomplishing
  specific tasks
- **Reference**: Information-oriented, theoretical material providing factual
  descriptions
- **Explanation**: Understanding-oriented, theoretical content offering context
  and deeper insights

## **Why Diátaxis Works**

**Clear Purpose Separation**: The framework's strength lies in preventing
content mixing that confuses users. Each documentation type serves a distinct
purpose, ensuring users can quickly find what they need without wading through
irrelevant information.[4][5]

**User-Centered Design**: Diátaxis emerges from identifying four core user needs
rather than imposing arbitrary categories. When users approach documentation,
they're either trying to learn, solve problems, look up information, or
understand concepts.[4]

**Systematic Structure**: The framework provides clear guidance for both writers
and readers. Writers know exactly what belongs in each section, while readers
understand where to find specific types of information.[6]

## **Comparison with Other Frameworks**

**Diátaxis vs. DITA**: While DITA (Darwin Information Typing Architecture)
shares similarities with three of Diátaxis's quadrants (task, concept,
reference), significant differences exist:[4]

- DITA is a formal XML standard requiring validation, while Diátaxis is
  implementation-agnostic
- DITA has extensive tooling ecosystems but more complex structural requirements
- Diátaxis focuses on four core types with prescriptive information
  architecture, while DITA allows more flexible arrangements
- DITA emphasizes content reusability through topic-based authoring, while
  Diátaxis prioritizes user needs organization

**Diátaxis vs. Traditional Approaches**: Unlike unstructured documentation that
mixes content types, Diátaxis provides systematic organization that scales with
project growth. The framework contrasts with ad-hoc approaches by offering
consistent principles that guide content creation and maintenance.[3][7]

## **Effectiveness and Evidence**

**Adoption Success Stories**: Major organizations have successfully implemented
Diátaxis with measurable results:[7]

- ClickHelp restructured their entire documentation using Diátaxis, resulting in
  fewer user questions about locating content and positive feedback on improved
  usability
- Canonical adopted Diátaxis as their foundational documentation approach[6]
- Python documentation community voted to adopt the framework[8][9]
- Companies like Gatsby and others report improved user experience after
  reorganizing around Diátaxis principles[3]

**User Feedback**: Organizations report that Diátaxis helps users "love adding
to" documentation and makes resources easier to discover when needed. The
framework has enabled teams to build "high-quality internal documentation that
users love".[3]

**Practical Implementation**: The framework proves effective in real-world
scenarios where teams need to balance diverse user needs, from new contributors
to experienced developers.[10]

## **Pros and Cons**

**Advantages**:

- **Clarity**: Prevents content mixing that creates user confusion[5]
- **Scalability**: Framework grows effectively with project size and
  complexity[7]
- **Writer Guidance**: Provides clear direction for content creators about what
  belongs where[6]
- **User Efficiency**: Helps users quickly locate appropriate information for
  their current needs[4]
- **Quality Control**: Creates systematic approach to maintaining documentation
  standards[3]
- **Implementation Flexibility**: Works with various tools and platforms without
  technical constraints[4]

**Limitations and Trade-offs**:

- **Learning Curve**: Teams need time to understand and internalize the
  framework principles[11]
- **Rigid Structure**: Some critics argue the four-category model can feel
  restrictive for certain content types[12][13]
- **Not Universal**: The framework works well for tools but may have limitations
  for programming languages or complex systems that don't fit neatly into the
  four categories[13]
- **Oversimplification Risk**: Real user needs don't always separate cleanly
  into four distinct modes[4]
- **Implementation Overhead**: Requires ongoing discipline to maintain clear
  boundaries between content types[7]

## **AI Tooling Integration**

Diátaxis works particularly well with AI tooling for several reasons:

**Clear Classification**: AI systems can be trained to automatically classify
documentation content into the four Diátaxis categories, as demonstrated by
tools like Katara's AI-agent workflow that maps existing content to appropriate
framework categories.[14][10]

**Structured Generation**: AI can generate content more effectively when given
clear parameters about the type of documentation needed. The framework's
specific purposes and patterns for each category provide excellent prompts for
AI content generation.[15][14]

**Gap Analysis**: AI tools can analyze existing documentation to identify
missing content types and suggest areas for improvement based on Diátaxis
principles.[10]

**Content Quality**: The framework's systematic approach helps AI maintain
consistency across different documentation sections, ensuring generated content
serves its intended purpose.[14]

**Automated Compliance**: AI systems can monitor new content to ensure it aligns
with Diátaxis principles, helping teams maintain framework compliance over
time.[10]

The framework's clear structure and well-defined content patterns make it
particularly suitable for AI-assisted documentation workflows, where systematic
organization principles translate effectively into algorithmic processes.

## **WKF Labs Implementation**

### Directory Structure

WKF Labs documentation follows the Diátaxis framework with this organization:

```
docs/
├── tutorials/          # Learning-oriented, hands-on exercises
├── how-to/            # Task-oriented, problem-solving guides
├── reference/         # Information-oriented, factual lookup
└── explanation/       # Understanding-oriented, concepts and context
```

### The Four Types in Practice

#### 1. Tutorials (Learning-Oriented)

**Purpose**: Teaching newcomers, taking them by the hand through their first
steps.

**Characteristics**:

- Assumes no prior knowledge
- Provides a complete, working example
- Focuses on learning, not achieving a real goal
- Like teaching a child to cook

**Location**: `docs/tutorials/`

**Examples**:

- Setting up your first WKF Labs project
- Creating your first application
- Understanding Nx basics through practice

#### 2. How-To Guides (Task-Oriented)

**Purpose**: Helping users accomplish specific goals.

**Characteristics**:

- Assumes some knowledge and experience
- Provides step-by-step instructions
- Focuses on results, not concepts
- Like a recipe in a cookbook

**Location**: `docs/how-to/`

**Examples**:

- How to add a new library
- How to deploy to production
- How to debug build failures

#### 3. Reference (Information-Oriented)

**Purpose**: Providing factual information for lookup.

**Characteristics**:

- Describes the system objectively
- Organized for quick access
- Consistent and complete
- Like a dictionary or encyclopedia

**Location**: `docs/reference/`

**Examples**:

- API documentation
- Command reference
- Configuration options
- File structure

#### 4. Explanation (Understanding-Oriented)

**Purpose**: Deepening understanding of concepts and design decisions.

**Characteristics**:

- Provides context and background
- Discusses alternatives and trade-offs
- Connects topics together
- Like an academic paper or discussion

**Location**: `docs/explanation/`

**Examples**:

- Architecture decisions
- Why we use conventions
- Benefits of monorepo structure
- Testing philosophy

## **How to Use This Structure**

### For Documentation Writers

1. **Identify the type** before writing
2. **Stay within boundaries** - don't mix types
3. **Cross-reference** between types when needed
4. **Keep focused** on the specific purpose

### For Documentation Readers

1. **Know your need**:

   - New to the project? → Start with **Tutorials**
   - Have a specific task? → Use **How-To Guides**
   - Need details? → Check **Reference**
   - Want to understand? → Read **Explanation**

2. **Navigate efficiently**:
   - Each section has its own README with an index
   - The main README provides quick access to all sections

## **Common Pitfalls to Avoid**

### Don't Mix Types

❌ **Wrong**: A tutorial that explains architecture decisions ✅ **Right**: A
tutorial that focuses on doing, with links to explanations

❌ **Wrong**: A how-to guide that teaches concepts ✅ **Right**: A how-to guide
that assumes knowledge and focuses on the task

❌ **Wrong**: Reference documentation with opinions ✅ **Right**: Reference
documentation that states facts objectively

❌ **Wrong**: Explanations with step-by-step instructions ✅ **Right**:
Explanations that discuss concepts, linking to how-to guides

### Don't Create Hybrids

Instead of one document that tries to be everything:

- Create focused documents for each need
- Link between them appropriately
- Let users choose their path

## **Benefits of This Approach**

1. **Clear Purpose**: Each document has one job and does it well
2. **Better Navigation**: Users can find what they need quickly
3. **Easier Maintenance**: Clear boundaries make updates simpler
4. **Complete Coverage**: The framework ensures no user need is forgotten
5. **Scalable**: New documents fit naturally into the structure

## **Examples in WKF Labs**

### A User Journey

1. **New developer** joins the team:

   - Starts with `tutorials/first-steps.md`
   - Follows `tutorials/create-first-app.md`

2. **Needs to add a feature**:

   - Uses `how-to/add-new-project.md`
   - References `reference/commands.md` for specific commands

3. **Encounters an error**:

   - Follows `how-to/debug-issues.md`
   - Checks `reference/error-codes.md`

4. **Wants to understand why**:
   - Reads `explanation/architecture.md`
   - Studies `explanation/monorepo-benefits.md`

## **Further Reading**

- [Diátaxis Framework Website](https://diataxis.fr/)
- [Documentation System Guide](https://documentation.divio.com/)
- [Write the Docs: Documentation Types](https://www.writethedocs.org/guide/docs-as-code/)

---

_This framework was created by Daniele Procida. WKF Labs has adopted it to
provide clear, effective documentation for all users._

## **References**

[1] https://drostan.org/notes/documentation/explanations/diataxis/ [2]
https://diataxis.fr/start-here/ [3] https://diataxis.fr [4]
https://idratherbewriting.com/blog/what-is-diataxis-documentation-framework [5]
https://mintlify.com/blog/breaking-down-common-documentation-mistakes [6]
https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation
[7]
https://clickhelp.com/clickhelp-technical-writing-blog/diataxis-how-it-helped-clickhelp-to-transform-the-documentation-experience/
[8]
https://discuss.python.org/t/adopting-the-diataxis-framework-for-python-documentation/15072?page=2
[9]
https://discuss.python.org/t/adopting-the-diataxis-framework-for-python-documentation/15072
[10] https://www.katara.ai/success-stories/partisia [11]
https://kodesage.ai/en/blog-1/article/9-best-software-documentation-tools-in-2025-1/24
[12] https://news.ycombinator.com/item?id=36610846 [13]
https://www.hillelwayne.com/post/problems-with-the-4doc-model/ [14]
https://dev.to/joshmo_dev/improving-documentation-with-ai-using-rig-rust-1ami
[15] https://www.mintlify.com/guides/content-types
