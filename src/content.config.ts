import {defineCollection,z} from 'astro:content';
import {glob} from 'astro/loaders';
const shared={id:z.string(),title:z.string().min(1)};
const imported={...shared,summary:z.string().default(''),sourcePath:z.string(),bodyHtml:z.string(),sourceMeta:z.record(z.string(),z.unknown()).default({})};
const collection=(folder,schema)=>defineCollection({loader:glob({pattern:'**/*.json',base:`./src/content/${folder}`}),schema});
export const collections={
 technologies:collection('technologies',z.object({...imported,sector:z.string(),stage:z.string(),confidenceLabel:z.string(),estimate:z.string(),estimateYear:z.number().nullable(),companies:z.array(z.string()),evidenceStatus:z.string(),businessMeaning:z.string(),investmentLens:z.string(),reviewedAt:z.string().nullable()})),
 companies:collection('companies',z.object({...imported,sector:z.string(),symbol:z.string(),exchange:z.string(),private:z.boolean(),businessMeaning:z.string(),investmentLens:z.string(),evidenceStatus:z.string()})),
 sectors:collection('sectors',z.object({...shared,aliases:z.array(z.string()),businessQuestion:z.string(),investorQuestion:z.string()})),
 articles:collection('articles',z.object({...imported,provenance:z.string().default('preserved')})),
 decks:collection('decks',z.object({...shared,sector:z.string(),mode:z.enum(['evergreen','snapshot']),added:z.string(),technologies:z.array(z.string()),blocks:z.array(z.string()),snapshotData:z.record(z.string(),z.unknown()).optional()})),
 blocks:collection('blocks',z.object({...shared,points:z.array(z.string())}))
};
