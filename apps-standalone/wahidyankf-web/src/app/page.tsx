"use client";

import {
  Briefcase,
  FolderOpen,
  Github,
  Linkedin,
  Mail,
  Star,
  Code,
  Package,
} from "lucide-react";
import Link from "next/link";
import { useSearchParams, useRouter } from "next/navigation";
import {
  cvData,
  getTopSkillsLastFiveYears,
  getTopLanguagesLastFiveYears,
  getTopFrameworksLastFiveYears,
  formatDuration,
} from "@/app/data";
import { Navigation } from "@/components/Navigation";
import { useState, useEffect } from "react";
import { filterItems } from "@/utils/search";
import { SearchComponent } from "@/components/SearchComponent";
import { HighlightText } from "@/components/HighlightText";
import { Suspense } from "react";
import { parseMarkdownLinks } from "@/utils/markdown";

function HomeContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const initialSearchTerm = searchParams.get("search") || "";
  const [searchTerm, setSearchTerm] = useState(initialSearchTerm);

  const aboutMe = cvData.find((entry) => entry.type === "about");
  const topSkills = getTopSkillsLastFiveYears(cvData);
  const topLanguages = getTopLanguagesLastFiveYears(cvData);
  const topFrameworks = getTopFrameworksLastFiveYears(cvData);

  const filteredSkills = filterItems(
    topSkills.map((item) => ({ ...item, duration: item.duration.toString() })),
    searchTerm,
    ["name"]
  );
  const filteredLanguages = filterItems(
    topLanguages.map((item) => ({
      ...item,
      duration: item.duration.toString(),
    })),
    searchTerm,
    ["name"]
  );
  const filteredFrameworks = filterItems(
    topFrameworks.map((item) => ({
      ...item,
      duration: item.duration.toString(),
    })),
    searchTerm,
    ["name"]
  );

  useEffect(() => {
    setSearchTerm(initialSearchTerm);
  }, [initialSearchTerm]);

  const updateURL = (term: string) => {
    const newURL = term ? `/?search=${encodeURIComponent(term)}` : "/";
    router.push(newURL, { scroll: false });
  };

  const filteredAboutMe = aboutMe
    ? {
        ...aboutMe,
        details:
          filterItems([{ details: aboutMe.details.join("\n") }], searchTerm, [
            "details",
          ])[0]?.details.split("\n") || [],
      }
    : null;

  const handleItemClick = (item: string) => {
    router.push(`/cv?search=${encodeURIComponent(item)}&scrollTop=true`);
  };

  return (
    <main className="min-h-screen bg-gray-900 text-green-400 p-4 sm:p-8 md:p-12 lg:p-16 lg:ml-80 flex flex-col pb-20 lg:pb-0">
      <Navigation />
      <div className="flex-grow max-w-4xl mx-auto w-full">
        <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-8 text-center text-yellow-400">
          Welcome to My Portfolio
        </h1>

        <SearchComponent
          searchTerm={searchTerm}
          setSearchTerm={setSearchTerm}
          updateURL={updateURL}
          placeholder="Search skills, languages, or frameworks..."
        />

        {/* About Me section */}
        <section className="mb-8 border border-green-400 rounded-lg p-4">
          <h2 className="text-xl sm:text-2xl md:text-3xl mb-4 text-yellow-400">
            About Me
          </h2>
          {filteredAboutMe && filteredAboutMe.details.length > 0 ? (
            filteredAboutMe.details.map((detail: string, index: number) => (
              <p key={index} className="mb-4 text-green-300">
                {parseMarkdownLinks(detail, searchTerm)}
              </p>
            ))
          ) : (
            <p className="text-center text-yellow-400">
              No matching content in the About Me section.
            </p>
          )}
        </section>

        {/* Skills & Expertise section */}
        <section className="mb-8 border border-green-400 rounded-lg p-4">
          <h2 className="text-xl sm:text-2xl md:text-3xl mb-4 text-yellow-400">
            Skills & Expertise
          </h2>
          <div className="space-y-4">
            {/* Top Skills */}
            <div>
              <h3 className="text-lg font-semibold mb-2 text-green-300">
                Top Skills Used in The Last 5 Years
              </h3>
              <div className="flex flex-wrap gap-2">
                {filteredSkills.map(({ name, duration }) => (
                  <button
                    key={name}
                    onClick={() => handleItemClick(name)}
                    className="bg-gray-800 text-green-400 px-2 py-1 rounded-md text-sm flex items-center hover:bg-gray-700 transition-colors duration-200 group"
                  >
                    <Star className="w-4 h-4 mr-2 text-yellow-400" />
                    <span className="mr-2 group-hover:text-white transition-colors duration-200">
                      <HighlightText text={name} searchTerm={searchTerm} />
                    </span>
                    <span className="text-xs text-green-300 group-hover:text-white transition-colors duration-200">
                      ({formatDuration(Number(duration))})
                    </span>
                  </button>
                ))}
              </div>
            </div>
            {/* Top Programming Languages */}
            <div>
              <h3 className="text-lg font-semibold mb-2 text-green-300">
                Top Programming Languages Used in The Last 5 Years
              </h3>
              <div className="flex flex-wrap gap-2">
                {filteredLanguages.map(({ name }) => (
                  <button
                    key={name}
                    onClick={() => handleItemClick(name)}
                    className="bg-gray-800 text-green-400 px-2 py-1 rounded-md text-sm flex items-center hover:bg-gray-700 transition-colors duration-200 group"
                  >
                    <Code className="w-4 h-4 mr-2 text-yellow-400" />
                    <span className="group-hover:text-white transition-colors duration-200">
                      <HighlightText text={name} searchTerm={searchTerm} />
                    </span>
                  </button>
                ))}
              </div>
            </div>
            {/* Top Frameworks & Libraries */}
            <div>
              <h3 className="text-lg font-semibold mb-2 text-green-300">
                Top Frameworks & Libraries Used in The Last 5 Years
              </h3>
              <div className="flex flex-wrap gap-2">
                {filteredFrameworks.map(({ name }) => (
                  <button
                    key={name}
                    onClick={() => handleItemClick(name)}
                    className="bg-gray-800 text-green-400 px-2 py-1 rounded-md text-sm flex items-center hover:bg-gray-700 transition-colors duration-200 group"
                  >
                    <Package className="w-4 h-4 mr-2 text-yellow-400" />
                    <span className="group-hover:text-white transition-colors duration-200">
                      <HighlightText text={name} searchTerm={searchTerm} />
                    </span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Quick Links section */}
        <section className="mb-8 border border-green-400 rounded-lg p-4">
          <h2 className="text-xl sm:text-2xl md:text-3xl mb-4 text-yellow-400">
            Quick Links
          </h2>
          <div className="flex flex-wrap gap-4">
            <Link
              href="/cv"
              className="flex items-center text-yellow-400 hover:text-green-400 transition-colors duration-200"
            >
              <Briefcase className="w-5 h-5 mr-2" />
              View My CV
            </Link>
            <Link
              href="/personal-projects"
              className="flex items-center text-yellow-400 hover:text-green-400 transition-colors duration-200"
            >
              <FolderOpen className="w-5 h-5 mr-2" />
              Browse My Personal Projects
            </Link>
          </div>
        </section>

        {/* Connect With Me section */}
        <section className="mb-8 border border-green-400 rounded-lg p-4">
          <h2 className="text-xl sm:text-2xl md:text-3xl mb-4 text-yellow-400">
            Connect With Me
          </h2>
          <div className="flex flex-wrap gap-4">
            {aboutMe?.links &&
              Object.entries(aboutMe.links).map(([key, value]) => (
                <a
                  key={key}
                  href={value}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center text-yellow-400 hover:text-green-400 transition-colors duration-200"
                >
                  {key === "github" && <Github className="w-5 h-5 mr-2" />}
                  {key === "linkedin" && <Linkedin className="w-5 h-5 mr-2" />}
                  {key === "email" && <Mail className="w-5 h-5 mr-2" />}
                  {key.charAt(0).toUpperCase() + key.slice(1)}
                </a>
              ))}
          </div>
        </section>
      </div>
    </main>
  );
}

export default function Home() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HomeContent />
    </Suspense>
  );
}
