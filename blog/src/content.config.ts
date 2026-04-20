import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    author: z.string().default('FTWR'),
    tags: z.array(z.string()),
    category: z.enum([
      'technical-tutorial',
      'case-study',
      'model-documentation',
      'market-analysis',
      'community-spotlight',
      'meta',
    ]),
    draft: z.boolean().default(false),
    ogImage: z.string().optional(),
  }),
});

export const collections = { blog };
