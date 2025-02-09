import { test, expect } from '@playwright/test';

test('categories page loads and has content', async ({ page }) => {
  await page.goto('/c');

  // Check page title or heading
  await expect(page.getByText(/Contents/i)).toBeVisible();

  // Check for categories navigation
  const categoryLinks = page.getByRole('link');
  await expect(categoryLinks.first()).toBeVisible();
});
