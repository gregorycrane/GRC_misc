# Work inventory — 1914 source edition

Updated 2026-09-07. This edition supersedes the 1970 OCR as the main reading base, at the user's request. The 1970 edition remains available separately.

| Completed work | Result |
|---|---|
| Verified the new source | Both volume title pages read MCMXIV; PDF has 1,094 pages |
| Rebuilt the base | All PDF pages rendered; fresh OCR generated locally; no old XML prose used as base |
| Preserved printed wording | Page images are the authority, with optional unproofread OCR |
| Preserved skipped translation supplements | Gemini-attributed Tiberius 43–44 remain separate and unchanged |
| Preserved remaining inherited material | Chapters 45–47 kept as archival alternatives; Rolfe English remains in main text |
| Verified note anchors | 58 printed note-to-text attachments recorded with image evidence |
| Rejected unsupported material | Extra Titus 7.1 cross-reference rejected for the 1914 base |
| Resolved previously missing-note cases | All 14 confirmed cases now have printed note and marker evidence |
| Updated earlier review records | 44 legacy records have PDF decisions; 18 source-note records have no asserted legacy match |
| Investigated language | 12 documented findings distinguish printing variants, unsupported recasting, and translation coverage |
| Preserved remaining review work | 1,170 unresolved-attachment records and 156 remaining letter-marker candidates |
| Preserved attribution questions | 442 records still lack an explicit legacy `resp`; source provenance and personal authorship kept distinct |
| Validated package | Source page/reader/XML consistency, supplement fidelity, evidence links and inventory checksums |

Counts are records, not unique printed notes. Some legacy editions repeat the same note. The 1,582-record legacy ledger represents 1,584 original note nodes, with two nested notes included in their parent record text.

## Package contents

- `READ.html`: self-contained reader interface, loading local page images.
- `pages/`: all 1,094 full-page images from the 1914 PDF.
- `edition/`: two OCR page editions, active Gemini supplement, and verified-anchor record in TEI XML.
- `sources/`: fresh OCR, unchanged legacy Tiberius XML, and the full inherited five-chapter supplement.
- `review/`: PDF decisions, wording findings, resolved records, remaining queues, source-only notes and OCR quality statistics.
- `manifest.json`: source PDF identity, checksum, edition policy and limitations.
- `validation.json`: results of the edition checks.
- `file-inventory.csv`: file paths, sizes and checksums, excluding itself.
- `tools/`: workspace-configured build, OCR and validation code for continuing this work.

## Remaining work

The complete OCR has not been proofread against images. Most note attachments remain unverified. Greek OCR, marginal dates, broken words and superscripts require particular care. Printed labels beyond inspected pages are sequence-based. No uninspected candidate has been promoted to a verified attachment, and no semantic guess is recorded as direct source evidence.
