import { Metadata } from 'next';
import { getAllPostSlugs, getPostData } from '../../../lib/markdownUtils';

// Define types for params and page props
type Params = {
  slug: string[];
};

interface PageProps {
  params: Promise<Params>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}

export async function generateStaticParams() {
  const paths = getAllPostSlugs();
  return paths.map((slug) => ({ slug: slug.split('/') }));
}

export async function generateMetadata({ 
  params 
}: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const slugString = slug.join('/');
  const postData = await getPostData(slugString);

  return {
    title: postData.title,
    description: postData.description,
  };
}

export default async function Post({ params }: PageProps) {
  const { slug } = await params;
  const slugString = slug.join('/');
  const postData = await getPostData(slugString);
  
  return (
    <article>
      <h1>{postData.title}</h1>
      {postData.description && <p>{postData.description}</p>}
      <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
    </article>
  );
}
