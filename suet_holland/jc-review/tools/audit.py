from pathlib import Path
from lxml import etree as E
import re,json,difflib,csv,collections,hashlib
O=Path('outputs/Holland-Julius-review');W=Path('work/holland-jc');N={'t':'http://www.tei-c.org/ns/1.0'}
files={'uc1':Path('/Users/gcrane/Downloads/suetonius-holland-01-uc1-b3114462-1788787677.txt'),'hvd':Path('/Users/gcrane/Downloads/suetonius-holland-01-hvd-32044024292195-1788787412.txt')}
def tokenize(s):return [m.group().lower() for m in re.finditer(r'[^\W_]+',s)]
def note_text(e):
 copy=E.fromstring(E.tostring(e,with_tail=False))
 for x in copy.xpath('.//t:l | .//t:p',namespaces=N):x.tail='\n'+(x.tail or '')
 return ''.join(copy.itertext())
def norm(s):return re.sub(r'(?<=\w)[-¬]\s*\n\s*(?=\w)','',s)
def clean(s):
 s=norm(s);lines=s.splitlines();return '\n'.join(l for l in lines if l.strip() not in ['THE HISTORIE OF','TWELVE CÆSARS','CAIUS','JULIUS','CÆSAR','CESAR','ANNOTATIONS','ΑΝΝΟΤΑTIONS'] and not re.fullmatch(r'\s*\d+\s*',l))
P={}
for k,f in files.items():
 blocks=re.split(r'^## p\. (.*?)\(#(\d+)\) #+\s*$',f.read_text(),flags=re.M);pages=[]
 for i in range(1,len(blocks),3):
  label=blocks[i].strip();pg={'page':label,'seq':int(blocks[i+1]),'raw':blocks[i+2],'text':clean(blocks[i+2])};pg['tokens']=tokenize(pg['text']);pages.append(pg)
 P[k]={int(p['page']):p for p in pages if p['page'].isdigit()}
 (W/(k+'-pages.json')).write_text(json.dumps(pages,ensure_ascii=False))
src=Path('/Users/gcrane/github/GRC_misc/suet_holland/suetonius.jc.holland1898-section.xml');tree=E.parse(str(src));chunks={};notes=[];page=None;context=''
def walk(e):
 global page,context
 if not isinstance(e.tag,str):return
 tag=E.QName(e).localname
 if tag=='pb':page=int(e.get('n'));return
 if tag=='note':
  ref='.'.join(x.get('n') for x in reversed(list(e.iterancestors())) if x.tag=='{'+N['t']+'}div')
  notes.append({'index':len(notes)+1,'ref':ref,'line':e.sourceline,'page':page,'series':e.get('type','footnote'),'marker':e.get('n'),'text':note_text(e),'left':tokenize(context)[-9:],'element_path':tree.getpath(e)})
  return
 if e.text:chunks[page]=chunks.get(page,'')+e.text;context+=e.text
 for c in e:
  old=len(notes);walk(c)
  if len(notes)>old:notes[-1]['right_tail']=c.tail or ''
  if c.tail:chunks[page]=chunks.get(page,'')+c.tail;context+=c.tail
walk(tree.find('.//t:body',N))
# Match complete notes against a page pair, allowing page continuations.
pairs={}
for k,pages in P.items():
 pairs[k]=[(pg,pages[pg]['tokens']+(pages[pg+1]['tokens'] if pg+1 in pages else [])) for pg in list(range(15,81))+list(range(228,249)) if pg in pages]
for idx,n in enumerate(notes):
 nt=tokenize(norm(n['text']));n['witnesses']={}
 for k in P:
  candidates=[(pg,ts) for pg,ts in pairs[k] if (pg>=228)==(n['series']=='annotation') and (n['series']=='annotation' or abs(pg-n['page'])<=1)]
  ranked=sorted(candidates,key=lambda x:len(set(nt)&set(x[1])),reverse=True)[:8];best=None
  for pg,ts in ranked:
   seed=difflib.SequenceMatcher(None,nt,ts,autojunk=False).find_longest_match(0,len(nt),0,len(ts)); offset=max(0,seed.b-seed.a-8); window=ts[offset:seed.b-seed.a+len(nt)+9]; sm=difflib.SequenceMatcher(None,nt,window,autojunk=False);bs=[b for b in sm.get_matching_blocks() if b.size];score=sum(b.size for b in bs)/max(1,len(nt))
   if not bs:continue
   lo=bs[0].b-bs[0].a;hi=bs[-1].b+bs[-1].size+(len(nt)-bs[-1].a-bs[-1].size)
   lo=max(0,lo)+offset;hi=min(len(window),hi)+offset
   # Prefer the smaller source span among equal-coverage candidates.
   rank=score-.001*max(0,hi-lo-len(nt))
   if best is None or rank>best[0]:best=(rank,pg,ts,lo,hi,score,bs)
  if best is None:
   n['witnesses'][k]={'page':n['page'],'score':0,'start':0,'end':0,'span':'','differences':[],'edge_match':False};continue
  _,pg,ts,lo,hi,score,bs=best
  span=ts[lo:hi];diffs=[{'kind':op,'a':i,'b':j,'before':' '.join(nt[i:j]),'after':' '.join(span[l:r])} for op,i,j,l,r in difflib.SequenceMatcher(None,nt,span,autojunk=False).get_opcodes() if op!='equal']
  n['witnesses'][k]={'page':pg,'score':round(score,4),'start':lo,'end':hi,'span':' '.join(span),'differences':diffs,'edge_match':bs[0].a==0 and bs[-1].a+bs[-1].size==len(nt)}
 if (idx+1)%60==0:print('notes',idx+1,flush=True)
(W/'notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2))
# Page-based main text alignment; matching note spans removed, no conjectural OCR cleanup.
main=[]; global_sources={k:[] for k in P}
for pg,xml in chunks.items():
 if pg is None:continue
 xt=tokenize(xml);w={}
 for k in P:
  pt=P[k][pg]['tokens'];removed=set()
  for n in notes:
   if n['series']=='annotation':continue
   hit=n['witnesses'][k]
   if len(tokenize(norm(n['text'])))<5 or hit['score']<.82 or hit['end']-hit['start']>len(tokenize(norm(n['text'])))*1.35+3:continue
   plen=len(P[k][hit['page']]['tokens'])
   if hit['page']==pg:removed.update(range(hit['start'],min(hit['end'],plen)))
   elif hit['page']+1==pg:removed.update(range(max(0,hit['start']-plen),max(0,hit['end']-plen)))
  ts=[x for i,x in enumerate(pt) if i not in removed];global_sources[k]+=ts;diffs=[]
  for op,i,j,l,r in difflib.SequenceMatcher(None,xt,ts,autojunk=False).get_opcodes():
   if op=='equal':continue
   diffs.append({'kind':op,'a':i,'b':j,'before':' '.join(xt[i:j]),'after':' '.join(ts[l:r]),'left':' '.join(xt[max(0,i-5):i]),'right':' '.join(xt[j:j+5])})
  w[k]=diffs
 main.append({'page':pg,'xml':xml,'witnesses':w})
whole=tokenize(' '.join(chunks[p] for p in chunks if p is not None)); global_diffs={}
for k,ts in global_sources.items():
 global_diffs[k]=[{'kind':op,'a':i,'b':j,'before':' '.join(whole[i:j]),'after':' '.join(ts[l:r]),'left':' '.join(whole[max(0,i-7):i]),'right':' '.join(whole[j:j+7])} for op,i,j,l,r in difflib.SequenceMatcher(None,whole,ts,autojunk=False).get_opcodes() if op!='equal']
(W/'global.json').write_text(json.dumps(global_diffs,ensure_ascii=False,indent=2))
(W/'main.json').write_text(json.dumps(main,ensure_ascii=False,indent=2))
manifest={'xml':str(src),'xml_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'sources':{k:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in files.items()},'chapters':len(tree.xpath('//t:div[@type="chapter"]',namespaces=N)),'sections':len(tree.xpath('//t:div[@type="section"]',namespaces=N)),'notes':len(notes),'main_pages':len(main)}
(O/'manifest.json').write_text(json.dumps(manifest,indent=2));(O/'original.xml').write_bytes(src.read_bytes());print(manifest)
