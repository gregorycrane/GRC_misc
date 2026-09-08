from pathlib import Path
from lxml import etree as E
import json,re,unicodedata,csv
N={'t':'http://www.tei-c.org/ns/1.0'};t=E.parse('outputs/Holland-Julius-review/suetonius.jc.holland1898-section.xml');ns=json.load(open('work/holland-jc/notes.json'));buf='';offsets=[]
def walk(e):
 global buf
 if not isinstance(e.tag,str):return
 tag=E.QName(e).localname
 if tag=='note':offsets.append(len(buf));return
 if tag=='pb':return
 if e.text:buf+=e.text
 for c in e:walk(c);buf+=c.tail or ''
walk(t.find('.//t:body',N));rows=[]
for n,e in zip(ns,t.xpath('//t:note',namespaces=N)):n['marker']=e.get('n')
def words(s):return re.findall(r'[^\W_]+',s.lower())
def norm(s):return unicodedata.normalize('NFKC',re.sub(r'(?<=\w)[-¬]\s*\n\s*(?=\w)','',s)).lower()
P={k:{int(p['page']):p for p in json.load(open('work/holland-jc/'+k+'-pages.json')) if p['page'].isdigit()} for k in ['uc1','hvd']}
for n,off in zip(ns,offsets):
 left=words(buf[:off])[-4:];right=words(buf[off:])[:4];hits=[]
 if left and right:
  pat=r'\b'+r'\W+'.join(map(re.escape,left))+r'(?P<gap>.{0,24}?)'+r'\W+'.join(map(re.escape,right))+r'\b'
  for k,pages in P.items():
   for pg in range(max(15,n['page']-1),min(80,n['page']+1)+1):
    s=norm(pages[pg]['raw'])
    for m in re.finditer(pat,s,re.S):
     gap=m.group('gap');marker=''.join(re.findall('[a-z0-9]',gap));expected=n['marker']
     supported=bool(expected) and bool(re.fullmatch('[a-f0-9]{1,3}',marker)) and expected in re.findall(r'\d+|[a-f]',marker)
     hits.append({'witness':k,'page':pg,'gap':gap,'marker_evidence':supported,'context':m.group()})
 verified=[x for x in hits if x['marker_evidence']]
 rows.append({'note_index':n['index'],'reference':n['ref'],'series':n['series'],'marker':n['marker'],'xml_line':n['line'],'left':' '.join(left),'right':' '.join(right),'status':'OCR marker supports existing location' if verified else ('Context found; marker unresolved' if hits else 'Location unresolved'),'evidence':json.dumps(hits,ensure_ascii=False)})
with open('outputs/Holland-Julius-review/note-locations.csv','w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('Marker-supported:',sum(r['status'].startswith('OCR') for r in rows),'of',len(rows))
