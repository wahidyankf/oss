import * as fs from 'fs';
import * as path from 'path';
import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

const postsDirectory = path.join(process.cwd(), 'contents');

function getAllPostSlugs(): string[] {
  const slugs: string[] = [];

  function traverseDirectory(dir: string): void {
    // Skip directories with README.md
    if (fs.existsSync(path.join(dir, 'README.md'))) {
      return;
    }

    const files = fs.readdirSync(dir);

    for (const file of files) {
      const filePath = path.join(dir, file);
      const stat = fs.statSync(filePath);

      if (stat.isDirectory()) {
        traverseDirectory(filePath);
      } else if (path.extname(file) === '.md' && file !== 'README.md') {
        const relativePath = path.relative(postsDirectory, filePath);
        const slug = relativePath.replace(/\.md$/, '');
        slugs.push(slug);
      }
    }
  }

  traverseDirectory(postsDirectory);
  return slugs;
}

function getCategories(): string[] {
  const slugs = getAllPostSlugs();
  const categories = [...new Set(
    slugs.map(slug => 
      slug.includes('/') ? slug.split('/')[0] : 'Uncategorized'
    )
  )];
  return categories;
}

function getPostsByCategory(category: string): string[] {
  const slugs = getAllPostSlugs().filter(slug => 
    slug.startsWith(`${category}/`) || slug === category
  );
  return slugs;
}

interface PostData {
  slug: string;
  contentHtml: string;
  title: string;
  date: string;
  formattedDate?: string;
  description?: string;
  tags?: string[];
  category?: string;
}

function getPostData(slug: string): PostData {
  const fullPath = path.join(postsDirectory, `${slug}.md`);
  const fileContents = fs.readFileSync(fullPath, 'utf8');
  const { data, content } = matter(fileContents);

  const processedContent = remark().use(html).processSync(content);
  const contentHtml = processedContent.toString();

  return {
    slug,
    contentHtml,
    title: data.title || '',
    date: data.date || '',
    description: data.description,
    tags: data.tags,
    category: data.category,
  };
}

function getAllPosts(): PostData[] {
  const slugs = getAllPostSlugs();
  return slugs
    .map(slug => getPostData(slug))
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
}

function getRecentPosts(limit: number = 5): PostData[] {
  return getAllPosts().slice(0, limit);
}

function getPostsByDateRange(startDate: Date, endDate: Date): PostData[] {
  return getAllPosts().filter(post => {
    const postDate = new Date(post.date);
    return postDate >= startDate && postDate <= endDate;
  });
}

function generateCategoryPages(): void {
  const categories = getCategories();
  const appDir = path.join(process.cwd(), 'src', 'app', 'posts');

  categories.forEach(category => {
    // Skip if it's already a page or Uncategorized
    if (category === 'Uncategorized') return;
    
    const categoryPagePath = path.join(appDir, category, 'page.tsx');
    
    // Create directory if it doesn't exist
    fs.mkdirSync(path.dirname(categoryPagePath), { recursive: true });
    
    // Only create page if it doesn't already exist
    if (!fs.existsSync(categoryPagePath)) {
      const pageContent = `import Link from 'next/link';
import { getPostsByCategory, getPostData } from '../../../lib/markdownUtils';

export default function ${category.charAt(0).toUpperCase() + category.slice(1)}Posts() {
  const slugs = getPostsByCategory('${category}');
  const posts = slugs.map(slug => {
    const post = getPostData(slug);
    return {
      ...post,
      formattedDate: new Date(post.date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    };
  });

  return (
    <div>
      <h1>${category.charAt(0).toUpperCase() + category.slice(1)} Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.slug}>
            <Link href={\`/posts/\${post.slug}\`}>
              {post.title}
            </Link>
            <p>Published on: {post.formattedDate}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}`;
      
      fs.writeFileSync(categoryPagePath, pageContent);
      console.log(`Generated category page for: ${category}`);
    }
  });
}

export {
  getAllPostSlugs,
  getCategories,
  getPostsByCategory,
  getPostData,
  getAllPosts,
  getRecentPosts,
  getPostsByDateRange,
  generateCategoryPages
};
