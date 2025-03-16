import { test, expect, Page } from '@playwright/test';

test.describe('Home Page', () => {
  let page: Page;

  test.beforeEach(async ({ page: p }) => {
    page = p;
    await page.goto('/');
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
    const sections = [
      'Welcome to My Portfolio',
      'About Me',
      'Skills & Expertise',
      'Quick Links',
      'Connect With Me',
    ];
    for (const section of sections) {
      await checkSectionVisibility(section);
    }
  });

  test('should render Navigation components', async () => {
    // Check for mobile navigation (visible on smaller screens)
    await page.setViewportSize({ width: 375, height: 667 });
    await expect(page.locator('nav.lg\\:hidden')).toBeVisible();

    // Check for desktop navigation (visible on larger screens)
    await page.setViewportSize({ width: 1280, height: 720 });
    await expect(page.locator('nav.hidden.lg\\:block')).toBeVisible();

    // Reset viewport to default size
    await page.setViewportSize({ width: 1280, height: 720 });
  });

  test('should render SearchComponent', async () => {
    await checkComponentVisibility(
      '',
      'Search skills, languages, or frameworks...',
    );
  });

  test('should render about me section', async () => {
    await expect(
      page.locator('section', { hasText: 'About Me' }),
    ).toBeVisible();
  });

  const checkSkillButtonVisibility = async (skillName: string) => {
    await expect(
      page.getByRole('button', { name: new RegExp(skillName, 'i') }),
    ).toBeVisible();
  };

  test('should render skills, languages, and frameworks', async () => {
    const skills = [
      'Software Engineering',
      'JavaScript',
      'React.js',
      'React Native',
      'ReasonReact',
    ];
    for (const skill of skills) {
      await checkSkillButtonVisibility(skill);
    }
  });

  test('should render quick links', async () => {
    await expect(page.getByRole('link', { name: 'View My CV' })).toBeVisible();
    await expect(
      page.getByRole('link', { name: 'Browse My Personal Projects' }),
    ).toBeVisible();
  });

  test('should render connect with me links', async () => {
    const links = [
      { name: 'Github', exact: true },
      { name: 'GithubOrg', exact: true },
      { name: 'Linkedin', exact: true },
      { name: 'Email', exact: true },
    ];

    for (const link of links) {
      await expect(
        page.getByRole('link', { name: link.name, exact: link.exact }),
      ).toBeVisible();
    }
  });

  test('should update URL when searching', async () => {
    const searchInput = page.getByPlaceholder(
      'Search skills, languages, or frameworks...',
    );
    await searchInput.fill('React');
    await searchInput.press('Enter');
    await expect(page).toHaveURL('/?search=React');
  });

  test('should filter content based on search term', async () => {
    const searchInput = page.getByPlaceholder(
      'Search skills, languages, or frameworks...',
    );
    await searchInput.fill('React');
    await searchInput.press('Enter');

    await expect(page.getByRole('button', { name: 'React.js' })).toBeVisible();
    await expect(
      page.getByRole('button', { name: 'Software Engineering' }),
    ).not.toBeVisible();
  });

  const clickButtonByText = async (buttonText: string) => {
    await page.evaluate((text) => {
      const buttons = Array.from(document.querySelectorAll('button'));
      const button = buttons.find((b) => b.textContent?.includes(text));
      if (button) {
        (button as HTMLElement).click();
      } else {
        throw new Error(`${text} button not found`);
      }
    }, buttonText);
  };

  test('should navigate to CV page when clicking on a skill', async () => {
    await page.waitForSelector('button', { state: 'visible' });
    await clickButtonByText('React.js');
    await page.waitForURL('/cv?search=React.js&scrollTop=true');
    await expect(page).toHaveURL('/cv?search=React.js&scrollTop=true');
  });

  const navigateByLinkText = async (linkText: string, expectedUrl: string) => {
    await page.evaluate((text) => {
      const link = Array.from(document.querySelectorAll('a')).find(
        (a) => a.textContent === text,
      ) as HTMLAnchorElement;
      if (link) {
        link.click();
      } else {
        throw new Error(`${text} link not found`);
      }
    }, linkText);
    await page.waitForURL(expectedUrl);
    await expect(page).toHaveURL(expectedUrl);
  };

  test('should navigate to correct pages from quick links', async () => {
    await navigateByLinkText('View My CV', '/cv');
    await page.goto('/');
    await navigateByLinkText(
      'Browse My Personal Projects',
      '/personal-projects',
    );
  });

  test('should open external links in new tabs', async ({ context }) => {
    await page.waitForSelector('a[target="_blank"]');
    const externalLinks = await page.$$('a[target="_blank"]');

    for (const link of externalLinks) {
      const href = await link.getAttribute('href');
      const linkText = await link.textContent();

      if (href) {
        const [newPage] = await Promise.all([
          context.waitForEvent('page'),
          page.evaluate((linkHref) => {
            const linkElement = document.querySelector(`a[href="${linkHref}"]`);
            if (linkElement) {
              (linkElement as HTMLAnchorElement).click();
            }
          }, href),
        ]);

        await newPage.waitForLoadState('domcontentloaded');
        console.log(`Checking link: ${linkText} (${href})`);

        if (linkText?.includes('Github')) {
          expect(newPage.url()).toContain('github.com');
        } else if (linkText?.includes('Linkedin')) {
          expect(newPage.url()).toContain('linkedin.com');
        } else if (linkText?.includes('Email')) {
          expect(newPage.url()).toContain('wahidyankf@gmail.com');
        }

        await newPage.close();
      }
    }
  });
});
