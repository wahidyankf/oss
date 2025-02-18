# Ayokoding Web

## Overview

Ayokoding Web is a modern, educational web platform designed to provide coding tutorials, resources, and learning paths for developers of all skill levels. Built with cutting-edge web technologies, this application offers an interactive and engaging learning experience.

## Purpose

The goal of Ayokoding Web is to:

- Provide high-quality, accessible coding tutorials
- Create learning paths for various programming technologies
- Share insights and best practices in software development
- Build a community of learners and developers

## Prerequisites

- Node.js 20.17.0
- npm 11.1.0

## Getting Started

### Installation

```bash
npm install
```

### Development

Run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser.

### Testing

Run tests:

```bash
npm test
```

### Build

Create a production build:

```bash
npm run build
```

## Features

- Next.js 15.1.6
- React 18
- TypeScript
- Tailwind CSS
- ESLint for linting

## Project Structure

- `src/app/`: Main application routes and components
- `src/app/__tests__/`: Test files
- `src/lib/`: Utility functions and helper modules
- `public/`: Static assets
- `scripts/`: Utility scripts for project management

## Configuration

### Environment Variables

Create a `.env.local` file in the project root and add the following variables:

- `NEXT_PUBLIC_SITE_URL`: Base URL for the application
- `NEXT_PUBLIC_ANALYTICS_ID`: Analytics tracking ID (optional)

## Scripts

- `dev`: Start development server
- `build`: Create production build
- `start`: Start production server
- `lint`: Run ESLint
- `typecheck`: Run TypeScript type checking
- `generate:category-pages`: Generate static category pages

## Deployment

Optimized for static and server-side rendering with Next.js. Recommended deployment platforms:

- Vercel
- Netlify
- Cloudflare Pages

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or support, please open an issue on GitHub or contact the maintainers.
