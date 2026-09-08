from pathlib import Path
from lxml import etree as E
import json,re,csv,difflib,hashlib,shutil
O=Path('outputs/Holland-Julius-review');name='suetonius.jc.holland1898-section.xml';raw=(O/'original.xml').read_text();original=raw;changes=[];N={'t':'http://www.tei-c.org/ns/1.0'}
def fix(ref,old,new,page,kind='wording',note=None):
 global raw
 assert raw.count(old)==1,(old,raw.count(old));raw=raw.replace(old,new)
 changes.append({'id':'H%03d'%(len(changes)+1),'reference':ref,'note_index':note,'kind':kind,'before':old,'after':new,'source_printed_page':page,'evidence':'Both supplied volume-I OCR witnesses agree; see source excerpts and original backup.'})
fix('73.1','invectives against him, him, and','invectives against him, and',66)
fix('78.2','indignation thereat, that','indignation therat, that',71)
fix('81.4','a written scrole, of the Conspiratours names, and those that were that sought his life','a written pamphlet, which layd open the conspiracie, and who they were that sought his life',75)
fix('2.1','Young gentlemen or noble bloud','Young gentlemen of noble bloud',231,'note wording',13)
fix('20.1','Ne si ambo fusces haberent','Ne si ambo fasces haberent',236,'note wording',90)
fix('39.2','Virgil, Eneid, 5.','Virgil, Æneid, 5.',241,'note wording',162)
fix('39.3','called in Latine Meta,','called in Latine Metæ,',241,'note wording',163)
fix('45.1','commemorant dubicæ per tempora','commemorant dubiæ per tempora',242,'note wording',191)
fix('84.3','Detulerunt.','Detulerant.',78,'note wording',349)
fix('89.1','A notable judgent of','A notable judgement of',80,'note wording',361)
fix('89.1','their Soveraie.','their Soveraine.',80,'note wording',361)
fix('82.1','<note place="bottom" n="5">Jugulum,','<note place="bottom" n="6">Jugulum,',75,'printed note number',326)
fix('84.3','<note place="bottom" n="2">Where he was murdered.','<note place="bottom" n="4">Where he was murdered.',78,'printed note number',350)
fix('41.3','whereas 320000 Citizens','whereas <num cert="low" source="#holland-uc1 #holland-hvd">3,020,000</num> Citizens',46,'OCR numeral; scan verification pending')
# Stable note IDs let the review inventory identify each existing note without changing its position.
i=0
def identify(m):
 global i
 i+=1;return '<note xml:id="holland-jc-note-%03d"'%i+m.group()[5:]
raw=re.sub(r'<note\b[^>]*>',identify,raw);assert i==361
raw=raw.replace('<p>Transcribed from PDF source files of Philemon Holland\'s 1898 edition.</p>', '''<p>Inherited description: transcribed from PDF source files of Philemon Holland's 1898 edition. The two supplied volume-I OCR witnesses both identify D. Nutt, London, 1899. Their title-page OCR also reads 1899. The historical filename is retained; the 1898 claim has not been independently established.</p>
        <listBibl>
          <bibl xml:id="holland-uc1">History of twelve Caesars, translated by Philemon Holland, D. Nutt, 1899, volume I. University of California witness uc1.b3114462; supplied OCR: suetonius-holland-01-uc1-b3114462-1788787677.txt.</bibl>
          <bibl xml:id="holland-hvd">Same title and printing information, volume I. Harvard witness hvd.32044024292195; supplied OCR: suetonius-holland-01-hvd-32044024292195-1788787412.txt.</bibl>
        </listBibl>''')
raw=raw.replace('  </teiHeader>', '''    <encodingDesc><editorialDecl><p>Review of 2026-09-07 retains the existing 89 chapters, 187 sections, numbered footnotes, and lettered end annotations. Fourteen source-supported wording/number corrections are recorded in <ref target="jc-review/changes.json">the change inventory</ref>. Notes continued across pages remain combined. OCR marker evidence and unresolved locations are recorded separately; no note location has been inferred from meaning alone. The review does not certify character-for-character identity: punctuation, case, ligatures, marginal dates and uncertain OCR remain subject to collation.</p></editorialDecl></encodingDesc>
    <revisionDesc><change when="2026-09-07">Codex: two-witness collation and incremental cleanup. All original notes and citation divisions retained; stable note IDs added. See <ref target="jc-review/REPORT.md">state of work</ref> and the exact original backup in jc-review/original.xml.</change></revisionDesc>
  </teiHeader>''')
(O/name).write_text(raw);(O/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n');(O/'changes.diff').write_text(''.join(difflib.unified_diff(original.splitlines(True),raw.splitlines(True),fromfile='original/'+name,tofile='reviewed/'+name)))
a=E.fromstring(original.encode());b=E.fromstring(raw.encode());an=a.xpath('//t:note',namespaces=N);bn=b.xpath('//t:note',namespaces=N)
def refs(n):return '.'.join(x.get('n') for x in reversed(list(n.iterancestors())) if x.tag=='{'+N['t']+'}div')
assert [(d.get('type'),d.get('n')) for d in a.xpath('//t:div',namespaces=N)]==[(d.get('type'),d.get('n')) for d in b.xpath('//t:div',namespaces=N)]
assert len(an)==len(bn)==361
assert [refs(n) for n in an]==[refs(n) for n in bn]
assert [n.text for n in a.xpath('//comment()')]==[n.text for n in b.xpath('//comment()')]
assert [p.get('n') for p in a.xpath('//t:pb',namespaces=N)]==[p.get('n') for p in b.xpath('//t:pb',namespaces=N)]
changed=[i for i,(x,y) in enumerate(zip(an,bn),1) if ''.join(x.itertext())!=''.join(y.itertext())]
assert changed==[13,90,162,163,191,349,361],changed
v={'passed':True,'chapters_preserved':89,'sections_preserved':187,'notes_preserved':361,'numbered_footnotes':212,'lettered_annotations':149,'wording_and_number_changes':len(changes),'notes_with_wording_changes':changed,'note_number_changes':[326,350],'note_moves':0,'original_sha256':hashlib.sha256((O/'original.xml').read_bytes()).hexdigest(),'reviewed_sha256':hashlib.sha256((O/name).read_bytes()).hexdigest(),'limitations':'XML well-formedness and preservation checks; not full TEI schema validation or complete character identity.'}
(O/'validation.json').write_text(json.dumps(v,indent=2)+'\n');print(v)
