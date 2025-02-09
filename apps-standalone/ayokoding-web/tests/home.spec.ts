import { test, expect } from '@playwright/test';

test('homepage has title and navigation', async ({ page }) => {
  await page.goto('/');

  // Check page title
  await expect(page).toHaveTitle('AyoKoding');

  // Check navigation elements
  const navLinks = page.getByRole('link');
  await expect(navLinks.filter({ hasText: 'Home' })).toBeVisible();
  await expect(navLinks.filter({ hasText: 'Categories' })).toBeVisible();
});

test('homepage displays content tree', async ({ page }) => {
  await page.goto('/');

  // Check content tree section by finding the top-level list containing category links
  const contentTreeSection = page.locator('main').getByRole('list').first();
  await expect(contentTreeSection).toBeVisible();

  // Check for expected top-level categories
  const expectedCategories = ['blog', 'tech', 'travel'];
  for (const category of expectedCategories) {
    const categoryLink = contentTreeSection.getByRole('link', {
      name: `${category}/`,
    });
    await expect(categoryLink).toBeVisible();
  }
});

test('homepage displays recent contents', async ({ page }) => {
  await page.goto('/');

  // Check recent contents section
  const recentContentsHeading = page.getByRole('heading', {
    name: 'Recent Contents',
  });
  await expect(recentContentsHeading).toBeVisible();

  // Check that there are recent content articles
  const recentContentArticles = page.locator('article');
  await expect(recentContentArticles.first()).toBeVisible();

  // Check that each article has a title, publication date, and read more link
  const firstArticle = recentContentArticles.first();
  await expect(firstArticle.getByRole('heading')).toBeVisible();
  await expect(firstArticle.getByText(/Published on:/)).toBeVisible();
  await expect(firstArticle.getByText('Read More')).toBeVisible();
});

test('homepage displays recent contents details', async ({ page }) => {
  await page.goto('/');

  // Check recent contents section
  const recentContentsHeading = page.getByRole('heading', {
    name: 'Recent Contents',
  });
  await expect(recentContentsHeading).toBeVisible();

  // Check that there are recent content articles
  const recentContentArticles = page.locator('article');
  const articleCount = await recentContentArticles.count();

  // Verify at least one article is displayed (up to 5 as per getRecentContents)
  expect(articleCount).toBeGreaterThan(0);
  expect(articleCount).toBeLessThanOrEqual(5);

  // Detailed checks for each article
  for (let i = 0; i < articleCount; i++) {
    const article = recentContentArticles.nth(i);

    // Check article title
    const titleLink = article
      .getByRole('heading', { level: 3 })
      .getByRole('link');
    await expect(titleLink).toBeVisible();
    const title = await titleLink.textContent();
    expect(title).toBeTruthy();

    // Check publication date
    const dateElement = article.getByText(/Published on:/);
    await expect(dateElement).toBeVisible();
    const dateText = await dateElement.textContent();
    expect(dateText).toMatch(/Published on: [A-Za-z]+ \d{1,2}, \d{4}/);

    // Check "Read More" link
    const readMoreLink = article.getByText('Read More');
    await expect(readMoreLink).toBeVisible();

    // Verify links are correct
    const postLink = await titleLink.getAttribute('href');
    const readMoreLink2 = await readMoreLink.getAttribute('href');

    expect(postLink).toMatch(/^\/posts\/.+/);
    expect(readMoreLink2).toMatch(/^\/c\/.+/);
  }
});
