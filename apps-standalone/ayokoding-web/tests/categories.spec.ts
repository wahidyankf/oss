import { test, expect } from '@playwright/test';

test('categories page loads and has content', async ({ page }) => {
  // Navigate to the categories page
  await page.goto('/c');

  // Check page title or heading
  const headingLocator = page.getByRole('heading', { name: 'All Contents' });
  await expect(headingLocator).toBeVisible();

  // Check for categories navigation
  const categoryLinks = page.getByRole('link');
  await expect(categoryLinks.first()).toBeVisible();
});
