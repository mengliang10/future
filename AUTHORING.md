# Authoring and changing hundreds of slides

## The format

Edit JSON records and Markdown notes, not generated HTML. Astro Content Collections validate records at build time. Reveal.js presents the generated HTML. Shared CSS controls all slide appearance.

Every slide has explicit machine-readable hooks:

```html
<section data-slide-id="tech:artificial-general-intelligence"
         data-record-id="artificial-general-intelligence">
  <h2 data-field="title" data-ref="artificial-general-intelligence:title">…</h2>
  <strong data-field="stage" data-ref="artificial-general-intelligence:stage">…</strong>
</section>
```

Deck documents have `data-deck-id` and `data-mode`. Website record documents also expose `data-record-id` and `data-collection`.

Use these hooks for audits, scraping, targeted exports and verification. Apply updates to canonical records, then regenerate HTML. Direct changes to `dist/` will be overwritten on the next build.

## Change a technology once

Create a JSON patch with only the fields to change:

```json
{
  "businessMeaning": "Which workflow becomes more useful, what would adoption cost, and what evidence would justify a bounded pilot?"
}
```

Preview the impact:

```sh
npm run update -- --collection technologies --id artificial-general-intelligence --patch scripts/update-patch-example.json
```

Apply the change, with a backup of the previous record:

```sh
npm run update -- --collection technologies --id artificial-general-intelligence --patch scripts/update-patch-example.json --apply
npm run build
```

The tool prints affected evergreen deck IDs and the number of historical snapshots excluded from changes. Backups are written to `source/edit-history`. The update command supports technologies, companies, reusable blocks and sectors. It refuses ID/provenance/raw-note changes and unknown fields. Astro schema validation runs during the build.

A company edit changes its company page. Technology slides only change when they reference that company's field; current briefing slides reference technology and sector records, not copied company prices. Market snapshot JSON is separately timestamped and is not a live feed.

## Change a reusable slide everywhere

Edit `src/content/blocks/reading-framework.json`, or use the patch tool with `--collection blocks --id reading-framework`. This block is referenced by all 85 evergreen decks. A change to its title or points appears in every referencing deck after the build.

Edit `src/styles/slides.css` for fonts, colours, spacing and slide proportions. Edit `src/components/Slide.astro` for shared layout. These visual changes affect snapshots too: snapshot mode pins content, not the renderer. Keep exported PDF/HTML bundles if a historical visual appearance must also be immutable.

Generate the dependency map:

```sh
node scripts/dependencies.mjs
```

The result is `qa/dependencies.json`, keyed by `collection:stable-id`.

## Assemble a new briefing

Create `src/content/decks/my-briefing.json`:

```json
{
  "id": "my-briefing",
  "title": "My technology briefing",
  "sector": "ai",
  "mode": "evergreen",
  "added": "2026-11-16",
  "blocks": ["reading-framework", "evidence-check"],
  "technologies": ["artificial-general-intelligence"]
}
```

Use the actual date you add the deck. IDs must match existing records. Build to create `/presentations/my-briefing/`, with a catalogue entry automatically generated. Each briefing consists of a cover, opening framework, one slide per referenced technology, and closing evidence framework. Use the current two-block convention.

The initial 85 decks are grouped by normalised sector, with up to 12 technology slides each. These are generated research briefings, not newly fact-checked investment theses or replicas of a pre-existing slide deck.

## Preserve a historical presentation

```sh
node scripts/snapshot-deck.mjs ai-01
npm run build
```

A new dated snapshot manifest includes copies of its resolved technology, sector and block content. Later canonical content edits do not change that snapshot's content. The included `ai-01-snapshot-2026-11-16` demonstrates this. Evergreen manifests continue to reference current records.

## Edit the research narrative

Each technology/company record retains `bodyMarkdown`, `bodyHtml`, source metadata and a source hash. Source Markdown downloads remain unchanged for provenance. The imported JSON record is the editable working copy; update its structured fields directly or through the update tool.

For narrative edits, update `bodyMarkdown` then regenerate its HTML using the notes renderer:

```sh
python3 scripts/render-notes.py technologies artificial-general-intelligence
```

Do not run `npm run import:source -- --refresh` over edited data without a backup: refresh explicitly replaces working records with the archived import. The normal import command preserves existing JSON files and adds missing source records.

## Reproducing existing HTML decks

Do not blindly replace independent HTML decks. Add their metadata and link first. To gain central updates, convert selected slide content into stable records/blocks and render it through the shared components. Embedded standalone HTML does not automatically inherit canonical data changes.
