import streamlit as st

# -------------------------------
# CONFIGURAZIONE PAGINA
# -------------------------------
st.set_page_config(
    page_title="Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------
# TITOLO E INTRO
# -------------------------------
st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)")
st.caption("Educational demo – Non usare per scopi clinici. Filippo x ChatGPT 2025 🧬")

# -------------------------------
# 1️⃣ CARATTERISTICHE CLINICO-MORFOLOGICHE
# -------------------------------
st.header("1️⃣ Caratteristiche clinico-morfologiche")

sede = st.selectbox("Seleziona la sede:", ["Lobo frontale", "Lobo temporale", "Tronco encefalico", "Cervelletto"])
pattern = st.radio("Pattern di crescita:", ["Diffuso", "Circostritto"])
eta = st.radio("Fascia d'età:", ["Pediatrico", "Adulto"])

# Visualizza immagine di esempio istologico
st.subheader("📸 Immagine istologica di esempio")

try:
    st.image("assets/sample_histology.png",
             caption="Sezione istologica esemplificativa – H&E",
             use_container_width=True)
except:
    st.info("🔍 Inserisci 'sample_histology.png' in assets per mostrare una microfotografia reale.")

# -------------------------------
# 2️⃣ PANNELLO IMMUNOISTOCHIMICO
# -------------------------------
st.header("2️⃣ Pannello Immunoistochimico")

# Mostra immagine ATRX/BRAF
st.image("assets/atrx_braf_marker.png", caption="Pattern ATRX/BRAF – WHO CNS5", use_container_width=True)

# Scelte IHC
idh1 = st.radio("IDH1 R132H:", ["Non testato", "Positivo", "Negativo"], index=0)
atrx = st.radio("ATRX:", ["Non testato", "Perdita", "Conservato"], index=0)
braf = st.radio("BRAF V600E:", ["Non testato", "Mutato", "Non mutato"], index=0)

# -------------------------------
# 3️⃣ PROFILO MOLECOLARE AVANZATO
# -------------------------------
st.header("3️⃣ Studi Molecolari Avanzati")
st.write("🔬 Visualizza suggerimenti di studio molecolare:")

st.markdown("""
- **IDH1/2 mutational status**
- **1p/19q codelezione** (se indicato)
- **MGMT metilazione**
- **H3K27M** (in forme pediatriche o midollo)
""")

mgmt = st.radio("Metilazione MGMT:", ["Non testato", "Metilato", "Non metilato"], index=0)
tert = st.radio("Mutazione TERT:", ["Non testato", "Presente", "Assente"], index=0)

# -------------------------------
# 4️⃣ DIAGNOSI SUGGERITA (SEMPLIFICATA)
# -------------------------------
st.header("4️⃣ Diagnosi suggerita")

diagnosi = ""
if idh1 == "Positivo" and atrx == "Perdita":
    diagnosi = "Astrocitoma diffuso IDH-mutato, ATRX perso."
elif idh1 == "Negativo" and tert == "Presente":
    diagnosi = "Probabile glioblastoma IDH-wildtype."
elif braf == "Mutato":
    diagnosi = "Astrocitoma pilocitico BRAF-mutato (CNS WHO grade I)."
else:
    diagnosi = "Pattern non definito: considera ulteriori test molecolari e correlazione clinica."

st.success(f"🔬 {diagnosi}")

# -------------------------------
# 5️⃣ RIFERIMENTI BIBLIOGRAFICI E FOOTER
# -------------------------------
st.markdown("---")
st.header("📚 Riferimenti bibliografici")

# Link WHO CNS5 (sito IARC ufficiale)
st.markdown("🔗 [WHO Classification of Tumours of the Central Nervous System (CNS5) – IARC](https://publications.iarc.fr/Book-And-Report-Series/Who-Classification-Of-Tumours/WHO-Classification-Of-Tumours-Of-The-Central-Nervous-System-2021)")

# Link articolo su Brain 2021
st.markdown("🔗 [Louis DN et al. The 2021 WHO Classification of Tumors of the CNS: a summary. *Brain* 2021](https://doi.org/10.1093/brain/awab093)")

# Download PDF se disponibile
try:
    with open("assets/Brain2021.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 Scarica Brain 2021 (PDF)",
        data=PDFbyte,
        file_name="Brain2021.pdf",
        mime='application/octet-stream'
    )
except FileNotFoundError:
    st.warning("⚠️ PDF Brain2021 non trovato nella cartella assets!")

st.caption("---")
st.caption("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")
