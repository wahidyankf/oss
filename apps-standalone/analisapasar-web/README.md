# analisapasar-web

Market analysis platform providing insights and educational content about financial markets in Indonesian and English. Currently in early development phase.

## Overview

AnalisaPasar ("Market Analysis" in Indonesian) is designed to be a comprehensive platform for market analysis content, targeting Indonesian traders and investors who want to understand market dynamics better.

## Status

⚠️ **In Development**: This project is in its early stages with minimal content. The infrastructure is set up and ready for content creation.

## Features

- **Bilingual Support**: Indonesian (primary) and English
- **Documentation-style Layout**: Using Hextra theme for clear presentation
- **SEO Optimized**: Hugo static site generation
- **Responsive Design**: Mobile-friendly interface
- **Dark/Light Theme**: User preference support

## Tech Stack

- **Static Site Generator**: Hugo (latest)
- **Theme**: Hextra documentation theme
- **Content Format**: Markdown with YAML frontmatter
- **Deployment**: Netlify/Vercel ready
- **Build Tools**: Custom build script

## Getting Started

### Prerequisites

- Node.js 22.20.0 (managed by Volta)
- npm 11.1.0
- Hugo extended version (latest)

### Installation

```bash
# Install Hugo (macOS)
brew install hugo

# Navigate to project
cd apps-standalone/analisapasar-web

# Install dependencies
npm install
```

### Development

```bash
# Start development server
npm run dev
# or
hugo server -D

# Server runs at http://localhost:1313
```

### Building

```bash
# Build for production
npm run build
# or
./build.sh
# or
hugo --minify

# Output will be in public/ directory
```

## Content Structure

```
content/
├── _index.md          # Homepage
├── docs/              # Documentation section
│   ├── _index.md
│   └── first-page.md  # Template page
├── en/                # English content
│   └── _index.md
└── id/                # Indonesian content
    └── _index.md
```

### Creating Content

#### Market Analysis Articles (Indonesian)

```bash
hugo new content/id/analisa/nama-topik.md
```

#### Market Analysis Articles (English)

```bash
hugo new content/en/analysis/topic-name.md
```

### Content Frontmatter

```yaml
---
title: 'Analisa Pasar Saham Hari Ini'
date: 2024-01-01
draft: false
description: 'Analisa teknikal dan fundamental pasar saham'
tags: ['saham', 'analisa-teknikal', 'IHSG']
categories: ['daily-analysis']
weight: 10
---
```

## Configuration

Main configuration in `hugo.yaml`:

```yaml
baseURL: 'https://analisapasar.com/'
title: 'Analisa Pasar'
theme: hextra

languages:
  id:
    languageName: 'Indonesia'
    weight: 1
  en:
    languageName: 'English'
    weight: 2

defaultContentLanguage: 'id'
```

## Planned Content Categories

### Technical Analysis

- Chart patterns
- Technical indicators
- Trading strategies
- Market psychology

### Fundamental Analysis

- Company analysis
- Sector analysis
- Economic indicators
- Financial ratios

### Market Education

- Trading basics
- Investment principles
- Risk management
- Portfolio management

### Daily/Weekly Analysis

- Market overview
- Stock picks
- Sector rotation
- Economic calendar

## Development Roadmap

1. **Phase 1**: Infrastructure setup ✅
2. **Phase 2**: Content structure design 🚧
3. **Phase 3**: Initial content creation
4. **Phase 4**: Interactive features
5. **Phase 5**: Community features

## Scripts

```bash
npm run dev      # Start development server
npm run build    # Build for production
./build.sh       # Custom build script
```

## Deployment

### Netlify Configuration

```toml
[build]
command = "hugo --minify"
publish = "public"

[build.environment]
HUGO_VERSION = "0.xxx.x"
```

### Vercel Configuration

```json
{
  "buildCommand": "hugo --minify",
  "outputDirectory": "public",
  "build": {
    "env": {
      "HUGO_VERSION": "0.xxx.x"
    }
  }
}
```

## Contributing

This project is in early development. If you're interested in contributing:

1. Check the roadmap above
2. Create content in Markdown
3. Follow the content structure
4. Submit a pull request

## Future Features

- Real-time market data integration
- Interactive charts
- Trading calculators
- Community discussions
- Email newsletters
- Mobile app

## Related Documentation

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Hextra Theme Documentation](https://imfing.github.io/hextra/)
- [Standalone Projects Guide](/docs/reference/standalone-projects.md)
- [Adding New Project Guide](/docs/how-to/add-new-project.md)

## License

MIT License - see the [LICENSE](LICENSE) file for details.
