
"""
CNS Tumour Diagnostic Assistant – WHO CNS5 2021 (extended demo, stable)
Streamlit single‑file app
Educational demo • NOT for clinical use
"""

import streamlit as st
from typing import Dict, List, Set

# ===== Knowledge base =====
ENTITIES: Dict[str, Dict] = {
    # adult diffuse
    "Astrocitoma IDH‑mutato": {
        "pattern": "diffuse",
        "necrosis": (0, 1),
        "microvascular": (0, 1),
        "IDH1_R132H": "pos",
        "ATRX": "loss",
        "mol": {"IDH_mut": "pos", "Code1p19q": "neg"},
    },
    "Oligodendroglioma IDH‑mut 1p/19q": {
        "pattern": "diffuse",
        "necrosis": (0, 1),
        "microvascular": (0, 1),
        "IDH1_R132H": "pos",
        "ATRX": "retain",
        "mol": {"IDH_mut": "pos", "Code1p19q": "pos"},
    },
    "Glioblastoma IDH‑wt": {
        "pattern": "diffuse",
        "necrosis": (2, 3),
        "microvascular": (1, 1),
        "IDH1_R132H": "neg",
        "mol": {"EGFR_amp": "pos"},
    },
    # pediatric diffuse
    "Diffuse midline glioma H3 K27‑alt": {
        "pattern": "diffuse",
        "site": "midline",
        "H3K27M": "pos",
        "mol": {"H3K27M_mut": "pos"},
    },
    "Diffuse hemispheric glioma H3 G34‑mut": {
        "pattern": "diffuse",
        "site": "emisferica",
        "H3G34": "pos",
        "ATRX": "loss",
        "mol": {"H3G34_mut": "pos"},
    },
    # circumscribed
    "Pilocitoma": {
        "pattern": "circumscribed",
        "rosenthal": 1,
        "mol": {"KIAA1549_BRAF_fusion": "pos"},
    },
    "PXA": {
        "pattern": "circumscribed",
        "xanthomatous": 1,
        "BRAF_V600E": "pos",
        "mol": {"BRAF_V600E_mut": "pos"},
    },
    # ependymal
    "Ependimoma ZFTA‑fusion": {
        "pattern": "ependymal",
        "L1CAM": "pos",
        "mol": {"ZFTA_fusion": "pos"},
    },
    # embryonal
    "Medulloblastoma WNT": {
        "pattern": "embryonal",
        "beta_catenin": "pos",
        "YAP1": "pos",
        "mol": {"CTNNB1_mut": "pos"},
    },
}

IHC_PANELS = {
    "diffuse": ["IDH1_R132H", "ATRX", "H3K27M", "H3G34"],
    "circumscribed": ["GFAP", "BRAF_V600E"],
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
    "CTNNB1_mut": ["CTNNB1 sequencing"],
}

# ===== helper =====
def match_morph(m):
    res=set(ENTITIES)
    for dx,r in ENTITIES.items():
        if r["pattern"]!=m["pattern"]:
            res.discard(dx);continue
        for f in ("necrosis","microvascular","rosenthal","xanthomatous"):
            if f in m and f in r:
                v=m[f]; spec=r[f]
                if isinstance(spec,tuple):
                    if not (spec[0]<=v<=spec[1]): res.discard(dx)
                elif v!=spec: res.discard(dx)
        if r.get("site") and r["site"]!=m.get("site"): res.discard(dx)
    return sorted(res)

def refine(cands, results):
    if not results: return cands
    out=[]
    for dx in cands:
        ok=True
        rule=ENTITIES[dx]
        for k,v in results.items():
            if k in rule and rule[k]!=v:
                ok=False;break
        if ok: out.append(dx)
    return out or cands

def refine_mol(cands, mol):
    if not mol: return cands
    out=[]
    for dx in cands:
        need=ENTITIES[dx].get("mol",{})
        if all(mol.get(f)==v for f,v in need.items()):
            out.append(dx)
    return out or cands

# ===== UI =====
st.set_page_config(page_title="CNS Tumour Assistant", layout="wide")
st.title("CNS Tumour Assistant – extended demo")

ss=st.session_state
for k in ["dx","panel","ihc_res","mol_panel","mol_res"]:
    ss.setdefault(k,None)

st.header("1️⃣ Morphology")
pattern=st.selectbox("Pattern", list(IHC_PANELS))
m={"pattern":pattern}
if pattern=="diffuse":
    c1,c2,c3=st.columns(3)
    m["necrosis"]=c1.slider("Necrosis",0,3,0)
    m["microvascular"]=1 if c2.radio("Micro‑vascular",["neg","pos"])=="pos" else 0
    m["site"]=c3.radio("Site",["emisferica","midline","altro"])
elif pattern=="circumscribed":
    c1,c2=st.columns(2)
    m["rosenthal"]=1 if c1.radio("Rosenthal/EGB",["neg","pos"])=="pos" else 0
    m["xanthomatous"]=1 if c2.radio("Xanthomatous",["neg","pos"])=="pos" else 0

if st.button("Compute dx"):
    ss.dx=match_morph(m)
    ss.panel=IHC_PANELS[pattern]
    ss.ihc_res=None
    ss.mol_panel=None
    ss.mol_res=None

if ss.dx:
    st.subheader("Possibili diagnosi: "+", ".join(ss.dx))
    if ss.panel:
        st.write("IHC panel:", ", ".join(ss.panel))
        with st.form("ihc_form"):          # key different from session
            ihc={}
            for ab in ss.panel:
                ihc[ab]=st.radio(ab,["neg","pos"],horizontal=True)
            if st.form_submit_button("Apply IHC"):
                ss.ihc_res=ihc
                ss.dx=refine(ss.dx,ihc)
                flags=set(f for d in ss.dx for f in ENTITIES[d].get("mol",{}))
                ss.mol_panel=sorted(flags)

if ss.ihc_res and ss.dx:
    st.subheader("DX after IHC: "+", ".join(ss.dx))
    if ss.mol_panel:
        with st.form("mol_form"):
            mol={}
            for f in ss.mol_panel:
                mol[f]=st.radio(f,["neg","pos"],horizontal=True)
            if st.form_submit_button("Apply molecular"):
                ss.mol_res=mol
                ss.dx=refine_mol(ss.dx,mol)

if ss.mol_res and ss.dx:
    st.success("Final dx: "+", ".join(ss.dx))
