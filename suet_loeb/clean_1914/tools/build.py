#!/usr/bin/env python3
import csv,hashlib,html,json,re,shutil,sys
from pathlib import Path
from collections import Counter
from lxml import etree as E
from PIL import Image
HERE=Path(__file__).resolve().parent
BASE=HERE.parent.parent
OCR=BASE/'work/suetonius-pdf/full'
OUT=BASE/'outputs/Suetonius-1914-edition'
OLD=BASE/'outputs/Suetonius-clean-edition'
PDF=Path('/Users/gcrane/Library/Mobile Documents/iCloud~com~apple~iBooks/Documents/Suetonius_Loeb-rolfe.pdf')
NS='http://www.tei-c.org/ns/1.0';XML='http://www.w3.org/XML/1998/namespace';N={'t':NS}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def el(p,t,text=None,**a):
 n=E.SubElement(p,'{%s}%s'%(NS,t),**a);n.text=text;return n
def doc(title,ident):
 r=E.Element('{%s}TEI'%NS,nsmap={None:NS});r.set('{%s}id'%XML,ident)
 h=el(r,'teiHeader');fd=el(h,'fileDesc');ts=el(fd,'titleStmt');el(ts,'title',title);el(ts,'author','Suetonius')
 rs=el(ts,'respStmt');el(rs,'resp','Printed English translation');el(rs,'name','J. C. Rolfe')
 rs=el(ts,'respStmt');rs.set('{%s}id'%XML,'gemini3');el(rs,'resp','Supplementary translation attributed in inherited XML');el(rs,'name','Gemini 3')
 el(el(fd,'publicationStmt'),'p','Local 1914 source edition, 2026-09-07; OCR not fully proofread.')
 sd=el(fd,'sourceDesc');b=el(sd,'bibl');b.set('{%s}id'%XML,'pdf1914');el(b,'title','Suetonius, with an English translation by J. C. Rolfe');el(b,'date','1914');el(b,'publisher','William Heinemann / The Macmillan Co.');el(b,'note','Both title pages read MCMXIV. User-supplied PDF SHA-256: '+sha(PDF))
 ed=el(el(h,'encodingDesc'),'editorialDecl');el(el(ed,'correction'),'p','The facsimile is the textual authority. OCR is newly generated from the PDF, with no lexical rewriting. Verified footnote attachments are recorded separately with witness-specific evidence. No text from 1970 is silently substituted.')
 return r,el(el(r,'text'),'body')
def write(root,path):E.ElementTree(root).write(str(path),encoding='utf-8',xml_declaration=True,pretty_print=True)
for d in ['edition','sources','review','pages','tools']:(OUT/d).mkdir(parents=True,exist_ok=True)
assert len(list(OCR.glob('p*.txt')))==1094,'OCR incomplete'
D=json.loads((BASE/'work/suetonius-pdf/decisions.json').read_text())
W=json.loads((BASE/'work/suetonius-pdf/wording-decisions.json').read_text())
# Use PDF positions as the primary citation. Printed page sequence is a secondary label.
verified=set([2,533,1094])
for d in D:verified.update(d['pdf_note_pages']+[d['pdf_body_page']])
for d in W:verified.update([d['pdf_page']]+d.get('additional_pdf_pages',[]))
volumes=[];quality=[];raw_source=[]
for v,lo,hi in [(1,1,529),(2,530,1094)]:
 root,body=doc('Suetonius — Rolfe 1914 — volume %d'%v,'suetonius-rolfe1914-v%d'%v);pages=[]
 for number in range(lo,hi+1):
  source=OCR/('p%04d.txt'%number);text=source.read_text().strip();text=''.join(c for c in text if ord(c)>=32 or c in '\n\t')
  seq=number-lo+1
  label=str(number-30) if v==1 and 31<=number<=527 else (str(number-536) if v==2 and 537<=number<=1091 else '')
  # A few identified front-matter leaves and stemmata remain identified by PDF page.
  page={'seq':seq,'pdf_page':number,'label':label,'text':text,'label_status':'visually inspected' if number in verified else 'sequence-based; consult image'}
  pages.append(page)
  div=el(body,'div',type='source-page',n=str(number));div.set('{%s}id'%XML,'v%d-s%d'%(v,seq))
  el(div,'pb',n=label or '[unnumbered / unverified label]',facs='../pages/p%04d.jpg'%number)
  ab=el(div,'ab',text,type='unproofread-ocr');ab.set('{%s}space'%XML,'preserve')
  img=OUT/'pages'/('p%04d.jpg'%number)
  if not img.exists():Image.open(OCR/('p%04d.png'%number)).convert('RGB').save(img,quality=85,optimize=True)
  raw_source.append('## PDF page %d | volume %d | printed label %s\n\n%s\n\n'%(number,v,label,text))
  rows=list(csv.DictReader((OCR/('p%04d.tsv'%number)).open(),delimiter='\t',quoting=csv.QUOTE_NONE))
  words=[r for r in rows if r.get('level')=='5' and r.get('text','').strip()]
  conf=[float(r['conf']) for r in words]
  quality.append({'pdf_page':number,'volume':v,'printed_label':label,'words':len(words),'mean_confidence':round(sum(conf)/len(conf),2) if conf else '', 'words_below_50':sum(x<50 for x in conf),'proofreading_status':'Selected notes/wording checked' if number in verified else 'Not manually proofread'})
 write(root,OUT/'edition'/('suetonius.rolfe1914.volume%d.ocr.xml'%v));volumes.append({'number':v,'pages':pages})
(OUT/'sources'/'1914-fresh-ocr.txt').write_text(''.join(raw_source))
shutil.copy2(OLD/'sources'/'suetonius.tib.loeb_eng1.legacy.xml',OUT/'sources'/'suetonius.tib.loeb_eng1.legacy.xml')
shutil.copy2(OLD/'edition'/'suetonius.tiberius.gemini-supplement.xml',OUT/'sources'/'inherited-gemini43-47.xml')
legacy=E.parse(str(OUT/'sources/inherited-gemini43-47.xml'))
supp=[];root,body=doc('Tiberius 43–44 — Gemini-attributed English supplements','suetonius-tiberius-gemini43-44')
el(body,'head','Supplementary English — Gemini 3 attribution inherited from legacy XML')
el(body,'p','These two chapters are untranslated in the English column of the 1914 print. The inherited prose is preserved without rewriting. Chapters 45–47 already have Rolfe English and are retained only as archival alternatives in sources/inherited-gemini43-47.xml.')
for ch in range(43,48):
 old=legacy.xpath('//t:div[@type="supplement"][@n="%d"]'%ch,namespaces=N)[0]
 if ch<=44:
  new=E.fromstring(E.tostring(old));body.append(new)
 sections=[{'n':s.get('n'),'paragraphs':[''.join(p.itertext()) for p in s.findall('t:p',N)]} for s in old.xpath('./t:div[@subtype="section"]',namespaces=N)]
 notes=[{'section':n.get('n'),'text':''.join(n.itertext())} for n in old.xpath('./t:div[@type="unverified-legacy-notes"]/t:ab',namespaces=N)]
 supp.append({'chapter':ch,'sections':sections,'notes':notes})
write(root,OUT/'edition'/'suetonius.tiberius.gemini43-44.xml')
attribution=''.join(legacy.xpath('//t:div[@type="legacy-attribution"]/t:p',namespaces=N)[0].itertext())
payload=json.dumps({'volumes':volumes,'supplements':supp,'attribution':attribution,'decisions':D},ensure_ascii=False).replace('<','\\u003c')
(OUT/'READ.html').write_text((HERE/'reader.html').read_text().replace('/*EDITION_DATA*/null',payload))
for name,obj in [('pdf-decisions.json',D),('wording-decisions.json',W)]: (OUT/'review'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def csvwrite(name,rows):
 with (OUT/'review'/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
csvwrite('ocr-quality-by-page.csv',quality)
# Preserve every earlier evidence field. New decisions are explicitly for the 1914 witness.
rows=list(csv.DictReader((OLD/'review/all-legacy-notes.csv').open(encoding='utf-8-sig')))
updates={i:d for d in D for i in d['legacy_ids']}
assert len(updates)==sum(len(d['legacy_ids']) for d in D)
for r in rows:
 r['prior_review_status']=r['review_status'];r['comparison_excerpt_witness']='1970 Hathi OCR from earlier audit'
 r['edition_page_link']='' # An old 1970 source-sequence link must not be redirected to a 1914 page.
 r['pdf_decision_id']='';r['pdf_body_page']='';r['pdf_note_pages']='';r['verified_reference_1914']='';r['verified_marker_1914']=''
 if r['review_id'] in updates:
  d=updates[r['review_id']];r.update(review_status=d['review_status'],reviewer='Codex',decision=d['decision'],verified_anchor=d['verified_anchor'],evidence='Direct visual inspection of the 1914 PDF; see '+d['id'],pdf_decision_id=d['id'],pdf_body_page=d['pdf_body_page'],pdf_note_pages=';'.join(map(str,d['pdf_note_pages'])),verified_reference_1914=d['reference'],verified_marker_1914=d['marker'])
csvwrite('all-legacy-notes.csv',rows)
csvwrite('unattributed-notes.csv',[r for r in rows if not r['legacy_resp']])
csvwrite('remaining-unresolved-attachments.csv',[r for r in rows if r['kind_or_comparison'] not in ('documented-editorial-addition','marginal-date-review') and r['review_status']=='Unreviewed' and r['anchor_status']!='letter-marker-at-anchor'])
csvwrite('remaining-marker-candidates.csv',[r for r in rows if r['kind_or_comparison'] not in ('documented-editorial-addition','marginal-date-review') and r['review_status']=='Unreviewed' and r['anchor_status']=='letter-marker-at-anchor'])
csvwrite('resolved-legacy-records.csv',[r for r in rows if r['review_id'] in updates])
csvwrite('newly-located-source-notes.csv',[{k:(';'.join(map(str,v)) if isinstance(v,list) else v) for k,v in d.items()} for d in D if not d['legacy_ids']])
shutil.copy2(OLD/'review/coverage-review.json',OUT/'review/coverage-review.json')
confirmed=list(csv.DictReader((OLD/'review/confirmed-source-discrepancies.csv').open(encoding='utf-8-sig')))
cm={'N01':'P031','N02':'P021','N03':'P022','N04':'P023',**{'N%02d'%(n+4):'P%03d'%n for n in range(1,11)}}
for c in confirmed:
 c['pdf_decision_id']=cm[c['id']];c['pdf_review_status']='Note and anchor verified in 1914 PDF'
csvwrite('confirmed-source-discrepancies.csv',confirmed)
# Machine-readable verification layer, separate from the original OCR characters.
r,b=doc('Verified note anchors in the 1914 PDF','suetonius-1914-verified-anchors')
lst=el(b,'list')
for d in D:
 item=el(lst,'item');item.set('{%s}id'%XML,d['id']);el(item,'label',d['work']+' '+d['reference'])
 el(item,'p',d['decision']);el(item,'p','Printed anchor: '+d['verified_anchor']+'; marker: '+d['marker'])
 el(item,'p','Note identifier (not a full note transcription): '+d['note_identifier'])
 for p in sorted(set(d['pdf_note_pages']+[d['pdf_body_page']])):el(item,'ref','PDF page '+str(p),target='../pages/p%04d.jpg'%p)
write(r,OUT/'edition'/'suetonius.rolfe1914.verified-anchors.xml')
lines=['# Verified resolutions from the 1914 PDF\n','Both title pages read MCMXIV. All decisions below are specific to this witness. Markers and note text were inspected on page images; semantic plausibility was not used to invent attachments.\n','58 note anchors are verified; one unsupported extra note is rejected. Repeated legacy versions retain their own record IDs. “Note identifier” is a descriptive excerpt, not a replacement transcription of the full note.\n']
for d in D:
 lines+=['## '+d['id']+'\n',f"**{d['work']} {d['reference']}** — {d['review_status']}.\n",'Note identifier: '+d['note_identifier']+'\n',('Printed marker **'+d['marker']+'** follows **'+d['verified_anchor']+'**.\n') if d['marker'] else '',d['decision']+'\n','Evidence: '+', '.join('[PDF page %d](../pages/p%04d.jpg)'%(p,p) for p in sorted(set(d['pdf_note_pages']+[d['pdf_body_page']])))+'.\n','Legacy records: '+(', '.join(d['legacy_ids']) or 'No corresponding legacy record selected; source-only note.')+'\n']
lines+=['# Wording findings\n']
for w in W:lines+=['## '+w['work']+' '+w['reference']+'\n','1914: **'+w['reading_1914']+'**. '+w['finding']+' [PDF page %d](../pages/p%04d.jpg).\n'%(w['pdf_page'],w['pdf_page'])]
(OUT/'review'/'PDF-RESOLUTIONS.md').write_text('\n'.join(lines))
# Static HTML index makes every decision accessible without a Markdown renderer.
parts=['<!doctype html><html lang="en"><meta charset="utf-8"><title>1914 note resolutions</title><style>body{max-width:960px;margin:40px auto;padding:0 24px;font:17px/1.65 Georgia,serif;color:#252a28;background:#faf8f2}article{border-top:1px solid #ccc;margin-top:24px}a{color:#315d49}</style><h1>1914 note resolutions</h1><p>58 printed anchors verified; one unsupported legacy extra rejected. <a href="REVIEW.md">Review guide and remaining lists</a></p>']
for d in D:
 parts.append('<article id="%s"><h2>%s · %s %s</h2><p>%s</p><p>Marker: %s. Anchor: <strong>%s</strong></p><p>%s</p><p>%s</p></article>'%(d['id'].lower(),d['id'],d['work'],d['reference'],html.escape(d['note_identifier']),html.escape(d['marker'] or 'none'),html.escape(d['verified_anchor']),html.escape(d['decision']),' · '.join('<a href="../pages/p%04d.jpg">PDF page %d</a>'%(p,p) for p in sorted(set(d['pdf_note_pages']+[d['pdf_body_page']])))))
parts.append('</html>');(OUT/'review/NOTES.html').write_text('\n'.join(parts))
manifest={'title':'Suetonius — Rolfe 1914 source edition','date':'2026-09-07','source_pdf_path':str(PDF),'source_pdf_sha256':sha(PDF),'pdf_pages':1094,'volumes':[{'volume':1,'pdf_pages':[1,529]},{'volume':2,'pdf_pages':[530,1094]}], 'base':'1914 PDF images; newly generated OCR, not the 1970 text or legacy LLM XML','active_gemini_supplements':[43,44],'archival_gemini_alternatives':[45,46,47],'verified_note_anchors':58,'rejected_extra_notes':1,'legacy_records_with_pdf_decisions':len(updates),'wording_findings':len(W),'ocr_engine':'Tesseract, eng, PSM 3, page rendering 2200 pixels on longer side; source images retained as JPEG quality 85','limitations':['Not every page or note has been manually proofread.','Printed labels beyond inspected pages are sequence-based; PDF page numbers are authoritative locators.','OCR is uncorrected and may misread Greek, superscripts, marginal dates and damaged printing.','A printed note is attributed to its source edition, not silently assigned a personal author from an absent legacy resp.']}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
for name in ['build.py','reader.html','validate.py']:shutil.copy2(HERE/name,OUT/'tools'/name)
shutil.copy2(BASE/'work/suetonius-pdf/ocr_all.py',OUT/'tools/ocr_all.py')
for name in ['README.md','INVENTORY.md']:shutil.copy2(HERE/name,OUT/name)
shutil.copy2(HERE/'REVIEW.md',OUT/'review/REVIEW.md')
print(json.dumps(manifest,indent=2))
