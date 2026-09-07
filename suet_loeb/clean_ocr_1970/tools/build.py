#!/usr/bin/env python3
"""Build a conservative page edition from the supplied OCR, without rewriting it."""
import argparse
import copy
import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from lxml import etree as E

HERE = Path(__file__).resolve().parent
NS = 'http://www.tei-c.org/ns/1.0'
XML = 'http://www.w3.org/XML/1998/namespace'
N = {'t': NS}
FILES = ['suetonius-loeb01-uc1-32106005388886-1788786343.txt',
         'suetonius-loeb-02-uc1-32106005389009-1788786407.txt']

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def el(parent, tag, text=None, **attrs):
    n = E.SubElement(parent, '{%s}%s' % (NS, tag), **attrs)
    n.text = text
    return n

def document(title, ident, description):
    root = E.Element('{%s}TEI' % NS, nsmap={None: NS})
    root.set('{%s}id' % XML, ident)
    h = el(root, 'teiHeader')
    fd = el(h, 'fileDesc')
    ts = el(fd, 'titleStmt')
    el(ts, 'title', title)
    el(ts, 'author', 'Suetonius')
    rs = el(ts, 'respStmt'); el(rs, 'resp', 'English translation in the printed source')
    el(rs, 'name', 'J. C. Rolfe')
    rs = el(ts, 'respStmt'); rs.set('{%s}id' % XML, 'edition-editor')
    el(rs, 'resp', 'OCR preservation, attribution and reading layout; no lexical emendation')
    el(rs, 'name', 'Codex, at the direction of Gregory Crane')
    pub = el(fd, 'publicationStmt'); el(pub, 'p', 'Local working edition, 2026-09-07. Not a proofread critical edition.')
    sd = el(fd, 'sourceDesc'); el(sd, 'p', description)
    enc = el(h, 'encodingDesc'); ed = el(enc, 'editorialDecl')
    el(el(ed, 'correction', method='markup', status='low'), 'p',
       'No words, punctuation, OCR markers or internal line breaks in source-page blocks are corrected. '
       'Only export page delimiters, form-feed characters and boundary whitespace are excluded from those blocks. '
       'Original export files are retained byte for byte.')
    el(el(ed, 'normalization', method='markup'), 'p',
       'Page-based documentary transcription. Notes and apparatus remain in their source-page context. '
       'No inline note anchors or chapter/section boundaries are inferred. All OCR remains unproofread. '
       'Gemini-attributed material is a separate supplement, never substituted for the source.')
    rev = el(h, 'revisionDesc'); el(rev, 'change', 'Created from the supplied OCR with separately labelled inherited supplements.', when='2026-09-07', who='#edition-editor')
    return root, el(el(root, 'text'), 'body')

def write_xml(root, path):
    E.ElementTree(root).write(str(path), encoding='UTF-8', xml_declaration=True, pretty_print=True)

def page_parse(path):
    raw = path.read_text(encoding='utf-8')
    parts = re.split(r'^## p\.\s*(.*?)\s*\(#(\d+)\) #+\n', raw, flags=re.M)
    assert len(parts) > 3 and (len(parts)-1) % 3 == 0
    return [{'label': parts[i].strip(), 'seq': int(parts[i+1]),
             'text': parts[i+2].replace('\f', '').strip()} for i in range(1, len(parts), 3)]

def clean_paragraph(p):
    p = copy.deepcopy(p)
    # Remove apparatus from the reading paragraph, preserving its following text.
    # The apparatus itself is separately transcribed and the original XML is archived.
    for n in list(p.xpath('.//t:note|.//t:pb', namespaces=N)):
        tail = n.tail or ''
        prev = n.getprevious(); parent = n.getparent()
        if prev is None: parent.text = (parent.text or '') + tail
        else: prev.tail = (prev.tail or '') + tail
        parent.remove(n)
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sources', type=Path, default=Path('/Users/gcrane/Downloads'))
    ap.add_argument('--legacy', type=Path, default=Path('/Users/gcrane/github/GRC_misc/suet_loeb/suetonius.tib.loeb_eng1.xml'))
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    out = args.output; out.mkdir(parents=True, exist_ok=True)
    for folder in ['sources', 'edition', 'tools']: (out/folder).mkdir(exist_ok=True)
    records = []; volumes = []
    for v, name in enumerate(FILES, 1):
        source = args.sources/name
        shutil.copy2(source, out/'sources'/name)
        pages = page_parse(source)
        assert [p['seq'] for p in pages] == list(range(1, len(pages)+1))
        desc = ('Supplied HathiTrust OCR of Suetonius with an English translation by J. C. Rolfe, '
                'volume %d, Harvard University Press / William Heinemann, 1970 printing (title page MCMLXX). '
                '%s The export catalogue date 1913–1914 is not the printing date. Source: ../sources/%s; SHA-256 %s.'
                % (v, 'Volume I states Revised and Reprinted 1951.' if v == 1 else 'Volume II lists reprints through 1970.', name, sha(source)))
        root, body = document('Suetonius — Rolfe, 1970 printing — volume %d — OCR page edition' % v, 'suetonius-rolfe-1970-v%d' % v, desc)
        for page in pages:
            div = el(body, 'div', type='source-page', n=str(page['seq']))
            div.set('{%s}id' % XML, 'v%d-s%d' % (v, page['seq']))
            el(div, 'pb', n=page['label'] or '[unnumbered]',
               facs='https://babel.hathitrust.org/cgi/pt?id=uc1.%s&seq=%d' % ('32106005388886' if v == 1 else '32106005389009', page['seq']))
            ab = el(div, 'ab', page['text'], type='unproofread-ocr')
            ab.set('{%s}space' % XML, 'preserve')
        dest = out/'edition'/('suetonius.rolfe1970.volume%d.ocr.xml' % v)
        write_xml(root, dest)
        volumes.append({'number': v, 'pages': pages})
        records.append({'volume': v, 'file': name, 'sha256': sha(source), 'pages': len(pages),
                        'characters_in_page_blocks': sum(len(p['text']) for p in pages)})

    legacy_dest = out/'sources'/'suetonius.tib.loeb_eng1.legacy.xml'
    shutil.copy2(args.legacy, legacy_dest)
    legacy = E.parse(str(args.legacy))
    attribution = legacy.xpath('//t:note[contains(., "Gemini 3")]', namespaces=N)
    assert len(attribution) == 1
    root, body = document('Suetonius, Tiberius 43–47 — inherited Gemini-attributed supplement',
                         'suetonius-tiberius-gemini-supplement',
                         'Copied from ../sources/suetonius.tib.loeb_eng1.legacy.xml, SHA-256 %s. '
                         'The legacy editorial note attributes chapters 43–47 to Gemini 3; this attribution is inherited, '
                         'not independent proof that every sentence was generated by Gemini.' % sha(args.legacy))
    ts = root.find('.//{%s}titleStmt' % NS)
    rs = el(ts, 'respStmt'); rs.set('{%s}id' % XML, 'gemini3')
    el(rs, 'resp', 'Supplementary English translation, attributed in the legacy XML')
    el(rs, 'name', 'Gemini 3')
    el(body, 'head', 'Gemini-attributed supplement — separate from the OCR base')
    el(body, 'p', 'The legacy attribution covers chapters 43–47. In the supplied 1970 OCR, '
       'chapters 43–44 are in Latin in the English column, but chapters 45–47 already appear in English. '
       'All five inherited chapters are retained here without rewriting. Their attribution is not extended to the OCR base.')
    legacy_note = el(body, 'div', type='legacy-attribution')
    el(legacy_note, 'head', 'Original attribution, verbatim; its claim about untranslated chapters 45–47 is inaccurate for this witness')
    el(legacy_note, 'p', ''.join(attribution[0].itertext()))
    supplements = []
    for ch in range(43, 48):
        matches = legacy.xpath('//t:div[@subtype="chapter"][@n="%d"]' % ch, namespaces=N)
        assert len(matches) == 1
        chapter = matches[0]
        div = el(body, 'div', type='supplement', subtype='chapter', n=str(ch), resp='#gemini3')
        div.set('{%s}id' % XML, 'gemini-tib-%d' % ch)
        div.set('{%s}lang' % XML, 'en')
        el(div, 'head', 'Tiberius %d — Gemini-attributed legacy supplement' % ch)
        data = {'chapter': ch, 'sections': [], 'notes': []}
        for section in chapter.xpath('./t:div[@subtype="section"]', namespaces=N):
            sec = el(div, 'div', type='textpart', subtype='section', n=section.get('n'))
            paragraphs = []
            for p in section.xpath('./t:p', namespaces=N):
                copied = clean_paragraph(p)
                # Keep the exact inherited prose; page references are source metadata, not source text.
                text = ''.join(copied.itertext())
                el(sec, 'p', text)
                paragraphs.append(text)
            data['sections'].append({'n': section.get('n'), 'paragraphs': paragraphs})
            for note in section.xpath('.//t:note[not(contains(., "Gemini 3"))]', namespaces=N):
                text = ''.join(note.itertext())
                data['notes'].append({'section': section.get('n'), 'text': text})
        if data['notes']:
            nd = el(div, 'div', type='unverified-legacy-notes')
            el(nd, 'head', 'Inherited editorial notes — original section association retained; word-level placement unverified')
            for note in data['notes']:
                el(nd, 'ab', note['text'], n=note['section'], type='legacy-note')
        supplements.append(data)
    write_xml(root, out/'edition'/'suetonius.tiberius.gemini-supplement.xml')
    manifest = {'edition': 'Suetonius, Rolfe 1970 OCR page edition', 'date': '2026-09-07',
                'base_policy': 'Source-only; no lexical correction; page-resident apparatus; no inferred note anchors.',
                'sources': records, 'legacy_source_sha256': sha(args.legacy),
                'supplement_chapters': list(range(43, 48)),
                'supplement_attribution': 'Inherited Gemini 3 attribution; 45–47 already English in the supplied OCR.',
                'normalization': ['Remove export page delimiter from page blocks', 'Remove form-feed characters',
                                  'Trim page-boundary whitespace; retain all internal characters and line breaks'],
                'status': 'Unproofread OCR; no claim of complete note identification or validated word-level anchors.'}
    (out/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    data = {'volumes': volumes, 'supplements': supplements,
            'attribution': ''.join(attribution[0].itertext())}
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    template = (HERE/'reader.html').read_text()
    (out/'READ.html').write_text(template.replace('/*EDITION_DATA*/null', payload))
    shutil.copy2(HERE/'README.md', out/'README.md')
    for name in ['build.py', 'validate.py', 'reader.html', 'README.md']:
        shutil.copy2(HERE/name, out/'tools'/name)
    print(json.dumps(manifest, indent=2))

if __name__ == '__main__': main()
