# %% [markdown]
# # Suetonius OCR Correction and WER Calculation
# This notebook processes the 1677 English translation of Suetonius's *Life of Augustus*.
# It applies a consolidated dictionary of OCR error corrections, safely handles ambiguous 
# misreadings using contextual regex, injects `<corr>` tags, and calculates the Word Error Rate.

# %%
import re
import os

# 1. Consolidated Dictionary of Unambiguous Errors
# (Merged from Ch 1-101, with genuine 'f' words and ambiguous terms removed)
unambiguous_errors = {
    # Ligatures & Artifacts
    "Oftavius": "Octavius", "Oitavia": "Octavia", "Affium": "Actium", 
    "Auguftus": "Auguſtus", "$A/ia$": "Aſia", "$A_{H}g_{H}ft_{HS}$": "Auguſtus", 
    "$Ce\\int ar$": "Cæſar", "CaShier": "Caſhier", "duxty": "durty", 
    "plaod": "plac'd", "Antoniu,": "Antonius,", "Prator": "Prætor",
    "Quastors": "Quæſtors", "Prators": "Prætors", "Quastor": "Quæſtor",
    "Cefar": "Cæſar", "Cafar": "Cæſar", "Cafaria": "Cæſaria", 
    "firit ": "firſt ", "Atid ": "Atia ", "look''d": "look'd", "Itland": "Iſland",
    "Ferufalem": "Jeruſalem", "certan ": "certain ", "unknow ": "unknown ",
    "pople": "people", "Sunıptuary": "Sumptuary", "ſuſhcient": "ſufficient",
    "ſnould": "ſhould", "refolutión": "reſolutión", "ágain": "again",
    "farcaſine": "ſarcaſme", "cafily": "eaſily", "poflible": "poſſible",
    "eft.": "eſt.", "Tome time": "ſome time", "neceſſlity": "neceſſity",
    "be be ſtript": "be ſtript",
    
    # U/N and M/N Confusion
    "Tullins": "Tullius", "Cains": "Caius", "Angustus": "Auguſtus", 
    "Martins": "Martius", "Hirtins": "Hirtius", "Angures": "Augures",
    "Domitinus": "Domitius", "from then,": "from them,", "Cornelins": "Cornelius",
    "Entichus": "Eutichus",
    
    # Missing / Spurious Word Breaks
    "allhis": "all his", "fuchas": "ſuch as", "toimitate": "to imitate",
    "ifany": "if any", "heappointed": "he appointed", "Hebrought": "He brought",
    "fre quently": "frequently", "Centumvir al": "Centumviral", "himſelfto": "himſelf to",
    "Heunderstood": "He underſtood", "whomalſo": "whom alſo", "E- nemy": "Enemy",
    "interrupti ons": "interruptions", "re poſe": "repoſe", "whi ther": "whither",
    "under- Stand": "underſtand", "Pul leiaceius": "Pulleiaceius", "Sylla bles": "Syllables",
    "Apollodo- Yus": "Apollodorus", "Authorswhich": "Authors which", "Lu-ftrum": "Luſtrum",
    "fuf-pended": "ſuſpended", "Apollo-nia": "Apollonia", "pub-lick": "publick",

    # Long-S (ſ) Dropped -> Plain f (Distinctive Proper Names)
    "Prifcus": "Priſcus", "Beffi": "Beſſi", "Caffius": "Caſſius", "Parmenfis": "Parmenſis",
    "Perufium": "Peruſium", "Sofius": "Soſius", "Pfilli": "Pſilli", "Audafius": "Audaſius",
    "Saturnius": "Saturninus", "Afprenas": "Aſprenas", "Diafcorides": "Diaſcorides",
    "Caffius Patavinus": "Caſſius Patavinus", "Antiftius": "Antiſtius", "Caftricius": "Caſtricius",
    "Meffala": "Meſſala", "Ifauricus": "Iſauricus", "Marfelles": "Marſeilles",
    "Rhatian": "Rhætian", "Saluftius": "Saluſtius", "Afiatick": "Aſiatick",
    "Dionyfius": "Dionyſius", "Spharus": "Sphærus", "Afclepiades": "Aſclepiades",
    "Theffalian": "Theſſalian", "Afturia": "Aſturia", "Mafgabas": "Maſgabas",
    "Thrafyllus": "Thraſyllus", "Drufius": "Druſius",
    
    # Long-S (ſ) Dropped -> Plain f (General Words)
    "confecrated": "conſecrated", "facrificing": "ſacrificing", "Magiftracy": "Magiſtracy",
    "fuffrage": "ſuffrage", "greateft": "greateſt", "Poffeffor": "Poſſeſſor",
    "furpriſed": "ſurpriſed", "inconfiderately": "inconſiderately", "Teftament": "Teſtament",
    "curiofities": "curioſities", "plaufible": "plauſible", "profecute": "proſecute",
    "vigouroufly": "vigourouſly", "defſiſted": "deſiſted", "afſlaſſinate": "aſſaſſinate",
    "difcover'd": "diſcover'd", "infinuated": "inſinuated", "fubrogated": "ſubrogated",
    "defperately": "deſperately", "poffeflion": "poſſeſſion", "confufion": "confuſion",
    "prefuming": "preſuming", "facrificed": "ſacrificed", "Prifoners": "Priſoners",
    "Confuls": "Conſuls", "Confulſhip": "Conſulſhip", "fome": "ſome", "fide": "ſide",
    "felf": "ſelf", "himfelf": "himſelf", "fays": "ſays", "fuddenly": "ſuddenly",
    "fudden": "ſudden", "fent": "ſent", "foon": "ſoon", "fuch": "ſuch", "fmall": "ſmall",
    "fickness": "ſickneſs", "fecond": "ſecond", "fole": "ſole", "flain": "ſlain",
    "faid": "ſaid", "fincere": "ſincere", "fubmitted": "ſubmitted", "furrender": "ſurrender",
    "furname": "ſurname", "faluted": "ſaluted", "fufficient": "ſufficient", 
    "fatisfied": "ſatisfied", "befides": "beſides", "abfent": "abſent", "refolve": "reſolve",
    "refolv'd": "reſolv'd", "repofe": "repoſe", "promife": "promiſe", "affum'd": "aſſum'd",
    "befieg'd": "beſieg'd", "deferv'd": "deſerv'd", "elfe": "elſe", "fleep": "ſleep",
    "fignal": "ſignal", "folemn": "ſolemn", "fuffer": "ſuffer", "infolent": "inſolent",
    "foveraignty": "ſoveraignty", "difpenc'd": "diſpenc'd", "feveral": "ſeveral",
    "fuck": "ſuck", "defire": "deſire", "occafion": "occaſion", "perfons": "perſons",
    "perfon": "perſon", "alfo": "alſo", "fometimes": "ſometimes", "fet": "ſet", "fo": "ſo",
    "difenable": "diſenable", "feldom": "ſeldom", "neceffity": "neceſſity", "reafon": "reaſon",
    "fquallour": "ſquallour", "fuppreft": "ſuppreſt", "fervants": "ſervants", 
    "indifpofition": "indiſpoſition", "refcue": "reſcue", "fack": "ſack", 
    "furprize": "ſurprize", "Confulary": "Conſulary", "confifting": "conſiſting", 
    "Feafts": "Feaſts", "Magiftrates": "Magiſtrates", "fhould": "ſhould", "fum": "ſum",
    "afide": "aſide", "chofen": "choſen", "Tranfvection": "Tranſvection", "horfes": "horſes",
    "leflen'd": "leſſen'd", "Aflemblies": "Aſſemblies", "diftributed": "diſtributed",
    "fecure": "ſecure", "feventeen": "ſeventeen", "Sefterces": "Seſterces",
    "folicitous": "ſolicitous", "difcipline": "diſcipline", "fcarcity": "ſcarcity",
    "folemnity": "ſolemnity", "confufions": "confuſions", "Affemblies": "Aſſemblies",
    "diftinguiſhed": "diſtinguiſhed", "afligned": "aſſigned", "Wreftlers": "Wreſtlers",
    "defiring": "deſiring", "diffimulation": "diſſimulation", "confideration": "conſideration",
    "deferts": "deſerts", "fevere": "ſevere", "fexes": "ſexes", "Caufes": "Cauſes",
    "hioown": "his own", "reſfcued": "reſcued", "Malefaltor": "Malefactor", 
    "impreflion": "impreſſion", "exhaufted": "exhauſted", "fuffrages": "ſuffrages",
    "whatfoever": "whatſoever", "eafie": "eaſie", "fafe": "ſafe", 
    "licentioufneſs": "licentiouſneſs", "purfued": "purſued", "inftructed": "inſtructed",
    "Tuskan": "Tuſkan", "difpofed": "diſpoſed", "fedition": "ſedition", "impofed": "impoſed",
    "refpect": "reſpect", "fucceſſors": "ſucceſſors", "figned": "ſigned", 
    "infolence": "inſolence", "preffing": "preſſing", "allufion": "alluſion",
    "pleafantneſs": "pleaſantneſs", "Sponfal": "Sponſal", "refolving": "reſolving",
    "perſwafions": "perſwaſions", "difparagement": "diſparagement", "oppofed": "oppoſed",
    "difpoſſeſs": "diſpoſſeſs", "demonftration": "demonſtration", "filently": "ſilently",
    "Cafes": "Caſes", "accufed": "accuſed", "confulted": "conſulted", 
    "profperity": "proſperity", "conftantly": "conſtantly", "univerfal": "univerſal",
    "Sifter": "Siſter", "Epiftles": "Epiſtles", "controverfies": "controverſies",
    "Confular": "Conſular", "fordid": "ſordid", "fcars": "ſcars", "impofthumes": "impoſthumes",
    "fowr": "ſowr", "defperate": "deſperate", "fufpicion": "ſuſpicion", 
    "difpleafure": "diſpleaſure", "prefumption": "preſumption", "infolently": "inſolently",
    "ficknefs": "ſickneſs", "reprefenting": "repreſenting", "profcrib": "proſcrib",
    "flander": "ſlander", "fomething": "ſomething", "confiderable": "conſiderable",
    "houfes": "houſes", "parfimony": "parſimony", "fcanty": "ſcanty", 
    "facctious": "facetious", "fpeak": "ſpeak", "Aftrologers": "Aſtrologers",
    "Philofophers": "Philoſophers", "feafts": "feaſts", "fwim": "ſwim", 
    "Grand-fon": "Grand-ſon", "ufually": "uſually", "Houfhold": "Houſhold",
    "paffing": "paſſing", "fextants": "ſextants", "Domefticks": "Domeſticks",
    "filent": "ſilent", "ferenity": "ſerenity", "pafling": "paſſing",
    "fomewhat": "ſomewhat", "ftood": "ſtood", "Phyfick": "Phyſick", "fubject": "ſubject",
    "conftant": "conſtant", "feafons": "ſeaſons", "Waftcoat": "Waſtcoat",
    "fuperficially": "ſuperficially", "fentences": "ſentences", "noifomneſs": "noiſomneſs",
    "fuccinctly": "ſuccinctly", "reprehenfion": "reprehenſion", "indifcreet": "indiſcreet",
    "verbofity": "verboſity", "difcourſe": "diſcourſe", "fayes": "ſayes", 
    "fignifie": "ſignifie", "acquiefce": "acquieſce", "tranſpofition": "tranſpoſition",
    "omiffion": "omiſſion", "aftoniſh'd": "aſtoniſh'd", "ipfi": "ipſi", 
    "obfervation": "obſervation", "courtefie": "courteſie", 
    "pufillanimoufly": "puſillanimouſly", "forefight": "foreſight", 
    "apprehenfion": "apprehenſion", "fubjects": "ſubjects", "Southfayers": "Southſayers",
    "Tufcane": "Tuſcane", "Roftra": "Roſtra", "profperous": "proſperous", 
    "fecret": "ſecret", "furmounted": "ſurmounted", "Deftiny": "Deſtiny",
    "ferene": "ſerene", "Profperity": "Proſperity", "coafted": "coaſted",
    "expreffions": "expreſſions", "Auguftum": "Auguſtum", "cuftody": "cuſtody",
    "fixth": "ſixth", "Verfes": "Verſes", "fpent": "ſpent", "Priefts": "Prieſts",
    "Sisters": "Siſters", "Ifles": "Iſles"
}

# 2. Contextual Rules for Ambiguous Errors
# We capture the surrounding context to ensure we don't accidentally replace a genuine word.
ambiguous_rules = [
    # "fame" -> "ſame" (same)
    (r'\b(the|that|this) (fame)\b', r'\1 <corr sic="\2">ſame</corr>'),
    # "fate" -> "ſate" (sate/sat)
    (r'\b(fate) (in|upon|down)\b', r'<corr sic="\1">ſate</corr> \2'),
    # "forts" -> "ſorts" (sorts)
    (r'\b(forts) (of)\b', r'<corr sic="\1">ſorts</corr> \2'),
    # "fold" -> "ſold" (sold)
    (r'\b(and|were) (fold)\b', r'\1 <corr sic="\2">ſold</corr>'),
    # "Cafe" -> "Caſe" (Case)
    (r'\b(the|this|in that) (Cafe)\b', r'\1 <corr sic="\2">Caſe</corr>'),
    # "to slay" -> "to day"
    (r'\b(to) (slay)\b', r'\1 <corr sic="\2">day</corr>')
]

# %% [markdown]
# ## Document Processing
# This function applies the direct replacements and context rules, injecting the `<corr>` XML tag.

# %%
def correct_ocr_text(text):
    correction_count = 0
    
    # 1. Apply Unambiguous Replacements
    for wrong, right in unambiguous_errors.items():
        # Avoid \b word boundaries if the string contains special characters like $
        prefix = r'\b' if wrong[0].isalnum() else r''
        suffix = r'\b' if wrong[-1].isalnum() else r''
        
        pattern = re.compile(prefix + re.escape(wrong) + suffix)
        
        def repl(match):
            nonlocal correction_count
            correction_count += 1
            return f'<corr sic="{wrong}">{right}</corr>'
            
        text = pattern.sub(repl, text)
        
    # 2. Apply Context-Aware Ambiguous Replacements
    for regex, replacement in ambiguous_rules:
        pattern = re.compile(regex)
        
        def repl_ambig(match):
            nonlocal correction_count
            correction_count += 1
            # Reconstruct the string using the replacement string
            return match.expand(replacement)
            
        text = pattern.sub(repl_ambig, text)
        
    return text, correction_count

# %% [markdown]
# ## Word Error Rate (WER) Calculation
# WER is computed as `(Substitutions + Insertions + Deletions) / Reference_Word_Count`. 
# Since we are directly replacing strings without standalone insertions/deletions, our error distance is equal to the number of words corrected. We calculate this mathematically using Levenshtein distance on the word arrays.

# %%
def levenshtein_distance(seq1, seq2):
    """Calculates the minimum edit distance between two sequences (lists of words)."""
    if len(seq1) < len(seq2):
        return levenshtein_distance(seq2, seq1)
    if len(seq2) == 0:
        return len(seq1)
    
    previous_row = range(len(seq2) + 1)
    for i, token1 in enumerate(seq1):
        current_row = [i + 1]
        for j, token2 in enumerate(seq2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (token1 != token2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def calculate_wer(corrected_xml):
    # Reconstruct the Hypothesis (Original OCR Text)
    # Extracts the "sic" attribute
    hyp_text = re.sub(r'<corr sic="([^"]+)">(.*?)</corr>', r'\1', corrected_xml)
    
    # Reconstruct the Reference (Corrected Text)
    # Extracts the intended correction inside the tag
    ref_text = re.sub(r'<corr sic="[^"]+">(.*?)</corr>', r'\1', corrected_xml)
    
    hyp_words = hyp_text.split()
    ref_words = ref_text.split()
    
    distance = levenshtein_distance(ref_words, hyp_words)
    wer = distance / len(ref_words) if ref_words else 0.0
    
    return distance, len(ref_words), wer

# %% [markdown]
# ## Execution Block
# Loads the `suetonius.aug.1677-eng.xml` file, processes the text, calculates WER, and saves the corrected version.

# %%
input_filename = 'suetonius.aug.1677-eng.xml'
output_filename = 'suetonius.aug.1677-eng.corrected.xml'

if os.path.exists(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    print("Starting OCR correction...")
    corrected_xml, num_corrections = correct_ocr_text(xml_content)
    print(f"Applied {num_corrections} <corr> tags.")

    print("Calculating Word Error Rate (WER)...")
    edits, ref_count, wer = calculate_wer(corrected_xml)
    print(f"Total Words (Ref): {ref_count}")
    print(f"Total Edit Distance: {edits}")
    print(f"Word Error Rate: {wer:.4%} ({wer:.4f})")

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(corrected_xml)
    print(f"Corrected XML saved to '{output_filename}'.")
else:
    print(f"Error: Could not find '{input_filename}'. Please ensure the file is in the same directory.")