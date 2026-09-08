from pathlib import Path
from lxml import etree as E
import json,csv,shutil,hashlib
O=Path('outputs/Holland-Julius-review');N={'t':'http://www.tei-c.org/ns/1.0'};t=E.parse(str(O/'suetonius.jc.holland1898-section.xml'));els=t.xpath('//t:note',namespaces=N)
notes=json.load(open('work/holland-jc/notes.json'));changes=json.load(open(O/'changes.json'));locations=list(csv.DictReader(open(O/'note-locations.csv',encoding='utf-8-sig')))
P={k:{int(p['page']):p for p in json.load(open('work/holland-jc/'+k+'-pages.json')) if p['page'].isdigit()} for k in ['uc1','hvd']}
def csvwrite(name,rows):
 with (O/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
manual={17:'OCR has interleaved the continuation “named Isauri, whom he subdued”; retain complete note.',74:'Em-brodered crosses pp. 234–235; retain combined word and note.',173:'Initial Con- is separated from trary in OCR; do not shorten Contrary.',191:'Note continues across pp. 242–243; UC library stamp is not note text. Only dubicæ → dubiæ corrected.',197:'The OCR places “2 Thus” before note 1; preserve logical note beginning Thus, not nearby word made.',227:'OCR interleaves note 1 between “to” and “Metellus”; preserve complete note.',246:'“3 Or” is displaced after the note in OCR; do not substitute the adjacent note’s word “word”.',260:'“2 And” is displaced after the note in OCR; do not substitute the adjacent note’s word “discipline”.',261:'Preserve verse-line boundaries and E viatico suo; UC reading order displaces the lemma.',296:'The words “that which brought him to” survive later in the same OCR footnote block. Do not delete them.',349:'Both OCR witnesses p. 78 read Detulerant; corrected.',355:'Cyripædia versus OCR Cyripadia: ligature/reading requires scan; not corrected.'}
rows=[]
for n,e,l in zip(notes,els,locations):
 fixed=[c['id'] for c in changes if c['note_index']==n['index']]
 rows.append({'note_id':e.get('{http://www.w3.org/XML/1998/namespace}id'),'index':n['index'],'reference':n['ref'],'series':n['series'],'original_marker':n['marker'],'reviewed_marker':e.get('n'),'original_xml_line':n['line'],'reviewed_xml_line':e.sourceline,'original_text':n['text'],'reviewed_text':''.join(e.itertext()),'uc1_page_pair_start':n['witnesses']['uc1']['page'],'hvd_page_pair_start':n['witnesses']['hvd']['page'],'uc1_word_match_score_before':n['witnesses']['uc1']['score'],'hvd_word_match_score_before':n['witnesses']['hvd']['score'],'uc1_comparison_span':n['witnesses']['uc1']['span'],'hvd_comparison_span':n['witnesses']['hvd']['span'],'location_status':l['status'],'changes':';'.join(fixed),'review_decision':manual.get(n['index'],'Word-sequence comparison is not punctuation/case or printed-image certification.')})
csvwrite('notes.csv',rows);csvwrite('unresolved-note-locations.csv',[r for r in rows if not r['location_status'].startswith('OCR')]);csvwrite('combined-and-reordered-notes.csv',[r for r in rows if r['index'] in manual]);csvwrite('notes-needing-text-review.csv',[r for r,n in zip(rows,notes) if not any(v['score']==1 and not v['differences'] for v in n['witnesses'].values())])
# Raw source evidence is retained separately from normalized alignment strings.
pgs=set([15,16,45,46,50,56,59,63,66,71,75,78,80,230,231,234,235,236,240,241,242,243,244])
(O/'source-excerpts.json').write_text(json.dumps({k:{str(p):P[k][p]['raw'] for p in sorted(pgs)} for k in P},ensure_ascii=False,indent=2)+'\n')
D=json.load(open('work/holland-jc/global.json'));out=[]
for k,ds in D.items():
 for d in ds:out.append({'witness':k,**d,'status':'Incoming XML comparison candidate; may be OCR marker, header, punctuation/ligature, or reading-order noise. Consult changes.json.'})
csvwrite('main-text-comparison.csv',out)
shutil.copy2('work/holland-jc/notes.json',O/'note-comparison-details.json')
parts=['# Exact corrections\n','All locations use the preserved XML chapter/section citations. OCR text evidence is in source-excerpts.json. Page-wrap and note-flow reconstruction is not a licence to paraphrase.\n']
for c in changes:
 parts+=['## '+c['id']+'\n','**'+c['reference']+' — '+c['kind']+'** (printed p. '+str(c['source_printed_page'])+').\n','Before: '+c['before']+'\n','After: '+c['after']+'\n',c['evidence']+'\n']
(O/'CHANGES.md').write_text('\n'.join(parts))
manifest=json.load(open(O/'manifest.json'));manifest['available_volume_II_not_used_for_Julius']=[]
for fname in ['suetonius-holland-02-uc1-b3114464-1788787746.txt','suetonius-holland-02-hvd-32044019809029-1788787496.txt']:
 p=Path('/Users/gcrane/Downloads')/fname;manifest['available_volume_II_not_used_for_Julius'].append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest['comparison_policy']='Line-wrap joins, case-folding and tokenization are used for candidate alignment only. Raw evidence is retained. Agreement of two OCR exports is not proof of independent recognition or printed-image verification.'
(O/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
v=json.load(open(O/'validation.json'));v['existing_locations_supported_by_OCR_marker']=sum(r['location_status'].startswith('OCR') for r in rows);v['unresolved_locations']=len(rows)-v['existing_locations_supported_by_OCR_marker'];v['incoming_notes_matching_word_sequence_in_at_least_one_OCR']=sum(any(w['score']==1 and not w['differences'] for w in n['witnesses'].values()) for n in notes);v['incoming_notes_matching_word_sequence_in_both_OCR']=sum(all(w['score']==1 and not w['differences'] for w in n['witnesses'].values()) for n in notes)
(O/'validation.json').write_text(json.dumps(v,indent=2)+'\n');print(v)
(O/'tools').mkdir(exist_ok=True)
for p in Path('work/holland-jc').glob('*.py'):shutil.copy2(p,O/'tools'/p.name)
