# Selective 1606 apparatus in the existing Julius XML

The existing edition now uses TEI `<app>`, `<lem wit="#holland1899">`, and `<rdg wit="#holland1606">`. Both witnesses are declared in `listWit`, and `variantEncoding` declares internal parallel segmentation. The historical 1898 filename is retained; the base witness is described as the current 1899-based edition.

Six readings were checked directly against the local EEBO-TCP A13126 transcription:

| Existing citation | Base lemma | TCP reading |
|---|---|---|
| 1.1, annotation a | CAIUS CÆSAR | LVCIVS CAESAR |
| 1.1, numbered note 1 | began | begin |
| 1.3 | Masters | M with superscript rs |
| 81.1 | overthrew | ouerthew |
| 81.3 | Calpurnia | CALPVRINA |
| 81.4 | Decimus Brutus | DECIVS BRVTVS |

These are readings of the TCP transcription, not claims of direct image verification. In particular, `ouerthew` is classified as a transcription variant rather than an established authorial or printing change. This apparatus is selective, not a completed collation of all 1606 spellings, punctuation and damaged passages. No TCP gap is represented as an intentional omission, and no missing TCP wording has been silently reconstructed.

Two existing notes were relocated using explicit early inline letter markers:

- `holland-jc-note-002`: after **Father**, supported by TCP `lost his (a) Father`.
- `holland-jc-note-013`: after **domesticall retinue**, supported by TCP `in the (a) domesticall retinue`.

These are explicitly TCP-supported attachments; a corresponding later-print image check is not claimed. All note wording remains unchanged when the base lemma is selected. The earlier `jc-review` location inventory remains a historical snapshot from before these corrections; this directory records the superseding decisions.

All 89 chapter divisions, 187 section divisions, and 361 notes survive. Tests confirm that extracting the lemma reading preserves the complete base running text, preserves every existing note’s base text, and resolves every apparatus witness reference. Chapter/section boundaries were preserved, not newly certified against the Latin.

**Reader requirement:** a consumer must select `lem` (the default base edition) or the appropriate `rdg`; concatenating all descendant text would mix both readings. Existing viewer rendering was not tested in this pass. XML well-formedness and apparatus/reference integrity passed; full EpiDoc schema validation is not claimed.

Files:

- `original.xml`: exact pre-apparatus backup.
- `evidence.json`: every variant’s source XPath, original TCP line, quotation, source checksum, and the two anchor decisions.
- `changes.diff`: reviewable modifications.
- `validation.json`: preservation and apparatus checks.

The original TCP XML is unchanged.
