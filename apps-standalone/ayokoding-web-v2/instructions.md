To create a Next.js project that automatically renders Markdown files from a directory structure and displays them with appropriate slugs using the App Router, follow these steps:

1. Set up the directory structure:

   - Create a `content` folder in the root of your project to store your Markdown files.
   - Organize your Markdown files and directories within the `content` folder.

2. Install necessary dependencies:

   - Install a Markdown parsing library (e.g., `remark` and `remark-html`)[7].
   - Install `gray-matter` for parsing frontmatter[7].

3. Create utility functions:

   - Implement a function to recursively traverse the `content` directory and gather Markdown file information.
   - Create a function to generate slugs based on file paths.
   - Develop a function to read and parse Markdown files, including frontmatter.

4. Set up dynamic routing:

   - In the `app` directory, create a `[...slug]` folder with a `page.tsx` file inside[8].
   - Implement the page component to render Markdown content based on the slug.

5. Implement server-side functions:

   - Create a `generateStaticParams` function to pre-render static pages for all Markdown files[8].
   - Implement a `getPostData` function to fetch and process Markdown content[7].

6. Render Markdown content:

   - Use the parsed Markdown content to render the page, including any frontmatter data[7].

7. Handle directory listings:
   - For directories without a `README.md`, create a component to display a list of pages up to two levels deep.
   - Implement logic to use `README.md` as the index page for directories when present.

Here's a basic implementation outline:

```typescript
// app/[...slug]/page.tsx

import { getPostData, getAllPosts } from '@/lib/posts';

export async function generateStaticParams() {
  const posts = getAllPosts();
  return posts.map((post) => ({
    slug: post.slug.split('/'),
  }));
}

export default async function Page({ params }: { params: { slug: string[] } }) {
  const slug = params.slug.join('/');
  const postData = await getPostData(slug);

  if (!postData) {
    // Handle directory listing or 404
    return <DirectoryListing slug={slug} />;
  }

  return (
    <article>
      <h1>{postData.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
    </article>
  );
}

// lib/posts.ts

import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

const contentDirectory = path.join(process.cwd(), 'content');

export function getAllPosts() {
  // Recursively get all Markdown files
  // Return an array of objects with slug and file path
}

export async function getPostData(slug: string) {
  const fullPath = path.join(contentDirectory, `${slug}.md`);

  if (!fs.existsSync(fullPath)) {
    // Check if it's a directory
    if (fs.existsSync(path.join(contentDirectory, slug))) {
      const readmePath = path.join(contentDirectory, slug, 'README.md');
      if (fs.existsSync(readmePath)) {
        // Use README.md as index
        return processMarkdownFile(readmePath);
      }
      return null; // Will trigger directory listing
    }
    return null; // 404
  }

  return processMarkdownFile(fullPath);
}

async function processMarkdownFile(filePath: string) {
  const fileContents = fs.readFileSync(filePath, 'utf8');
  const { data, content } = matter(fileContents);
  const processedContent = await remark().use(html).process(content);
  const contentHtml = processedContent.toString();

  return {
    ...data,
    contentHtml,
  };
}
```

This implementation provides a foundation for rendering Markdown files with dynamic routing, handling directory listings, and using `README.md` files as index pages. You'll need to expand on this code to fully meet your requirements, such as implementing the directory listing component and adding error handling[1][2][5][7][8].

Citations:
[1] https://dev.to/robertobutti/building-a-website-using-markdown-content-with-nextjs-app-router-and-fusionable-4kj7
[2] https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes
[3] https://www.youtube.com/watch?v=34bRv6cQezo
[4] https://github.com/vercel/next.js/discussions/60260
[5] https://www.colinhemphill.com/blog/markdown-syntax-highlighting-with-the-nextjs-app-router
[6] https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating
[7] https://nextjs.org/learn/pages-router/dynamic-routes-render-markdown
[8] https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes
[9] https://spacejelly.dev/posts/mdx-in-nextjs

---

Answer from Perplexity: pplx.ai/share
