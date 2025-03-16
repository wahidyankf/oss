import { test, expect, Page, BrowserContext } from '@playwright/test';

test.describe('Personal Projects Page', () => {
  let page: Page;

  test.beforeEach(async ({ page: p }) => {
    page = p;
    await page.goto('/personal-projects');
  });

  const checkSectionVisibility = async (headingText: string) => {
    await expect(
      page.getByRole('heading', { name: headingText }),
    ).toBeVisible();
  };

  const checkComponentVisibility = async (
    selector: string,
    placeholder?: string,
  ) => {
    if (placeholder) {
      await expect(page.getByPlaceholder(placeholder)).toBeVisible();
    } else {
      await expect(page.locator(selector)).toBeVisible();
    }
  };

  test('should render main sections', async () => {
    await checkSectionVisibility('Personal Projects');
    await checkComponentVisibility('', 'Search projects...');

    // Check for mobile navigation (visible on smaller screens)
    await page.setViewportSize({ width: 375, height: 667 });
    await expect(page.locator('nav.lg\\:hidden')).toBeVisible();

    // Check for desktop navigation (visible on larger screens)
    await page.setViewportSize({ width: 1280, height: 720 });
    await expect(page.locator('nav.hidden.lg\\:block')).toBeVisible();

    // Reset viewport to default size
    await page.setViewportSize({ width: 1280, height: 720 });
  });

  const checkProjectVisibility = async (
    projectName: string,
    isVisible: boolean,
  ) => {
    if (isVisible) {
      await expect(page.getByText(projectName)).toBeVisible();
    } else {
      await expect(page.getByText(projectName)).not.toBeVisible();
    }
  };

  test('should render all projects initially', async () => {
    const projects = ['AyoKoding', 'Organic Lever', 'The Organic'];
    for (const project of projects) {
      await checkProjectVisibility(project, true);
    }
  });

  const searchProjects = async (searchTerm: string) => {
    const searchInput = page.getByPlaceholder('Search projects...');
    await searchInput.fill(searchTerm);
    await searchInput.press('Enter');
  };

  test('should filter projects based on search term', async () => {
    await searchProjects('AyoKoding');
    await checkProjectVisibility('AyoKoding', true);
    await checkProjectVisibility('Organic Lever', false);
    await checkProjectVisibility('The Organic', false);
  });

  test("should display 'No projects found' message when no matches", async () => {
    await searchProjects('NonexistentProject');
    await expect(
      page.getByText('No projects found matching your search.'),
    ).toBeVisible();
  });

  test('should update URL when searching', async () => {
    await searchProjects('AyoKoding');
    await expect(page).toHaveURL('/personal-projects?search=AyoKoding');
  });

  const checkLinkAttribute = async (linkName: string, expectedUrl: string) => {
    const link = page
      .getByRole('link', { name: new RegExp(linkName, 'i') })
      .first();
    await expect(link).toHaveAttribute('href', expectedUrl);
  };

  test('should render project links correctly', async () => {
    await checkLinkAttribute(
      'Repository',
      'https://github.com/organiclever/ayokoding',
    );
    await checkLinkAttribute('Website', 'https://ayokoding.com/');
    await checkLinkAttribute('YouTube', 'https://www.youtube.com/@AyoKoding');
  });

  const checkExternalLink = async (
    linkName: string,
    expectedUrl: string,
    context: BrowserContext,
  ) => {
    const linkElement = page
      .getByRole('link', { name: new RegExp(linkName, 'i') })
      .first();
    const href = await linkElement.getAttribute('href');

    if (href) {
      const [newPage] = await Promise.all([
        context.waitForEvent('page'),
        page.evaluate((selector) => {
          const element = document.querySelector(selector) as HTMLAnchorElement;
          if (element) {
            element.click();
          }
        }, `a[href="${href}"]`),
      ]);

      await newPage.waitForLoadState('domcontentloaded');
      expect(newPage.url()).toBe(expectedUrl);
      await newPage.close();
    } else {
      throw new Error(
        `Link with name "${linkName}" not found or has no href attribute`,
      );
    }
  };

  test('should open external links in new tabs', async ({ context }) => {
    const links = [
      { name: 'Repository', url: 'https://github.com/organiclever/ayokoding' },
      { name: 'Website', url: 'https://ayokoding.com/' },
      { name: 'YouTube', url: 'https://www.youtube.com/@AyoKoding' },
    ];

    for (const link of links) {
      await checkExternalLink(link.name, link.url, context);
    }
  });

  test('should render project details correctly', async () => {
    const projectDetails = [
      'A website to learn about software engineering through books, blogs, and YouTube videos.',
      'Comprehensive learning resources for software engineering',
      'Public learning platform to share knowledge',
      'Includes a YouTube channel for video content',
    ];

    for (const detail of projectDetails) {
      await expect(page.getByText(detail)).toBeVisible();
    }
  });
});
