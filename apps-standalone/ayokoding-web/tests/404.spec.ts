import { test, expect } from '@playwright/test';

test('404 page has correct content', async ({ page }) => {
  await page.goto('/non-existent-page');

  // Check 404 text
  await expect(page.getByText('404')).toBeVisible();
  await expect(page.getByText('Page Not Found')).toBeVisible();

  // Check navigation links
  const navLinks = page.getByRole('link');
  await expect(navLinks.filter({ hasText: 'Go to Home' })).toBeVisible();
  await expect(navLinks.filter({ hasText: 'View Categories' })).toBeVisible();
});
