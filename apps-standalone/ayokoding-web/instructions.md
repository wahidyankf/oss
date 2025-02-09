To create a Next.js project that automatically renders all markdown files in a directory (including nested subdirectories) using the App Router, you'll need to follow these steps:

## Setting Up the Project

Since you already have a Next.js app using TypeScript up and running, we'll focus on adding the necessary components and configurations to handle markdown rendering.

## Install Dependencies

First, install the required dependencies:

```bash
npm install gray-matter remark remark-html @types/remark-html
```

## Create Utility Functions

Create a new file `lib/markdownUtils.ts` to handle markdown processing:

```typescript
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

const postsDirectory = path.join(process.cwd(), 'posts');

export function getAllPostSlugs() {
  const slugs: string[] = [];

  function traverseDirectory(dir: string) {
    const files = fs.readdirSync(dir);

    for (const file of files) {
      const filePath = path.join(dir, file);
      const stat = fs.statSync(filePath);

      if (stat.isDirectory()) {
        traverseDirectory(filePath);
      } else if (path.extname(file) === '.md') {
        const relativePath = path.relative(postsDirectory, filePath);
        const slug = relativePath.replace(/\.md$/, '');
        slugs.push(slug);
      }
    }
  }

  traverseDirectory(postsDirectory);
  return slugs;
}

export async function getPostData(slug: string) {
  const fullPath = path.join(postsDirectory, `${slug}.md`);
  const fileContents = fs.readFileSync(fullPath, 'utf8');
  const { data, content } = matter(fileContents);

  const processedContent = await remark().use(html).process(content);
  const contentHtml = processedContent.toString();

  return {
    slug,
    contentHtml,
    ...data,
  };
}
```

## Create Dynamic Route

Create a new file `app/posts/[...slug]/page.tsx`:

```typescript
import { getAllPostSlugs, getPostData } from '../../../lib/markdownUtils';

export async function generateStaticParams() {
  const paths = getAllPostSlugs();
  return paths.map((slug) => ({ slug: slug.split('/') }));
}

export default async function Post({ params }: { params: { slug: string[] } }) {
  const slug = params.slug.join('/');
  const postData = await getPostData(slug);

  return (
    <article>
      <h1>{postData.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
    </article>
  );
}
```

## Create a Posts List Page

Create a new file `app/posts/page.tsx` to display a list of all posts:

```typescript
import Link from 'next/link';
import { getAllPostSlugs, getPostData } from '../../lib/markdownUtils';

export default async function PostsList() {
  const slugs = getAllPostSlugs();
  const posts = await Promise.all(slugs.map(async (slug) => await getPostData(slug)));

  return (
    <div>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.slug}>
            <Link href={`/posts/${post.slug}`}>
              {post.title}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

## Add Markdown Files

Create a `posts` directory in the root of your project and add your markdown files. You can create nested directories within `posts` to organize your content.

For example:

```
posts/
  hello-world.md
  tech/
    nextjs-intro.md
    react-hooks.md
  travel/
    japan/
      tokyo.md
      kyoto.md
```

## Update Navigation

Update your main navigation component to include a link to the posts list:

```typescript
import Link from 'next/link';

export default function Navigation() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/posts">Blog</Link>
    </nav>
  );
}
```

With these changes, your Next.js app will automatically render all markdown files in the `posts` directory, including nested subdirectories. The blog posts will be accessible at URLs that match their file structure, for example:

- `/posts/hello-world`
- `/posts/tech/nextjs-intro`
- `/posts/travel/japan/tokyo`

The App Router handles the routing based on the file structure, and the `generateStaticParams` function ensures that all posts are pre-rendered at build time for optimal performance[1][3][5].

Citations:
[1] https://nextjs.org/learn/pages-router/dynamic-routes-render-markdown
[2] https://www.colinhemphill.com/blog/markdown-syntax-highlighting-with-the-nextjs-app-router
[3] https://github.com/xypnox/next-nested
[4] https://dev.to/logrocket/a-guide-to-nextjs-layouts-and-nested-layouts-5c0d?comments_sort=oldest
[5] https://www.youtube.com/watch?v=wUH0bbeP3WY
[6] https://blog.nrwl.io/read-and-render-md-files-with-next-js-and-nx-89a85c1d9b44?gi=08a57570ac90
[7] https://nextjs.org/learn/pages-router/data-fetching-blog-data
[8] https://www.reddit.com/r/nextjs/comments/w6q5xb/nested_directories_with_nextmdx/
[9] https://nextjs.org/learn/dashboard-app/creating-layouts-and-pages
[10] https://dev.to/willholmes/multi-nested-dynamic-routes-in-nextjs-30f7
[11] https://www.youtube.com/watch?v=34bRv6cQezo
[12] https://stackoverflow.com/questions/69122134/how-to-display-markdown-files-in-nested-folders-in-next-js
[13] https://nextjs.org/docs/app/building-your-application/configuring/mdx
[14] https://spacejelly.dev/posts/mdx-in-nextjs
[15] https://dev.to/robertobutti/building-a-website-using-markdown-content-with-nextjs-app-router-and-fusionable-4kj7
[16] https://www.youtube.com/watch?v=k7VTCtv1Q08
[17] https://www.alexchantastic.com/building-a-blog-with-next-and-mdx
[18] https://github.com/emanuelefavero/nextjs-app-router-blog
[19] https://www.singlehanded.dev/blog/building-markdown-blog-with-nextjs-app-router
[20] https://github.com/ardunster/nextjs-app-router-mdx
[21] https://stackoverflow.com/questions/69122134/how-to-display-markdown-files-in-nested-folders-in-next-js
[22] https://blog.logrocket.com/guide-next-js-layouts-nested-layouts/
[23] https://www.youtube.com/watch?v=34bRv6cQezo
[24] https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts
[25] https://github.com/vercel/next.js/issues/49881
[26] https://nextjs.org/learn/pages-router/dynamic-routes-render-markdown
[27] https://nextjs.org/docs/app/building-your-application/routing/route-groups
[28] https://www.youtube.com/watch?v=ICOBQCvbtNc
[29] https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes
[30] https://www.youtube.com/watch?v=QIIc5EYSZpw
[31] https://dev.to/robertobutti/building-a-website-using-markdown-content-with-nextjs-app-router-and-fusionable-4kj7
[32] https://developdbycherron.com/blog/nextjs-markdown-blog
[33] https://stackoverflow.com/questions/72855945/how-to-use-slug-url-in-nextjs
[34] https://github.com/vercel/next.js/discussions/41826
[35] https://staticmania.com/blog/creating-a-blog-with-nextjs-and-markdown
[36] https://nextjs.org/docs/app/building-your-application/configuring/mdx
[37] https://bionicjulia.com/blog/setting-up-nextjs-markdown-blog-with-typescript
[38] https://blog.bytescrum.com/nextjs-dynamic-routes-nested-routes-with-folder-structure
[39] https://tina.io/blog/simple-markdown-blog-nextjs
[40] https://dev.to/jameswallis/combining-markdown-and-dynamic-routes-to-make-a-more-maintainable-next-js-website-3ogl
[41] https://github.com/vercel/next.js/discussions/58575
[42] https://upsun.com/blog/avoid-common-mistakes-with-next-js-app-router/
[43] https://stackoverflow.com/questions/65570858/generate-next-js-static-pages-from-folder-of-markdown
[44] https://www.pullrequest.com/blog/build-a-blog-with-nextjs-and-markdown/

---

Answer from Perplexity: pplx.ai/share
