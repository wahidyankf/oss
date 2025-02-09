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
