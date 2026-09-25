"""Extract citing sentences of the new text (66c6331) and test each for verbatim
occurrence in the old text (90690f4).  Scratch script for the citation audit.
Usage: python extract.py <manuscript dir at 66c6331> <manuscript dir at 90690f4> <out.json>"""
import re, sys, json, unicodedata
from pathlib import Path

NEW = Path(sys.argv[1])   # manuscript/ at 66c6331 (paths made repository-relative)
OLD = Path(sys.argv[2])   # manuscript/ at 90690f4, e.g. from `git archive 90690f4 manuscript`
FILES = ["draft_v2.md", "si/S1_Text.md", "si/S2_Text.md", "si/S3_Text.md", "si/S5_Text.md",
         "supplementary.md", "figures/captions_v2.md"]
OLD_EXTRA = ["si/S4_Text.md"]  # also searched as "any file at 90690f4"

NAMES = ["Afyouni", "Alexander-Bloch", "Arbabshirani", "Barrett", "Bartlett", "Cliff", "Cousineau",
         "Down", "Faes", "Gatica", "Honari", "Huang", "Imperial-MIND-lab", "Ince", "Ito", "Kay",
         "Liardi", "Luppi", "Mediano", "Morey", "Murray", "Nago", "Raut", "Schaefer", "Singleton",
         "Tarchi", "Theiler", "Tian", "Timmermann", "Varley", "Váša", "Vasa", "Williams", "Beer", "Wu",
         "Yeo", "Zhang", "Prichard", "Wolff", "Zilio", "Nichols", "Lempel", "Ziv", "Kaspar", "Schuster",
         "Spearman", "Brown", "Fisher", "Efron", "Quenouille", "Lizier", "Rosas", "Seth", "Vaishnavi",
         "Loftus", "Masson", "Welch", "Student", "Benjamini", "Hochberg", "Newey", "West", "Politis",
         "Romano", "Kuceyeski", "Carhart-Harris", "Tagliazucchi", "Schartner", "Casali", "Bor",
         "Stamatakis", "Tononi", "Wang", "Sporns", "Deco", "Kringelbach", "Pedregosa", "Virtanen",
         "Harris", "Hunter", "Seabold", "Zalesky", "Margulies", "Breakspear", "Marinazzo", "Stramaglia"]
NAME_RE = r"(?:" + "|".join(re.escape(n) for n in sorted(NAMES, key=len, reverse=True)) + r")"
YEAR = r"(?:1[89]\d\d|20[0-4]\d)[a-z]?"
# author-year: Name ... Year within a short window without sentence end, or Name's (Year)
CITE_RE = re.compile(NAME_RE + r"(?:'s|’s)?(?:\s+et al\.?|\s*(?:&|and)\s*[A-ZÁ-Ž][\w\-]+)?(?:'s|’s)?[\s,(]*\(?" + YEAR)

ABBREV = {"al", "Eq", "Eqs", "Sec", "Secs", "Fig", "Figs", "p", "pp", "e.g", "i.e", "vs", "cf", "No",
          "approx", "Ref", "Refs", "Vol", "St", "Dr", "Mr", "Ms", "Prof", "resp", "ca", "ed", "eds",
          "Suppl", "Tab", "Ch", "Chap", "Nos", "nr", "min", "max", "incl", "var", "corr", "cov", "Corr",
          "U.S", "Ph.D", "et", "v", "ver", "vol", "Jr", "Sr", "Co", "Inc", "Ltd", "Mag", "Proc", "Rev",
          "Lett", "Phys", "Stat", "J", "R", "Soc", "Natl", "Acad", "Sci", "Neurosci"}

def norm(s, quotes=False):
    s = unicodedata.normalize("NFC", s)
    if quotes:
        s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\*\*|\*|__|`", "", s)          # markdown emphasis and code
    s = re.sub(r"(?<![A-Za-z0-9])_(?=\S)|(?<=\S)_(?![A-Za-z0-9])", "", s)  # _emphasis_ (not ts_gsr)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def blocks(text):
    """Yield (start_line, block_text) for paragraphs, table rows, list items, headings."""
    lines = text.split("\n")
    buf, start = [], None
    def flush():
        nonlocal buf, start
        if buf:
            yield_ = (start, " ".join(buf))
            buf, start = [], None
            return yield_
        return None
    out = []
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s:
            r = flush()
            if r: out.append(r)
            continue
        if s.startswith("|") or s.startswith("#") or re.match(r"^([-*+]|\d+\.)\s", s) or s.startswith(">"):
            r = flush()
            if r: out.append(r)
            if s.startswith("|"):
                out.append((i, s))
                continue
            buf, start = [s], i
            continue
        if start is None:
            start = i
        buf.append(s)
    r = flush()
    if r: out.append(r)
    return out

SPLIT_RE = re.compile(r"([.?!][)\]'’”\"*_]*)(\s+)")

def sentences(block):
    """Split a block into sentences; returns list of strings."""
    out, last = [], 0
    for m in SPLIT_RE.finditer(block):
        end = m.end(1)
        before = block[last:m.start(1)]
        tok = re.search(r"([\w.]+)$", before)
        token = tok.group(1) if tok else ""
        nxt = block[m.end():m.end() + 3]
        if m.group(1)[0] == "." and (token in ABBREV or token.split(".")[-1] in ABBREV or
                                     (re.fullmatch(r"[A-Z]", token) or re.fullmatch(r"(?:[A-Za-z]\.)+[A-Za-z]", token))):
            continue
        if not nxt:
            continue
        # do not split before a lowercase continuation after "et al." handled above; allow any start
        out.append(block[last:end].strip())
        last = m.end()
    tail = block[last:].strip()
    if tail:
        out.append(tail)
    return out

def load(path, cut_refs):
    t = path.read_text(encoding="utf-8")
    if cut_refs and "\n## References" in t:
        t = t[:t.index("\n## References")]
    return t

def main():
    old_norm = {}
    old_sents = set()
    for f in FILES + OLD_EXTRA:
        p = OLD / f
        t = p.read_text(encoding="utf-8")
        old_norm[f] = norm(t)
        for ln, b in blocks(t):
            for s in sentences(b):
                old_sents.add(norm(s))
    rows = []
    for f in FILES:
        t = (NEW / f).read_text(encoding="utf-8")
        refs_at = None
        if f == "draft_v2.md":
            refs_at = t.count("\n", 0, t.index("\n## References")) + 1
        for ln, b in blocks(t):
            in_refs = refs_at is not None and ln > refs_at
            for s in sentences(b):
                if not CITE_RE.search(s):
                    continue
                n = norm(s)
                exact = n in old_sents
                sub_any = [g for g, T in old_norm.items() if n in T]
                rows.append(dict(file=f, line=ln, in_refs=in_refs, sent=s, exact=exact,
                                 sub_same=f in sub_any, sub_any=sub_any))
    json.dump(rows, open(sys.argv[3], "w"), ensure_ascii=False, indent=1)
    import collections
    c = collections.Counter(); c2 = collections.Counter()
    for r in rows:
        key = r["file"] + (" [refs]" if r["in_refs"] else "")
        c[key] += 1
        if not r["sub_any"]:
            c2[key] += 1
    for k in c:
        print(f"{k}: citing {c[k]}, new (not substring of any old file) {c2[k]}")

if __name__ == "__main__":
    main()
