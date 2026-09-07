#!/usr/bin/env python3
"""Export review queues without converting audit candidates into editorial facts."""
import csv, hashlib, html, json, shutil, sys
from collections import Counter
from pathlib import Path

out=Path(sys.argv[1]); audit=Path(sys.argv[2]); repo=Path('/Users/gcrane/github/GRC_misc/suet_loeb')
dest=out/'review';dest.mkdir(exist_ok=True)
data=json.loads((audit/'audit.json').read_text())
lookup={(f['file'],str(n['index'])):(f,n) for f in data for n in f['notes']}
# Stop if the audit no longer describes the repository being inventoried.
for f in data:
    assert hashlib.sha256((repo/f['file']).read_bytes()).hexdigest()==f['sha256'],f['file']
rows=list(csv.DictReader((audit/'note-ledger.csv').open(encoding='utf-8-sig')))
for r in rows:
    f,n=lookup[(r['file'],r['note_index'])]
    r['review_id']='L%02d-N%04d'%(data.index(f)+1,int(r['note_index']))
    r['legacy_resp']=n['attributes'].get('resp','')
    r['author_attribution_status']='No explicit resp in legacy XML' if not r['legacy_resp'] else ('Generic editor; no personal name asserted' if r['legacy_resp']=='editor' else 'Explicit legacy label: '+r['legacy_resp'])
    r['source_match_caution']='Candidate OCR match only; excerpt may be clipped. Verify the complete source page.' if r['source_sequence'] else 'No source-page match established by the audit.'
    r['edition_page_link']='../READ.html#v%s-s%s'%(r['source_volume'],r['source_sequence']) if r['source_sequence'] else ''
    r['review_status']='Unreviewed'
    r['reviewer']='';r['decision']='';r['verified_anchor']='';r['evidence']=''
unattributed=[r for r in rows if not r['legacy_resp']]
generic=[r for r in rows if r['legacy_resp']=='editor']
footnotes=[r for r in rows if r['kind_or_comparison'] not in ('documented-editorial-addition','marginal-date-review')]
unplaced=[r for r in footnotes if r['anchor_status']!='letter-marker-at-anchor']
markers=[r for r in footnotes if r['anchor_status']=='letter-marker-at-anchor']
other=[r for r in rows if r not in footnotes]
def writecsv(name,records,fields=None):
    with (dest/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(records[0]));w.writeheader();w.writerows(records)
for name,rr in [('all-legacy-notes.csv',rows),('unattributed-notes.csv',unattributed),('unresolved-attachments.csv',unplaced),('marker-candidates.csv',markers),('generic-editor-attributions.csv',generic),('editorial-additions-and-dates.csv',other)]:
    writecsv(name,rr)
for name in ['confirmed-source-discrepancies.csv','coverage-review.json']:
    shutil.copy2(audit/name,dest/name)
htmlparts=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Suetonius note review</title><style>body{font:17px/1.6 Georgia,serif;max-width:1050px;margin:40px auto;padding:0 24px;color:#252a28;background:#faf8f2}h1,h2,h3{font-weight:normal}details{border:1px solid #cdd3c9;padding:12px 18px;margin:10px 0;background:#fffdf8}summary{cursor:pointer}pre{white-space:pre-wrap;font:15px/1.6 Georgia,serif}small,nav{font:14px/1.5 system-ui,sans-serif}a{color:#315d49}.warning{background:#eef1e9;padding:18px}</style><h1>Suetonius: note review</h1><p class="warning">These are review records, not certified note placements. Source matches and OCR markers are evidence to inspect. Repeated records from different XML versions have not been merged.</p><nav><a href="#unattributed">No explicit author attribution</a> · <a href="#unplaced">Unresolved attachments</a> · <a href="#markers">Marker candidates</a> · <a href="REVIEW.md">Review guide and additional lists</a></nav>']
esc=html.escape
for ident,title,rr in [('unattributed','No explicit author attribution',unattributed),('unplaced','Unresolved attachments',unplaced),('markers','Marker candidates — still require verification',markers)]:
    htmlparts.append('<h2 id="%s">%s (%d records)</h2>'%(ident,title,len(rr)))
    for r in rr:
        htmlparts.append('<details><summary>%s · %s · %s · %s</summary>'%tuple(esc(x) for x in [r['review_id'],r['file'],r['reference'] or 'reference unresolved',r['anchor_status']]))
        htmlparts.append('<small>Legacy attribution: %s. Text comparison: %s. XML line %s.</small><h3>Legacy note text</h3><pre>%s</pre>'%tuple(esc(x) for x in [r['author_attribution_status'],r['kind_or_comparison'],r['xml_line'],r['xml_note']]))
        htmlparts.append('<h3>Legacy attachment context — not an approved placement</h3><pre>%s ⟦NOTE⟧ %s</pre>'%(esc(r['xml_anchor_left']),esc(r['xml_anchor_right'])))
        htmlparts.append('<h3>Candidate OCR evidence</h3><p>%s</p><pre>%s</pre><p>Raw gap at candidate anchor: <code>%s</code></p>'%(esc(r['source_match_caution']),esc(r['source_excerpt'] or '[No matched excerpt]'),esc(r['ocr_anchor_gaps'] or '[No recovered gap]')))
        if r['source_sequence']:
            htmlparts.append('<p>Volume %s, printed page %s, scan %s. <a href="%s">Complete source page in edition</a> · <a href="%s">Scan image</a></p>'%tuple(esc(x,quote=True) for x in [r['source_volume'],r['source_page'],r['source_sequence'],r['edition_page_link'],r['source_url']]))
        htmlparts.append('</details>')
htmlparts.append('</html>');(dest/'NOTES.html').write_text('\n'.join(htmlparts))
counts={'legacy_records':len(rows),'without_explicit_resp':len(unattributed),'generic_editor_label':len(generic),'unresolved_attachments':len(unplaced),'letter_marker_candidates':len(markers),'editorial_additions_or_dates':len(other),'confirmed_source_discrepancies':14,'broad_coverage_candidates':len(json.loads((dest/'coverage-review.json').read_text()))}
(dest/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
(dest/'REVIEW.md').write_text('''# Note review guide

Start with [the readable note list](NOTES.html). The CSV lists contain the same evidence with blank reviewer, decision, verified-anchor and evidence columns for recording decisions.

“Unattributed” and “unattached” are different. The first list identifies missing explicit `resp` attributes in legacy XML; it does **not** prove that the printed note has an unknown author. The second identifies unresolved attachment evidence. The generic label `editor` is recorded separately and is not silently expanded to a named person.

| Review list | Records | Purpose |
|---|---:|---|
| [Unattributed notes](unattributed-notes.csv) | %d | No explicit author/responsibility label in legacy XML |
| [Unresolved attachments](unresolved-attachments.csv) | %d | No candidate letter-marker attachment established; includes uncertain OCR gaps and unmatched notes |
| [Marker candidates](marker-candidates.csv) | %d | A letter marker was detected; source-note correspondence and placement still require review |
| [Generic editor attributions](generic-editor-attributions.csv) | %d | `resp="editor"`, without identifying a person |
| [Editorial additions and dates](editorial-additions-and-dates.csv) | %d | Kept outside the footnote-attachment queue; not discarded |
| [All legacy notes](all-legacy-notes.csv) | %d | Complete prior audit ledger with stable review IDs |
| [Confirmed source discrepancies](confirmed-source-discrepancies.csv) | 14 | Manually identified source notes absent from the corresponding old XML; retained in the new page edition |
| [Broad source-coverage candidates](coverage-review.json) | %d | Heuristic candidates, including possible body text and combined notes; not confirmed missing notes |

These lists overlap. Counts are XML records across 17 files, including alternative versions, **not counts of unique printed notes**. The prior audit represented 1,584 actual note nodes as 1,582 top-level records; two nested notes remain inside their parent record's text.

No item is marked approved. Even letter-marker candidates require checking that the mark belongs to this note. The OCR match may be partial, clipped or on the wrong page; follow the complete-page link and inspect the image before accepting it. The displayed left/right attachment context is normalized legacy text, not a quotation of the OCR.

Review procedure:

1. Compare the complete source note and its marker with the scan, including the facing page and any continuation.
2. Record an attachment only when the marker or other direct source evidence establishes it. Do not use semantic plausibility alone.
3. Record any wording difference verbatim; distinguish OCR error, edition difference and editorial addition.
4. Enter the reviewer, decision, exact anchor and evidence in the CSV. Leave unresolved items explicitly unresolved.

All notes present in the OCR remain in the page edition, including ones not recognized by these candidate lists. This review package is **not an exhaustive segmentation of every printed/source note**. It combines the prior legacy-note audit with source-only coverage candidates, without inventing missing matches or attachments.
'''%(len(unattributed),len(unplaced),len(markers),len(generic),len(other),len(rows),counts['broad_coverage_candidates']))

inventory=[]
for p in sorted(out.rglob('*')):
    if p.is_file() and p.name not in ['file-inventory.csv','INVENTORY.md']:
        inventory.append({'path':str(p.relative_to(out)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
with (out/'file-inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','sha256']);w.writeheader();w.writerows(inventory)
(out/'INVENTORY.md').write_text('''# Inventory of completed work

Updated 2026-09-07. This inventory covers the Suetonius OCR edition and its supporting note review.

| Work completed | Result | Status / boundary |
|---|---|---|
| Inspected supplied sources and previous XML | Two OCR volumes and 17 legacy XML files audited | Alternative XML versions retained as separate witnesses |
| Established printing provenance | Both source title pages say 1970; volume I records revision in 1951 | Export catalogue date not used as printing date |
| Built source-only XML base | Volume I: 554 scans; volume II: 580 scans; 1,134 total | All internal page characters preserved; OCR remains unproofread |
| Preserved notes and apparatus | Remain on their source pages, including facing-page and continued notes | No guessed word-level attachments |
| Preserved Gemini-attributed material | Tiberius 43–47, separate XML supplement | Inherited prose unchanged; 43–44 are Latin in the source English column, 45–47 already English |
| Preserved inherited supplement note | Chapter 47 note separated and labelled | Original association recorded; attachment unverified |
| Built reading edition | [READ.html](READ.html), two-page display, source links and separate supplements | Browser preview blocked by local-file policy; embedded text validated |
| Preserved provenance inputs | Byte-identical OCR exports and legacy Tiberius XML in `sources/` | SHA-256 values recorded |
| Ran edition checks | 48 checks passed: source equality, supplement equality, page coverage and known discrepancies | No assertion of completed image proofreading or full external TEI schema validation |
| Added review inventory | [Review guide](review/REVIEW.md), [readable notes](review/NOTES.html), CSV review queues | Attribution and attachment kept distinct; all records remain unreviewed |
| Saved new edition alongside old files | `suet_loeb/clean_ocr_1970/` | Original top-level XML unchanged; no commit, publishing or viewer registration |

## Review counts

- %d legacy note records lack an explicit `resp` attribution.
- %d footnote records have unresolved attachment evidence.
- %d further records have candidate letter markers requiring verification.
- %d records use the generic attribution `editor`.
- %d editorial-addition/date records are retained in a separate list.
- 14 confirmed source discrepancies and %d broad source-coverage candidates are included.

These are overlapping record counts across XML versions, not unique-note totals. Every review row preserves its file and note number. No uncertain placement was promoted to a verified anchor.

## Files and verification

[file-inventory.csv](file-inventory.csv) lists package paths, byte sizes and SHA-256 checksums (excluding itself and this inventory). [validation.json](validation.json) records the source-edition checks. The [review guide](review/REVIEW.md) explains evidence limitations and how to record decisions.

Remaining editorial work is explicit: verify notes and markers against page images, resolve OCR errors with evidence, identify source notes that escaped the earlier heuristic audit, and encode chapter/section boundaries if required. The present page edition preserves the evidence needed for that work.
'''%(len(unattributed),len(unplaced),len(markers),len(generic),len(other),counts['broad_coverage_candidates']))
assert len(rows)==len(lookup)==1582
assert len(unplaced)+len(markers)+len(other)==len(rows)
assert len({r['review_id'] for r in rows})==len(rows)
print(json.dumps(counts,indent=2))
