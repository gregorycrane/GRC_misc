#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract ENGLISH XML from a TEI file, preserving markup and characters exactly.
- Detects top-most English blocks via @xml:lang or @lang beginning with 'en',
  and also <div type="translation">.
- Deep-copies selected nodes; **all descendants are kept**, including <pb/>.
- Optional: --drop-notes removes only <note> elements (does NOT touch <pb/>).
"""
import argparse
from lxml import etree as LET
from copy import deepcopy

TEI_NS = "http://www.tei-c.org/ns/1.0"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS = {"tei": TEI_NS, "xml": XML_NS}

def is_en(val):
    if not val:
        return False
    v = val.strip().lower()
    return v == "en" or v.startswith("en-")

def find_top_english(root):
    candidates = []
    # any element with xml:lang or @lang = en*
    for el in root.xpath(".//*[@xml:lang] | .//*[@lang]"):
        lang = el.get(f"{{{XML_NS}}}lang") or el.get("lang")
        if is_en(lang):
            candidates.append(el)
    # any explicit translation div
    candidates += root.xpath(".//tei:div[@type='translation']", namespaces=NS)

    # unique preserve order
    seen = set()
    uniq = []
    for el in candidates:
        if el in seen:
            continue
        seen.add(el)
        uniq.append(el)

    # keep top-most only
    cand_set = set(uniq)
    tops = []
    for el in uniq:
        parent = el.getparent()
        keep = True
        while parent is not None:
            if parent in cand_set:
                keep = False
                break
            parent = parent.getparent()
        if keep:
            tops.append(el)

    # fallback
    if not tops:
        b = root.find(".//tei:body", namespaces=NS)
        if b is not None:
            tops = [b]
        else:
            t = root.find(".//tei:text", namespaces=NS)
            if t is not None:
                tops = [t]
    return tops

def build_new_tei(header_src, english_blocks, drop_notes=False):
    tei = LET.Element(f"{{{TEI_NS}}}TEI", nsmap={None: TEI_NS, "xml": XML_NS})
    if header_src is not None:
        tei.append(deepcopy(header_src))
    text = LET.SubElement(tei, f"{{{TEI_NS}}}text")
    body = LET.SubElement(text, f"{{{TEI_NS}}}body")

    for blk in english_blocks:
        cp = deepcopy(blk)
        if drop_notes:
            # remove only notes; do NOT touch <pb/>
            for n in list(cp.xpath(".//tei:note", namespaces=NS)):
                par = n.getparent()
                if par is not None:
                    par.remove(n)
        body.append(cp)
    return tei

def main():
    ap = argparse.ArgumentParser(description="Extract ENGLISH XML from TEI (preserving markup/characters).")
    ap.add_argument("input_xml")
    ap.add_argument("-o", "--output", help="Output TEI XML path (default: *_english.xml)")
    ap.add_argument("--no-header", action="store_true", help="Do not copy <teiHeader> into output")
    ap.add_argument("--drop-notes", action="store_true", help="Remove all <note> elements from the English blocks")
    args = ap.parse_args()

    parser = LET.XMLParser(remove_blank_text=False, recover=False, huge_tree=True)
    tree = LET.parse(args.input_xml, parser)
    root = tree.getroot()

    header = root.find(".//tei:teiHeader", namespaces=NS)
    english_blocks = find_top_english(root)

    if not english_blocks:
        raise SystemExit("No English blocks detected. Try setting xml:lang='en' on the translation container.")

    out_tei = build_new_tei(None if args.no_header else header, english_blocks, drop_notes=args.drop_notes)

    out_path = args.output or (args.input_xml.rsplit(".",1)[0] + "_english.xml")
    with open(out_path, "wb") as f:
        f.write(LET.tostring(out_tei, xml_declaration=True, encoding="UTF-8", pretty_print=True))
    print(out_path)

if __name__ == "__main__":
    main()
