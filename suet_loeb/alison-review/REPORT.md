# Augustus: state of the existing Alison XML

Reviewed 2026-09-07. Target: `phi1348.abo012.rolfe-eng1-alison.xml`. This is a review and incremental repair of the existing structured edition, not a new page-based edition. The source file’s original SHA-256 is `f2f1dc788a5a722a2f19ce1032679103d5eca504c394330c5f59e5cb8debd682`.

## Does it contain all footnotes?

**Complete coverage is not yet certified. This file already contains the ten Augustus notes previously reported missing from a different file, `suetonius.aug.loeb_eng1.xml`. Those omissions must not be attributed to this file.** No additional missing English explanatory footnote was confirmed in this focused pass. That is not proof that none remain.

The target has 212 note elements, represented by 211 top-level inventory records because one note contains another. This is not a count of 212 printed footnotes: it includes marginal dates, editorial comparisons, and notes combining printed text with later additions. Every note element has been preserved.

The ten already-restored notes concern passports (50.1), Dominus (53.1), morning calls (53.3), selection of senators (54.1), wills (56.1), benches and character testimony (existing XML 56.4), birthday dates (57.1), guilds (57.2), and the Genius (60.1). See `previously-missing-notes-now-confirmed-present.csv`. The source locations and printed markers had been checked on the PDF; the existing XML’s section numbering is retained, including 56.4. This pass does not certify that every section boundary agrees with an external CTS reference text.

The earlier automated comparison’s two “no-source-match” notes, **Pandataria** (65.3) and **Planasia** (65.4), are both printed on 1914 p. 222, with corresponding markers a and b on p. 223. These are real source notes, not grounds for deletion.

Some footnote text needed correction: “See not on Jul.” at 40.1 is printed “See note on Jul.”; “express the opinion freely” at 56.1 is printed “express their opinion freely.” Both are corrected. Every other existing note’s textual content remains unchanged, including earlier editorial annotations. No note has been relocated.

A definitive completeness claim still requires an independent enumeration of the printed explanatory notes across Augustus pp. 122–289, including continuations, followed by one-to-one comparison with this inventory. Matching the notes already in the XML cannot detect every omitted note, and OCR-only enumeration could itself miss notes. The Latin textual apparatus must be distinguished from English translation footnotes; the present English XML does not purport to reproduce the entire Latin apparatus.

## Where does its text differ?

There are three different situations, which must not be conflated.

| Passage | Incoming XML | 1914 evidence | Interpretation/action |
|---|---|---|---|
| 46.1, p. 201 | “legitimate sons or daughters”; “districts” | “worthy sons and daughters”; “city” | Incoming readings agree with the later OCR. Restored 1914 and retained exact prior readings in the change record. |
| 47.1, p. 201 | Recast sequence “others … he relieved; some … he rebuilt” | “he relieved others … rebuilt some …” | Restored the printed construction; later OCR also supports the printed construction. |
| 50.1, p. 205 | “sphinx” | “sphynx” | Source spelling restored; later witness has “sphinx”. |
| 51.1, p. 205 | “banishment” without “respectively” in the base | “banishment respectively” | Restored the missing word; retained the existing comparison noting the later additional “with”. |
| 51.2, p. 205 | “amongst other charges” | “among other charges” | Incoming wording agrees with the later witness; restored 1914. |
| 52.1, p. 207 | “most peremptorily … melted … dedicated” | “most emphatically … melting … dedicating” | Unexplained recasting relative to both witnesses; corrected. |
| 53.1, p. 207 | “applied to him”; “severely reprimanded” | “said of him”; “sharply reproved” | Corrected; later witness supports these readings too. |
| 54.1, p. 211 | “an ex-triumvir who was then in banishment” | “an old enemy of the emperor’s and at the time in banishment” | Restored 1914; later witness has a slightly different continuation, also describing an old enemy. |
| Existing XML 56.4, p. 213 | “an old soldier … facing an action for slander” | “one of his officers … accused of slander” | Restored 1914; later text says “one of his former officers”. |
| 60.1, p. 217 | “contribute jointly and finish at their own expense…” | “contribute the funds for finishing…” | Substantial recasting survives an earlier repair comment; restored the printed text. |
| 61.2, p. 217 | “the utmost devotion” | “marked devotion” | Corrected; later OCR agrees. |

The complete 31-item change inventory is in `CHANGES.md` and `changes.json`: 29 text corrections, one source label around an existing later addition, and one responsibility-attribute repair. This table is not the complete list.

Not every difference is an error. These examples were deliberately retained:

- Note at 2.1: 1914 begins “A term applied to the plebeian families…”, whereas the later witness starts more briefly. The XML’s longer form is appropriate to 1914.
- Note at 12.1: the abbreviated citations “Cic. Epist. 11. 20. 1” and “Vell. Paterc. 2. 62” are printed in 1914. Later expanded citations are not missing text from this base.
- Note at 45.2: 1914 includes the alternative interpretation “a contest in Greece.” Its absence from the later comparison excerpt does not make it an interpolation here.
- Note at 56.1: 1914 prints **Fulcinius Tiro**; the later witness has **Trio**. Preserve Tiro as the source reading.
- Note at 92.2: 1914 prints **de Div. 284**; the later witness has **2. 84**. Preserve and document the printed form rather than silently correcting the reference.

## Does it explain where and why it differs?

**Partly.** The original file has 70 comments recording missing notes, moved anchors, corrected retranslations, and section-boundary disputes. Several notes explicitly say “1951”. This evidence of prior work has all been preserved.

However, its original header names only 1914, calls correction “silent,” says “Gemini scan of PDF,” and records only “First version” on 2026-04-03. It does not summarize the extensive subsequent repair work or define a consistent policy for the mixture of witnesses. The reviewed header now identifies the actual 1914 PDF and the supplied 1970 impression/revised-1951 OCR, explains the remaining uncertainty, and links the correction inventory.

At 4.2, the Scott bibliography sentence is absent from the 1914 note ending on p. 127 but present in the later OCR. It is retained and now explicitly wrapped as a `seg type="later-edition-addition"` with a source pointer. An inherited comment mentions V1951, but the addition was not itself marked structurally before this pass.

Remaining limitations in attribution/documentation:

- “1951” labels are inherited claims. We have a 1970 impression identifying a 1951 revision, not a separately verified 1951 copy for every variant.
- Some editorial comparisons lack an edition label in their text, such as “fixed periods without interest” at 41.1 and the phrase at 101.3 beginning “well as his two paternal estates…”. See `later-edition-notes.csv`.
- At 7.2, “statuette” remains in the body where the 1914 OCR reads “bust”; an existing comment identifies the V1951 difference. It remains for further source review, rather than being silently homogenized in this bounded pass.
- Most notes have generic `resp="editor"`, which does not by itself identify their author. Responsibility labels `grc` and `GRC` are not normalized wholesale. The clear `n="grc"` typo has been corrected to `resp="grc"`.
- The passport note at 50.1 has no explicit `resp`. Its printed source is known; lack of a responsibility attribute is not lack of source evidence. It is the one remaining top-level record in `unattributed-notes.csv`.
- Earlier comments document repairs but are not a complete dated editorial history. We do not infer who caused an unsupported rewording.

## Deliverables and remaining work

- Reviewed XML: same filename; preserves all 101 chapters, 242 sections, 212 note elements, and 70 comments.
- `original.xml`: exact incoming copy, for recovery and comparison.
- `changes.diff`, `CHANGES.md`, `changes.json`: exact, reviewable modifications.
- `notes.csv`: all 211 top-level records, original/reviewed wording, citation, line numbers, and review state.
- `existing-comments.csv`, `later-edition-notes.csv`, `unattributed-notes.csv`: separate editorial review inventories.
- `1914-main-text-candidates.csv` and `1970-main-text-candidates.csv`: page-by-page comparisons of the incoming XML. These intentionally retain OCR noise, headings, hyphenation differences, and unmatched note text. They are review candidates, not counts of errors, and are not regenerated against the cleaned XML.
- `validation.json`: well-formed XML; citation structure, comments, note counts and note locations preserved; only the two declared footnotes change textual content. Full EpiDoc schema validation and full proofreading are not claimed.

The next work should continue on this XML: certify source-footnote coverage, review the remaining comparison candidates, make edition attributions consistent, and check disputed section boundaries against the project’s citation reference. The page images are evidence for that work, not a replacement edition.
