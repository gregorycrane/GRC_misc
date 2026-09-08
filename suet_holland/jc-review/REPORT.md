# Holland’s Julius Caesar: XML cleanup and state of work

Reviewed 2026-09-07. This work updates the existing `suetonius.jc.holland1898-section.xml`; it does not replace its chapter/section structure or start another edition.

## Result

- All **89 chapters, 187 sections, and 361 notes** retained: **212 numbered footnotes** and **149 lettered annotations**.
- **14 corrections**: 12 wording/numeral changes and two printed note-number corrections. The wording changes affect the main text and seven existing notes.
- Stable XML IDs added to the notes, so every inventory record points to an identifiable element.
- **192 existing note locations supported by OCR marker evidence**; **169 unresolved**. None was moved on the basis of a semantic guess.
- Original XML preserved byte-for-byte as `original.xml`; exact changes recorded in `changes.json`, `CHANGES.md`, and `changes.diff`.

## Textual basis

The two supplied volume-I exports are the California `uc1.b3114462` and Harvard `hvd.32044024292195` witnesses. Both catalogue descriptions and title-page OCR identify **D. Nutt, 1899**, whereas the incoming XML called the edition 1898. The header now records this discrepancy and the two actual comparison witnesses. The filename is retained. The volume-II exports are inventoried for subsequent work but were not used to compare Julius Caesar.

The main text was collated across its full 66-page range, pp. 15–80. The lettered annotations were searched separately in the rear annotation sequence, rather than treated as intrusions into the main text. Numbered footnotes were compared on their source pages and adjacent pages.

Both exports sometimes share OCR defects. Their agreement is corroboration within the supplied text, not proof of independent OCR recognition or a direct check of the printed image.

## Corrections

Examples:

| Existing XML | OCR-supported reading | Location |
|---|---|---|
| “against him, him, and” | “against him, and” | 73.1, p. 66 |
| “indignation thereat” | “indignation therat” | 78.2, p. 71 |
| “a written scrole, of the Conspiratours names, and those that…” | “a written pamphlet, which layd open the conspiracie, and who they…” | 81.4, p. 75 |
| “Young gentlemen or noble bloud” | “Young gentlemen of noble bloud” | annotation at 2.1, p. 231 |
| “fusces” | “fasces” | annotation at 20.1, p. 236 |
| “Eneid”; “Meta” | “Æneid”; “Metæ” | annotations at 39.2–3, p. 241 |
| “dubicæ” | “dubiæ” | annotation at 45.1, p. 242 |
| “Detulerunt” | “Detulerant” | footnote at 84.3, p. 78 |
| “judgent”; “Soveraie” | “judgement”; “Soveraine” | footnote at 89.1, p. 80 |

The note “Jugulum, or the chanell bone” is numbered **6**, not 5; “Where he was murdered” is numbered **4**, not 2. Both remain at their existing text positions.

At **41.3**, the incoming XML gives `320000`. California OCR gives `3,020,000` and Harvard gives `3020000`. The cleaned XML follows their shared digit sequence and records it as `<num cert="low">3,020,000</num>` with both source pointers. **Checking the image remains necessary**: this is fidelity to the supplied OCR, not a claim that this number is historically correct or that the OCR faithfully captured the print. The previous number remains in the change inventory and backup.

## Notes continued across pages or interleaved by OCR

The text of a note need not be split merely because its source crosses a page. These cases illustrate why blindly replacing a note with a contiguous OCR excerpt would damage it:

- Annotation 16.1: “Em-brodered” crosses pp. 234–235. The XML correctly combines the word and the note.
- Annotation 45.1 continues across pp. 242–243. A California library stamp interrupts one OCR stream; it is not part of the annotation.
- The note at 3.1 includes “named Isauri, whom he subdued,” although OCR reading order separates that continuation.
- “Thus Turnebus…” at 48.1: OCR puts “2 Thus” before the preceding note. Do not substitute the adjacent word “made” for “Thus”.
- At 55.3, another footnote is interleaved between “to” and “Metellus.” The XML’s joined note is retained.
- At 59.1 and 67.2, “Or” and “And” have been displaced to the ends of OCR footnote blocks. The adjacent words “word” and “discipline” are not replacements.
- At 78.1, “that which brought him to” survives later in the same OCR block. It is not an XML addition and has not been deleted.
- Consecutive verse elements are separate verse lines. They are treated as separated words during collation; apparent joins such as `malorumFacta` are not grounds for changing the poem.

See `combined-and-reordered-notes.csv` and the raw excerpts in `source-excerpts.json`.

## What is and is not verified

The inventory covers **all 361 existing notes**. Before correction, **301** matched the normalized word sequence in both OCR witnesses and **324** matched at least one. These figures concern word sequences, not punctuation, capitalization, or the correctness of the printed text. The other 37 records are retained in `notes-needing-text-review.csv`, with corrections and reading-order explanations recorded where applicable. These are baseline review counts, not a count of 37 remaining errors.

The location check requires surviving marker evidence between matching surrounding words. It does not promote a location merely because a note’s subject appears relevant. `note-locations.csv` records the actual intervening OCR and context from each witness; `unresolved-note-locations.csv` contains the remaining 169 cases. “OCR marker supports existing location” is narrower than image verification.

The first lettered annotation at 1.1, describing Caius Caesar’s death, currently follows “Flamen Dialis” along with the annotation about the priesthood. Its marker has not been recovered sufficiently to verify that placement. It remains an explicit review case, not an inferred relocation.

No new missing note was confirmed by this pass. This does **not** certify that the XML includes every source note: a definitive completeness check requires an independent enumeration of the printed footnotes and annotation entries, including markers omitted by OCR.

**Character-for-character identity is not yet certified.** The comparison handles line-wrap joins, case-folding and tokenization to locate differences; it does not prove identical punctuation, capitalization, ligatures or spacing. Uncertain Greek/Latin OCR, ligature substitutions, numerals, marginal dates and some page-break positions remain to be checked. Shared OCR defects are not automatically copied into the XML. No archaic wording is modernized for readability.

## Files and validation

- Reviewed XML: same existing filename; original preserved as `original.xml`.
- `CHANGES.md`, `changes.json`, `changes.diff`: exact corrections and source pages.
- `notes.csv`: all note IDs, citations, original and reviewed text, marker numbers, comparison evidence, and review decisions.
- `note-locations.csv`, `unresolved-note-locations.csv`: anchor evidence and unresolved cases.
- `notes-needing-text-review.csv`, `combined-and-reordered-notes.csv`: textual review queues and continuation decisions.
- `main-text-comparison.csv`, `note-comparison-details.json`: incoming-XML collation candidates. Headers, OCR debris and markers can produce false differences; these are not an error list.
- `source-excerpts.json`: raw OCR evidence, separate from normalized matching strings.
- `manifest.json`: source identities and checksums, including the unused volume-II witnesses.
- `validation.json`: well-formed XML; preserved chapter/section divisions, page-marker sequence, comments and note count; no note relocations; only the seven declared notes change their wording. Full TEI schema validation is not claimed.
- `tools/`: workspace-configured collation and cleanup code.

Continue from this XML and its outstanding review queues. The priority is uncertain anchors and exact punctuation/case comparison, followed by independent source-note coverage and disputed page breaks.
