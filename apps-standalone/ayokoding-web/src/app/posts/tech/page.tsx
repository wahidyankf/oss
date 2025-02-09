import Link from 'next/link';
import { getPostsByCategory, getPostData } from '../../../lib/markdownUtils';

export default async function TechPosts() {
  const slugs = getPostsByCategory('tech');
  const posts = await Promise.all(slugs.map(async (slug) => await getPostData(slug)));

  return (
    <div>
      <h1>Tech Blog Posts</h1>
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
