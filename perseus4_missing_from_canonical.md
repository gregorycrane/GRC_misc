# Perseus 4 works not represented in the canonical repositories

Source inventory: `/Users/gcrane/github/GRC_misc/perseus4-classics-collection.xml`

Repositories compared:

- `/Users/gcrane/github/canonical-greekLit`
- `/Users/gcrane/github/canonical-latinLit`
- `/Users/gcrane/github/canonical_pdlrefwk`
- `/Users/gcrane/github/canonical-pdlrefwk`

## Result

The Perseus 4 collection contains 1,257 work-level records: 1,256 `Perseus:abo:` records plus the standalone *A History of the Giza Necropolis Volume I*. The collection header itself was not counted as a work.

- 1,111 have a canonical work match by legacy identifier, normalized title, or title within the same textgroup.
- 102 more are represented under a different CTS work structure.
- 44 do not have a corresponding work record in any of the three repositories.

The 102 structural matches are not migration gaps. They consist principally of Livy's individual books and summaries (82 records) represented by `urn:cts:latinLit:phi0914.phi001`, Quintilian's individual books and preface (13) represented by `urn:cts:latinLit:phi1002.phi001`, four separately listed halves of Plutarchan paired lives represented by two combined CTS works, the Suetonius aggregate represented by the individual Caesars, the Perseus Encyclopedia with a spelling discrepancy in the canonical title, and the Allen and Greenough Cicero omnibus represented by its component commentaries.

## Missing Greek and Latin primary works

| Legacy identifier | Author | Title |
|---|---|---|
| `Perseus:abo:bede,001` | Venerable Bede | *Historia Ecclesiastica Gentis Anglorum* |
| `Perseus:abo:phi,0119,021` | Plautus | *Vidularia* |
| `Perseus:abo:phi,0972,001f` | Petronius | *Fragments* |
| `Perseus:abo:phi,0972,001p` | Petronius | *Poems* |
| `Perseus:abo:stoa,0045,023` | Ausonius | *Periochae Iliadis* |
| `Perseus:abo:stoa,0045,024` | Ausonius | *Periochae Odyssiae* |
| `Perseus:abo:tlg,0527,017` | Old Testament | *1 Esdras* |
| `Perseus:abo:tlg,0527,020` | Old Testament | *Judith* |
| `Perseus:abo:tlg,0527,021` | Old Testament | *Tobit* |
| `Perseus:abo:tlg,0527,023` | Old Testament | *1 Maccabees* |
| `Perseus:abo:tlg,0527,024` | Old Testament | *2 Maccabees* |
| `Perseus:abo:tlg,0527,025` | Old Testament | *3 Maccabees* |
| `Perseus:abo:tlg,0527,026` | Old Testament | *4 Maccabees* |
| `Perseus:abo:tlg,0527,033` | Old Testament | *Wisdom* |
| `Perseus:abo:tlg,0527,034` | Old Testament | *Ecclesiasticus* |
| `Perseus:abo:tlg,0527,050` | Old Testament | *Baruch* |
| `Perseus:abo:tlg,0527,052` | Old Testament | *Letter of Jeremiah* |
| `Perseus:abo:tlg,0527,055` | Old Testament | *Susanna* |
| `Perseus:abo:tlg,0527,058` | Old Testament | *Bel and the Dragon* |

## Missing commentaries, lexica, grammars, and secondary works

| Legacy identifier | Author/editor | Title |
|---|---|---|
| `Perseus:abo:oclc,685208` | — | *Elegy and Iambus* |
| `Perseus:abo:phi,2349,005` | Servius | *Commentary on the Aeneid of Vergil* |
| `Perseus:abo:phi,2349,006` | Servius | *Commentary on the Eclogues of Vergil* |
| `Perseus:abo:phi,2349,007` | Servius | *Commentary on the Georgics of Vergil* |
| `Perseus:abo:sec,00002` | A. A. Howard | *Allen and Greenough's New Latin Grammar* |
| `Perseus:abo:sec,00003` | Bernhard Gerth | *Ausfuerliche Grammatik der griechischen Sprache* |
| `Perseus:abo:sec,00005` | William Watson Goodwin | *Syntax of the Moods and Tenses of the Greek Verb* |
| `Perseus:abo:sec,00006` | Thomas R. Martin | *An Overview of Classical Greek History from Mycenae to Alexander* |
| `Perseus:abo:sec,00008` | J. B. Greenough | *Commentary on Caesar's Gallic War* |
| `Perseus:abo:sec,00010` | Henry George Liddell | *A Greek-English Lexicon* |
| `Perseus:abo:sec,00011` | Alan Boegehold | *Three Court Days* |
| `Perseus:abo:sec,00012` | Diana Buitron-Oliver | *Attic Vase Painting in New England Collections* |
| `Perseus:abo:sec,00013` | Diana Buitron-Oliver | *Douris* |
| `Perseus:abo:sec,00014` | L. D. Caskey | *Attic Vase Paintings in the Museum of Fine Arts, Boston* |
| `Perseus:abo:sec,00016` | Carol L. Lawton | *Attic Document Reliefs* |
| `Perseus:abo:sec,00017` | Susan Matheson | *Polygnotos and His Group* |
| `Perseus:abo:sec,00019` | Jenifer Neils | *Phintias and Euthymides* |
| `Perseus:abo:sec,00020` | John H. Oakley | *The Achilles Painter* |
| `Perseus:abo:sec,00021` | Michael Padgett | *The Harrow Painter, with a Note on the Geras Painter* |
| `Perseus:abo:sec,00022` | Michael Padgett | *The Kleophrades Painter* |
| `Perseus:abo:sec,00023` | William J. Slater | *Lexicon to Pindar* |
| `Perseus:abo:sec,00024` | Andrew Stewart | *One Hundred Greek Sculptors* |
| `Perseus:abo:sec,00025` | Ellen Reeder Williams | *The Archaeological Collection of the Johns Hopkins University (Selections)* |
| `Perseus:abo:sec,00026` | Richard Stillwell | *The Princeton Encyclopedia of Classical Sites* |
| `Perseus:text:1999.04.0103` | — | *A History of the Giza Necropolis Volume I* |

## Scope and caveats

This is an inventory-level comparison, not a file-by-file textual audit. A work counts as present when a CTS work record exists, even if a particular Perseus 4 edition or translation may still be absent. Conversely, the Petronian *Fragments* and *Poems* are listed as gaps because they have distinct Perseus 4 work identifiers but no distinct canonical work records; the presence of `phi0972.phi001` (*Satyricon*) does not by itself establish that these two separately cataloged bodies of text were migrated.

Both reference-work repositories were checked. The underscore repository, `canonical_pdlrefwk`, contains 47 CTS work records. The hyphenated repository, `canonical-pdlrefwk`, contains 33. Their union adds no match for any of the 44 works listed above, so adding the hyphenated repository does not change the result.

The hyphenated repository does contain two work records not found in the underscore repository—Sidgwick's *Eumenides* and *A Dictionary of Greek and Roman Biography and Mythology*—but neither resolves one of the Perseus 4 gaps in this report. Its remaining work records overlap records already present in the underscore repository.
