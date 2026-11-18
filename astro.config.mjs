import {defineConfig} from 'astro/config';

export default defineConfig({
  site: 'https://mengliang10.github.io',
  base: '/future',
  output: 'static',
  trailingSlash: 'always',
  server: {host: '127.0.0.1', port: 4330}
});
