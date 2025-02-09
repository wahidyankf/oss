import { test, expect } from '@playwright/test';

test('404 page has correct content', async ({ page }) => {
  // Navigate to a non-existent page
  await page.goto('/non-existent-page');

  // Check page not found text
  const notFoundHeading = page.getByRole('heading', { name: 'Page Not Found' });
  await expect(notFoundHeading).toBeVisible();

  // Check navigation links
  const homeLink = page.getByRole('link', { name: 'Home' });
  await expect(homeLink).toBeVisible();

  const categoriesLink = page.getByRole('link', { name: 'Categories' });
  await expect(categoriesLink).toBeVisible();
});
