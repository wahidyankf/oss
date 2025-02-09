import Navigation from '../components/Navigation';
import Link from 'next/link';
import { getRecentContents } from '../lib/markdownUtils';
import { readdirSync, statSync } from 'fs';
import path from 'path';

function generateContentTree(
  basePath: string,
  currentPath: string = '',
): React.ReactNode {
  const fullPath = path.join(basePath, currentPath);
  const items = readdirSync(fullPath);

  return (
    <ul className="pl-4">
      {items
        .map((item) => {
          const itemPath = path.join(fullPath, item);
          const relativePath = path.join(currentPath, item);
          const stats = statSync(itemPath);

          if (stats.isDirectory()) {
            return (
              <li key={item} className="my-1">
                <span className="font-semibold text-gray-700">{item}/</span>
                {generateContentTree(basePath, relativePath)}
              </li>
            );
          }

          if (item.endsWith('.md') && item !== 'README.md') {
            const slugPath = relativePath.replace(/\.md$/, '');
            return (
              <li key={item} className="my-1">
                <Link
                  href={`/c/${slugPath}`}
                  className="text-blue-600 hover:text-blue-800 hover:underline"
                >
                  {item}
                </Link>
              </li>
            );
          }

          return null;
        })
        .filter(Boolean)}
    </ul>
  );
}

export default async function Home() {
  const recentContents = (await getRecentContents()).map((post) => ({
    ...post,
    formattedDate: new Date(post.date).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    }),
  }));

  const postsPath = path.join(process.cwd(), 'contents');

  return (
    <div>
      <Navigation />
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold mb-8">Welcome to My Blog</h1>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-4">Recent Contents</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {recentContents.map((post) => (
              <article
                key={post.slug}
                className="bg-white shadow-md rounded-lg p-6"
              >
                <h3 className="text-xl font-bold mb-2">
                  <Link
                    href={`/posts/${post.slug}`}
                    className="hover:text-blue-600"
                  >
                    {post.title}
                  </Link>
                </h3>
                <p className="text-gray-600 mb-2">
                  Published on: {post.formattedDate}
                </p>
                <Link
                  href={`/c/${post.slug}`}
                  className="text-blue-500 hover:text-blue-700 transition-colors"
                >
                  Read More
                </Link>
              </article>
            ))}
          </div>
        </section>

        <section>
          <h2 className="text-2xl font-semibold mb-4">Contents</h2>
          <div className="bg-gray-50 p-6 rounded-lg shadow-inner">
            {generateContentTree(postsPath)}
          </div>
        </section>
      </main>
    </div>
  );
}
