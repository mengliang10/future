/**
 * Resolves a root path with Astro's configured BASE_URL.
 * Works seamlessly whether running locally at '/' or on GitHub Pages at '/future/'.
 */
export const base = (import.meta.env.BASE_URL ?? '/').replace(/\/+$/, '');

export function url(path: string = '/'): string {
  if (!path) return base ? `${base}/` : '/';
  if (path.startsWith('http://') || path.startsWith('https://') || path.startsWith('mailto:') || path.startsWith('#')) {
    return path;
  }
  const clean = path.startsWith('/') ? path : `/${path}`;
  return `${base}${clean}`;
}
