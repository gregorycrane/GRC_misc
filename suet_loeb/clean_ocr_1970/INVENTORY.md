# Inventory of completed work

Updated 2026-09-07. This inventory covers the Suetonius OCR edition and its supporting note review.

| Work completed | Result | Status / boundary |
|---|---|---|
| Inspected supplied sources and previous XML | Two OCR volumes and 17 legacy XML files audited | Alternative XML versions retained as separate witnesses |
| Established printing provenance | Both source title pages say 1970; volume I records revision in 1951 | Export catalogue date not used as printing date |
| Built source-only XML base | Volume I: 554 scans; volume II: 580 scans; 1,134 total | All internal page characters preserved; OCR remains unproofread |
| Preserved notes and apparatus | Remain on their source pages, including facing-page and continued notes | No guessed word-level attachments |
| Preserved Gemini-attributed material | Tiberius 43–47, separate XML supplement | Inherited prose unchanged; 43–44 are Latin in the source English column, 45–47 already English |
| Preserved inherited supplement note | Chapter 47 note separated and labelled | Original association recorded; attachment unverified |
| Built reading edition | [READ.html](READ.html), two-page display, source links and separate supplements | Browser preview blocked by local-file policy; embedded text validated |
| Preserved provenance inputs | Byte-identical OCR exports and legacy Tiberius XML in `sources/` | SHA-256 values recorded |
| Ran edition checks | 48 checks passed: source equality, supplement equality, page coverage and known discrepancies | No assertion of completed image proofreading or full external TEI schema validation |
| Added review inventory | [Review guide](review/REVIEW.md), [readable notes](review/NOTES.html), CSV review queues | Attribution and attachment kept distinct; all records remain unreviewed |
| Saved new edition alongside old files | `suet_loeb/clean_ocr_1970/` | Original top-level XML unchanged; no commit, publishing or viewer registration |

## Review counts

- 442 legacy note records lack an explicit `resp` attribution.
- 1204 footnote records have unresolved attachment evidence.
- 166 further records have candidate letter markers requiring verification.
- 1096 records use the generic attribution `editor`.
- 212 editorial-addition/date records are retained in a separate list.
- 14 confirmed source discrepancies and 89 broad source-coverage candidates are included.

These are overlapping record counts across XML versions, not unique-note totals. Every review row preserves its file and note number. No uncertain placement was promoted to a verified anchor.

## Files and verification

[file-inventory.csv](file-inventory.csv) lists package paths, byte sizes and SHA-256 checksums (excluding itself and this inventory). [validation.json](validation.json) records the source-edition checks. The [review guide](review/REVIEW.md) explains evidence limitations and how to record decisions.

Remaining editorial work is explicit: verify notes and markers against page images, resolve OCR errors with evidence, identify source notes that escaped the earlier heuristic audit, and encode chapter/section boundaries if required. The present page edition preserves the evidence needed for that work.
