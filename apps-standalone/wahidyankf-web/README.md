# Wahidyan KF Web - Personal Portfolio Website

This is a personal portfolio website for Wahidyan Kresna Fridayoka, a seasoned Software Engineer specializing in Frontend Engineering and Engineering Management. Built with Next.js, it showcases Wahidyan's professional experience, skills, and personal projects.

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

- Next.js (v14.2.13)
- React (v18)
- TypeScript
- Tailwind CSS (v3.4.1)
- Lucide React (v0.446.0) and react-icons (v5.3.0) for icons
- Vitest for unit testing
- Playwright for end-to-end testing
- ESLint and Prettier for code quality
- Husky and lint-staged for Git hooks
- Vercel for deployment

## Getting Started

### Prerequisites

- Node.js (v20.17.0 or later recommended)
- npm (v10.8.3 or later recommended)

### Installation

1. Clone the repository:
   `git clone https://github.com/wahidyankf/wahidyankf-web.git`
   `cd wahidyankf-web`

2. Install dependencies:
   `npm install`

3. Run the development server:
   `npm run dev`

4. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Testing

Run unit tests:
`npm run test:unit`

Run unit tests in watch mode:
`npm run test:unit:watch`

Run end-to-end tests:
`npm run test:e2e`

## Linting and Formatting

Run ESLint:
`npm run lint`

Format code with Prettier:
`npm run format`

## Building for Production

Build the application for production:
`npm run build`

## Deployment

The project is configured for deployment on Vercel, providing seamless integration with GitHub for continuous deployment.

## Project Structure

The project follows a modular structure:

- `src/`: Main application code
  - `app/`: Next.js App Router pages and layouts
  - `components/`: Reusable React components
  - `utils/`: Utility functions
- `e2e-tests/`: Playwright end-to-end tests
- `public/`: Static assets

## Key Components

- Navigation: Responsive navigation component for both mobile and desktop layouts
- SearchComponent: Reusable search input for filtering content
- HighlightText: Component for highlighting search terms within text

## Styling

The project uses a dual-theme system (dark and light) implemented with Tailwind CSS. The styling is consistent across all pages, with a focus on accessibility and responsiveness.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/wahidyankf/wahidyankf-web/issues).

## Author

Wahidyan Kresna Fridayoka - [wahidyankf.com](https://wahidyankf.com)

## License

This project is open source and available under the [MIT License](LICENSE).
