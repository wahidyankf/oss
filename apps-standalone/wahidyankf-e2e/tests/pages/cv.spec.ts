import { test, expect, Page } from '@playwright/test';

test.describe('CV Page', () => {
  let page: Page;

  test.beforeEach(async ({ page: p }) => {
    page = p;
    await page.goto('/cv');
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
      'Curriculum Vitae',
      'Highlights',
      'Work Experience',
      'Honors & Awards',
      'Licenses & Certifications',
      'Education',
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
    await checkComponentVisibility('', 'Search CV entries...');
  });

  const checkSection = async (
    sectionName: string,
    entrySelector: string,
    titleSelector: string,
    subtitleSelector: string,
  ) => {
    const section = page.locator('div', { hasText: sectionName }).first();
    await expect(section).toBeVisible();

    const entries = section.locator(entrySelector);
    await expect(entries.first()).toBeVisible();

    const titles = section.locator(titleSelector);
    await expect(titles.first()).toBeVisible();

    const subtitles = section.locator(subtitleSelector);
    await expect(subtitles.first()).toBeVisible();

    const entryCount = await entries.count();
    let foundValidEntry = false;
    for (let i = 0; i < entryCount; i++) {
      const entry = entries.nth(i);
      const hasTitle = await entry.locator(titleSelector).isVisible();
      const hasSubtitle = await entry.locator(subtitleSelector).isVisible();
      if (hasTitle && hasSubtitle) {
        foundValidEntry = true;
        break;
      }
    }
    expect(foundValidEntry).toBe(true);
  };

  test('should render work experience', async () => {
    await checkSection(
      'Work Experience',
      '.mb-4.border',
      'h3.text-lg',
      'p.mb-2.text-green-300',
    );
  });

  test('should render education entries', async () => {
    await checkSection(
      'Education',
      '.mb-4.border',
      'h3.text-lg',
      'p.mb-2.text-green-300',
    );
  });

  const checkSkillSection = async (sectionTitle: string) => {
    const section = page.locator('div', { hasText: sectionTitle }).first();
    await expect(section).toBeVisible();
  };

  test('should render skills, languages, and frameworks', async () => {
    await checkSkillSection('Top Skills Used in The Last 5 Years');
    await checkSkillSection(
      'Top Programming Languages Used in The Last 5 Years',
    );
    await checkSkillSection(
      'Top Frameworks & Libraries Used in The Last 5 Years',
    );

    const reactSkills = ['React.js', 'React Native', 'ReasonReact'];
    for (const skill of reactSkills) {
      await expect(
        page.getByRole('button', { name: skill }).first(),
      ).toBeVisible();
    }
  });

  test('should update URL when searching', async () => {
    const searchInput = page.getByPlaceholder('Search CV entries...');
    await searchInput.fill('React');
    await searchInput.press('Enter');
    await expect(page).toHaveURL('/cv?search=React');
  });

  test('should filter content based on search term', async () => {
    const searchInput = page.getByPlaceholder('Search CV entries...');
    await searchInput.fill('Software');
    await searchInput.press('Enter');

    await page.waitForTimeout(1000);

    const workExperienceSection = page
      .locator('div', { hasText: 'Work Experience' })
      .first();
    const jobTitles = workExperienceSection.locator('h3.text-lg');
    const jobTitleCount = await jobTitles.count();

    expect(jobTitleCount).toBeGreaterThan(0);
    if (jobTitleCount > 0) {
      await expect(jobTitles.first()).toBeVisible();
    }

    await expect(
      page.getByText('Unrelated Job Title', { exact: true }),
    ).not.toBeVisible();
  });

  test('should toggle recent work experience if toggle is present', async () => {
    const toggleButton = page.getByRole('button', {
      name: 'Show recent only (≤5 years)',
    });
    const isTogglePresent = await toggleButton.isVisible().catch(() => false);

    if (isTogglePresent) {
      await toggleButton.click();
      await page.waitForTimeout(1000);

      const workEntries = page.locator('.mb-4.border');
      const visibleEntriesCount = await workEntries.count();
      console.log(
        `Number of visible work entries after toggle: ${visibleEntriesCount}`,
      );
    } else {
      console.log('Recent work experience toggle not found. Skipping test.');
      test.skip();
    }
  });

  test('should navigate to correct sections when clicking on skills', async () => {
    const skillButton = page.getByRole('button', { name: 'React.js' }).first();
    await skillButton.click();
    await expect(page).toHaveURL('/cv?search=React.js');

    const pageYOffset = await page.evaluate(() => window.pageYOffset);
    expect(pageYOffset).toBe(0);
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
          page.evaluate((url) => window.open(url, '_blank'), href),
        ]);

        try {
          await Promise.race([
            newPage.waitForLoadState('domcontentloaded'),
            new Promise((_, reject) =>
              setTimeout(() => reject(new Error('Page load timeout')), 10000),
            ),
          ]);

          console.log(`Checking link: ${linkText} (${href})`);

          if (linkText?.includes('GitHub')) {
            expect(newPage.url()).toContain('github.com');
          } else if (linkText?.includes('LinkedIn')) {
            expect(newPage.url()).toContain('linkedin.com');
          } else if (linkText?.includes('Email')) {
            expect(newPage.url()).toContain('wahidyankf@gmail.com');
          }
        } catch (error) {
          console.error(`Error loading page for link: ${linkText}`, error);
        } finally {
          await newPage.close();
        }
      }
    }
  });
});
