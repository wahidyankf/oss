# Wahidyan KF Web

## 1. Overview

Wahidyan KF Web is a personal portfolio website for Wahidyan Kresna Fridayoka, a seasoned Software Engineer specializing in Frontend Engineering and Engineering Management. The website is designed to showcase Wahidyan's professional experience, skills, and personal projects.

Key features of the website include:

1. Responsive design: The website is built to be accessible and functional across various devices and screen sizes.

2. Interactive CV/Resume: A comprehensive and searchable CV page that highlights Wahidyan's work experience, education, skills, and achievements.

3. Personal projects showcase: A dedicated page to display Wahidyan's personal projects, including descriptions and links to repositories or live sites.

4. Dynamic content rendering: The website uses client-side rendering to provide a smooth and interactive user experience.

5. Search functionality: Users can search through CV entries and projects, making it easy to find specific information.

6. SEO optimization: The website is optimized for search engines to improve visibility and discoverability.

7. Theme toggle: Users can switch between light and dark themes for better readability and personal preference.

8. Analytics integration: The site includes Google Analytics and Google Tag Manager for tracking user interactions and gathering insights.

The website is built using modern web technologies, including Next.js, React, TypeScript, and Tailwind CSS. It follows best practices in web development, including responsive design, accessibility, and performance optimization.

This portfolio website serves as a comprehensive representation of Wahidyan's professional profile, making it easier for potential employers, clients, or collaborators to learn about his skills, experience, and projects in an engaging and user-friendly manner.

## 2. Tech Stack

The Wahidyan KF Web project utilizes a modern and robust tech stack:

### Core Technologies:

- Next.js (v14.2.13): React framework for production-grade applications
- React (v18): JavaScript library for building user interfaces
- TypeScript: Typed superset of JavaScript for improved developer experience and code quality

### Styling:

- Tailwind CSS (v3.4.1): Utility-first CSS framework
- tailwind-merge: Utility for merging Tailwind CSS classes
- tailwindcss-animate: Animation plugin for Tailwind CSS

### UI Components and Icons:

- class-variance-authority (v0.7.0): Library for creating variant classes
- clsx (v2.1.1): Utility for constructing className strings conditionally
- lucide-react (v0.446.0): Icon library for React
- react-icons (v5.3.0): Popular icon library for React

### Development Tools:

- ESLint: JavaScript and TypeScript linter
- Prettier (v2.8.8): Code formatter
- Husky (v9.1.6): Git hooks made easy
- lint-staged (v13.3.0): Run linters on git staged files

### Testing:

- Vitest (v0.31.0): Fast Vite-native unit test framework
- @testing-library/react (v14.0.0): Testing utilities for React
- @testing-library/jest-dom (v5.16.5): Custom jest matchers for DOM testing
- Playwright (v1.48.1): End-to-end testing framework

### Build and Development:

- Vite (v4.3.9): Next generation frontend tooling
- PostCSS (v8): Tool for transforming CSS with JavaScript

### Third-party Integrations:

- @next/third-parties (v14.2.14): Third-party integrations for Next.js (e.g., Google Analytics, Google Tag Manager)

### Deployment:

- Vercel: Platform for deploying and hosting Next.js applications, providing seamless integration with GitHub for continuous deployment

### Node.js Environment:

- Node.js: v20.17.0 (managed by Volta)
- npm: v10.8.3 (managed by Volta)

This tech stack provides a solid foundation for building a modern, performant, and maintainable web application. It combines the latest frontend technologies with robust development and testing tools to ensure high-quality code and an excellent user experience. The deployment on Vercel ensures fast, reliable hosting with automatic deployments triggered by changes in the GitHub repository.

## 3. Functional Requirements

### 3.1 Home Page

The Home Page serves as the main entry point for the portfolio website. It provides an overview of Wahidyan's professional profile and quick access to other sections of the site.

#### 3.1.1 Layout and Components

1. The page should have a responsive layout that adapts to different screen sizes.
2. It should include a Navigation component for easy access to other pages.
3. The main content should be centered with a maximum width for optimal readability.

#### 3.1.2 Content Sections

1. Welcome Header: A prominent title welcoming visitors to the portfolio.

2. Search Functionality:

   - A search input field allowing users to search for skills, languages, or frameworks.
   - The search should filter content in real-time as the user types.
   - The URL should update with the search term, enabling shareable search results.

3. About Me:

   - A section displaying a brief introduction about Wahidyan.
   - Content should be filterable based on the search term.
   - Links within the content should be clickable and styled distinctly.

4. Skills & Expertise:

   - Subsections for "Top Skills", "Top Programming Languages", and "Top Frameworks & Libraries" used in the last 5 years.
   - Each skill/language/framework should be displayed as a clickable button.
   - Buttons should show the item name and duration of experience.
   - Clicking a button should navigate to the CV page with the item pre-searched.

5. Quick Links:

   - Links to "View My CV" and "Browse My Personal Projects" pages.

6. Connect With Me:
   - Social media and contact links (GitHub, LinkedIn, Email).
   - Links should open in new tabs when clicked.

#### 3.1.3 Interactivity and Behavior

1. Search Functionality:

   - As the user types in the search field, content should be filtered in real-time.
   - The URL should update with the search term (e.g., "/?search=React").
   - When loading the page with a search parameter, the search field should be pre-filled, and content should be pre-filtered.

2. Skills & Expertise Interaction:

   - Clicking on a skill/language/framework button should navigate to the CV page with the search term pre-filled and the page scrolled to the top.

3. External Links:
   - All external links (GitHub, LinkedIn, Email) should open in new tabs.

#### 3.1.4 Performance and SEO

1. The page should load quickly and be optimized for performance.
2. Proper semantic HTML should be used for better SEO and accessibility.
3. The page title and meta description should be optimized for search engines.

#### 3.1.5 Testing Requirements

1. Unit tests should cover all major components and functions of the Home page.
2. End-to-end tests should verify:
   - Correct rendering of all main sections
   - Functionality of the search feature
   - Navigation to other pages (CV, Personal Projects)
   - Filtering of content based on search terms
   - Correct behavior of external links

### 3.2 CV Page

The CV Page presents a comprehensive view of Wahidyan's professional experience, skills, and qualifications. It offers an interactive and searchable interface for users to explore his career history and achievements.

#### 3.2.1 Layout and Components

1. The page should have a responsive layout that adapts to different screen sizes.
2. It should include a Navigation component for easy access to other pages.
3. The main content should be centered with a maximum width for optimal readability.

#### 3.2.2 Content Sections

1. Page Title: A prominent "Curriculum Vitae" heading at the top of the page.

2. Search Functionality:

   - A search input field allowing users to filter CV entries.
   - The search should update results in real-time as the user types.
   - The URL should update with the search term for shareable filtered views.

3. Highlights:

   - An "About Me" section providing a brief overview of Wahidyan's professional profile.
   - Display of top skills, programming languages, and frameworks/libraries used in the last 5 years.

4. Work Experience:

   - A chronological list of work experiences, grouped by organization.
   - Each entry should include job title, company name, employment period, and job details.
   - Option to toggle between showing all experiences or only those within the last 5 years.

5. Honors & Awards:

   - A list of professional honors and awards received.

6. Licenses & Certifications:

   - A list of professional licenses and certifications obtained.

7. Languages (if applicable):

   - A list of languages spoken and proficiency levels.

8. Education:
   - A list of educational qualifications, including degree, institution, and graduation year.

#### 3.2.3 Interactivity and Behavior

1. Search Functionality:

   - As the user types in the search field, CV entries should be filtered in real-time.
   - The URL should update with the search term (e.g., "/cv?search=React").
   - When loading the page with a search parameter, the search field should be pre-filled and content pre-filtered.

2. Skills and Keywords Interaction:

   - Skills, languages, and frameworks should be clickable.
   - Clicking on an item should update the search term and filter the CV accordingly.

3. Work Experience Toggle:

   - A toggle button to switch between showing all work experiences and only those within the last 5 years.

4. External Links:

   - Links to external profiles (e.g., GitHub, LinkedIn) or credentials should open in new tabs.

5. Scroll Behavior:
   - When navigating to the CV page with a search term, the page should automatically scroll to the top.

#### 3.2.4 Performance and SEO

1. The page should load quickly, with optimized rendering of potentially long lists of experiences and skills.
2. Use proper semantic HTML structure for better SEO and accessibility.
3. Implement appropriate meta tags for SEO optimization.

#### 3.2.5 Testing Requirements

1. Unit tests should cover all major components and functions of the CV page, including:

   - Rendering of all main sections
   - Search functionality
   - Filtering of CV entries based on search terms
   - Toggling of recent work experiences

2. End-to-end tests should verify:
   - Correct rendering and visibility of all CV sections
   - Functionality of the search feature, including URL updates
   - Proper behavior of the work experience toggle
   - Correct display and interaction with skills, languages, and frameworks
   - Opening of external links in new tabs
   - Scroll to top behavior when navigating with a search term

### 3.3 Personal Projects Page

The Personal Projects Page showcases Wahidyan's individual projects, providing visitors with insights into his personal work and interests outside of his professional career.

#### 3.3.1 Layout and Components

1. The page should have a responsive layout that adapts to different screen sizes.
2. It should include a Navigation component for easy access to other pages.
3. The main content should be centered with a maximum width for optimal readability.

#### 3.3.2 Content Sections

1. Page Title: A prominent "Personal Projects" heading at the top of the page.

2. Search Functionality:

   - A search input field allowing users to filter projects.
   - The search should update results in real-time as the user types.
   - The URL should update with the search term for shareable filtered views.

3. Project List:
   - Each project should be displayed in a separate card or section.
   - Project information should include:
     - Project title
     - Project description
     - Detailed list of project features or accomplishments
     - Links to relevant resources (e.g., repository, website, YouTube channel)

#### 3.3.3 Interactivity and Behavior

1. Search Functionality:

   - As the user types in the search field, projects should be filtered in real-time.
   - The URL should update with the search term (e.g., "/personal-projects?search=AyoKoding").
   - When loading the page with a search parameter, the search field should be pre-filled and projects pre-filtered.

2. Project Links:

   - All project links (repository, website, YouTube, etc.) should open in new tabs when clicked.

3. No Results Handling:
   - If no projects match the search term, a "No projects found matching your search" message should be displayed.

#### 3.3.4 Performance and SEO

1. The page should load quickly, with optimized rendering of project information and images (if any).
2. Use proper semantic HTML structure for better SEO and accessibility.
3. Implement appropriate meta tags for SEO optimization of the projects page.

#### 3.3.5 Testing Requirements

1. Unit tests should cover all major components and functions of the Personal Projects page, including:

   - Rendering of all projects
   - Search functionality
   - Filtering of projects based on search terms
   - Correct display of project details and links

2. End-to-end tests should verify:
   - Correct rendering and visibility of all projects
   - Functionality of the search feature, including URL updates
   - Proper filtering of projects based on search terms
   - Correct display of "No projects found" message when applicable
   - Opening of project links in new tabs
   - Responsive design across different screen sizes

#### 3.3.6 Content Management

1. Project data should be easily updatable, possibly stored in a separate data file or fetched from an API.
2. The structure should allow for easy addition of new projects or modification of existing ones.

#### 3.3.7 Accessibility

1. Ensure all interactive elements are keyboard accessible.
2. Provide appropriate ARIA labels for better screen reader support.
3. Maintain sufficient color contrast for text readability.

This Personal Projects Page will effectively showcase Wahidyan's individual work, allowing visitors to explore his projects in an interactive and user-friendly manner.

### 3.4 Navigation

The Navigation component provides a consistent and user-friendly way for visitors to move between different pages of the Wahidyan KF Web portfolio. It should be present on all pages and adapt to different screen sizes.

#### 3.4.1 Layout and Components

1. Mobile Navigation:

   - Fixed to the bottom of the screen on mobile devices.
   - Displays icons and labels for Home, CV, and Personal Projects.

2. Desktop Navigation:
   - Fixed to the left side of the screen on larger devices.
   - Displays as a sidebar with a folder-like structure.

#### 3.4.2 Content

1. Mobile Navigation Items:

   - Home
   - CV
   - Personal Projects

2. Desktop Navigation Items:
   - WahidyanKF (acts as a home link)
   - home.tsx
   - cv.tsx
   - personal-projects.tsx

#### 3.4.3 Interactivity and Behavior

1. Active Page Indication:

   - The current page should be visually distinct (e.g., different color or highlighting).

2. Linking:

   - Each navigation item should link to its respective page.
   - Clicking on an item should navigate to the corresponding page.

3. Responsiveness:
   - The navigation should automatically switch between mobile and desktop layouts based on screen size.

#### 3.4.4 Styling

1. Mobile Navigation:

   - Use a contrasting background color (e.g., bg-gray-900).
   - Include a top border (e.g., border-t border-green-400).
   - Display items in a row with even spacing.

2. Desktop Navigation:

   - Use a sidebar layout with a width of 80px.
   - Include a right border (e.g., border-r border-green-400).
   - Display items in a column.

3. Icons:

   - Use appropriate icons for each navigation item (e.g., Folder for home, File for other pages).

4. Typography:

   - Use a monospace font for the desktop navigation to enhance the code-like appearance.

5. Theme Compatibility:
   - Ensure navigation styling is compatible with both light and dark themes.

#### 3.4.5 Accessibility

1. Ensure all navigation items are keyboard accessible.
2. Use appropriate ARIA labels for better screen reader support.
3. Maintain sufficient color contrast for text and icon readability.

#### 3.4.6 Performance

1. The navigation component should be lightweight and not impact the overall page load time significantly.

#### 3.4.7 Testing Requirements

1. Unit tests should cover:

   - Correct rendering of navigation items for both mobile and desktop layouts.
   - Proper application of active page styling.

2. End-to-end tests should verify:
   - Correct navigation between pages when items are clicked.
   - Proper responsiveness and layout changes between mobile and desktop views.
   - Accessibility of navigation items via keyboard.

By implementing this navigation system, the Wahidyan KF Web portfolio will provide a consistent and intuitive way for users to explore different sections of the website, enhancing the overall user experience across all devices.

## 4. Non-Functional Requirements

### 4.1 Performance

1. Page Load Time:

   - Initial page load should be under 2 seconds on average network conditions.
   - Subsequent page navigations should be near-instantaneous due to client-side routing.

2. Optimization:

   - Implement code splitting and lazy loading for optimal performance.
   - Minimize bundle size by efficiently importing only necessary components and libraries.

3. Responsiveness:
   - The application should remain responsive during search operations and content filtering.

### 4.2 Scalability

1. Content Management:

   - The CV data structure should allow for easy addition of new entries and categories.
   - The personal projects section should be easily expandable with new projects.

2. Code Structure:
   - Maintain a modular code structure to facilitate future feature additions and modifications.

### 4.3 Maintainability

1. Code Quality:

   - Adhere to TypeScript best practices for type safety and code clarity.
   - Implement comprehensive unit tests for all components and utility functions.
   - Maintain consistent code style using ESLint and Prettier.

2. Documentation:
   - Provide clear inline comments for complex logic.
   - Maintain up-to-date documentation for component props and utility functions.

### 4.4 Accessibility

1. WCAG Compliance:

   - Aim for WCAG 2.1 Level AA compliance across all pages.
   - Ensure proper heading structure and ARIA labels for screen readers.

2. Keyboard Navigation:

   - All interactive elements should be accessible via keyboard navigation.

3. Color Contrast:
   - Maintain sufficient color contrast ratios for text readability in both light and dark themes.

### 4.5 SEO

1. Metadata:

   - Implement proper meta tags for title, description, and Open Graph data on all pages.
   - Use semantic HTML structure to improve search engine understanding of content.

2. Performance:
   - Optimize Core Web Vitals metrics to improve search engine rankings.

### 4.6 Cross-Browser Compatibility

1. Support latest versions of major browsers:

   - Chrome, Firefox, Safari, Edge

2. Graceful Degradation:
   - Ensure core functionality works on older browser versions, even if some visual enhancements are not supported.

### 4.7 Responsive Design

1. Device Support:
   - Ensure optimal viewing experience across a wide range of devices (mobile phones, tablets, desktops).
   - Implement fluid layouts that adapt to different screen sizes and orientations.

### 4.8 Security

1. Data Protection:

   - Implement appropriate measures to protect any sensitive information (e.g., contact details).
   - Use HTTPS for all communications.

2. Third-Party Libraries:
   - Regularly update dependencies to patch any security vulnerabilities.

### 4.9 Analytics and Monitoring

1. User Tracking:

   - Implement Google Analytics for tracking user interactions and page views.
   - Use Google Tag Manager for easy management of tracking scripts.

2. Error Monitoring:
   - Implement error logging and monitoring to catch and address issues promptly.

### 4.10 Internationalization

1. Language Support:
   - While the current implementation is in English, design the application structure to easily accommodate multiple languages in the future if needed.

### 4.11 Performance Testing

1. Load Testing:

   - Conduct performance tests to ensure the application can handle expected traffic levels.

2. Continuous Monitoring:
   - Implement tools to continuously monitor and report on application performance metrics.

By adhering to these non-functional requirements, the Wahidyan KF Web portfolio will ensure a high-quality, performant, and user-friendly experience while maintaining good development practices and future scalability.

## 5. Theme & Styling

The Wahidyan KF Web portfolio implements a dual-theme system with a dark theme as default and a light theme option. The styling is consistent across all pages, utilizing Tailwind CSS for a utility-first approach.

### 5.1 Color Scheme

1. Dark Theme (Default):

   - Background: Black (#000000)
   - Primary Text: White (#ffffff)
   - Headings and Highlights: Yellow (#facc15)
   - Links: Yellow (#facc15)

2. Light Theme:

   - Background: White (#ffffff)
   - Primary Text: Dark gray (#1e1e1e)
   - Headings: Brown (#795e26)
   - Links: Purple (#af00db)

3. Interactive Elements:
   - Consistent styling for hover effects in both themes

### 5.2 Typography

1. Font Family:

   - Body: Inter (sans-serif)
   - Code and Navigation: Monospace (for code-like appearance)

2. Font Sizes:

   - Page Titles: text-2xl sm:text-3xl md:text-4xl
   - Section Headings: text-xl sm:text-2xl md:text-3xl
   - Body Text: Base size with responsive scaling (18px on larger screens)

3. Font Weights:
   - Headings: font-bold
   - Body: Normal weight
   - Links and interactive elements: font-semibold

### 5.3 Layout and Spacing

1. Responsive Design:

   - Mobile: Single column layout
   - Desktop: Multi-column layout (lg:flex-row)

2. Consistent Spacing:

   - Page Padding: p-4 sm:p-8 md:p-12 lg:p-16
   - Vertical Spacing: mb-8 between major sections

3. Content Width:
   - Max width for readability: max-w-4xl mx-auto

### 5.4 Components and Elements

1. Cards and Sections:

   - Border: border border-green-400 (dark theme), border-light-primary (light theme)
   - Rounded Corners: rounded-lg
   - Internal Padding: p-4

2. Buttons and Interactive Elements:

   - Clear hover effects with color transitions
   - Consistent styling for similar interactions (e.g., skill buttons)

3. Form Elements:
   - Styled to match the overall theme
   - Clear focus states for accessibility

### 5.5 Icons

1. Icon Libraries: Lucide React and react-icons
2. Consistent sizing and alignment with text

### 5.6 Animations and Transitions

1. Smooth color transitions for hover effects (transition-colors duration-200)
2. Subtle animations for enhanced user experience

### 5.7 Theme Toggle

1. Easily accessible theme toggle button
2. Smooth transition between light and dark themes
3. Theme preference persists across page navigation
4. Default theme is dark

### 5.8 Accessibility Considerations

1. WCAG 2.1 AA compliant color contrast ratios
2. Appropriate focus indicators for interactive elements
3. Semantic HTML structure

### 5.9 Consistency and Theming System

1. Use of CSS variables for theme colors (defined in :root and .light-theme)
2. Tailwind CSS extended theme configuration for custom colors and styles
3. Consistent use of utility classes across components

### 5.10 Code Syntax Highlighting

[Remove this section as it's not implemented in the current version]

### 5.11 Implementation Details

1. Tailwind CSS configuration extends the default theme with custom colors and styles
2. Global CSS file (globals.css) defines base styles and theme-specific overrides
3. Use of the `light-theme` class to toggle between dark and light modes
4. Theme toggle implemented using client-side JavaScript

### 5.12 Responsiveness

1. Breakpoints:

   - Large (lg): 1024px

2. Layout Adjustments:

   - Mobile (< 1024px):
     - Full-width components
     - Bottom-fixed navigation menu
   - Desktop (≥ 1024px):
     - Sidebar navigation

3. Navigation:

   - Mobile: Bottom-fixed, icon-based navigation
   - Desktop: Left sidebar with expanded labels

4. Typography:

   - Fluid typography using responsive font sizes:
     - Page Titles: text-2xl sm:text-3xl md:text-4xl
     - Section Headings: text-xl sm:text-2xl md:text-3xl
   - Adjusted line heights and letter spacing for readability on different screen sizes

5. Images and Media:

   - Use of responsive image techniques (e.g., srcset, sizes attributes)
   - Fluid video embeds that maintain aspect ratio

6. Interactive Elements:

   - Touch-friendly tap targets on mobile (minimum size of 44x44 pixels)
   - Hover effects on desktop, touch effects on mobile

7. Content Adjustments:

   - Collapsible sections or tabs for dense content on mobile
   - Expanded view of all content on larger screens

8. Performance Considerations:

   - Lazy loading of images and non-critical content
   - Optimized asset delivery based on device capabilities

9. Testing:
   - Regular testing on various devices and browsers to ensure consistent experience
   - Use of browser developer tools to simulate different device sizes and resolutions

By implementing these responsive design principles, the Wahidyan KF Web portfolio ensures a seamless and engaging user experience across all devices, from mobile phones to large desktop monitors.

## 6. Project Structure

```
wahidyan-kf-web
├── README.md
├── components.json
├── e2e-tests
│   ├── components
│   │   └── theme.spec.ts
│   └── pages
│       ├── cv.spec.ts
│       ├── home.spec.ts
│       └── personal-projects.spec.ts
├─ next-env.d.ts
├── next.config.mjs
├── package-lock.json
├── package.json
├── playwright.config.ts
├── postcss.config.mjs
├── prd.md
├── src
│   ├── app
│   │   ├── cv
│   │   │   ├── page.test.tsx
│   │   │   └── page.tsx
│   │   ├── data.test.ts
│   │   ├── data.ts
│   │   ├── favicon.ico
│   │   ├── fonts
│   │   │   ├── GeistMonoVF.woff
│   │   │   └── GeistVF.woff
│   │   ├── globals.css
│   │   ├── head.tsx
│   │   ├── layout.test.tsx
│   │   ├── layout.tsx
│   │   ├── page.test.tsx
│   │   ├── page.tsx
│   │   └── personal-projects
│   │       ├── page.test.tsx
│   │       └── page.tsx
│   ├── components
│   │   ├── HighlightText.test.tsx
│   │   ├── HighlightText.tsx
│   │   ├── Navigation.test.tsx
│   │   ├── Navigation.tsx
│   │   ├── ScrollToTop.test.tsx
│   │   ├── ScrollToTop.tsx
│   │   ├── SearchComponent.test.tsx
│   │   ├── SearchComponent.tsx
│   │   └── ThemeToggle.tsx
│   ├── test
│   │   └── setup.ts
│   └── utils
│       ├── markdown.test.tsx
│       ├── markdown.tsx
│       ├── search.test.ts
│       ├── search.ts
│       ├── style.test.ts
│       └── style.ts
├── tailwind.config.ts
├── tsconfig.json
├── vite.config.ts
└── vitest.config.ts
```
