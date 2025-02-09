import { getAllPostSlugs, getPostData } from '../../../lib/markdownUtils';
import { Metadata } from 'next';

export async function generateStaticParams() {
  const paths = getAllPostSlugs();
  return paths.map((slug) => ({ slug: slug.split('/') }));
}

export async function generateMetadata({ params }: { params: { slug: string[] } }): Promise<Metadata> {
  const slug = params.slug.join('/');
  const postData = await getPostData(slug);

  return {
    title: postData.title,
    description: postData.description,
  };
}

export default async function Post({ params }: { params: { slug: string[] } }) {
  const slug = params.slug.join('/');
  const postData = await getPostData(slug);

  return (
    <article>
      <h1>{postData.title}</h1>
      {postData.description && <p>{postData.description}</p>}
      <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
    </article>
  );
}
