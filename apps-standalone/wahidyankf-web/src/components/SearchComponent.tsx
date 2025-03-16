import React from "react";
import { Search, X } from "lucide-react";

interface SearchComponentProps {
  searchTerm: string;
  setSearchTerm: (term: string) => void;
  updateURL: (term: string) => void;
  placeholder: string;
}

export const SearchComponent: React.FC<SearchComponentProps> = ({
  searchTerm,
  setSearchTerm,
  updateURL,
  placeholder,
}) => {
  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newTerm = e.target.value;
    setSearchTerm(newTerm);
    updateURL(newTerm);
  };

  const clearSearch = () => {
    setSearchTerm("");
    updateURL("");
  };

  return (
    <div className="mb-8 relative">
      <input
        type="text"
        placeholder={placeholder}
        value={searchTerm}
        onChange={handleSearchChange}
        className="w-full bg-gray-800 text-green-400 border border-green-400 rounded-lg py-2 px-4 pl-10 pr-12 focus:outline-none focus:ring-2 focus:ring-green-400"
      />
      <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-green-400" />
      {searchTerm && (
        <button
          onClick={clearSearch}
          className="absolute right-3 top-1/2 transform -translate-y-1/2 bg-yellow-400 text-gray-900 hover:bg-yellow-300 transition-colors duration-200 rounded-full p-1"
          aria-label="Clear search"
        >
          <X className="w-4 h-4" />
        </button>
      )}
    </div>
  );
};
