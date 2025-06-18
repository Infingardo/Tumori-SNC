
import streamlit as st
from typing import Dict, List, Set
from models import ENTITIES, DiagnosticEntity

# ---------- Static panels ----------
IHC_PANELS = {
    "diffuse": ["IDH1_R132H", "ATRX", "H3K27M", "H3G34"],
    "circumscribed": ["GFAP", "BRAF_V600E", "CD34"],
    "ependymal": ["EMA", "L1CAM", "H3K27me3"],
    "embryonal": ["β‑catenin", "YAP1", "INI1"],
}

MOL_TESTS = {
    "IDH_mut": ["IDH1/2 sequencing"],
    "Code1p19q": ["1p/19q FISH"],
    "EGFR_amp": ["EGFR amplification"],
    "H3K27M_mut": ["H3 K27M sequencing"],
    "H3G34_mut": ["H3 G34 sequencing"],
    "KIAA1549_BRAF_fusion": ["KIAA1549‑BRAF fusion"],
    "BRAF_V600E_mut": ["BRAF V600E sequencing"],
    "ZFTA_fusion": ["ZFTA fusion"],
    "EZHIP_over": ["EZHIP IHC / methylation"],
    "SMARCB1_del": ["SMARCB1 deletion"],
    "CTNNB1_mut": ["CTNNB1 sequencing"],
}

# ---------- Core functions ----------
@st.cache_data
def get_entities() -> Dict[str, DiagnosticEntity]:
    return ENTITIES

def match_morphology(m: Dict) -> List[str]:
    res: Set[str] = set(get_entities())
    for dx, ent in get_entities().items():
        if ent.pattern != m.get("pattern"):
            res.discard(dx)
            continue
        # numeric / boolean morphology
        for feat, spec in ent.morphology.items():
            if feat not in m:
                continue
            val = m[feat]
            if isinstance(spec, tuple):
                lo, hi = spec
                if not (lo <= val <= hi):
                    res.discard(dx)
            elif isinstance(spec, int):
                if val != spec:
                    res.discard(dx)
        if ent.site and ent.site != m.get("site"):
            res.discard(dx)
    return sorted(res)

def refine_ihc(cands: List[str], ihc: Dict[str, str]) -> List[str]:
    if not ihc:
        return cands
    out = []
    ents = get_entities()
    for dx in cands:
        ok = True
        for marker, result in ihc.items():
            if marker in ents[dx].ihc and ents[dx].ihc[marker] != result:
                ok = False
                break
        if ok:
            out.append(dx)
    return out or cands

def refine_mol(cands: List[str], mol: Dict[str, str]) -> List[str]:
    if not mol:
        return cands
    out = []
    ents = get_entities()
    for dx in cands:
        need = ents[dx].mol
        if all(mol.get(flag) == val for flag, val in need.items()):
            out.append(dx)
    return out or cands
