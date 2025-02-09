import { Metadata } from 'next';
import { getAllPostSlugs, getPostData } from '../../../lib/markdownUtils';

type SlugParams = {
  slug: string[];
};

export async function generateStaticParams(): Promise<SlugParams[]> {
  const paths = getAllPostSlugs();
  return paths.map((slug) => ({ slug: slug.split('/') }));
}

export async function generateMetadata({ params }: { params: SlugParams }): Promise<Metadata> {
  const slug = params.slug.join('/');
  const postData = await getPostData(slug);

  return {
    title: postData.title,
    description: postData.description,
  };
}

export default async function Post({ params }: { params: SlugParams }) {
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
