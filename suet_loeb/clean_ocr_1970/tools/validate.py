#!/usr/bin/env python3
"""Independently verify the source and supplement fidelity of the page edition."""
import hashlib
import json
import re
import sys
from pathlib import Path
from lxml import etree as E

out = Path(sys.argv[1])
ns = {'t': 'http://www.tei-c.org/ns/1.0'}
manifest = json.loads((out/'manifest.json').read_text())
checks = []
def check(condition, name):
    assert condition, name
    checks.append(name)
pages = {}
for src in manifest['sources']:
    v=src['volume']; raw=(out/'sources'/src['file']).read_bytes()
    check(hashlib.sha256(raw).hexdigest()==src['sha256'], 'Volume %d source checksum' % v)
    # Use a separate delimiter scan rather than importing the builder parser.
    text=raw.decode('utf-8'); marks=list(re.finditer(r'^## p\.(.*?)\(#(\d+)\) #+\n',text,re.M))
    tree=E.parse(str(out/'edition'/('suetonius.rolfe1970.volume%d.ocr.xml'%v)))
    divs=tree.xpath('//t:body/t:div',namespaces=ns)
    check(len(divs)==len(marks)==src['pages'],'Volume %d complete page count'%v)
    for i,(mark,div) in enumerate(zip(marks,divs)):
        s=text[mark.end():marks[i+1].start() if i+1<len(marks) else len(text)].replace('\f','').strip()
        ab=div.find('t:ab',ns)
        assert (ab.text or '')==s, (v,i+1,'text mismatch')
        assert int(div.get('n'))==int(mark.group(2))==i+1
        assert div.find('t:pb',ns).get('n')==(mark.group(1).strip() or '[unnumbered]')
        pages[(v,mark.group(1).strip())]=s
    check(True,'Volume %d every source-page character and page label matches'%v)
    check(not tree.xpath('//t:body//t:note|//t:body//t:anchor|//t:body//t:ptr',namespaces=ns),
          'Volume %d no inferred note attachments'%v)
    check(not tree.xpath('//t:body//t:div[@type="supplement"]',namespaces=ns),'Volume %d no supplements blended into base'%v)

legacy_path=out/'sources'/'suetonius.tib.loeb_eng1.legacy.xml'
check(hashlib.sha256(legacy_path.read_bytes()).hexdigest()==manifest['legacy_source_sha256'],'Legacy XML archived byte for byte')
legacy=E.parse(str(legacy_path));supp=E.parse(str(out/'edition'/'suetonius.tiberius.gemini-supplement.xml'))
def prose(p):
    def walk(node):
        if E.QName(node).localname in ('note','pb'): return ''
        return (node.text or '')+''.join(walk(c)+(c.tail or '') for c in node)
    return walk(p)
for ch in range(43,48):
    orig=legacy.xpath('//t:div[@subtype="chapter"][@n="%d"]'%ch,namespaces=ns)[0]
    new=supp.xpath('//t:div[@type="supplement"][@n="%d"]'%ch,namespaces=ns)[0]
    op=orig.xpath('./t:div[@subtype="section"]/t:p',namespaces=ns)
    np=new.xpath('./t:div[@subtype="section"]/t:p',namespaces=ns)
    check([prose(p) for p in op]==[''.join(p.itertext()) for p in np],'Tiberius %d supplement prose unchanged'%ch)
    check(new.get('resp')=='#gemini3','Tiberius %d explicitly attributed'%ch)
    oldnotes=orig.xpath('.//t:note[not(contains(.,"Gemini 3"))]',namespaces=ns)
    newnotes=new.xpath('./t:div[@type="unverified-legacy-notes"]/t:ab',namespaces=ns)
    check([''.join(n.itertext()) for n in oldnotes]==[''.join(n.itertext()) for n in newnotes],
          'Tiberius %d inherited notes retained separately'%ch)

# Regressions for specific errors found in the earlier audit.
check('threw about gift-tokens"' in pages[(1,'431')].replace('\n',' '),'Caligula gift-tokens and marker debris restored from source')
for fragment in ['a See note on Vesp. ix.','See Aug. xliii. 1.','• When the water had been let out; cf. Nero, xxvii. 2.']:
    check(fragment in pages[(2,'330')], 'Titus source note retained: '+fragment)
check('amphitheatrea' in pages[(2,'331')],'Titus amphitheatre marker retained')
check('a Cf. Nero, xxxiii. 2 and 3.' in pages[(2,'322')],'Titus note retains Cf., not See')
check('XLV. How grossly' in pages[(1,'355')].replace('\n',' '),'Tiberius 45 already English in OCR')
check('XLVI. In money matters' in pages[(1,'357')].replace('\n',' '),'Tiberius 46 already English in OCR')
check('XLVII. While emperor' in pages[(1,'357')].replace('\n',' '),'Tiberius 47 already English in OCR')
check('XLIII. Secessu' in pages[(1,'353')].replace('\n',' '),'Tiberius 43 source Latin retained')
check('XLIV. Maior' in pages[(1,'355')].replace('\n',' '),'Tiberius 44 source Latin retained')

reader=(out/'READ.html').read_text()
payload=re.search(r'const DATA=(.*);\nconst \$=',reader).group(1)
data=json.loads(payload)
for v in data['volumes']:
    tree=E.parse(str(out/'edition'/('suetonius.rolfe1970.volume%d.ocr.xml'%v['number'])))
    texts=tree.xpath('//t:body/t:div/t:ab',namespaces=ns)
    check([p['text'] for p in v['pages']]==[n.text or '' for n in texts], 'Reader volume %d matches XML'%v['number'])
check([s['chapter'] for s in data['supplements']]==list(range(43,48)),'Reader includes all five supplements')
for s in data['supplements']:
    xmlps=supp.xpath('//t:div[@type="supplement"][@n="%d"]/t:div[@subtype="section"]/t:p'%s['chapter'],namespaces=ns)
    check([p for section in s['sections'] for p in section['paragraphs']]==[''.join(p.itertext()) for p in xmlps],
          'Reader supplement %d matches XML'%s['chapter'])
for path in (out/'edition').glob('*.xml'):
    tree=E.parse(str(path));ids=tree.xpath('//@xml:id',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'})
    check(len(ids)==len(set(ids)),path.name+' IDs unique')
    for resp in tree.xpath('//@resp'):
        for ref in resp.split():
            if ref.startswith('#'): assert ref[1:] in ids

result={'passed':len(checks),'checks':checks,'source_pages':sum(s['pages'] for s in manifest['sources']),
        'supplement_chapters':5,'lexical_emendations_to_ocr':0,'inferred_note_anchors':0,
        'limits':['OCR has not been proofread against page images.',
                  'Notes remain on source pages; individual note completeness and word-level anchors are not certified.',
                  'XML well-formedness and project invariants checked; no claim of full external TEI schema validation.']}
(out/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
