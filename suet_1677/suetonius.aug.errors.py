"""
OCR error corrections for Suetonius, Life of Augustus (1677 English translation)
Chapters 1–15

Each entry maps the erroneous OCR string to its correction.
Long ſ is preserved as original orthography throughout.

Errors are grouped by type with chapter references in comments.
"""

ocr_errors = {

    # =====================================================================
    # 1. CT-LIGATURE MISREADINGS (ct read as ft, ff, or it)
    # =====================================================================
    "Oftavius": "Octavius",          # ch.1, ch.3
    "Oitavia": "Octavia",            # ch.4 ("Octavia the younger")
    "Affium": "Actium",              # ch.9
    "Auguftus": "Auguſtus",          # ch.13 §3

    # =====================================================================
    # 2. GARBLED / LATEX-LIKE OCR ARTIFACTS
    # =====================================================================
    "$A/ia$": "Aſia",                # ch.3
    "$A_{H}g_{H}ft_{HS}$": "Auguſtus",  # ch.5
    "$Ce\\int ar$": "Cæſar",         # ch.8, ch.10 (multiple occurrences)

    # =====================================================================
    # 3. U/N CONFUSION (similar letterforms in old type)
    # =====================================================================
    "Tullins": "Tullius",            # ch.2
    "Cains": "Caius",                # ch.2
    "Angustus": "Auguſtus",          # ch.2 ("Angustus his great Grand-father")
    "Martins": "Martius",            # ch.3 ("Campus Martius")
    "Hirtins": "Hirtius",            # ch.10
    "Angures": "Augures",            # ch.7
    "Prifcus": "Priſcus",            # ch.2 ("Tarquinius Priscus")

    # =====================================================================
    # 4. LONG-S (ſ) DROPPED → PLAIN f
    #    Where the original print clearly has ſ but OCR rendered f.
    #    Only listing distinctive words, not every instance of common
    #    words like "fome"→"ſome" which recur dozens of times.
    # =====================================================================

    # --- Unique or distinctive words (not recurring throughout) ---
    "confecrated": "conſecrated",    # ch.1, ch.5, ch.7
    "facrificing": "ſacrificing",    # ch.1, ch.14
    "Magiftracy": "Magiſtracy",      # ch.2
    "fuffrage": "ſuffrage",          # ch.2
    "greateft": "greateſt",          # ch.2
    "Beffi": "Beſſi",                # ch.3
    "Caffius": "Caſſius",            # ch.4, ch.9, ch.10
    "Parmenfis": "Parmenſis",        # ch.4
    "Poffeffor": "Poſſeſſor",        # ch.5, ch.6
    "furpriſed": "ſurpriſed",        # ch.6
    "inconfiderately": "inconſiderately",  # ch.6
    "Teftament": "Teſtament",        # ch.7
    "curiofities": "curioſities",    # ch.7
    "Perufium": "Peruſium",          # ch.9
    "plaufible": "plauſible",        # ch.10
    "profecute": "proſecute",        # ch.10
    "vigouroufly": "vigourouſly",    # ch.10
    "defſiſted": "deſiſted",         # ch.10 (extra f AND dropped ſ)
    "afſlaſſinate": "aſſaſſinate",   # ch.10 (transposed letters)
    "difcover'd": "diſcover'd",      # ch.10
    "infinuated": "inſinuated",      # ch.10
    "fubrogated": "ſubrogated",      # ch.10
    "defperately": "deſperately",    # ch.10
    "poffeflion": "poſſeſſion",      # ch.11
    "confufion": "confuſion",        # ch.11
    "fatisfied": "ſatisfied",        # ch.13
    "prefuming": "preſuming",        # ch.14
    "facrificed": "ſacrificed",      # ch.15
    "Prifoners": "Priſoners",        # ch.15
    "Confuls": "Conſuls",            # ch.10 (and recurring)
    "Confulſhip": "Conſulſhip",      # ch.4 (and recurring)

    # --- High-frequency words (ſ dropped → f) ---
    # These recur many times across chapters 1–15.
    "fome": "ſome",
    "fide": "ſide",
    "felf": "ſelf",
    "himfelf": "himſelf",
    "fays": "ſays",
    "fate": "ſate",                  # ch.2 ("which ſate in the Senate")
    "fuddenly": "ſuddenly",
    "fudden": "ſudden",
    "fent": "ſent",
    "foon": "ſoon",
    "fuch": "ſuch",
    "fmall": "ſmall",
    "fickness": "ſickneſs",
    "fecond": "ſecond",
    "fole": "ſole",
    "flain": "ſlain",
    "faid": "ſaid",
    "fincere": "ſincere",
    "fubmitted": "ſubmitted",
    "furrender": "ſurrender",
    "furname": "ſurname",
    "faluted": "ſaluted",
    "fufficient": "ſufficient",
    "fatisfied": "ſatisfied",
    "befides": "beſides",
    "abfent": "abſent",
    "refolve": "reſolve",
    "refolv'd": "reſolv'd",
    "repofe": "repoſe",
    "promife": "promiſe",
    "affum'd": "aſſum'd",
    "befieg'd": "beſieg'd",
    "deferv'd": "deſerv'd",
    "elfe": "elſe",

    # =====================================================================
    # 5. MISSING / EXTRA / WRONG CHARACTERS
    # =====================================================================
    "neceſſlity": "neceſſity",       # ch.6 (spurious 'l')
    "CaShier": "Caſhier",            # ch.4 (spurious capital S)
    "duxty": "durty",                # ch.4 (r misread as x)
    "plaod": "plac'd",               # ch.13 (missing 'c' and apostrophe)
    "Antoniu,": "Antonius,",         # ch.15 (missing final 's')
    "Prator": "Prætor",              # ch.10 (missing æ ligature)

    # =====================================================================
    # 6. MISSING WORD BREAKS
    # =====================================================================
    "allhis": "all his",             # ch.10
    "fuchas": "ſuch as",             # ch.12
    "toimitate": "to imitate",       # ch.3

    # =====================================================================
    # 7. WRONG WORD (misread from similar letterforms)
    # =====================================================================
    "Tome time": "ſome time",        # ch.8 (ſ misread as T)
    "Cafe": "Caſe",                  # ch.8 (ſ dropped)
    "fame": "ſame",                  # ch.10 ("the ſame practices")
    "Cafar": "Cæſar",                # ch.2 and throughout (æ→a, ſ→f)
    "eft.": "eſt.",                  # ch.7 (Latin quote: "Roma eſt.")

}


# =====================================================================
# Notes
# =====================================================================
#
# The above dictionary covers errors found in chapters 1–15 of the
# XML transcription compared against the 1677 PDF page images.
#
# "Cafar" → "Cæſar" is the single most frequent error, appearing
# in nearly every chapter. It combines two issues: the æ ligature
# rendered as plain 'a', and the long ſ rendered as 'f'.
#
# The long-s (ſ) → f errors are extremely pervasive. The entries
# above capture the most common and distinctive instances, but many
# additional occurrences of the same words exist throughout the text.
#
# Some readings are ambiguous (e.g. "Mortius Philippus" in ch.8
# matches the PDF and may be the translator's rendering of "Marcius").
# These have been excluded from the error list.


"""
OCR error corrections for Suetonius, Life of Augustus (1677 English translation)
Chapters 16–30

Each entry maps the erroneous OCR string to its correction.
Long ſ is preserved as original orthography throughout.

Errors are grouped by type with chapter references in comments.
"""

ocr_errors_ch16_30 = {

    # =====================================================================
    # 1. U/N CONFUSION (similar letterforms in old type)
    # =====================================================================
    "Domitinus": "Domitius",          # ch.17 ("Tr. Domitius")

    # =====================================================================
    # 2. M/N CONFUSION
    # =====================================================================
    "from then,": "from them,",       # ch.16 §3 ("escape from them")

    # =====================================================================
    # 3. SPURIOUS ACCENT
    # =====================================================================
    "Capitólinus": "Capitolinus",     # ch.30 (spurious accent on 'o')

    # =====================================================================
    # 4. LONG-S (ſ) DROPPED → PLAIN f
    #    Where the original print clearly has ſ but OCR rendered f.
    # =====================================================================

    # --- Proper names ---
    "Sofius": "Soſius",               # ch.17 ("C. Soſius")
    "Pfilli": "Pſilli",               # ch.17 (the snake-bite healers)
    "Audafius": "Audaſius",           # ch.19 ("L. Audaſius")

    # --- Distinctive words (not in ch.1–15 dictionary) ---
    "fleep": "ſleep",                 # ch.16
    "fignal": "ſignal",               # ch.16
    "folemn": "ſolemn",               # ch.16 (and recurring)
    "fuffer": "ſuffer",               # ch.16 (and recurring)
    "infolent": "inſolent",           # ch.16
    "foveraignty": "ſoveraignty",     # ch.16
    "difpenc'd": "diſpenc'd",         # ch.17
    "feveral": "ſeveral",             # ch.17 (and recurring)
    "fuck": "ſuck",                   # ch.17 (ſ dropped: "to ſuck out the poiſon")
    "defire": "deſire",               # ch.17 (and recurring)
    "fatisfied": "ſatisfied",         # ch.17 §3 (also in ch.1–15 dict)
    "fent": "ſent",                   # ch.17 §3 (also in ch.1–15 dict)
    "Confuls": "Conſuls",             # ch.17 (also in ch.1–15 dict)
    "occafion": "occaſion",           # ch.20 (and recurring)
    "perfons": "perſons",             # ch.21 (and recurring)
    "perfon": "perſon",               # ch.20 (and recurring)
    "alfo": "alſo",                   # ch.21 (and recurring)
    "fometimes": "ſometimes",         # ch.21 (and recurring)
    "fet": "ſet",                     # ch.23 (and recurring)
    "fo": "ſo",                       # ch.23 (and recurring)
    "fame": "ſame",                   # ch.21 (and recurring; also in ch.1–15)

    # --- Ch.23 specific ---
    # Note: "times" in "many times against the doors" is CORRECT (not "tinres")

    # --- Ch.24 ---
    "difenable": "diſenable",         # ch.24

    # --- Ch.25 ---
    "feldom": "ſeldom",               # ch.25

    # --- Ch.27 ---
    "Saturnius": "Saturninus",        # ch.27 — PDF shows "Saturnius" matching XML,
                                      # but the correct name is "Saturninus";
                                      # this is likely a u/n confusion in the
                                      # 1677 print itself rather than an OCR error.
                                      # Included here for completeness.

    # --- Ch.29 ---
    # "Cawſeys" is correct 17th-c. spelling for "causeways" — not an error

    # =====================================================================
    # 5. HIGH-FREQUENCY ſ→f WORDS (recurring across ch.16–30)
    #    Many of these also appear in the ch.1–15 dictionary.
    # =====================================================================
    "himfelf": "himſelf",
    "fome": "ſome",
    "fuch": "ſuch",
    "fide": "ſide",
    "faid": "ſaid",
    "elfe": "elſe",
    "felf": "ſelf",
}


# =====================================================================
# COMBINED dictionary: merges ch.1–15 and ch.16–30
# =====================================================================

# Import ch.1–15 errors (from ocr_errors.py)
# from ocr_errors import ocr_errors as ocr_errors_ch1_15

ocr_errors_ch1_15 = {
    # CT-LIGATURE MISREADINGS
    "Oftavius": "Octavius",
    "Oitavia": "Octavia",
    "Affium": "Actium",
    "Auguftus": "Auguſtus",
    # GARBLED OCR ARTIFACTS
    "$A/ia$": "Aſia",
    "$A_{H}g_{H}ft_{HS}$": "Auguſtus",
    "$Ce\\int ar$": "Cæſar",
    # U/N CONFUSION
    "Tullins": "Tullius",
    "Cains": "Caius",
    "Angustus": "Auguſtus",
    "Martins": "Martius",
    "Hirtins": "Hirtius",
    "Angures": "Augures",
    "Prifcus": "Priſcus",
    # LONG-S DROPPED (distinctive words)
    "confecrated": "conſecrated",
    "facrificing": "ſacrificing",
    "Magiftracy": "Magiſtracy",
    "fuffrage": "ſuffrage",
    "greateft": "greateſt",
    "Beffi": "Beſſi",
    "Caffius": "Caſſius",
    "Parmenfis": "Parmenſis",
    "Poffeffor": "Poſſeſſor",
    "furpriſed": "ſurpriſed",
    "inconfiderately": "inconſiderately",
    "Teftament": "Teſtament",
    "curiofities": "curioſities",
    "Perufium": "Peruſium",
    "plaufible": "plauſible",
    "profecute": "proſecute",
    "vigouroufly": "vigourouſly",
    "defſiſted": "deſiſted",
    "afſlaſſinate": "aſſaſſinate",
    "difcover'd": "diſcover'd",
    "infinuated": "inſinuated",
    "fubrogated": "ſubrogated",
    "defperately": "deſperately",
    "poffeflion": "poſſeſſion",
    "confufion": "confuſion",
    "prefuming": "preſuming",
    "facrificed": "ſacrificed",
    "Prifoners": "Priſoners",
    "Confulſhip": "Conſulſhip",
    # LONG-S DROPPED (high-frequency)
    "fome": "ſome",
    "fide": "ſide",
    "felf": "ſelf",
    "himfelf": "himſelf",
    "fays": "ſays",
    "fate": "ſate",
    "fuddenly": "ſuddenly",
    "fudden": "ſudden",
    "fent": "ſent",
    "foon": "ſoon",
    "fuch": "ſuch",
    "fmall": "ſmall",
    "fickness": "ſickneſs",
    "fecond": "ſecond",
    "fole": "ſole",
    "flain": "ſlain",
    "faid": "ſaid",
    "fincere": "ſincere",
    "fubmitted": "ſubmitted",
    "furrender": "ſurrender",
    "furname": "ſurname",
    "faluted": "ſaluted",
    "fufficient": "ſufficient",
    "fatisfied": "ſatisfied",
    "befides": "beſides",
    "abfent": "abſent",
    "refolve": "reſolve",
    "refolv'd": "reſolv'd",
    "repofe": "repoſe",
    "promife": "promiſe",
    "affum'd": "aſſum'd",
    "befieg'd": "beſieg'd",
    "deferv'd": "deſerv'd",
    "elfe": "elſe",
    # MISSING/EXTRA/WRONG CHARACTERS
    "neceſſlity": "neceſſity",
    "CaShier": "Caſhier",
    "duxty": "durty",
    "plaod": "plac'd",
    "Antoniu,": "Antonius,",
    "Prator": "Prætor",
    # MISSING WORD BREAKS
    "allhis": "all his",
    "fuchas": "ſuch as",
    "toimitate": "to imitate",
    # WRONG WORD
    "Tome time": "ſome time",
    "Cafe": "Caſe",
    "fame": "ſame",
    "Cafar": "Cæſar",
    "eft.": "eſt.",
}

# Merge both dictionaries
all_ocr_errors = {**ocr_errors_ch1_15, **ocr_errors_ch16_30}

if __name__ == "__main__":
    print(f"Ch.1–15 errors:  {len(ocr_errors_ch1_15)}")
    print(f"Ch.16–30 errors: {len(ocr_errors_ch16_30)}")
    print(f"Combined total:  {len(all_ocr_errors)}")
    print()
    print("=== New errors in ch.16–30 (not in ch.1–15) ===")
    new_keys = set(ocr_errors_ch16_30.keys()) - set(ocr_errors_ch1_15.keys())
    for k in sorted(new_keys):
        print(f"  {k!r:30s} → {ocr_errors_ch16_30[k]!r}")


"""
OCR error corrections for Suetonius, Life of Augustus (1677 English translation)
Chapters 31–45

Each entry maps the erroneous OCR string to its correction.
Long ſ is preserved as original orthography throughout.

Errors are grouped by type with chapter references in comments.
"""

ocr_errors_ch31_45 = {

    # =====================================================================
    # 1. MISSING CHARACTERS
    # =====================================================================
    "unknow ": "unknown ",            # ch.31 (missing final 'n')
    "pople": "people",                # ch.43 (missing 'e': "the pople")

    # =====================================================================
    # 2. GARBLED / WRONG CHARACTERS
    # =====================================================================
    "Sunıptuary": "Sumptuary",        # ch.34 (dotless ı for m, n→m)
    "ſuſhcient": "ſufficient",        # ch.35 (h for f, missing f)
    "ſnould": "ſhould",               # ch.32 (n for h)
    "refolutión": "reſolutión",       # ch.40 (ſ→f; accent may be spurious too)

    # =====================================================================
    # 3. MISSING WORD BREAKS
    # =====================================================================
    "ifany": "if any",                # ch.32
    "heappointed": "he appointed",    # ch.33
    "Hebrought": "He brought",        # ch.43

    # =====================================================================
    # 4. SPURIOUS WORD BREAKS
    # =====================================================================
    "fre quently": "frequently",      # ch.38 (spurious space + ſ→f)
    "Centumvir al": "Centumviral",    # ch.36 (spurious space)

    # =====================================================================
    # 5. MISSING LIGATURES / WRONG VOWELS
    # =====================================================================
    "Quastors": "Quæſtors",           # ch.36 (æ→a, ſ→f — recurring)
    "Prators": "Prætors",             # ch.36 (æ→a)

    # =====================================================================
    # 6. LONG-S (ſ) DROPPED → PLAIN f
    #    Only listing words NEW to this chapter range (not in ch.1–30).
    # =====================================================================

    # --- Proper names ---
    "Afprenas": "Aſprenas",           # ch.43

    # --- Distinctive words ---
    "neceffity": "neceſſity",         # ch.31 (ſſ→ff)
    "reafon": "reaſon",              # ch.31 (and recurring)
    "fquallour": "ſquallour",        # ch.32
    "fuppreft": "ſuppreſt",          # ch.32
    "fervants": "ſervants",          # ch.32
    "factions": "factions",          # ch.32 — NOTE: "factions" is correct! 
                                     # (the 'f' is genuine, not a long-s)
    "indifpofition": "indiſpoſition", # ch.33
    "refcue": "reſcue",              # ch.33
    "fack": "ſack",                  # ch.33
    "furprize": "ſurprize",          # ch.33
    "Confulary": "Conſulary",        # ch.33
    "confifting": "conſiſting",      # ch.35
    "Feafts": "Feaſts",             # ch.35
    "Magiftrates": "Magiſtrates",    # ch.36 (and recurring)
    "fhould": "ſhould",             # ch.36 (recurring, very common)
    "fum": "ſum",                    # ch.36
    "afide": "aſide",               # ch.37
    "chofen": "choſen",             # ch.37 (and recurring)
    "Tranfvection": "Tranſvection",  # ch.38
    "horfes": "horſes",             # ch.38
    "leflen'd": "leſſen'd",         # ch.40 (ſſ→ff→fl)
    "Aflemblies": "Aſſemblies",     # ch.40
    "diftributed": "diſtributed",   # ch.40
    "fecure": "ſecure",             # ch.41
    "feventeen": "ſeventeen",       # ch.41
    "Sefterces": "Seſterces",       # ch.41 (inconsistent — correct form 
                                     # also appears elsewhere)
    "folicitous": "ſolicitous",     # ch.42
    "difcipline": "diſcipline",     # ch.42
    "fcarcity": "ſcarcity",         # ch.42
    "folemnity": "ſolemnity",       # ch.43 (and recurring)
    "confufions": "confuſions",     # ch.44
    "Affemblies": "Aſſemblies",     # ch.44 (variant of Aflemblies)
    "diftinguiſhed": "diſtinguiſhed", # ch.44 (mixed: diſt→dift)
    "afligned": "aſſigned",         # ch.44
    "Wreftlers": "Wreſtlers",       # ch.44
    "defiring": "deſiring",         # ch.44
    "diffimulation": "diſſimulation", # ch.45
    "confideration": "conſideration", # ch.45
    "deferts": "deſerts",           # ch.45 (and recurring)
    "fevere": "ſevere",             # ch.45 (and recurring)

    # --- High-frequency ſ→f words (also in earlier chapters) ---
    "fome": "ſome",
    "fuch": "ſuch",
    "fexes": "ſexes",
    "fome": "ſome",
    "perfon": "perſon",
    "occafion": "occaſion",
    "Caufes": "Cauſes",
    "alfo": "alſo",
    "fometimes": "ſometimes",
    "feveral": "ſeveral",
}


# =====================================================================
# Remove the incorrect "factions" entry (genuine 'f', not long-s)
# =====================================================================
del ocr_errors_ch31_45["factions"]


if __name__ == "__main__":
    print(f"Ch.31–45 errors: {len(ocr_errors_ch31_45)}")
    print()
    print("=== All entries ===")
    for k, v in ocr_errors_ch31_45.items():
        print(f"  {k!r:30s} → {v!r}")


"""
OCR error corrections for Suetonius, Life of Augustus (1677 English translation)
Chapters 46–60

Each entry maps the erroneous OCR string to its correction.
Long ſ is preserved as original orthography throughout.

Errors are grouped by type with chapter references in comments.
"""

ocr_errors_ch46_60 = {

    # =====================================================================
    # 1. MISSING WORD BREAKS
    # =====================================================================
    "himſelfto": "himſelf to",        # ch.51
    "Heunderstood": "He underſtood",  # ch.52 (also ſ→f in "understood")
    "whomalſo": "whom alſo",          # ch.53

    # =====================================================================
    # 2. SPURIOUS WORD BREAKS / HYPHENS
    # =====================================================================
    "E- nemy": "Enemy",               # ch.56 (spurious space + hyphen)

    # =====================================================================
    # 3. WRONG / GARBLED CHARACTERS
    # =====================================================================
    "hioown": "his own",              # ch.54 (garbled: "s " → "o")
    "reſfcued": "reſcued",            # ch.56 (extra 'f')
    "Malefaltor": "Malefactor",       # ch.56 (ct ligature → lt; also ſ→f)
    "impreflion": "impreſſion",       # ch.50 (ſſ → fl)

    # =====================================================================
    # 4. MISSING LIGATURES
    # =====================================================================
    "Cafaria": "Cæſaria",             # ch.60 (æ→a, ſ→f)
    "Cæfar": "Cæſar",                # ch.58 (ſ→f; note: æ preserved here)

    # =====================================================================
    # 5. LONG-S (ſ) DROPPED → PLAIN f
    #    Only listing words NEW to this chapter range.
    # =====================================================================

    # --- Proper names ---
    "Diafcorides": "Diaſcorides",     # ch.50
    "Caffius Patavinus": "Caſſius Patavinus",  # ch.51
    "Antiftius": "Antiſtius",         # ch.54
    "Caftricius": "Caſtricius",       # ch.56
    "Meffala": "Meſſala",             # ch.58 (inconsistent — correct form 
                                       # "Meſſala" also appears)

    # --- Distinctive words ---
    "exhaufted": "exhauſted",         # ch.46
    "fuffrages": "ſuffrages",         # ch.46
    "whatfoever": "whatſoever",        # ch.46 (and recurring)
    "eafie": "eaſie",                 # ch.47
    "fafe": "ſafe",                   # ch.47
    "licentioufneſs": "licentiouſneſs",  # ch.47
    "purfued": "purſued",             # ch.47
    "inftructed": "inſtructed",       # ch.48
    "Tuskan": "Tuſkan",              # ch.49 — note: PDF shows "Tuſkan"
    "difpofed": "diſpoſed",          # ch.49
    "fedition": "ſedition",          # ch.49
    "impofed": "impoſed",            # ch.49
    "refpect": "reſpect",            # ch.49 (and recurring)
    "fucceſſors": "ſucceſſors",      # ch.50
    "figned": "ſigned",              # ch.50
    "defamatory": "defamatory",      # ch.51 — NOTE: actually correct!
                                      # "de-" prefix + "famatory", the f 
                                      # is genuine. REMOVE below.
    "infolence": "inſolence",        # ch.51
    "preffing": "preſſing",          # ch.51 (ſſ→ff)
    "allufion": "alluſion",          # ch.53
    "pleafantneſs": "pleaſantneſs",  # ch.53
    "Sponfal": "Sponſal",            # ch.53
    "refolving": "reſolving",        # ch.53
    "perſwafions": "perſwaſions",    # ch.53
    "difparagement": "diſparagement", # ch.55
    "oppofed": "oppoſed",            # ch.55
    "difpoſſeſs": "diſpoſſeſs",     # ch.56
    "demonftration": "demonſtration", # ch.56
    "filently": "ſilently",          # ch.56
    "Cafes": "Caſes",                # ch.56 (and recurring)
    "accufed": "accuſed",            # ch.56 (and recurring)
    "confulted": "conſulted",        # ch.56
    "profperity": "proſperity",      # ch.57
    "conftantly": "conſtantly",      # ch.57
    "forts": "ſorts",                # ch.57
    "univerfal": "univerſal",        # ch.58
    "faluted": "ſaluted",            # ch.58 (also in ch.1-15 dict)
    "fickneſs": "ſickneſs",          # ch.59 (also in ch.1-15 dict)
    "inftituted": "inſtituted",      # ch.59
    "confent": "conſent",            # ch.60 (and recurring)

    # --- High-frequency ſ→f (also in earlier chapters) ---
    "fome": "ſome",
    "fuch": "ſuch",
    "feveral": "ſeveral",
    "perfon": "perſon",
    "perfons": "perſons",
    "occafion": "occaſion",
    "faid": "ſaid",
    "alfo": "alſo",
    "fet": "ſet",                     # ch.52 ("ſet up", "ſet down")
    "fold": "ſold",                   # ch.52 ("melted down, and ſold")
}

# Remove the incorrect entry
del ocr_errors_ch46_60["defamatory"]  # genuine 'f', not long-s


if __name__ == "__main__":
    print(f"Ch.46–60 errors: {len(ocr_errors_ch46_60)}")
    print()
    print("=== All entries ===")
    for k, v in ocr_errors_ch46_60.items():
        print(f"  {k!r:30s} → {v!r}")

"""
OCR error corrections for Suetonius, Life of Augustus (1677 English translation)
Chapters 61–75

Each entry maps the erroneous OCR string to its correction.
Long ſ is preserved as original orthography throughout.
"""

ocr_errors_ch61_75 = {

    # =====================================================================
    # 1. U/N CONFUSION (recurring from earlier chapters)
    # =====================================================================
    "Cains": "Caius",                  # ch.64 (recurring from ch.2)
    "Cenfors": "Cenſors",             # ch.64 (u→n AND ſ→f)

    # =====================================================================
    # 2. MISSING / WRONG CHARACTERS
    # =====================================================================
    "certan ": "certain ",             # ch.69 (missing 'i')
    "to slay": "to day",              # ch.71 (d misread as ſl — PDF p.123
                                       # clearly shows "both yeſterday and to day")
    "poflible": "poſſible",           # ch.61 (ſſ→fl)
    "pub-lick": "publick",            # ch.64 (spurious hyphen from line break)

    # =====================================================================
    # 3. REPEATED WORD
    # =====================================================================
    "be be ſtript": "be ſtript",       # ch.69 (duplicated "be")

    # =====================================================================
    # 4. LONG-S (ſ) DROPPED → PLAIN f
    #    Only listing words NEW to this chapter range.
    # =====================================================================

    # --- Proper names ---
    "Ifauricus": "Iſauricus",         # ch.62
    "Marfelles": "Marſeilles",        # ch.65 (ſ→f; also 'i' missing)
    "Sifter": "Siſter",              # ch.63 (and recurring)
    "Epiftles": "Epiſtles",          # ch.70

    # --- Distinctive words ---
    "controverfies": "controverſies",  # ch.62
    "Confular": "Conſular",           # ch.62
    "fordid": "ſordid",              # ch.65
    "Quastor": "Quæſtor",            # ch.65 (æ→a AND ſ→f)
    "Confidents": "Confidents",       # ch.65 — NOTE: genuine 'f' (con-fidents)
    "fcars": "ſcars",                # ch.65
    "impofthumes": "impoſthumes",    # ch.65
    "fowr": "ſowr",                  # ch.66
    "defperate": "deſperate",        # ch.66
    "fufpicion": "ſuſpicion",        # ch.66 (ſ→f twice)
    "difpleafure": "diſpleaſure",    # ch.66 (ſ→f twice)
    "prefumption": "preſumption",    # ch.67
    "infolently": "inſolently",      # ch.67
    "ficknefs": "ſickneſs",          # ch.67 (ſ→f twice; variant of fickneſs)
    "reprefenting": "repreſenting",  # ch.70
    "Cefar": "Cæſar",               # ch.70 (æ→e, ſ→f)
    "farcaſine": "ſarcaſme",         # ch.70 (ſ→f; also n→m possible)
    "profcrib": "proſcrib",          # ch.70 (prefix)
    "cafily": "eaſily",             # ch.71 (initial e dropped + ſ→f)
    "flander": "ſlander",           # ch.71
    "fomething": "ſomething",        # ch.71 (and recurring)
    "confiderable": "conſiderable",  # ch.72
    "houfes": "houſes",             # ch.72 (and recurring)
    "parfimony": "parſimony",       # ch.73
    "fcanty": "ſcanty",             # ch.73
    "facctious": "facetious",       # ch.74 (ſ→f? No — this is ct→cct;
                                     # the word should be "facetious")
    "fpeak": "ſpeak",               # ch.74
    "Aftrologers": "Aſtrologers",   # ch.74
    "Philofophers": "Philoſophers", # ch.74
    "feafts": "feaſts",             # ch.74
    "fwim": "ſwim",                 # ch.64

    # --- High-frequency (also in earlier chapters) ---
    "fome": "ſome",
    "fuch": "ſuch",
    "feveral": "ſeveral",
    "perfon": "perſon",
    "perfons": "perſons",
    "alfo": "alſo",
    "faid": "ſaid",
    "fometimes": "ſometimes",
    "himfelf": "himſelf",
    "Grand-fon": "Grand-ſon",
}

# Fix: "Confidents" is genuine 'f', remove
# Also fix "cafily" - looking at PDF p.123 it shows "eaſily" but XML has "cafily"
# Actually re-examining: the XML has "cafily" which = "eaſily" with 'e' dropped and ſ→f

# Fix facctious - PDF p.126 shows "facetious" but XML has "facctious"
# This combines ct→cct error AND the word is actually "facetious" not "facctious"

if __name__ == "__main__":
    print(f"Ch.61–75 errors: {len(ocr_errors_ch61_75)}")
    print()
    # Show just the new distinctive entries
    common = {"fome","fuch","feveral","perfon","perfons","alfo","faid",
              "fometimes","himfelf","Grand-fon"}
    print("=== New distinctive entries ===")
    for k, v in ocr_errors_ch61_75.items():
        if k not in common:
            print(f"  {k!r:30s} → {v!r}")


"""
OCR error corrections for Suetonius, Life of Augustus (1677 English translation)
Chapters 76–90

Each entry maps the erroneous OCR string to its correction.
Long ſ is preserved as original orthography throughout.
"""

ocr_errors_ch76_90 = {

    # =====================================================================
    # 1. U/N CONFUSION
    # =====================================================================
    "Cornelins": "Cornelius",          # ch.77

    # =====================================================================
    # 2. SPURIOUS WORD BREAKS
    # =====================================================================
    "interrupti ons": "interruptions",  # ch.78
    "re poſe": "repoſe",              # ch.78
    "whi ther": "whither",            # ch.82
    "under- Stand": "underſtand",     # ch.86 (also ſ→f and S→ſ)
    "Pul leiaceius": "Pulleiaceius",  # ch.87
    "Sylla bles": "Syllables",        # ch.88
    "Apollodo- Yus": "Apollodorus",   # ch.89 (line-break error + Y→r)

    # =====================================================================
    # 3. MISSING WORD BREAKS
    # =====================================================================
    "Authorswhich": "Authors which",   # ch.89

    # =====================================================================
    # 4. SPURIOUS ACCENT
    # =====================================================================
    "ágain": "again",                  # ch.80

    # =====================================================================
    # 5. LONG-S (ſ) DROPPED → PLAIN f
    #    Only listing words NEW to this chapter range.
    # =====================================================================

    # --- Proper names ---
    "Rhatian": "Rhætian",             # ch.77 (æ→a also)
    "Saluftius": "Saluſtius",         # ch.86
    "Afiatick": "Aſiatick",           # ch.86
    "Dionyfius": "Dionyſius",         # ch.89
    "Spharus": "Sphærus",            # ch.89 (æ→a also)

    # --- Distinctive words ---
    "ufually": "uſually",             # ch.76
    "Houfhold": "Houſhold",           # ch.76
    "paffing": "paſſing",             # ch.76 (ſſ→ff)
    "fextants": "ſextants",           # ch.77
    "feldom": "ſeldom",               # ch.77
    "Domefticks": "Domeſticks",       # ch.78
    "filent": "ſilent",               # ch.79
    "ferenity": "ſerenity",           # ch.79
    "pafling": "paſſing",             # ch.79 (variant: ſſ→fl — same word)
    "fomewhat": "ſomewhat",           # ch.79
    "ftood": "ſtood",                 # ch.79
    "fomentation": "fomentation",     # ch.80 — NOTE: genuine 'f'! REMOVE
    "Phyfick": "Phyſick",             # ch.81
    "fomentations": "fomentations",   # ch.81 — NOTE: genuine 'f'! REMOVE
    "fubject": "ſubject",             # ch.81
    "conftant": "conſtant",           # ch.81
    "feafons": "ſeaſons",             # ch.81 (double ſ→f)
    "Waftcoat": "Waſtcoat",           # ch.82
    "fuperficially": "ſuperficially", # ch.85
    "fentences": "ſentences",         # ch.86
    "noifomneſs": "noiſomneſs",       # ch.86
    "fuccinctly": "ſuccinctly",       # ch.86
    "reprehenfion": "reprehenſion",   # ch.86
    "indifcreet": "indiſcreet",       # ch.86
    "verbofity": "verboſity",         # ch.86
    "difcourſe": "diſcourſe",         # ch.86 (mixed: diſ→dif)
    "ingenie": "ingenie",             # ch.86 — correct as-is (17th-c.)
    "fayes": "ſayes",                 # ch.86
    "fignifie": "ſignifie",           # ch.87
    "acquiefce": "acquieſce",         # ch.87
    "tranſpofition": "tranſpoſition", # ch.88 (mixed: one ſ kept, one dropped)
    "omiffion": "omiſſion",           # ch.88 (ſſ→ff)
    "aftoniſh'd": "aſtoniſh'd",      # ch.88
    "ipfi": "ipſi",                   # ch.88
    "obfervation": "obſervation",     # ch.89
    "courtefie": "courteſie",         # ch.89
    "pufillanimoufly": "puſillanimouſly",  # ch.90 (triple ſ→f)
    "forefight": "foreſight",         # ch.90
    "apprehenfion": "apprehenſion",   # ch.90

    # --- High-frequency (also in earlier chapters) ---
    "fome": "ſome",
    "fuch": "ſuch",
    "feveral": "ſeveral",
    "fubjects": "ſubjects",
    "alfo": "alſo",
    "fometimes": "ſometimes",
    "himfelf": "himſelf",
}

# Remove incorrect entries (genuine 'f' words)
del ocr_errors_ch76_90["fomentation"]   # "fo-mentation" — genuine f
del ocr_errors_ch76_90["fomentations"]  # same
del ocr_errors_ch76_90["ingenie"]       # correct 17th-c. form


if __name__ == "__main__":
    print(f"Ch.76–90 errors: {len(ocr_errors_ch76_90)}")
    print()
    common = {"fome","fuch","feveral","fubjects","alfo","fometimes","himfelf"}
    print("=== New distinctive entries ===")
    for k, v in ocr_errors_ch76_90.items():
        if k not in common:
            print(f"  {k!r:30s} → {v!r}")

"""
OCR error corrections for Suetonius, Life of Augustus (1677 English translation)
Chapters 91–101 (end)

Each entry maps the erroneous OCR string to its correction.
Long ſ is preserved as original orthography throughout.
"""

ocr_errors_ch91_101 = {

    # =====================================================================
    # 1. WRONG CHARACTERS / GARBLED
    # =====================================================================
    "Itland": "Iſland",               # ch.92 (ſ→t — unusual misread)
    "Ferufalem": "Jeruſalem",         # ch.93 (J→F, ſ→f)
    "Entichus": "Eutichus",           # ch.96 (u→n — PDF p.144 shows "Eutichus")
    "firit ": "firſt ",               # ch.95 (ſt→i — garbled)
    "Atid ": "Atia ",                 # ch.94 (a→d)
    "look''d": "look'd",             # ch.96 (doubled apostrophe)
    "thererefore": "therefore",        # ch.96 — actually XML has "therefore", 
                                       # not an error. REMOVE.

    # =====================================================================
    # 2. SPURIOUS WORD BREAKS / HYPHENS
    # =====================================================================
    "Lu-ftrum": "Luſtrum",            # ch.97 (line-break artifact + ſ→f)
    "fuf-pended": "ſuſpended",        # ch.97 (line-break + ſ→f)
    "Apollo-nia": "Apollonia",        # ch.94 (line-break artifact)

    # =====================================================================
    # 3. U/N CONFUSION (recurring)
    # =====================================================================
    "Angustus": "Auguſtus",           # ch.94 (recurring from ch.2)

    # =====================================================================
    # 4. LONG-S (ſ) DROPPED → PLAIN f
    #    Only listing words NEW to this chapter range.
    # =====================================================================

    # --- Proper names ---
    "Afclepiades": "Aſclepiades",     # ch.94
    "Theffalian": "Theſſalian",       # ch.96
    "Southfayers": "Southſayers",     # ch.97 (inconsistent — correct also appears)
    "Tufcane": "Tuſcane",             # ch.97
    "Afturia": "Aſturia",             # ch.97
    "Mafgabas": "Maſgabas",           # ch.98
    "Thrafyllus": "Thraſyllus",       # ch.98
    "Drufius": "Druſius",             # ch.100
    "Roftra": "Roſtra",               # ch.100
    "Martins": "Martius",             # ch.97 (recurring from ch.3 — u→n also)

    # --- Distinctive words ---
    "profperous": "proſperous",       # ch.92
    "fecret": "ſecret",              # ch.93
    "furmounted": "ſurmounted",      # ch.94
    "Deftiny": "Deſtiny",            # ch.94
    "ferene": "ſerene",              # ch.95
    "Profperity": "Proſperity",      # ch.95
    "coafted": "coaſted",            # ch.98
    "expreffions": "expreſſions",    # ch.100 (ſſ→ff)
    "Auguftum": "Auguſtum",          # ch.100
    "cuftody": "cuſtody",            # ch.101
    "fixth": "ſixth",                # ch.101
    "Verfes": "Verſes",              # ch.98 (inconsistent — correct also appears)
    "fpent": "ſpent",                # ch.98

    # --- High-frequency (also in earlier chapters) ---
    "fome": "ſome",
    "fuch": "ſuch",
    "feveral": "ſeveral",
    "faid": "ſaid",
    "alfo": "alſo",
    "himfelf": "himſelf",
    "folemn": "ſolemn",
    "Priefts": "Prieſts",
    "Cafar": "Cæſar",
    "Sifters": "Siſters",
    "Confuls": "Conſuls",
    "Ifles": "Iſles",
}

# Remove incorrect entry
if "thererefore" in ocr_errors_ch91_101:
    del ocr_errors_ch91_101["thererefore"]


if __name__ == "__main__":
    print(f"Ch.91–101 errors: {len(ocr_errors_ch91_101)}")
    print()
    common = {"fome","fuch","feveral","faid","alfo","himfelf","folemn",
              "Priefts","Cafar","Sifters","Confuls","Ifles"}
    print("=== New distinctive entries ===")
    for k, v in ocr_errors_ch91_101.items():
        if k not in common:
            print(f"  {k!r:30s} → {v!r}")