# Suetonius: Rolfe source edition with Gemini-attributed supplements

Open **READ.html** for the reading edition. It works as a standalone local file, with volume, work and page navigation, a choice of flowing text or OCR lines, and a separate supplement view.

See [the inventory of completed work](INVENTORY.md) and [the note review guide](review/REVIEW.md). The review package distinguishes missing author labels from unresolved note attachments and includes editable review lists with source evidence.

This is a conservative **page-based edition**, not a fully proofread chapter-and-section edition. It provides a source-faithful replacement base for the mixed wording in the previous XML. All 1,134 scan pages are included: 554 in volume I and 580 in volume II, including blank scans, Latin, English, introductions, apparatus, footnotes, indexes and end matter.

## Base text

The base is exclusively the two OCR exports supplied by Gregory Crane. Both scanned title pages identify the **1970 printing**; volume I also records **“Revised and Reprinted 1951.”** The export catalogue's 1913–1914 date is not the date of these printings.

No words, punctuation, apparent footnote markers or OCR debris have been corrected or substituted from the old XML. Source-page blocks retain their internal characters and line breaks. The only changes are removal of export page-delimiter lines and form-feed characters, and trimming of whitespace at page boundaries. The two original files are also retained byte for byte, including their export metadata.

The flowing display changes whitespace presentation only. Ambiguous line-end hyphens remain. Running headings, marginal numbers and uncertain OCR remain in the source transcription. They have not been guessed away as noise. Every page is explicitly marked `unproofread-ocr` in the XML.

## Notes

All note text captured in the supplied OCR remains on its source page, together with the surrounding text and apparatus. English footnotes often appear under the facing Latin page; both pages are displayed together. No existing XML note attachment is treated as proof of its printed location, and no new word-level attachment is inferred.

This restores the OCR evidence omitted by the old XML, including the three Titus notes on volume II page 330 and Caligula's “gift-tokens” marker debris on volume I page 431. It also avoids importing the unsupported additional note after “second Nero” from the old Titus XML. Source notes are not reworded to match the previous XML: for example, the note on volume II page 322 retains “Cf.” rather than “See”.

Preserving every OCR page establishes that this edition loses no notes **present in that OCR**. It does not establish that the OCR captured every printed note, nor certify the attachment of every note to a word. Those questions still require image-based proofreading. Continued notes remain on their separate source pages rather than being joined speculatively.

## Gemini-attributed supplements

The legacy Tiberius XML explicitly attributes chapters **43–47** to Gemini 3. All five chapters are retained in a separate supplement, with their inherited prose unchanged. The original XML and its attribution are archived for comparison.

The legacy attribution incorrectly says all five chapters were untranslated in the English text. In the supplied 1970 OCR, **43–44 are Latin in the English column, while 45–47 are already English**. The reader labels this distinction and preserves the entire inherited block instead of silently discarding or reassigning part of it. “Gemini-attributed” reports the existing attribution; it does not independently certify the authorship of every sentence.

The inherited editorial note in chapter 47 is retained separately as an unverified legacy note. Its old section association is recorded, but its word-level attachment is not endorsed. Original page-break markup remains available in the archived legacy XML. No new translation was generated.

Other legacy editorial notes discussing 1951 readings are not classified as Gemini supplements. They are not incorporated into the new OCR base. The existing repository XML files remain available independently.

## Files

| File | Contents |
|---|---|
| `READ.html` | Self-contained reading edition; no server or external scripts needed |
| `edition/suetonius.rolfe1970.volume1.ocr.xml` | Complete volume I source-page transcription |
| `edition/suetonius.rolfe1970.volume2.ocr.xml` | Complete volume II source-page transcription |
| `edition/suetonius.tiberius.gemini-supplement.xml` | Explicitly attributed chapters 43–47, with legacy notes separated |
| `sources/` | Unmodified OCR exports and the legacy Tiberius XML |
| `manifest.json` | Source checksums, provenance, transformation policy and limitations |
| `validation.json` | Fidelity and regression-check results |
| `tools/` | Reproducible builder, reader template and independent validator |

The XML uses the TEI namespace. Source pages have stable IDs such as `v1-s391` and a printed-page label plus scan link. No new CTS chapter/section citation scheme is asserted for the OCR base. Shared pages between Lives occur once, without speculative text splitting.

## Validation

The independent validator passes 48 checks, including equality of every source-page character after the declared boundary normalization, all source checksums and page labels, unchanged supplement prose, preservation of inherited supplement notes, separation of supplements from the OCR base, reader/XML equality and regressions for previously identified discrepancies. XML well-formedness and unique IDs are checked; full external TEI schema validation is not claimed.

Browser preview could not be exercised because the browser's security policy blocked access to the local HTML file. The reader's embedded text was verified against the XML; visual and interactive browser testing remains unperformed.

To rebuild from inside this directory with Python 3 and lxml installed:

```sh
python3 tools/build.py --sources sources --legacy sources/suetonius.tib.loeb_eng1.legacy.xml --output ../suetonius-rebuilt
python3 tools/validate.py ../suetonius-rebuilt
```

This edition is installed alongside the old XML rather than replacing it. No repository commit or viewer registration is included.
