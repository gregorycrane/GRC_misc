# Normalizing the Perseus catalog: Livy and Thucydides

## Executive conclusion

The replacement for the Perseus collections page should be a work-centered catalog, not a list of readable CTS versions. Its core path should be:

> Agent / textgroup → work → bibliographic edition or translation → digital manifestation → provider-specific resource

This separation is required by the source data. In `catalog_data` at commit `dc5871c3609c6a2ffc7e787fbdc70f6924ba4be6`, Livy has 17 MODS records across four CTS works and Thucydides has 80 across two. Most of those records describe printed editions, translations, multivolume sets, or scans. Only a subset points to a verified Perseus TEI file. The current collections page therefore exposes much less than the catalog knows: it lists readable corpus texts, while the MODS records also expose Internet Archive, Google Books, HathiTrust, SLUB, Open Library, WorldCat, and Library of Congress resources.

The decisive rule is: **a CTS version URN in MODS is an identifier claim, not proof of a readable digital text**. A version becomes “Read in Perseus” only after it is reconciled to the current CTS inventory and an existing TEI manifestation.

## What is in the two clusters

### Livy

The MADS authority record gives the preferred name `Livy`, VIAF `99942145`, CITE authority URN `urn:cite:perseus:author.840.1`, PHI author `914`, and alternate identifiers including `stoa0179`. It enumerates PHI works `914.1` through `914.4`.

The normalized work set is:

| CTS work | Catalog title | MODS records |
|---|---|---:|
| `urn:cts:latinLit:phi0914.phi001` | *Ab Urbe Condita* | 7 |
| `urn:cts:latinLit:phi0914.phi002` | *Periochae* | 4 |
| `urn:cts:latinLit:phi0914.phi003` | *Fragmenta* | 4 |
| `urn:cts:latinLit:phi0914.phi004` | *Oxyrrhyncus Epitome of Livy* | 2 |

Representative records:

- `phi0914.phi001.opp-lat3` describes Ogilvie’s 1974 OCT, volume I/books I–IV. It has ISBN, LCCN, OCLC, PHI, Stoa, and CTS identifiers plus WorldCat and LC catalog links, but no digital full text. It is a bibliographic edition, not a TEI manifestation.
- `phi0914.phi001.opp-lat17` describes Egbert’s 1913 *Livy, the second Punic war*, restricted to book XXI and selections from XXII–XXX. Google Books and HathiTrust are provider endpoints for digitizations; the coverage must not be represented as the complete work.
- `phi0914.phi001.opp-eng2` is a Loeb volume whose constituent records include *Periochae*, the Oxyrrhynchus epitome, *Fragmenta*, and Julius Obsequens. One physical publication therefore contains several classical works and even crosses author/textgroup boundaries.
- `phi0914.phi002.opp-lat1` is filed under *Periochae* but contains a related *Ab urbe condita* item with its own PHI/Stoa/Perseus identifiers and Internet Archive link. The work relationship must be taken from identifiers at the level where they occur, not inherited blindly from the directory path.
- `phi0914.phi002.perseus-eng1` has a legacy Perseus reader URL and `Perseus:text:1999.02.0150`. This should be preserved as a legacy resource, then reconciled to the current canonical CTS inventory before being labeled as active.

Current canonical metadata uses `urn:cts:latinLit:phi0914.phi001.perseus-eng3` for the Roberts translation and `...perseus-lat2` for the Weissenborn/Müller edition. Those active identifiers do not line up one-for-one with the 17 MODS filenames. This is a concrete instance of catalog/corpus drift.

### Thucydides

The MADS record gives preferred name `Thucydides`, Greek variant `Θουκυδίδης`, VIAF `95161463`, CITE authority URN `urn:cite:perseus:author.1403.1`, and TLG textgroup `0003`.

The normalized work set is:

| CTS work | Catalog title | MODS records |
|---|---|---:|
| `urn:cts:greekLit:tlg0003.tlg001` | *History of the Peloponnesian War* | 73 |
| `urn:cts:greekLit:tlg0003.tlg002` | *Epigramma* | 7 |

Representative records:

- `tlg0003.tlg001.perseus-grc2` describes the Jones/Powell Greek OCT and points directly to a canonical TEI XML file. Its CTS version is present in the current canonical inventory. This is the clean “edition → TEI manifestation → raw source and reader resources” case.
- `tlg0003.tlg001.opp-eng12` describes Hobbes’s 1812 English translation. Two `relatedItem type="constituent"` blocks represent volumes I and II, each with a different Internet Archive object and a matching Open Library interface. This should become one bibliographic translation, two scan manifestations, and multiple provider resources.
- `tlg0003.tlg001.opp-grc9` describes a four-volume 1788 Greek/Latin edition. Its four constituent volumes have distinct Internet Archive IDs, while sharing the same OCLC record. It is one bilingual bibliographic edition with four scan manifestations—not four works and not one undifferentiated PDF.
- `tlg0003.tlg001.opp-lat17` exposes multiple volumes through Internet Archive/Open Library and HathiTrust. The Hathi handles may represent different scanned copies from the OCA objects, so they should remain separate manifestations unless copy-level evidence establishes equivalence.
- `tlg0003.tlg002.opp-grc3` describes an epigram embedded in Bergk’s *Poetae lyrici Graeci* and supplies page-level Google Books and Internet Archive stream links in addition to whole-volume links. This needs a coverage selector on the resource or manifestation.

The current canonical inventory contains 13 active Thucydides versions for `tlg001` (Greek plus English, German, French, Italian, and Latin translations). The beta collections page presents those readable texts. The other MODS records remain valuable as editions and scans even when no TEI file exists.

## Normalized entities and invariants

The accompanying JSON Schema defines six top-level arrays:

1. **Agent**: persons and organizations, including preferred/variant names and authority identifiers.
2. **Work**: the abstract classical work, normally keyed by a CTS work URN.
3. **Edition**: a bibliographic edition, translation, bilingual edition, excerpt, commentary, or mixed publication. Contributors, publication facts, language, and work coverage belong here.
4. **Manifestation**: one digital embodiment, such as a TEI transcription, a particular volume scan, PDF, OCR derivative, or metadata object.
5. **Resource**: a provider-specific endpoint through which an edition or manifestation is read, downloaded, queried, or described.
6. **SourceRecord**: provenance back to MADS, MODS, CTS inventory, or TEI headers, including repository path and commit.

Required invariants:

- Every edition references at least one work.
- Every manifestation references exactly one edition. A multivolume edition therefore has multiple manifestations.
- A provider URL is always a resource; it is never used as the identity of a work or edition.
- WorldCat/LC links attach directly to an edition as catalog resources. They do not create a scan manifestation.
- Internet Archive, Google Books, HathiTrust, or SLUB objects create manifestations when they identify a distinct digital object. Multiple interfaces to the same object are separate resources on that manifestation.
- A CTS work URN identifies a work. A CTS version URN identifies a textual version claim attached to an edition and, when verified, its TEI manifestation.
- No UI “Read” action is generated from a CTS URN alone. It requires a verified CTS-inventory entry, an existing TEI object, and an available reader endpoint.
- Every derived fact retains `sourceRecordIds`; lossy normalization must not destroy the original MODS/MADS evidence.

## Deterministic mapping rules

### MADS → Agent

1. Create one Agent from `mads:authority/mads:name`.
2. Map `authority`, `authorityURI`, and `valueURI` to structured identifiers; extract VIAF’s numeric ID without discarding the URI.
3. Map each `mads:variant` to a localized variant name. Preserve the original language code in provenance, but normalize public language tags.
4. Map `mads:identifier` values by type. `citeurn` is a legacy authority ID; `tlg`, `phi`, and `stoa-author` are authority crosswalks.
5. Treat the identifiers in `mads:extension` as related-work assertions, not identifiers of the person.

### Directory and CTS identifiers → Work

1. Parse CTS URNs structurally: namespace, textgroup, work, version, and optional passage. Never split by guessed fixed widths.
2. Prefer an explicit `mods:identifier type="ctsurn"`; derive the parent work URN by removing the version component.
3. Reconcile that result with `mods:identifier type="tlg"` or `type="phi"` and with `citecoll/works.xml` or current `__cts__.xml`.
4. When directory path and record-level identifier disagree, keep the record-level assertion, emit a warning, and queue the record for review.
5. Use a parent/relationship field for summaries, fragments, excerpts, and epitomes; do not flatten them into *Ab urbe condita* merely because readers may conceptually group them there.

### MODS top level → Edition

1. Use `titleInfo type="uniform"` to connect to the work, not as the display title of the publication. Use the ordinary title/subtitle/part fields for the edition title.
2. Infer edition type from roles and languages:
   - translator present → `translation`;
   - original and target languages present → `bilingual_edition`;
   - editor present without translator → `edition`;
   - multiple work IDs or conflicting roles/languages → `mixed` pending review.
3. Map `mods:name` and `mods:roleTerm` to contributions. Normalize role spelling, but retain the source string.
4. Map `originInfo` and `physicalDescription` to publication facts. Preserve display dates as strings and derive numeric start/end dates only when parsing is unambiguous.
5. Map ISBN, OCLC, LCCN, and local record IDs to publication identifiers. Normalize whitespace and leading zeros conservatively; retain the literal value in provenance.
6. A `ctsurn` beginning `...opp-*` remains `catalog_assigned` until current canonical metadata proves it resolves to a text. A `...perseus-*` value also requires verification; its prefix is evidence, not proof.

### `relatedItem` → coverage, contained works, and manifestations

1. `relatedItem type="constituent"` with a part/volume label creates child coverage under the same Edition.
2. A constituent’s Archive/Hathi/Google/SLUB object creates a manifestation scoped to that volume or passage.
3. If a constituent carries a distinct PHI/TLG/CTS work identifier, add that Work to `edition.workIds` and attach coverage to the correct work. Do not inherit only the parent file’s work.
4. `relatedItem type="series"` maps to publication series, not to a new work.
5. Nested titles and contributors override inherited values only for that constituent.

### URLs → Manifestations and Resources

Normalize provider labels case-insensitively (`Worldcat`/`WorldCat`, `GoogleBooks`/`Google Books`) and classify by hostname, not label alone.

| Host/pattern | Provider | Default access type | Object key |
|---|---|---|---|
| `archive.org/details/{id}` or `/stream/{id}` | Internet Archive | read | `{id}` |
| `openlibrary.org/details/{id}` | Open Library | landing page | `{id}` |
| `books.google.*?id={id}` | Google Books | read | query `id` |
| `hdl.handle.net/2027/{id}` | HathiTrust | read | handle suffix |
| `digital.slub-dresden.de/...` | SLUB Dresden | read | stable SLUB ID when present |
| `worldcat.org/oclc/{id}` | WorldCat | catalog record | OCLC number |
| `lccn.loc.gov/{id}` | Library of Congress | catalog record | LCCN |
| canonical repository `.xml` | PerseusDL canonical | source | filename/commit |
| beta CTS route | Perseus Digital Library | read | CTS URN + passage |
| legacy `hopper/text?doc=Perseus:text:*` | Perseus legacy | read | legacy text ID |

Rules:

- Upgrade HTTP to HTTPS only after a successful canonical redirect or provider rule; preserve the literal source URL separately.
- Remove tracking parameters, but retain semantic selectors such as Google `pg`, Archive `#page`, or CTS passages as coverage.
- Open Library and Internet Archive resources sharing the same OCA/Archive ID normally point to the same scan manifestation.
- Google Books, HathiTrust, and Internet Archive links for the same publication must not be merged automatically: they may be different physical copies.
- Repository branch URLs are not stable identifiers. The stable identity is the CTS URN; store a commit-pinned source URL when reproducibility matters.
- Run link checks asynchronously and store status plus `lastChecked`; broken links remain catalog evidence and are not deleted.

### Language normalization

Use one canonical public vocabulary, preferably BCP 47 / ISO 639-3 forms: `eng`, `grc`, `lat`, `deu`, `fra`, `ita`. Normalize source variants such as `ENG` → `eng`, `ger`/`deu` → `deu`, and `fre` → `fra`, while preserving the original code in the source record.

### Deduplication

Use exact identifiers before heuristics:

1. exact CTS version for a verified textual version;
2. exact OCLC/ISBN/LCCN plus compatible title/date/roles for an edition;
3. exact provider object ID for a digital manifestation;
4. only then a fingerprint of normalized title, contributors, language, publisher, date, edition statement, and volume.

Never merge records solely because they share a work URN, uniform title, or OCLC number. OCLC often describes a multivolume set, while the scans are volume- and copy-specific.

## Edge cases that need explicit handling

- **Catalog/corpus drift:** old MODS links target the retired monolithic `PerseusDL/canonical` layout; current content is split into namespace repositories and may use changed version labels.
- **Legacy CTS granularity:** the bundled `perseus/perseuscts.xml` contains book- and summary-level Livy “works” such as `phi00111s`, while the catalog work table uses `phi001`–`phi004`. Preserve aliases, but choose one canonical work hierarchy.
- **CTS without TEI:** many `opp-*` records have CTS-looking version URNs but only scans or metadata.
- **TEI without matching MODS:** current canonical inventories may add `1st1K-*` or newer `perseus-*` versions not represented by a same-named MODS file.
- **One publication, many works:** Loeb and anthology volumes contain multiple works, summaries, fragments, or material by another author.
- **One edition, many volumes:** constituents share edition-level identifiers but have distinct digital object IDs and coverage.
- **One publication, many copies:** IA, Google, and Hathi may digitize different exemplars.
- **Bilingual/polyglot records:** a “Greek” record may include a Latin translation and Latin notes. Keep language roles where MODS provides them; otherwise mark mixed rather than choosing one by filename suffix.
- **Partial coverage:** selected books, speeches, epigrams, page ranges, summaries, and fragments must expose coverage in search results.
- **Repeated or inconsistent identifiers:** leading-zero OCLC values, duplicate OCLCs, blank LC/Google/OCA URLs, case-varying language/provider labels, and empty record identifiers occur.
- **Attribution uncertainty:** the Thucydidean epigram records include “attributed author”; model attribution as a contribution assertion, not unquestioned authorship.
- **Rights and access:** “open metadata” does not guarantee that every linked scan or TEI text has the same reuse terms. Rights belong on manifestations/resources.
- **Link rot and redirects:** old WorldCat Identities, OCLC LAF, HTTP provider URLs, Hopper links, and GitHub branch paths require periodic validation.

## Recommended implementation path

### Phase 1: lossless importer and audit

Build a namespace-aware MODS/MADS importer that emits the normalized objects plus complete `SourceRecord` provenance. Do not mutate source XML. Produce validation reports for missing titles, malformed CTS URNs, empty URLs, directory/identifier conflicts, and language/provider normalization.

Acceptance test: all 17 Livy and 80 Thucydides MODS files import without data loss, and every URL/identifier can be traced to an XML path and commit.

### Phase 2: CTS and TEI reconciliation

Ingest the current `__cts__.xml` inventories and canonical repository manifests. Verify each CTS version against both inventory membership and file existence. Classify identifiers as `verified`, `catalog_assigned`, `legacy`, `deprecated`, or `unresolved`. Read TEI headers to enrich edition statements, responsibility, licenses, and citation coverage.

Acceptance test: the current 13 Thucydides corpus versions and current Livy corpus versions receive live reader actions; scan-only records do not.

### Phase 3: manifestation clustering and link checking

Expand constituent volumes, canonicalize provider object IDs, and group alternate interfaces to the same digital object. Keep cross-provider copies separate until evidence supports equivalence. Add scheduled HTTP checks and retain historical status.

Acceptance test: Hobbes 1812 appears once as a translation with two volumes, each volume having the appropriate Internet Archive/Open Library resources.

### Phase 4: API and materialized views

Store normalized entities relationally or as versioned JSON documents, but expose stable API shapes:

- `/agents/{id}`
- `/works/{cts-work-urn}`
- `/editions/{id}`
- `/manifestations/{id}`
- `/search?author=&work=&language=&type=&provider=&readable=`

Precompute a work page view containing counts and grouped cards; do not flatten the source model merely for rendering.

### Phase 5: collections-page replacement

Render `Author → Work`, then group records into:

1. **Read as text** — verified TEI manifestations, grouped by edition/translation and language;
2. **Digitized editions and translations** — scans/PDFs, grouped by bibliographic edition and volume;
3. **Catalog records** — WorldCat/LC metadata when no digital copy is available;
4. **Related/partial works** — summaries, fragments, epitomes, excerpts, and attributed material.

Show language, editor/translator, date, volume/coverage, provider, and availability. Filters should include language, edition vs. translation, readable TEI vs. scan, provider, date, and complete vs. partial coverage.

### Phase 6: migration and governance

Run the new catalog alongside the current collections page. Compare every existing collections-page link against the new “Read” view and require no regressions before redirecting. Publish schema/version changes, maintain identifier redirects, and introduce curator review queues for ambiguous clustering rather than silently guessing.

## Deliverables

- `normalized-catalog.schema.json`: JSON Schema Draft 2020-12 for the normalized graph.
- `livy-thucydides.normalized.sample.json`: validated sample showing a Thucydides work, a scan-only Hobbes translation, a verified Jones/Powell TEI edition, volume manifestations, and provider resources.

## Primary source links

- [catalog_data repository](https://github.com/gregorycrane/catalog_data)
- [Livy MADS authority](https://github.com/gregorycrane/catalog_data/blob/master/mads/PrimaryAuthors/L/Livy/author.840.1.mads.xml)
- [Thucydides MADS authority](https://github.com/gregorycrane/catalog_data/blob/master/mads/PrimaryAuthors/T/Thucydides/author.1403.1.mads.xml)
- [Livy Ogilvie MODS](https://github.com/gregorycrane/catalog_data/blob/master/mods/latinLit/phi0914/phi001/opp-lat3/phi0914.phi001.opp-lat3.mods1.xml)
- [Livy Egbert MODS](https://github.com/gregorycrane/catalog_data/blob/master/mods/latinLit/phi0914/phi001/opp-lat17/phi0914.phi001.opp-lat17.mods1.xml)
- [Livy mixed Loeb MODS](https://github.com/gregorycrane/catalog_data/blob/master/mods/latinLit/phi0914/phi001/opp-eng2/phi0914.phi001.opp-eng2.mods1.xml)
- [Thucydides Jones/Powell TEI-backed MODS](https://github.com/gregorycrane/catalog_data/blob/master/mods/greekLit/tlg0003/tlg001/perseus-grc2/tlg0003.tlg001.perseus-grc2.mods1.xml)
- [Thucydides Hobbes 1812 MODS](https://github.com/gregorycrane/catalog_data/blob/master/mods/greekLit/tlg0003/tlg001/opp-eng12/tlg0003.tlg001.opp-eng12.mods1.xml)
- [Thucydides 1788 four-volume MODS](https://github.com/gregorycrane/catalog_data/blob/master/mods/greekLit/tlg0003/tlg001/opp-grc9/tlg0003.tlg001.opp-grc9.mods1.xml)
- [Current Thucydides canonical CTS inventory](https://github.com/PerseusDL/canonical-greekLit/blob/master/data/tlg0003/tlg001/__cts__.xml)
- [Current Livy canonical CTS inventory](https://github.com/PerseusDL/canonical-latinLit/blob/master/data/phi0914/phi001/__cts__.xml)
- [Current Perseus collections page](https://beta.perseus.tufts.edu/collections/)
