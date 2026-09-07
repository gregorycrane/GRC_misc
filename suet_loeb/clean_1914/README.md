# Suetonius — Rolfe 1914 edition

Open **[READ.html](READ.html)**. This is now the main source edition. It uses the **1914 PDF**, with page images as the textual authority and fresh OCR available for searching and copying. The earlier 1970 OCR edition remains a separate comparison witness.

Both title pages of the supplied PDF read **MCMXIV**. The PDF contains **1,094 pages**, including both volumes, front matter, Latin and English, notes, indexes and blank leaves. Its embedded text is defective: ordinary extraction returns control characters instead of the words. Fresh OCR was therefore generated locally from rendered page images, rather than importing the old XML's potentially altered language.

The source images are displayed by default. The optional OCR is not fully proofread and can misread Greek, superscripts, marginal dates and damaged type. No lexical rewriting has been applied to it. The edition is page-based; it does not claim complete chapter/section encoding. PDF page numbers are the primary locators; printed page labels outside inspected leaves are based on sequence and should be checked against the image.

## Gemini supplements

**Tiberius 43–44** remain untranslated in the English column of the 1914 printing. Their inherited Gemini-attributed English translations are retained, unchanged and explicitly labelled, in a separate supplement.

**Chapters 45–47 already have Rolfe's English translation in 1914.** The inherited versions attributed to Gemini are preserved as collapsed archival alternatives in the reader and in `sources/inherited-gemini43-47.xml`. They do not replace Rolfe's English in the main edition. The old attribution claiming that all five chapters were untranslated is retained as historical metadata, with the error explained.

## Resolved notes and wording

The [PDF resolution record](review/PDF-RESOLUTIONS.md) records **58 visually verified note anchors**, **one rejected extra legacy note**, and **12 findings about wording or translation coverage**. The [readable note index](review/NOTES.html) links each decision to its page images.

These findings update **44 legacy note records**; **18 additional source-note records** are recorded without claiming a corresponding legacy match. Those figures overlap the 58 anchors plus one rejection because some notes occur in multiple legacy versions. All **14 previously confirmed missing-note cases** now have 1914 note-and-marker evidence.

Examples of resolved placements include Augustus 73.1 (after “house,”), Titus 8.2 (after “gestures,”), Titus 9.1 (after “pontifex maximus”), Titus 9.2 (after “offered him,”) and Titus 10.2 (after “divine.”). The three omitted Titus 7.3 notes attach to “amphitheatre,” “naumachia,” and “gladiators” at their printed markers. The unsupported extra after “second Nero” is excluded from the 1914 base.

The PDF also establishes genuine older readings such as “gifts,” “a huge body,” “Do your duty,” “as an adept in the art,” and “grand-daughter.” Other disputed Augustus wording agrees in both the 1914 PDF and 1970 OCR, so those legacy XML discrepancies are not explained by these two printing dates. The record does not claim to establish who caused each alteration.

## Review and preservation

See [INVENTORY.md](INVENTORY.md) for completed work and [review/REVIEW.md](review/REVIEW.md) for remaining questions. The complete prior note ledger is retained with separate fields for new 1914 decisions. A prior 1970 OCR excerpt is explicitly labelled as such, never represented as a transcription of this PDF.

The base images and OCR contain all captured notes in their page positions. Only the inspected anchors are marked verified. Missing personal attribution in an XML `resp` attribute is distinct from locating a note in Rolfe's printed edition; no personal authorship is inferred from a generic label.

The PDF itself is unchanged and remains at the user-supplied location, recorded with its SHA-256 checksum in `manifest.json`. Full-page image derivatives are included, so the reader does not need the original PDF to display the text. The legacy XML and the full inherited supplement are retained for provenance. No old top-level XML is overwritten, and no commit, publication or viewer registration is performed.

## Validation

`validation.json` records page coverage, image availability, OCR/XML/reader equality, supplement preservation, resolution-to-ledger consistency, and evidence image links. OCR confidence statistics in `review/ocr-quality-by-page.csv` help prioritize proofreading; they are not an error count or a certification of accuracy.

Browser-based visual testing was unavailable because local-file navigation was blocked by browser security policy. Source pages were rendered and inspected directly. Reader data and structure were checked locally. The remaining unproofread OCR and unresolved notes are explicitly recorded.
