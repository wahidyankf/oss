import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import path from 'path';
import fs from 'fs';
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
  params,
}: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const slugString = slug.join('/');

  try {
    const postData = getPostData(slugString);
    return {
      title: postData.title,
      description: postData.description,
    };
  } catch (error) {
    console.log(error);
    return {
      title: slugString,
      description: 'Content directory',
    };
  }
}

export default async function Post({ params }: PageProps) {
  const { slug } = await params;
  const slugString = slug.join('/');
  const postsDirectory = path.join(process.cwd(), 'contents');
  const fullPath = path.join(postsDirectory, slugString);

  // Check if the path is a directory
  if (fs.existsSync(fullPath) && fs.statSync(fullPath).isDirectory()) {
    const items = fs.readdirSync(fullPath);
    const readmeFile = items.find((item) => item.toLowerCase() === 'readme.md');
    const markdownFiles = items.filter(
      (item) => item.endsWith('.md') && item.toLowerCase() !== 'readme.md',
    );

    // If README.md exists, display its content
    if (readmeFile) {
      const readmeSlug = path.join(slugString, readmeFile).replace(/\.md$/, '');
      try {
        const readmeData = getPostData(readmeSlug);
        return (
          <article className="container mx-auto px-4 py-8 prose lg:prose-xl">
            <h1>{readmeData.title || slugString}</h1>
            {readmeData.description && (
              <p className="lead">{readmeData.description}</p>
            )}
            <div dangerouslySetInnerHTML={{ __html: readmeData.contentHtml }} />

            {markdownFiles.length > 0 && (
              <section className="mt-12">
                <h2 className="text-2xl font-semibold mb-4">Other Contents</h2>
                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {markdownFiles
                    .map((file) => {
                      const filePath = path.join(slugString, file);
                      const fileSlug = filePath.replace(/\.md$/, '');

                      try {
                        const postData = getPostData(fileSlug);
                        return (
                          <article
                            key={fileSlug}
                            className="bg-white shadow-md rounded-lg p-6"
                          >
                            <h3 className="text-xl font-bold mb-2">
                              <Link
                                href={`/c/${fileSlug}`}
                                className="hover:text-blue-600"
                              >
                                {postData.title}
                              </Link>
                            </h3>
                            {postData.description && (
                              <p className="text-gray-600 mb-2">
                                {postData.description}
                              </p>
                            )}
                            <p className="text-sm text-gray-500">
                              Published on:{' '}
                              {new Date(postData.date).toLocaleDateString(
                                'en-US',
                                {
                                  year: 'numeric',
                                  month: 'long',
                                  day: 'numeric',
                                },
                              )}
                            </p>
                            <Link
                              href={`/c/${fileSlug}`}
                              className="text-blue-500 hover:text-blue-700 transition-colors mt-2 inline-block"
                            >
                              Read More
                            </Link>
                          </article>
                        );
                      } catch (error) {
                        console.log(error);
                        return null;
                      }
                    })
                    .filter(Boolean)}
                </div>
              </section>
            )}
          </article>
        );
      } catch (error) {
        console.log(error);
        // Fallback if README.md can't be processed
        return (
          <div className="container mx-auto px-4 py-8">
            <h1 className="text-4xl font-bold mb-8">{slugString} Contents</h1>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {markdownFiles
                .map((file) => {
                  const filePath = path.join(slugString, file);
                  const fileSlug = filePath.replace(/\.md$/, '');

                  try {
                    const postData = getPostData(fileSlug);
                    return (
                      <article
                        key={fileSlug}
                        className="bg-white shadow-md rounded-lg p-6"
                      >
                        <h3 className="text-xl font-bold mb-2">
                          <Link
                            href={`/c/${fileSlug}`}
                            className="hover:text-blue-600"
                          >
                            {postData.title}
                          </Link>
                        </h3>
                        {postData.description && (
                          <p className="text-gray-600 mb-2">
                            {postData.description}
                          </p>
                        )}
                        <p className="text-sm text-gray-500">
                          Published on:{' '}
                          {new Date(postData.date).toLocaleDateString('en-US', {
                            year: 'numeric',
                            month: 'long',
                            day: 'numeric',
                          })}
                        </p>
                        <Link
                          href={`/c/${fileSlug}`}
                          className="text-blue-500 hover:text-blue-700 transition-colors mt-2 inline-block"
                        >
                          Read More
                        </Link>
                      </article>
                    );
                  } catch (error) {
                    console.log(error);
                    return null;
                  }
                })
                .filter(Boolean)}
            </div>

            {markdownFiles.length === 0 && (
              <p className="text-center text-gray-600 mt-8">
                No markdown files found in this directory.
              </p>
            )}
          </div>
        );
      }
    }

    // If no README.md, show the previous directory listing
    return (
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold mb-8">{slugString} Contents</h1>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {markdownFiles
            .map((file) => {
              const filePath = path.join(slugString, file);
              const fileSlug = filePath.replace(/\.md$/, '');

              try {
                const postData = getPostData(fileSlug);
                return (
                  <article
                    key={fileSlug}
                    className="bg-white shadow-md rounded-lg p-6"
                  >
                    <h3 className="text-xl font-bold mb-2">
                      <Link
                        href={`/c/${fileSlug}`}
                        className="hover:text-blue-600"
                      >
                        {postData.title}
                      </Link>
                    </h3>
                    {postData.description && (
                      <p className="text-gray-600 mb-2">
                        {postData.description}
                      </p>
                    )}
                    <p className="text-sm text-gray-500">
                      Published on:{' '}
                      {new Date(postData.date).toLocaleDateString('en-US', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                      })}
                    </p>
                    <Link
                      href={`/c/${fileSlug}`}
                      className="text-blue-500 hover:text-blue-700 transition-colors mt-2 inline-block"
                    >
                      Read More
                    </Link>
                  </article>
                );
              } catch (error) {
                console.log(error);
                return null;
              }
            })
            .filter(Boolean)}
        </div>

        {markdownFiles.length === 0 && (
          <p className="text-center text-gray-600 mt-8">
            No markdown files found in this directory.
          </p>
        )}
      </div>
    );
  }

  // Try to get post data
  try {
    const postData = getPostData(slugString);

    return (
      <article className="container mx-auto px-4 py-8 prose lg:prose-xl">
        <h1>{postData.title}</h1>
        {postData.description && <p className="lead">{postData.description}</p>}
        <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
      </article>
    );
  } catch (error) {
    console.log(error);
    // If no markdown file is found, show a 404
    notFound();
  }
}
