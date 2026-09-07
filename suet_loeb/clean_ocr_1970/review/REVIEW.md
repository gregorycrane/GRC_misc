# Note review guide

Start with [the readable note list](NOTES.html). The CSV lists contain the same evidence with blank reviewer, decision, verified-anchor and evidence columns for recording decisions.

“Unattributed” and “unattached” are different. The first list identifies missing explicit `resp` attributes in legacy XML; it does **not** prove that the printed note has an unknown author. The second identifies unresolved attachment evidence. The generic label `editor` is recorded separately and is not silently expanded to a named person.

| Review list | Records | Purpose |
|---|---:|---|
| [Unattributed notes](unattributed-notes.csv) | 442 | No explicit author/responsibility label in legacy XML |
| [Unresolved attachments](unresolved-attachments.csv) | 1204 | No candidate letter-marker attachment established; includes uncertain OCR gaps and unmatched notes |
| [Marker candidates](marker-candidates.csv) | 166 | A letter marker was detected; source-note correspondence and placement still require review |
| [Generic editor attributions](generic-editor-attributions.csv) | 1096 | `resp="editor"`, without identifying a person |
| [Editorial additions and dates](editorial-additions-and-dates.csv) | 212 | Kept outside the footnote-attachment queue; not discarded |
| [All legacy notes](all-legacy-notes.csv) | 1582 | Complete prior audit ledger with stable review IDs |
| [Confirmed source discrepancies](confirmed-source-discrepancies.csv) | 14 | Manually identified source notes absent from the corresponding old XML; retained in the new page edition |
| [Broad source-coverage candidates](coverage-review.json) | 89 | Heuristic candidates, including possible body text and combined notes; not confirmed missing notes |

These lists overlap. Counts are XML records across 17 files, including alternative versions, **not counts of unique printed notes**. The prior audit represented 1,584 actual note nodes as 1,582 top-level records; two nested notes remain inside their parent record's text.

No item is marked approved. Even letter-marker candidates require checking that the mark belongs to this note. The OCR match may be partial, clipped or on the wrong page; follow the complete-page link and inspect the image before accepting it. The displayed left/right attachment context is normalized legacy text, not a quotation of the OCR.

Review procedure:

1. Compare the complete source note and its marker with the scan, including the facing page and any continuation.
2. Record an attachment only when the marker or other direct source evidence establishes it. Do not use semantic plausibility alone.
3. Record any wording difference verbatim; distinguish OCR error, edition difference and editorial addition.
4. Enter the reviewer, decision, exact anchor and evidence in the CSV. Leave unresolved items explicitly unresolved.

All notes present in the OCR remain in the page edition, including ones not recognized by these candidate lists. This review package is **not an exhaustive segmentation of every printed/source note**. It combines the prior legacy-note audit with source-only coverage candidates, without inventing missing matches or attachments.
