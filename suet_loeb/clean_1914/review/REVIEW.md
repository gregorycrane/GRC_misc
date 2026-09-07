# Review guide — 1914 edition

Start with the [verified PDF decisions](NOTES.html) or the [full resolution record](PDF-RESOLUTIONS.md). These record the exact printed anchor, note marker, source page and reason for each decision.

| List | Records | Meaning |
|---|---:|---|
| [All legacy notes](all-legacy-notes.csv) | 1,582 | Complete earlier ledger, with explicit 1914 decision fields |
| [Resolved legacy records](resolved-legacy-records.csv) | 44 | Notes whose placement or rejection is now supported by the PDF |
| [Newly located source notes](newly-located-source-notes.csv) | 18 | Verified source notes without an asserted corresponding legacy record |
| [Remaining unresolved attachments](remaining-unresolved-attachments.csv) | 1,170 | No verified anchor and no prior letter-marker candidate |
| [Remaining marker candidates](remaining-marker-candidates.csv) | 156 | Earlier OCR letter-marker candidates still needing image verification |
| [Unattributed notes](unattributed-notes.csv) | 442 | No explicit `resp` label in the legacy XML; this is not the same as missing placement |
| [Previously confirmed source discrepancies](confirmed-source-discrepancies.csv) | 14 | All now linked to a visually verified 1914 note and marker |
| [Broad coverage candidates](coverage-review.json) | 89 | Earlier heuristic candidates, including possible false positives; preserved for further work |
| [OCR quality by page](ocr-quality-by-page.csv) | 1,094 | Fresh OCR confidence statistics to help prioritize proofreading |

Lists overlap and include repeated notes in alternative XML files. Counts must not be added as unique-note totals.

The `source_excerpt` fields in the legacy ledger still describe the **1970 Hathi OCR audit**, as explicitly labelled in the new `comparison_excerpt_witness` field. The new PDF fields describe **1914**. Prior OCR matching scores remain candidate evidence only. Old relative edition links have been cleared rather than silently redirected to the wrong witness.

`Verified in 1914 PDF` resolves the recorded attachment in this witness, not necessarily every spelling in the old XML note. Complete printed notes remain visible on the linked images. Note identifiers in the decision list are descriptive excerpts, not replacement full-note transcriptions. Personal note authorship is not inferred from a generic `editor` label or missing `resp` attribute.

To review a remaining item, compare the full note and printed marker on the image, including any facing-page or continued note. Record exact evidence and a decision in the CSV. If the marker is not established, leave the attachment unresolved. Neither a plausible meaning nor an automatic OCR match is sufficient.
