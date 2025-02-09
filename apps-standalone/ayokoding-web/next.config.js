/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: {
    // Disable type checking during build to prevent blocking
    ignoreBuildErrors: false,
    // Optional: Add strict type checking
    tsconfigPath: './tsconfig.json'
  },
  // Optional: Add additional webpack configuration if needed
  webpack: (config) => {
    return config;
  }
};

module.exports = nextConfig;
