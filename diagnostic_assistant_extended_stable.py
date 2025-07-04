import streamlit as st

st.set_page_config(
    page_title="CNS Tumour Diagnostic Assistant EXTENDED+",
    page_icon="🧠",
)

st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)")
st.caption("Educational demo – Non usare per scopi clinici. Filippo x ChatGPT 2025 🧬")

# ============================
# 1️⃣ Informazioni clinico-morfologiche
# ============================

st.header("1️⃣ Caratteristiche clinico-morfologiche")

sede = st.selectbox("Seleziona la sede:", ["Lobo frontale", "Cervelletto", "Tronco encefalico", "Midollo spinale"])
pattern = st.selectbox("Pattern di crescita:", ["Diffuso", "Circoscritto", "Multi-focale"])
età = st.radio("Fascia d'età:", ["Pediatrico", "Adulto"])

st.write(f"**Ipotesi iniziale:**")
if sede == "Cervelletto" and età == "Pediatrico":
    st.success("🟢 Possibile Astrocitoma pilocitico o Ependimoma posteriore.")
elif sede == "Lobo frontale" and pattern == "Diffuso":
    st.success("🟢 Considerare Astrocitoma diffuso o Oligodendroglioma.")
else:
    st.info("ℹ️ Consulta pattern più rari: Medulloblastoma? Tumori embrionali?")

# ============================
# 🔬 Immagine istologica (placeholder)
# ============================

st.header("📸 Immagine istologica di esempio")

st.image(
    "assets/sample_histology.png",
    caption="Sezione istologica esemplificativa – H&E",
    use_container_width=True
)

st.info("👉 Sostituisci 'sample_histology.png' in assets/ con una microfotografia reale o diagramma schematico.")

# ============================
# 2️⃣ Pannello Immunoistochimico
# ============================

st.header("2️⃣ Pannello Immunoistochimico")

st.image(
    "assets/atrx_braf_marker.png",
    caption="Pattern ATRX/BRAF – WHO CNS5",
    use_container_width=True
)

st.write("**Indica i risultati IHC:**")

atrx_status = st.radio("ATRX:", ["Perdita", "Conservato"])
braf_status = st.radio("BRAF:", ["Mutato", "Non mutato"])

if atrx_status == "Perdita" and braf_status == "Mutato":
    st.success("🔬 **Ipotesi ristretta:** Astrocitoma pilocitico BRAF-mutato (CNS WHO grade I).")
    st.info("📌 Suggeriti: FISH BRAF/KIAA1549, conferma con IHC di supporto.")
elif atrx_status == "Perdita" and braf_status == "Non mutato":
    st.success("🔬 **Ipotesi ristretta:** Astrocitoma diffuso IDH-mutato, ATRX loss.")
elif atrx_status == "Conservato" and braf_status == "Mutato":
    st.success("🔬 **Ipotesi ristretta:** Possibile ganglioglioma BRAF-mutato.")
else:
    st.warning("⚡ Profila ulteriormente: MGMT, IDH1 R132H, p53?")

# ============================
# 3️⃣ Studi Molecolari Avanzati
# ============================

st.header("3️⃣ Studi Molecolari Avanzati")

if st.checkbox("Visualizza suggerimenti di studio molecolare"):
    st.write("""
    - **IDH1/2** mutational status
    - **1p/19q codelezione** (se indicato)
    - **MGMT metilazione**
    - **H3K27M** (in forme pediatriche o midollo)
    """)
    st.link_button(
        "📖 Capitolo WHO CNS5 – Sito IARC",
        "https://www.iarc.who.int/news-events/who-classification-of-tumours-5th-edition-volume-6-central-nervous-system-tumours-2/"
    )
    st.link_button(
        "📑 Scarica WHO Blue Book CNS5 (se hai accesso)",
        "https://publications.iarc.fr/632"
    )

# ============================
# 📚 Riferimenti Bibliografici
# ============================

with st.expander("📚 Riferimenti bibliografici"):
    st.markdown("""
    1. WHO Classification of Tumours Editorial Board. *Central Nervous System Tumours*, 5th ed., IARC, Lyon, 2021.
    2. Louis DN et al. *The 2021 WHO Classification of Tumors of the Central Nervous System: a summary*. Neuro-Oncology, 2021.
    3. Brat DJ, Aldape K, et al. *Molecular Pathology of CNS Tumors*. J Neuropathol Exp Neurol. 2021.
    """)

# ============================
# Footer
# ============================

st.caption("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")



