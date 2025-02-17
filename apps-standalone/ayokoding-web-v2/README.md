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

## Deployment

### Vercel Deployment

To deploy this subfolder to Vercel:

1. **Monorepo Deployment**

   - In Vercel, select the main `ayokoding` repository
   - Configure a new project
   - Set the root directory to `apps-standalone/ayokoding-web-v2`
   - Build Command: `hugo`
   - Output Directory: `public`
   - Framework Preset: Hugo
   - Hugo Version: 0.134.3+extended

2. **Alternative: Direct Subfolder Deployment**
   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/wahidyankf/ayokoding&directory=apps-standalone/ayokoding-web-v2)

**Note:**

- Ensure you have a Vercel account
- The repository must be connected to your GitHub account
- For monorepo deployment, configure the project settings carefully

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
