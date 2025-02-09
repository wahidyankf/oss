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
