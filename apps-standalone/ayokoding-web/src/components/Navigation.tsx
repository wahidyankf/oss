import Link from 'next/link';

export default function Navigation() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <span className="mx-2">|</span>
      <Link href="/c">Categories</Link>
    </nav>
  );
}
