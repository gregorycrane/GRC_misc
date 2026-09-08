# Suetonius: Holland and Rolfe corpus review and installation

The existing structured XML remains the basis of this edition. This pass covers all twelve lives in Holland and all twelve English Rolfe lives. It does not replace them with page-based OCR. Augustus uses the previously reviewed Alison XML. Existing canonical English and Latin files are registered independently and have not been edited.

## Changes

The change inventory records 41 curated operations, in addition to the Julius and Augustus work completed earlier. Routine metadata and stable note identifiers are recorded by the file inventories and original copies.

- Restored Holland Tiberius 43.2–46.1 from both supplied OCR witnesses, printed pages 205–206. Five footnotes have surviving markers; three further notes are preserved in explicitly unattached back matter. The annotation formerly following Spintriae now follows the surviving `Caprineus1a` marker. The OCR reading `millian` is retained without conjectural correction.
- Removed the first, incomplete duplicates of Holland Nero chapters 11 and 22. The fuller second copies agree with the OCR sequence. Removed copies, including their notes, are archived separately rather than discarded.
- Repaired Holland Titus’s chapter offset: the existing education passage is now 2.1, and following chapters are 3–11. Repaired the Vespasian offset by separating the existing liberality passage as 17.1 and numbering subsequent chapters 18–25. No words were added in these citation repairs.
- Converted explicit section milestones in Holland Nero 9–10 and Claudius 39 into section divisions with their existing numbers. Removed inherited `[cite: ...]` placeholders, which are LLM citation debris, not printed footnotes.
- Retained Julius’s six 1606 variants and added one selective opening-passage variant to each other Holland life. These 17 readings are labelled as TCP transcription evidence; this is not an exhaustive apparatus. TCP gaps have not been promoted to readings. In PMV the later lemma remains in the running text and the early reading is available through the apparatus.
- Restored seven Rolfe notes whose printed markers were verified in the earlier 1914 PDF review: Caligula 18.2; Tiberius 46.1, the saying in 59, and 60.1; Titus 7.3 (three notes). Reattached Caligula’s note on the thin legs to 50.1. Corrected three Titus cross-references and archived the unsupported extra note at 7.1.
- Corrected Rolfe Nero’s second 31.3 to 31.4, matching the hidden-treasure passage in the Latin. Retained and labelled Gemini supplements for Tiberius 43–44; corrected the inherited claim that 45–47 lacked a Rolfe translation. Existing later-edition notes remain labelled as edition variants.

## What is and is not verified

All 24 source files underwent automated note and section comparison with the supplied OCR. The 6,028 comparison records are evidence for review, not a claim of full proofreading. Word matching folds case and joins page-end hyphens for comparison; it does **not** establish character-for-character identity. Greek, page continuations, interleaved notes, and OCR debris still require attention. No wholesale wording correction was made from fuzzy matches.

There is no warranted claim that every printed note is present or correctly located. The notes inventory includes the text of all retained notes; the unresolved-location inventory deliberately includes uncertain cases. Generic `resp="editor"` is not treated as personal attribution. Previously image-verified decisions are identified in the change inventory; automated marker support is a separate, weaker category. An unresolved entry is not itself proof of a misplaced note.

All 24 reviewed editions now have the same chapter/section citation keys as the canonical Ihm Latin (`perseus-lat2`). The 2,464 English sections were reviewed by comparing their openings against the Latin, with fuller passage examination where the openings disagreed. Restructuring affected 125 chapters in 21 files; cross-chapter repairs were also made. Altogether 281 section divisions have changed contents relative to the pre-alignment stage. Three editions needed no further boundary edits in this pass. Matching counts alone was not used as evidence of alignment.

The alignment repair preserves every non-whitespace character of the running translation, the full content and order of all notes, and every body note's position relative to the running text. These invariants pass for all 24 files. A separate source correction restored the omitted 74-word end of Holland Nero 10.2: both volume-II OCR witnesses agree, printed page 106. That restoration is labelled in TEI and recorded in `changes.json`; it precedes the alignment baseline. The original incoming XML is retained separately.

English clause order sometimes differs from Latin: for example Nero 35.4–5 divides the Rufrius Crispinus sentence within the Latin. The corresponding English boundary is placed at “being yet of tender yeeres” in Holland and “a mere boy” in Rolfe, preserving the translators' ordering rather than rewriting it. Alignment uses Ihm's sections; different underlying readings and omitted or supplemented translation remain textual issues, separately documented. The canonical Thomson versions are often chapter-only and retain their actual granularity. The existing canonical editions have not been rewritten.


## Review files

- `changes.json`: concrete corrections, removals, restorations, and source evidence.
- `inventory.csv`: 24 reviewed files, section/note/apparatus counts and hashes.
- `registered-files.csv`: all 61 PMV registry entries, destination/source paths and hashes.
- `notes.csv`: retained note text and attribution/location status.
- `unattributed-notes.csv`: absent or generic editor attributions.
- `unresolved-note-locations.csv`: anchors still requiring review or consultation of the curated change evidence.
- `*.audit.json`: per-note and per-section OCR matches, differences, and surviving marker context against the incoming XML. These remain an audit of the originals, not silently recomputed to erase corrected differences.
- `citation-review.json`: citation-key checks against the Latin; no differences remain.
- `section-alignment.csv`: all 2,464 English sections with Latin and English openings/endings and source paths.
- `changed-section-alignment.csv`: the 281 divisions whose contents changed.
- `alignment-changes.json`, `alignment-summary.json`, `alignment-preservation.json`: boundary decisions, per-life counts, and preservation checks.
- `before-alignment/`: the source-cleaned baseline used for the boundary repairs, distinct from the incoming originals.
- `originals/`: exact incoming XML backups. `nero-duplicate-11.xml` and `nero-duplicate-22.xml`: removed duplicate blocks.
- `installation.json`, `parser-validation.json`, `validation.json`: installation and validation records.

The installed corpus uses distinct `holland1899-eng1` and `rolfe1914review-eng1` version identifiers, leaving inherited canonical Rolfe versions available for comparison. Each work has CTS metadata and chapter/section citation declarations. Source dates and the limited review status are stated in the headers.

## PMV compilation

The corpus registry contains 61 Suetonius versions: the 24 reviewed Holland/Rolfe files and the 37 existing canonical English/Latin files. Suetonius and all twelve work titles are installed in the pipeline name tables.

The compiled-data audit exposed a pre-existing section fallback: when an edition lacked another edition’s section key, ingestion copied that edition’s section 1 to the missing key. Suetonius now enables `strict_section_alignment` to prevent this false alignment. Other works retain their prior behavior. The regression suite passes all 41 tests, including the new strict-alignment and compatibility cases. `compiled-validation.json` records the final comparison of compiled Suetonius rows with the XML parser output; `pmv-build.log` records the twelve-work rebuild.

The same compiled check found five Augustus Latin sections encoded entirely with `<l>` elements (53.2, 53.3, 70.2, 98.5, 99.2). The former paragraph-only parser skipped them. For strictly aligned works, the parser now retains paragraph, line, verse-group, quotation, and anonymous-block contents in document order, without rendering nested blocks twice. A regression test covers both a line-only section and mixed prose/verse. Source Latin XML was not changed.
