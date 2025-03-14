# Ayokoding Web V2

## Overview

Ayokoding Web V2 is a multilingual Hugo-powered website for learning and sharing knowledge in both English and Indonesian.

## Features

- 🌐 Multilingual support (English and Indonesian)
- 📚 Hugo Book theme
- 🔍 Full-text search functionality
- 📱 Responsive design
- 🌓 Light/dark mode support
- 🧭 Breadcrumb navigation for enhanced user experience

## Prerequisites

- **Hugo**: Install using Homebrew or manually as described:
  ```bash
  brew install hugo
  ```

- **Volta**: Install Volta for managing JavaScript tools:
  ```bash
  curl https://get.volta.sh | bash
  ```
  Verify the installation:
  ```bash
  volta --version
  ```

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
├── README.md
├── archetypes
│   └── default.md         # Hugo archetypes for content templates
├── assets
│   └── custom.scss        # Custom SCSS styles
├── build.sh               # Build script for the project
├── content
│   ├── _index.md          # Main site index
│   ├── en                 # English content directory
│   ├── id                 # Indonesian content directory
│   ├── template           # Template for new content
│   └── terms-and-conditions.md
├── go.mod                 # Go module definition
├── go.sum                 # Go module checksum
├── hugo.toml              # Hugo configuration file
├── layouts
│   ├── _default           # Default layout templates
│   ├── partials           # Partial layout components
│   └── shortcodes         # Custom shortcode definitions
├── package.json           # Node.js project dependencies
├── static
│   ├── css                # Static CSS files
│   ├── images             # Static image assets
│   └── js                 # Static JavaScript files
├── themes
│   └── hugo-book          # Hugo Book theme
├── vercel.json            # Vercel deployment configuration
```

### Directory Descriptions

- `archetypes/`: Contains content templates for Hugo
- `assets/`: Custom SCSS and asset preprocessing
- `content/`: All site content, organized by language
- `layouts/`: Custom layout templates and shortcodes
- `static/`: Static assets like CSS, JS, and images
- `themes/`: Hugo theme (currently using hugo-book)

## Customization

### Theme

The site uses the [Hugo Book theme](https://github.com/alex-shpak/hugo-book) with several customizations:

- Custom SCSS styles in `assets/custom.scss`
- Layout overrides in `layouts/` directory
- Menu configuration in `hugo.toml`

### Breadcrumb Navigation

The site includes breadcrumb navigation to improve user experience and site navigation:

- **Implementation**: Custom partial template in `layouts/partials/docs/breadcrumb.html`
- **Layout Override**: Added to the main layout via `layouts/_default/baseof.html`
- **Styling**: Breadcrumb styles defined in `assets/custom.scss`
- **Format**: Shows the full navigation path (e.g., `Home > en > learn > topic > subtopic`)

### Content Structure

- Edit `hugo.toml` to modify site settings
- Add content in `content/en/` or `content/id/`
- Customize CSS in `static/css/custom.css`

### Layout Overrides

Hugo Book theme supports layout overrides, which we use throughout this project:

- `/layouts/_default/baseof.html` - Main layout override to add breadcrumb navigation
- `/layouts/partials/docs/breadcrumb.html` - Custom breadcrumb navigation template
- `/layouts/partials/docs/inject/head.html` - Custom styles injection

### Styling

Custom styles are implemented through Hugo's partial injection system:

- Custom styles are added in `/layouts/partials/docs/inject/head.html`
- This approach avoids potential SCSS compilation issues
- Styles include breadcrumb formatting, sticky navigation, and image alignment

### Breadcrumb Navigation

- Displays the current page hierarchy in a user-friendly format
- Auto-capitalizes URL segments for better readability (e.g., "how-to-learn" becomes "How To Learn")
- Does not display "Home >" when on the home page
- Implemented as a sticky navigation element that remains visible when scrolling

### Mobile Responsiveness

- Responsive design for various screen sizes
- Font size adjustments for smaller screens
- Navigation elements adapt to mobile view

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

#### Deployment Environment Challenges

- **No sudo access**: Build scripts must work without root privileges
- **Limited PATH modifications**: Install tools in user space
- **Strict security constraints**: Minimal system modifications

#### Debugging Deployment

1. Verify Hugo Installation

   ```bash
   # Check Hugo version and path
   which hugo
   hugo version
   ```

2. Build Script Validation
   - Ensure script uses user-space installations
   - Avoid system-wide modifications
   - Use `$HOME/bin` for local binaries

#### Common Deployment Pitfalls

- Attempting to use `sudo`
- Hardcoding system paths
- Assuming root access

#### Recommended Build Strategy

- Download binaries directly
- Install in user home directory
- Modify PATH temporarily
- Use minimal system interactions

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

**Vercel-Specific Tips**:

- Always test build script locally
- Simulate Vercel environment
- Check build logs carefully
- Minimize external dependencies

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
