"use client";

import { Navigation } from "@/components/Navigation";
import { filterItems } from "@/utils/search";
import { Github, Globe, Youtube } from "lucide-react";
import { useState, useEffect, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { SearchComponent } from "@/components/SearchComponent";
import { HighlightText } from "@/components/HighlightText";

type Project = {
  title: string;
  description: string;
  details: string[];
  links: {
    [key: string]: string;
  };
};

const projects: Project[] = [
  {
    title: "AyoKoding",
    description:
      "A website to learn about software engineering through books, blogs, and YouTube videos. Created to learn in public and give back to the community.",
    details: [
      "Comprehensive learning resources for software engineering",
      "Public learning platform to share knowledge",
      "Includes a YouTube channel for video content",
    ],
    links: {
      repository: "https://github.com/organiclever/ayokoding",
      website: "https://ayokoding.com/",
      YouTube: "https://www.youtube.com/@AyoKoding",
    },
  },
  {
    title: "Organic Lever",
    description:
      "A web application focused on team and personal productivity (in progress).",
    details: [
      "Aims to improve team collaboration",
      "Enhances personal productivity",
      "Web-based application for easy access",
    ],
    links: {
      website: "http://organiclever.com/",
    },
  },
  {
    title: "The Organic",
    description:
      "A repository to showcase open source projects and toy-projects.",
    details: [
      "Collection of various open source contributions",
      "Includes experimental and learning projects",
      "Demonstrates diverse coding skills and interests",
    ],
    links: {
      repository: "https://github.com/organiclever/the-organic",
    },
  },
];

const LinkIcon = ({ type }: { type: string }) => {
  switch (type.toLowerCase()) {
    case "repository":
      return <Github className="inline-block w-4 h-4 mr-1" />;
    case "youtube":
      return <Youtube className="inline-block w-4 h-4 mr-1" />;
    default:
      return <Globe className="inline-block w-4 h-4 mr-1" />;
  }
};

function ProjectsContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const initialSearchTerm = searchParams.get("search") || "";
  const [searchTerm, setSearchTerm] = useState(initialSearchTerm);

  useEffect(() => {
    setSearchTerm(initialSearchTerm);
  }, [initialSearchTerm]);

  const updateURL = (term: string) => {
    const newURL = term
      ? `/personal-projects?search=${encodeURIComponent(term)}`
      : "/personal-projects";
    router.push(newURL, { scroll: false });
  };

  const filteredProjects = filterItems(projects, searchTerm, [
    "title",
    "description",
    "details",
    "links",
  ]);

  return (
    <div className="flex-grow max-w-4xl mx-auto w-full">
      <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-8 text-center text-yellow-400">
        Personal Projects
      </h1>

      <SearchComponent
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        updateURL={updateURL}
        placeholder="Search projects..."
      />

      {filteredProjects.length > 0 ? (
        filteredProjects.map((project, index) => (
          <div
            id={`project-${index}`}
            key={index}
            className="mb-8 border border-green-400 rounded-lg p-4"
          >
            <h2 className="text-xl sm:text-2xl md:text-3xl mb-2 text-yellow-400">
              <HighlightText text={project.title} searchTerm={searchTerm} />
            </h2>
            <p className="mb-2 text-green-300">
              <HighlightText
                text={project.description}
                searchTerm={searchTerm}
              />
            </p>
            <ul className="list-disc list-inside mb-2 text-green-200">
              {project.details.map((detail: string, index: number) => (
                <li key={index} className="mb-1">
                  <HighlightText text={detail} searchTerm={searchTerm} />
                </li>
              ))}
            </ul>
            <div className="mt-4">
              {Object.entries(project.links).map(([key, value]) => (
                <a
                  key={key}
                  href={value as string}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-yellow-400 underline decoration-yellow-400 hover:text-green-400 hover:decoration-green-400 transition-all duration-200 mr-4 inline-flex items-center"
                >
                  <LinkIcon type={key} />
                  <HighlightText
                    text={key.charAt(0).toUpperCase() + key.slice(1)}
                    searchTerm={searchTerm}
                  />
                </a>
              ))}
            </div>
          </div>
        ))
      ) : (
        <p className="text-center text-yellow-400">
          No projects found matching your search.
        </p>
      )}
    </div>
  );
}

export default function Projects() {
  return (
    <main className="min-h-screen bg-gray-900 text-green-400 p-4 sm:p-8 md:p-12 lg:p-16 lg:ml-80 flex flex-col pb-20 lg:pb-0">
      <Navigation />
      <div className="flex-grow max-w-4xl mx-auto w-full">
        <Suspense fallback={<div>Loading...</div>}>
          <ProjectsContent />
        </Suspense>
      </div>
    </main>
  );
}
