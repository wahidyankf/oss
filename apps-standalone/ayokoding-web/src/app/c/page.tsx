import Link from 'next/link';
import {
  getAllPostSlugs,
  getContentsByCategory,
  PostData,
} from '../../lib/markdownUtils';

export default async function PostsList({
  searchParams,
}: {
  searchParams: Promise<{ category?: string }>;
}) {
  const { category } = await searchParams;
  const slugs = getAllPostSlugs();

  // Filter slugs based on category or folder
  const filteredSlugs = category
    ? slugs.filter(
        (slug) =>
          slug.startsWith(`${category}/`) ||
          slug === category ||
          slug.split('/')[0] === category,
      )
    : slugs;

  const posts: PostData[] = [];
  for (const slug of filteredSlugs) {
    const categorySlug = slug.split('/')[0];
    const categoryPosts = await getContentsByCategory(categorySlug);
    posts.push(...categoryPosts);
  }

  // Get unique categories
  const categories = [
    ...new Set(
      slugs.map((slug) =>
        slug.includes('/') ? slug.split('/')[0] : 'Uncategorized',
      ),
    ),
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">
        {category ? `Contents in ${category}` : 'All Contents'}
      </h1>

      {/* Category navigation */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Categories</h2>
        <div className="flex flex-wrap gap-4">
          {categories.map((cat) => (
            <Link
              key={cat}
              href={`/c?category=${cat}`}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
            >
              {cat}
            </Link>
          ))}
        </div>
      </div>

      {/* Contents list */}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {posts.map((post) => (
          <article
            key={post.slug}
            className="bg-white shadow-md rounded-lg p-6"
          >
            <h3 className="text-xl font-bold mb-2">
              <Link href={`/c/${post.slug}`} className="hover:text-blue-600">
                {post.title}
              </Link>
            </h3>
            {post.description && (
              <p className="text-gray-600 mb-2">{post.description}</p>
            )}
            <p className="text-sm text-gray-500">
              Published on:{' '}
              {new Date(post.date).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}
            </p>
            <Link
              href={`/c/${post.slug}`}
              className="text-blue-500 hover:text-blue-700 transition-colors mt-2 inline-block"
            >
              Read More
            </Link>
          </article>
        ))}
      </div>

      {posts.length === 0 && (
        <p className="text-center text-gray-600 mt-8">
          No contents found in this category.
        </p>
      )}
    </div>
  );
}
