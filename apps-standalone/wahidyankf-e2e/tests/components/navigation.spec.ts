import { test, expect } from '@playwright/test';

const routes = [
  { name: 'Home', path: '/' },
  { name: 'CV', path: '/cv' },
  { name: 'Personal Projects', path: '/personal-projects' },
];

test.describe('Navigation Component', () => {
  test.describe('Desktop Navigation (Sidebar)', () => {
    test.beforeEach(async ({ page }) => {
      await page.setViewportSize({ width: 1280, height: 720 });
    });

    test('should display desktop navigation on large screens', async ({
      page,
    }) => {
      await page.goto('/');
      const desktopNav = page.locator('nav.hidden.lg\\:block');
      await expect(desktopNav).toBeVisible();
      const linkCount = await desktopNav.locator('li').count();
      expect(linkCount).toBe(routes.length);
    });

    test('should highlight active page and not highlight inactive pages', async ({
      page,
    }) => {
      for (const route of routes) {
        await page.goto(route.path);
        await page.waitForLoadState('networkidle');

        // Check if the current route is highlighted
        const activeLink = page
          .locator(`nav.hidden.lg\\:block a[href="${route.path}"]`)
          .filter({ hasText: route.name });
        await expect(activeLink).toHaveClass(/active-nav-item/);

        // Check if other links are not highlighted
        for (const otherRoute of routes.filter((r) => r.path !== route.path)) {
          const otherLink = page
            .locator(`nav.hidden.lg\\:block a[href="${otherRoute.path}"]`)
            .filter({ hasText: otherRoute.name });
          await expect(otherLink).not.toHaveClass(/active-nav-item/);
        }
      }
    });

    test('desktop navigation should be fixed and main content should be present', async ({
      page,
    }) => {
      await page.goto('/');
      const desktopNav = page.locator('nav.hidden.lg\\:block');
      const mainContent = page.locator('main');

      await expect(desktopNav).toBeVisible();
      await expect(mainContent).toBeVisible();

      const navBoundingBox = await desktopNav.boundingBox();
      const contentBoundingBox = await mainContent.boundingBox();

      expect(navBoundingBox?.width).toBeGreaterThan(0);
      expect(contentBoundingBox?.width).toBeGreaterThan(0);

      const navRightEdge =
        (navBoundingBox?.x || 0) + (navBoundingBox?.width || 0);
      const contentRightEdge =
        (contentBoundingBox?.x || 0) + (contentBoundingBox?.width || 0);

      expect(contentRightEdge).toBeGreaterThan(navRightEdge);
    });
  });

  test.describe('Mobile Navigation (Bottom)', () => {
    test.beforeEach(async ({ page }) => {
      await page.setViewportSize({ width: 375, height: 667 });
    });

    test('should display mobile navigation on small screens', async ({
      page,
    }) => {
      await page.goto('/');
      const mobileNav = page.locator('nav.lg\\:hidden');
      await expect(mobileNav).toBeVisible();
      const linkCount = await mobileNav.locator('a').count();
      expect(linkCount).toBe(routes.length);
    });

    test('should highlight active page and not highlight inactive pages', async ({
      page,
    }) => {
      for (const route of routes) {
        await page.goto(route.path);
        await page.waitForLoadState('networkidle');

        // Check if the current route is highlighted
        const activeLink = page
          .locator(`nav.lg\\:hidden a[href="${route.path}"]`)
          .filter({ hasText: route.name });
        await expect(activeLink).toHaveClass(/text-yellow-400/);

        // Check if other links are not highlighted
        for (const otherRoute of routes.filter((r) => r.path !== route.path)) {
          const otherLink = page
            .locator(`nav.lg\\:hidden a[href="${otherRoute.path}"]`)
            .filter({ hasText: otherRoute.name });
          await expect(otherLink).toHaveClass(/text-green-400/);
        }
      }
    });
  });

  test.describe('Navigation Accessibility', () => {
    test('navigation should be accessible on desktop', async ({ page }) => {
      await page.setViewportSize({ width: 1280, height: 720 });
      await page.goto('/');

      const nav = page.locator('nav.hidden.lg\\:block');
      await expect(nav).toBeVisible();

      const links = nav.locator('a');
      const count = await links.count();

      expect(count).toBeGreaterThanOrEqual(routes.length);

      for (let i = 0; i < count; i++) {
        const link = links.nth(i);
        const linkText = await link.innerText();
        expect(linkText.trim()).not.toBe('');
      }
    });

    test('navigation should be accessible on mobile', async ({ page }) => {
      await page.setViewportSize({ width: 375, height: 667 });
      await page.goto('/');

      const nav = page.locator('nav.lg\\:hidden');
      await expect(nav).toBeVisible();

      const links = nav.locator('a');
      const count = await links.count();

      expect(count).toBeGreaterThanOrEqual(routes.length);

      for (let i = 0; i < count; i++) {
        const link = links.nth(i);
        const linkText = await link.innerText();
        expect(linkText.trim()).not.toBe('');
      }
    });
  });
});
