#!/usr/bin/env python3
import csv,hashlib,json,re,sys
from pathlib import Path
from lxml import etree as E
from PIL import Image
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[2]/'outputs/Suetonius-1914-edition'
N={'t':'http://www.tei-c.org/ns/1.0'}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(n):return list(csv.DictReader((OUT/'review'/n).open(encoding='utf-8-sig')))
checks=[]
def check(name,ok):
 checks.append({'check':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
manifest=json.loads((OUT/'manifest.json').read_text())
check('Original PDF checksum',digest(Path(manifest['source_pdf_path']))==manifest['source_pdf_sha256'])
reader=(OUT/'READ.html').read_text();data=json.loads(re.search(r'const DATA=(.*);\n',reader).group(1))
seen=[];ocr=[]
raw=Path.cwd()/'work/suetonius-pdf/full'
prior=Path.cwd()/'outputs/Suetonius-clean-edition'
for v in data['volumes']:
 tree=E.parse(str(OUT/'edition'/('suetonius.rolfe1914.volume%d.ocr.xml'%v['number'])))
 divs=tree.xpath('//t:div[@type="source-page"]',namespaces=N)
 check('Volume %d page count'%v['number'],len(divs)==len(v['pages'])==(529 if v['number']==1 else 565))
 for div,p in zip(divs,v['pages']):
  n=p['pdf_page'];seen.append(n)
  if raw.exists():
   source=(raw/('p%04d.txt'%n)).read_text().strip()
   assert p['text']==''.join(c for c in source if ord(c)>=32 or c in '\n\t')
  assert div.get('n')==str(n) and div.get('{http://www.w3.org/XML/1998/namespace}id')=='v%d-s%d'%(v['number'],p['seq'])
  assert (div.find('t:ab',N).text or '')==p['text']
  image=OUT/'pages'/('p%04d.jpg'%n)
  with Image.open(image) as im:
   assert max(im.size)==2200;im.verify()
  assert (OUT/'edition'/div.find('t:pb',N).get('facs')).resolve()==image
  ocr.append('## PDF page %d | volume %d | printed label %s\n\n%s\n\n'%(n,v['number'],p['label'],p['text']))
check('All 1094 PDF pages, images, XML IDs and reader texts agree',seen==list(range(1,1095)))
check('Fresh OCR source equals XML and reader without lexical changes',(OUT/'sources/1914-fresh-ocr.txt').read_text()==''.join(ocr))
check('OCR quality ledger covers every page',[int(r['pdf_page']) for r in rows('ocr-quality-by-page.csv')]==seen)
old=E.parse(str(OUT/'sources/inherited-gemini43-47.xml'));new=E.parse(str(OUT/'edition/suetonius.tiberius.gemini43-44.xml'))
active=new.xpath('//t:div[@type="supplement"]',namespaces=N)
check('Only chapters 43 and 44 active',[d.get('n') for d in active]==['43','44'])
for d in active:
 original_div=old.xpath('//t:div[@type="supplement"][@n="%s"]'%d.get('n'),namespaces=N)[0]
 check('Chapter '+d.get('n')+' supplement unchanged',E.tostring(d,with_tail=False)==E.tostring(original_div,with_tail=False))
check('All five inherited chapters retained in reader',[s['chapter'] for s in data['supplements']]==list(range(43,48)))
D=json.loads((OUT/'review/pdf-decisions.json').read_text());ids={d['id']:d for d in D}
check('59 distinct decisions, 58 anchors, one rejected extra',len(ids)==59 and sum(d['kind']=='note-anchor' for d in D)==58 and sum(d['kind']=='unsupported-note' for d in D)==1)
check('Reader decisions identical to review record',data['decisions']==D)
for d in D:
 for n in d['pdf_note_pages']+[d['pdf_body_page']]:assert n in seen
 assert 'id="'+d['id'].lower()+'"' in (OUT/'review/NOTES.html').read_text()
ledger=rows('all-legacy-notes.csv');linked={i:d for d in D for i in d['legacy_ids']}
if prior.exists():
 previous=list(csv.DictReader((prior/'review/all-legacy-notes.csv').open(encoding='utf-8-sig')))
 protected=[k for k in previous[0] if k not in ['review_status','reviewer','decision','verified_anchor','evidence','edition_page_link']]
 assert all(all(a[k]==b[k] for k in protected) for a,b in zip(previous,ledger))
 assert digest(OUT/'sources/suetonius.tib.loeb_eng1.legacy.xml')==digest(prior/'sources/suetonius.tib.loeb_eng1.legacy.xml')
 assert digest(OUT/'sources/inherited-gemini43-47.xml')==digest(prior/'edition/suetonius.tiberius.gemini-supplement.xml')
check('Complete legacy ledger preserved',len(ledger)==1582 and len({r['review_id'] for r in ledger})==1582)
for r in ledger:
 if r['review_id'] in linked:
  d=linked[r['review_id']];assert r['pdf_decision_id']==d['id'] and r['verified_anchor']==d['verified_anchor']
check('All 44 legacy decisions consistent',len(linked)==len(rows('resolved-legacy-records.csv'))==44)
for f,n in [('unattributed-notes.csv',442),('remaining-unresolved-attachments.csv',1170),('remaining-marker-candidates.csv',156),('newly-located-source-notes.csv',18)]:check(f,len(rows(f))==n)
confirmed=rows('confirmed-source-discrepancies.csv')
check('All 14 previously confirmed missing notes resolved',len(confirmed)==14 and all(r['pdf_decision_id'] in ids for r in confirmed))
check('12 wording findings retained',len(json.loads((OUT/'review/wording-decisions.json').read_text()))==12)
for p,anchor in [('P011','house'),('P024','gestures'),('P027','pontifex'),('P028','offered'),('P029','divine')]:check(p+' corrected attachment',anchor in ids[p]['verified_anchor'])
check('Three missing Titus 7.3 markers verified',[ids[p]['marker'] for p in ['P021','P022','P023']]==['a','b','c'])
for path in (OUT/'edition').glob('*.xml'):E.parse(str(path))
ann=E.parse(str(OUT/'edition/suetonius.rolfe1914.verified-anchors.xml'))
check('Every evidence image link resolves',all((OUT/'edition'/r.get('target')).exists() for r in ann.xpath('//t:ref',namespaces=N)))
check('1914 image-first reader and unresolved status visible','image' in reader and 'proofreading' in reader.lower())
report={'passed':True,'checks':checks,'check_count':len(checks),'limitations':['No claim of full OCR proofreading or TEI schema validation.','Browser visual preview unavailable because local-file navigation was blocked.']}
(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
with (OUT/'file-inventory.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['path','bytes','sha256'])
 for p in sorted(OUT.rglob('*')):
  if p.is_file() and p.name!='file-inventory.csv':w.writerow([str(p.relative_to(OUT)),p.stat().st_size,digest(p)])
print(json.dumps({'passed':True,'checks':len(checks),'pages':len(seen)}))
