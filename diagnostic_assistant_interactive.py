import streamlit as st

st.set_page_config(page_title="CNS Tumour Diagnostic Assistant", page_icon="🧠")

st.sidebar.image(
    "assets/flowchart_who_cns5.png",
    caption="WHO CNS5 Tumours Flowchart",
    use_container_width=True
)

st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5")
st.subheader("Educational Demo – Classificazione Integrata")

st.write("Questo strumento guida l'utente in una classificazione di tipo accademico secondo la WHO CNS5 (2021).")

# Sede anatomica
sede = st.selectbox(
    "1️⃣ Sede anatomica:",
    ["Lobo frontale", "Lobo temporale", "Tronco encefalico", "Cervelletto", "Midollo spinale", "Altro"]
)

# Pattern di crescita
pattern = st.radio("2️⃣ Pattern di crescita:", ["Diffuso", "Circoscritto", "Esofittico"])

# Grading istologico preliminare
grading = st.selectbox(
    "3️⃣ Grading istologico (WHO):",
    ["Non determinabile", "Grado I", "Grado II", "Grado III", "Grado IV"]
)

# Pannello IHC
st.markdown("### 4️⃣ Pannello immunoistochimico")
idh = st.radio("IDH1 R132H:", ["Positivo", "Negativo"])
atrx = st.radio("ATRX:", ["Perdita", "Conservato"])
p53 = st.radio("p53:", ["Overespresso", "Normale"])
olig2 = st.radio("OLIG2:", ["Positivo", "Negativo"])
ema = st.radio("EMA:", ["Positivo", "Negativo"])
gfap = st.radio("GFAP:", ["Positivo", "Negativo"])

# Molecolare
st.markdown("### 5️⃣ Biologia molecolare")
codeletion_1p19q = st.radio("1p/19q:", ["Codeleted", "Non codeleted"])
tert = st.radio("TERT promoter:", ["Mutato", "Wildtype"])
braf = st.radio("BRAF V600E:", ["Mutato", "Wildtype"])
h3k27 = st.radio("H3 K27M:", ["Mutato", "Wildtype"])

# Algoritmo diagnostico (semplificato)
st.markdown("### 🔬 6️⃣ Diagnosi suggerita")

diagnosi = ""
if idh == "Positivo" and codeletion_1p19q == "Codeleted":
    diagnosi = "Oligodendroglioma IDH-mutato, 1p/19q codeleted"
elif idh == "Positivo" and atrx == "Perdita":
    diagnosi = "Astrocitoma IDH-mutato (con ATRX loss)"
elif h3k27 == "Mutato":
    diagnosi = "Glioma diffuso midline H3 K27M-mutato"
elif braf == "Mutato" and pattern == "Circoscritto":
    diagnosi = "Ganglioglioma o Pilocitico con BRAF V600E"
elif tert == "Mutato" and idh == "Negativo":
    diagnosi = "GBM IDH-wildtype (considera TERT, EGFR, AAP)"
else:
    diagnosi = "Quadro non definito univocamente – rivedere correlazioni clinico-radiologiche."

st.success(f"**Diagnosi suggerita:** {diagnosi}")
st.info(f"Sede: {sede} | Pattern: {pattern} | Grading: {grading}")

# Riferimenti
st.markdown("### 📚 7️⃣ Riferimenti bibliografici")
st.markdown("""
- WHO Classification of Tumours of the Central Nervous System, 5th Ed. IARC, 2021.
- Louis DN et al. *The 2021 WHO Classification of Tumors of the Central Nervous System: a summary*. Neuro Oncol. 2021.
- Capper D, Jones DTW. *Molecular diagnostics: New WHO CNS5 insights*. Brain Pathol. 2022.
""")

st.caption("Demo educativa – Non usare per scopi clinici. Filippo x ChatGPT 2025 🧬")
