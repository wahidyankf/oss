# wahidyankf-web

Personal portfolio website for Wahidyan Kresna Fridayoka, showcasing professional experience as a Software Engineer specializing in Islamic Finance/Sharia-compliant Fintech and Engineering Leadership.

## Features

- Responsive design for various devices and screen sizes
- Interactive and searchable CV/Resume page
- Personal projects showcase
- Dynamic content rendering with client-side interactions
- Advanced search functionality across CV entries and projects
- SEO optimization
- Theme toggle between light and dark modes
- Analytics integration with Google Analytics and Google Tag Manager

## Tech Stack

- **Framework**: Next.js 14.2.13 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS 3.4.1, class-variance-authority, tailwind-merge
- **Icons**: Lucide React, React Icons
- **Testing**: Vitest (unit), Playwright (E2E)
- **Code Quality**: ESLint, Prettier, Husky, lint-staged
- **Analytics**: Google Analytics, Google Tag Manager
- **Deployment**: Vercel

## Getting Started

### Prerequisites

- Node.js 22.20.0 (managed by Volta)
- npm 11.1.0

### Installation

From the repository root:

```bash
# Navigate to project
cd apps-standalone/wahidyankf-web

# Install dependencies
npm install
```

### Development

```bash
# Start development server
npm run dev
# or from root: npm run wahidyankf-web:dev

# Open http://localhost:3000
```

## Testing

### Unit Tests (Vitest)

```bash
# Run unit tests
npm run test:unit

# Watch mode
npm run test:unit:watch

# Run with UI
npx vitest --ui
```

### E2E Tests

E2E tests are located in a separate project: `apps-standalone/wahidyankf-e2e`

```bash
cd ../wahidyankf-e2e
npm test
```

## Building and Code Quality

### Linting and Formatting

```bash
# ESLint
npm run lint

# Format with Prettier
npm run format

# Git hooks automatically format on commit
```

### Production Build

```bash
# Build for production
npm run build
# or from root: npm run wahidyankf-web:build

# Start production server
npm start
```

## Deployment

Configured for Vercel deployment with `vercel.json`:

- Automatic deployments disabled for main branch
- Manual deployments via Vercel CLI or dashboard
- Environment variables configured in Vercel dashboard

## Project Structure

```
wahidyankf-web/
├── src/
│   ├── app/                 # Next.js App Router
│   │   ├── cv/              # CV page with search
│   │   ├── personal-projects/ # Projects showcase
│   │   ├── layout.tsx       # Root layout with theme
│   │   └── page.tsx         # Home page
│   ├── components/          # Reusable components
│   │   ├── Navigation.tsx   # Responsive navigation
│   │   ├── SearchComponent.tsx # Search functionality
│   │   └── HighlightText.tsx # Text highlighting
│   └── utils/               # Utility functions
├── public/                  # Static assets
├── vitest.config.ts         # Vitest configuration
└── vercel.json              # Vercel configuration
```

## Key Features

### Advanced CV Search

- Real-time filtering of CV entries
- Skill-based search
- Highlighted search results
- Responsive search interface

### Theme System

- Dark/light mode toggle
- System preference detection
- Persistent theme selection
- Smooth transitions

### Performance Optimizations

- Optimized images and fonts
- Code splitting
- Memoized search algorithms
- Minimal bundle size

## Environment Variables

```bash
# .env.local
NEXT_PUBLIC_GA_ID=your-google-analytics-id
NEXT_PUBLIC_GTM_ID=your-google-tag-manager-id
```

## Scripts Reference

```bash
npm run dev          # Development server
npm run build        # Production build
npm start            # Start production server
npm run lint         # Run ESLint
npm test             # Run unit tests
npm run test:unit    # Run unit tests
npm run test:unit:watch # Watch mode
npm run format       # Format with Prettier
npm run prepare      # Setup git hooks
```

## Related Documentation

- [Standalone Projects Guide](/docs/reference/standalone-projects.md)
- [Common Commands Reference](/docs/reference/commands.md)
- [Development Workflow](/docs/how-to/development-workflow.md)
- [Troubleshooting Guide](/docs/how-to/troubleshoot-issues.md)

## License

MIT License - see the [LICENSE](LICENSE) file for details.
