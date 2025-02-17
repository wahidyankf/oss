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

#### Deployment Steps

1. Go to Vercel Dashboard
2. Import the `ayokoding` repository
3. Configure Project Settings:
   - **Root Directory**: `apps-standalone/ayokoding-web-v2`
   - **Build Command**: `./build.sh`
   - **Output Directory**: `public`
   - **Install Command**: Leave blank (handled in build script)

#### Vercel Configuration Details

- Framework: Static Site
- Build Tool: Custom Build Script
- Hugo Version: 0.134.3 Extended

#### Troubleshooting

- Ensure Vercel has read access to the repository
- Check build logs for any specific errors
- Verify Hugo extended version is installed in build environment

**Important Notes**:

- The custom `build.sh` script handles Hugo installation and site generation
- Monorepo deployment requires precise root directory configuration

### Vercel Deployment Troubleshooting

#### Common Deployment Errors

- **wget/curl not found**:
  - Ensure build script uses available system commands
  - Fallback to alternative download methods

#### Debugging Steps

1. Check Vercel Build Logs
2. Verify Build Script Permissions
3. Test Build Script Locally

#### Vercel Configuration Checklist

- [ ] Root Directory: `apps-standalone/ayokoding-web-v2`
- [ ] Build Script: Executable and compatible with Vercel environment
- [ ] Hugo Version: Explicitly specified
- [ ] Output Directory: `public`

#### Potential Solutions

```bash
# Verify build script works
chmod +x build.sh
./build.sh

# Check Hugo installation
hugo version
```

**Troubleshooting Tips**:

- Use `curl` instead of `wget`
- Ensure build script has proper error handling
- Check Vercel documentation for platform-specific build requirements

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
