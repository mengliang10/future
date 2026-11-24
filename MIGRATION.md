# Migration and evidence record

Source repository: https://github.com/mengliang10/future

Source commit: `070a5da211c921ed23e6a695e698753a153a229a`.

Imported locally on 16 November 2026. No remote publication or push was performed.

The original Jekyll repository and Git history remain at `source/original`. Original Markdown files are retained under `public/source`; original supplemental data files remain in `public/source-data`. The import manifest records every migrated file and its SHA-256 source hash. Five narrative frontmatter files had unquoted scalar colons: the importer quotes those values for parsing and preserves the original download unchanged.

The new canonical source uses Astro collections: 913 technology records, 137 company records, 15 normalised sectors, 39 narrative/reference records, 85 evergreen deck manifests and 2 reusable slide blocks. One demonstration snapshot was subsequently added.

Category aliases are normalised for navigation while original category strings remain in source metadata. This is not deduplication or validation of 913 unique technologies. Similar or overlapping source records remain separate until reviewed.

Technology and company Markdown bodies are retained. Liquid widgets are replaced by native Astro explorers; source narrative is available in reference views and original Markdown downloads. Source labels, confidence scores and source counts are preserved as reported metadata, not verified facts. Malformed/broken source links route to the relevant explorer rather than invented target records.

Known unresolved company relationship: `nrg` is referenced by imported technology content but has no company record in the source. It is reported in `qa/validation.json`; no company profile was fabricated.

Market data is a static imported JSON snapshot with its source timestamp. It is not described as live pricing. The original fetch scripts and workflows remain archived and are not scheduled in this project. No research pipeline, paid API, vector database, financial model or autonomous data refresh was installed or claimed operational.

This is a structural/UX migration and reusable presentation implementation. It is not a complete current-facts audit of technology, companies, price data or investment claims. The initial commercial/investment panels provide questions to investigate. Record-specific editorial fields can be filled after evidence review.

Legacy source slugs are handled through local aliases. The original GitHub Pages URL remains untouched. A future production deployment will require a domain/base-path decision and a separate deployment configuration.

The counts in this file describe the import-time snapshot of 16 November 2026. Current counts are in `README.md` and `qa/validation.json`, which `npm run build` regenerates.
