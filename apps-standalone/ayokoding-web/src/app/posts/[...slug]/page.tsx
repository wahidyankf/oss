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
