import { test, expect, Page } from '@playwright/test';

test.describe('Theme and Responsiveness', () => {
  let page: Page;

  test.beforeEach(async ({ page: p }) => {
    page = p;
    await page.goto('/');
  });

  const toggleTheme = async () => {
    const themeToggle = page.getByRole('button', { name: /theme/i });
    if (await themeToggle.isVisible()) {
      const currentTheme = await page.evaluate(
        () => window.getComputedStyle(document.body).backgroundColor,
      );
      await themeToggle.click();
      await page.waitForFunction(
        (oldTheme) =>
          window.getComputedStyle(document.body).backgroundColor !== oldTheme,
        currentTheme,
      );
      return true;
    }
    return false;
  };

  const checkTheme = async (isLight: boolean) => {
    const expectedColor = isLight ? 'rgb(255, 255, 255)' : 'rgb(0, 0, 0)';
    await expect(page.locator('body')).toHaveCSS(
      'background-color',
      expectedColor,
    );
  };

  test('should toggle between light and dark themes', async () => {
    const initialTheme = await page.evaluate(
      () => window.getComputedStyle(document.body).backgroundColor,
    );
    const isInitiallyLight = initialTheme === 'rgb(255, 255, 255)';

    await checkTheme(isInitiallyLight);
    if (await toggleTheme()) {
      await checkTheme(!isInitiallyLight);
      await toggleTheme();
      await checkTheme(isInitiallyLight);
    } else {
      test.skip();
    }
  });

  test('should persist theme preference across page navigation', async () => {
    if (await toggleTheme()) {
      await checkTheme(true);
      await page.goto('/cv');
      await checkTheme(true);
    } else {
      test.skip();
    }
  });

  const checkResponsiveness = async (
    width: number,
    height: number,
    isDesktop: boolean,
  ) => {
    await page.setViewportSize({ width, height });
    const desktopNav = page.locator('nav.hidden.lg\\:block');
    const mobileNav = page.locator('nav.lg\\:hidden');

    if (isDesktop) {
      await expect(desktopNav).toBeVisible();
      await expect(mobileNav).not.toBeVisible();
    } else {
      await expect(desktopNav).toHaveClass(/hidden/);
      await expect(mobileNav).toBeVisible();
    }
  };

  test('should be responsive on mobile devices', async () => {
    await checkResponsiveness(375, 667, false);
  });

  test('should be responsive on tablet devices', async () => {
    await checkResponsiveness(768, 1024, false);
  });

  test('should be responsive on desktop devices', async () => {
    await checkResponsiveness(1280, 800, true);
  });

  const checkLayoutForSize = async (width: number, height: number) => {
    await page.setViewportSize({ width, height });
    const mainContent = page.locator('main');
    const boundingBox = await mainContent.boundingBox();
    expect(boundingBox?.width).toBeLessThanOrEqual(width);

    const images = page.locator('img');
    for (let i = 0; i < (await images.count()); i++) {
      const imageBoundingBox = await images.nth(i).boundingBox();
      expect(imageBoundingBox?.width).toBeLessThanOrEqual(width);
    }
  };

  test('should adjust layout for different screen sizes', async () => {
    await checkLayoutForSize(375, 667);
    await checkLayoutForSize(768, 1024);
    await checkLayoutForSize(1280, 800);
  });

  const checkReadability = async (width: number, height: number) => {
    await page.setViewportSize({ width, height });
    await toggleTheme();

    const textElements = page.locator('h1, h2, h3, p');
    for (let i = 0; i < (await textElements.count()); i++) {
      const element = textElements.nth(i);
      const color = await element.evaluate(
        (el) => window.getComputedStyle(el).color,
      );
      const backgroundColor = await element.evaluate(
        (el) => window.getComputedStyle(el).backgroundColor,
      );
      expect(color).not.toBe(backgroundColor);
    }

    await toggleTheme();
  };

  test('should have readable text on all themes and screen sizes', async () => {
    await checkReadability(375, 667);
    await checkReadability(768, 1024);
    await checkReadability(1280, 800);
  });

  const checkColors = async (isDarkTheme: boolean) => {
    const expectedColors = {
      background: isDarkTheme ? 'rgb(0, 0, 0)' : 'rgb(255, 255, 255)',
      text: isDarkTheme ? 'rgb(255, 255, 255)' : 'rgb(30, 30, 30)',
      heading: isDarkTheme ? 'rgb(250, 204, 21)' : 'rgb(121, 94, 38)',
      link: isDarkTheme ? 'rgb(250, 204, 21)' : 'rgb(175, 0, 219)',
    };

    const bodyBgColor = await page.evaluate(
      () => window.getComputedStyle(document.body).backgroundColor,
    );
    const textColor = await page.evaluate(
      () => window.getComputedStyle(document.body).color,
    );
    const headingColor = await page
      .locator('h1')
      .first()
      .evaluate((el) => window.getComputedStyle(el).color);
    const linkColor = await page
      .locator('a')
      .first()
      .evaluate((el) => window.getComputedStyle(el).color);

    expect(bodyBgColor).toBe(expectedColors.background);
    expect(textColor).toBe(expectedColors.text);
    expect(headingColor).toBe(expectedColors.heading);
    expect(linkColor).toBe(expectedColors.link);
  };

  test('should have correct color palette for both themes', async () => {
    await checkColors(true);
    await toggleTheme();
    await checkColors(false);
    await toggleTheme();
    await checkColors(true);
  });
});
