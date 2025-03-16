import Link from "next/link";
import { File, Folder } from "lucide-react";
import React from "react";
import { usePathname } from "next/navigation";

export const Navigation: React.FC = () => {
  const pathname = usePathname();

  const navItems = [
    { href: "/", label: "Home" },
    { href: "/cv", label: "CV" },
    { href: "/personal-projects", label: "Personal Projects" },
  ];

  return (
    <>
      {/* Mobile Navigation */}
      <nav
        data-testid="mobile-nav"
        className="lg:hidden fixed bottom-0 left-0 right-0 bg-gray-900 border-t border-green-400 p-4 flex justify-around z-50"
      >
        {navItems.map((item) => (
          <NavLink
            key={item.href}
            href={item.href}
            isActive={pathname === item.href}
            label={item.label}
          />
        ))}
      </nav>

      {/* Desktop Navigation */}
      <nav
        data-testid="desktop-nav"
        className="hidden lg:block fixed left-0 top-0 bottom-0 w-80 bg-gray-900 border-r border-green-400 p-4 overflow-y-auto z-50"
      >
        <Link
          href="/"
          className="block mb-4 p-4 hover:text-yellow-400 transition-colors duration-200 light-theme:text-light-primary light-theme:hover:text-light-accent"
        >
          <Folder className="inline-block mr-2" />
          <span className="font-bold">WahidyanKF</span>
        </Link>
        <hr className="border-t border-green-400 mx-4 mb-4 light-theme:border-light-primary" />
        <ul className="pl-4">
          {navItems.map((item) => (
            <NavItem
              key={item.href}
              href={item.href}
              isActive={pathname === item.href}
              label={item.label}
            />
          ))}
        </ul>
      </nav>
    </>
  );
};

// Helper components
const NavLink: React.FC<{
  href: string;
  isActive: boolean;
  label: string;
}> = ({ href, isActive, label }) => (
  <Link
    href={href}
    className={`flex flex-col items-center ${
      isActive
        ? "text-yellow-400 light-theme:text-light-accent"
        : "text-green-400 light-theme:text-light-primary"
    } hover:text-yellow-400 transition-colors duration-200`}
  >
    <File className="w-6 h-6" />
    <span className="text-xs">{label}</span>
  </Link>
);

const NavItem: React.FC<{
  href: string;
  isActive: boolean;
  label: string;
}> = ({ href, isActive, label }) => (
  <li className="mb-2">
    <Link
      href={href}
      className={`flex items-center ${
        isActive
          ? "text-yellow-400 light-theme:text-light-accent active-nav-item"
          : "text-green-400 light-theme:text-light-primary"
      } hover:text-yellow-400 transition-colors duration-200`}
    >
      <File className="inline-block mr-2" />
      {label}
    </Link>
  </li>
);
