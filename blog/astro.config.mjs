// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import expressiveCode from 'astro-expressive-code';

export default defineConfig({
  site: 'https://blog.ftwr.app',
  output: 'static',
  integrations: [
    expressiveCode({
      themes: ['github-light'],
      styleOverrides: {
        borderRadius: '0px',
        borderColor: 'rgba(28, 27, 27, 0.12)',
        codeFontFamily: "'JetBrains Mono', monospace",
        codeFontSize: '13px',
        codeBackground: '#f3f0ef',
        frames: {
          shadowColor: 'transparent',
        },
      },
    }),
    mdx(),
    sitemap(),
  ],
});
