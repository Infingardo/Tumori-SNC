import streamlit as st
from diagnostic_engine import (
    match_morphology,
    refine_ihc,
    refine_mol,
    IHC_PANELS,
    MOL_TESTS,
    get_entities,
)

# -------- legend ----------
LEGEND = {
    "PXA": "Xantoastrocitoma pleomorfo",
    "GBM": "Glioblastoma IDH-wt",
    "IDH-Astro": "Astrocitoma IDH-mutato",
    "ODG": "Oligodendroglioma IDH-mut 1p/19q",
    "DMG": "Diffuse midline glioma H3 K27-alt",
    "DHG-G34": "Diffuse hemispheric glioma H3 G34-mut",
    "PA": "Astrocitoma pilocitico",
    "GG": "Ganglioglioma",
    "EP-ZFTA": "Ependimoma ZFTA-fusion",
    "EP-PFA": "Ependimoma PFA",
    "MB-WNT": "Medulloblastoma WNT",
    "AT/RT": "Atypical Teratoid/Rhabdoid Tumour",
}

st.set_page_config(page_title="CNS Tumour Assistant", layout="wide")
st.title("🧠 CNS Tumour Assistant – modular extended")

ss = st.session_state
for k in ["step", "dx", "panel", "ihc", "mol_panel", "mol"]:
    ss.setdefault(k, None)

# ---------- Morphology ----------
st.header("1️⃣ Morphology")
pattern = st.selectbox("Growth pattern", list(IHC_PANELS))
m = {"pattern": pattern}
if pattern == "diffuse":
    c1, c2, c3 = st.columns(3)
    m["necrosis"] = c1.slider("Necrosis", 0, 3, 0)
    m["microvascular"] = 1 if c2.radio("Microvascular prolif.", ["neg", "pos"]) == "pos" else 0
    m["site"] = c3.radio("Site", ["emisferica", "midline", "altro"])
elif pattern == "circumscribed":
    c1, c2 = st.columns(2)
    m["rosenthal"] = 1 if c1.radio("Rosenthal/EGB", ["neg", "pos"]) == "pos" else 0
    m["xanthomatous"] = 1 if c2.radio("Xanthomatous", ["neg", "pos"]) == "pos" else 0

if st.button("Compute diagnoses"):
    ss.dx = match_morphology(m)
    ss.panel = IHC_PANELS[pattern]
    ss.ihc = None
    ss.mol_panel = None
    ss.mol = None
    ss.step = 1

if ss.step and ss.dx:
    st.subheader("Possible diagnoses: " + ", ".join(ss.dx))
    st.write("**IHC panel:** " + ", ".join(ss.panel))

    # ---------- IHC -----------
    with st.form("ihc_form"):
        ihc_res = {ab: st.radio(ab, ["neg", "pos"], horizontal=True) for ab in ss.panel}
        if st.form_submit_button("Apply IHC"):
            ss.ihc = ihc_res
            ss.dx = refine_ihc(ss.dx, ihc_res)
            ss.mol_panel = sorted({flag for d in ss.dx for flag in get_entities()[d].mol})
            ss.step = 2

if ss.step == 2 and ss.dx:
    st.subheader("Diagnoses after IHC: " + ", ".join(ss.dx))

    # ---------- Molecular ----------
    with st.form("mol_form"):
        mol_res = {flag: st.radio(flag, ["neg", "pos"], horizontal=True) for flag in ss.mol_panel}
        if st.form_submit_button("Apply molecular"):
            ss.mol = mol_res
            ss.dx = refine_mol(ss.dx, mol_res)
            ss.step = 3

if ss.step == 3 and ss.dx:
    st.success("Final diagnoses: " + ", ".join(ss.dx))
    # legenda
    st.markdown("### ℹ️ Legenda sigle")
    for abbr, full in LEGEND.items():
        st.markdown(f"- **{abbr}** = {full}")
