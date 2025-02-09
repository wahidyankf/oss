# Ayokoding Monorepo

## Project Overview

This is a Next.js monorepo built with Nx, designed to provide a scalable and maintainable web application architecture.

## Tech Stack

- **Framework**: Next.js
- **Monorepo Management**: Nx
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Testing**: 
  - Unit Testing: Jest
  - E2E Testing: Playwright

## Project Structure

```
ayokoding/
├── apps/
│   ├── web/           # Main Next.js web application
│   └── web-e2e/       # End-to-end tests for the web application
├── libs/              # Shared libraries and components
```

## Getting Started

### Prerequisites

- Node.js (v18 or later)
- npm (v9 or later)

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

### Running the Application

- Start development server:
  ```bash
  npx nx serve web
  ```

- Build for production:
  ```bash
  npx nx build web
  ```

- Run tests:
  ```bash
  npx nx test web
  npx nx e2e web-e2e
  ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [Your Email]

Project Link: [https://github.com/yourusername/ayokoding](https://github.com/yourusername/ayokoding)
