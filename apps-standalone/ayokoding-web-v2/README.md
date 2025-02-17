# Ayokoding Web V2

## Overview

Ayokoding Web V2 is a multilingual Hugo-powered website for learning and sharing knowledge in both English and Indonesian.

## Features

- 🌐 Multilingual support (English and Indonesian)
- 📚 Hugo Book theme
- 🔍 Full-text search functionality
- 📱 Responsive design
- 🌓 Light/dark mode support

## Prerequisites

- [Hugo](https://gohugo.io/) (Extended version recommended)
- [Go](https://golang.org/) (for module support)

## Getting Started

### Installation

1. Clone the repository

```bash
git clone https://github.com/wahidyankf/ayokoding-web-v2.git
cd ayokoding-web-v2
```

2. Install Hugo modules

```bash
hugo mod get
```

### Development

Start the local development server:

```bash
hugo server -D
```

- `-D` flag includes draft content
- Access the site at `http://localhost:1313`

### Building for Production

Generate static files:

```bash
hugo
```

The generated site will be in the `public/` directory.

## Project Structure

```
.
├── content/
│   ├── en/           # English content
│   │   └── learn/
│   └── id/           # Indonesian content
│       └── belajar/
├── static/           # Static assets
│   ├── css/
│   └── js/
├── themes/           # Hugo themes
│   └── hugo-book/
└── hugo.toml         # Hugo configuration
```

## Customization

- Edit `hugo.toml` to modify site settings
- Add content in `content/en/` or `content/id/`
- Customize CSS in `static/css/custom.css`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

## Acknowledgments

- [Hugo](https://gohugo.io/)
- [Hugo Book Theme](https://github.com/alex-shpak/hugo-book)
