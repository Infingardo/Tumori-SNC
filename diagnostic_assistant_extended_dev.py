import streamlit as st

st.set_page_config(
    page_title="🧠 Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)")
st.caption("Educational demo – Non usare per scopi clinici. Filippo x ChatGPT 2025 🧬")

# 1️⃣ Caratteristiche clinico-morfologiche
st.subheader("1️⃣ Caratteristiche clinico-morfologiche")

sede = st.selectbox("Seleziona la sede:", ["Seleziona...", "Lobo frontale", "Lobo parietale", "Cervelletto", "Midollo spinale"])
pattern = st.radio("Pattern di crescita:", ["Diffuso", "Circostritto"])
fascia_eta = st.radio("Fascia d'età:", ["Pediatrico", "Adulto"])

if sede != "Seleziona...":
    st.info(f"📍 Sede selezionata: {sede}")

# Ipotesi diagnostica base
if fascia_eta == "Adulto" and pattern == "Diffuso":
    st.success("🟢 Ipotesi iniziale: Astrocitoma diffuso o Oligodendroglioma.")
elif fascia_eta == "Pediatrico" and pattern == "Circostritto":
    st.success("🟢 Ipotesi iniziale: Possibile PNET o Medulloblastoma.")
else:
    st.info("ℹ️ Ipotesi: valutare correlazione con imaging e clinica.")

# Mostra immagine rosetta se pattern circoscritto
if pattern == "Circostritto":
    st.image(
        "assets/rosetta.png",
        caption="Rosette di Homer-Wright, Flexner-Wintersteiner e pseudorosette di ependimoma.",
        use_container_width=True
    )

# 2️⃣ Pannello Immunoistochimico
st.subheader("2️⃣ Pannello IIC di base")
idh1 = st.radio("IDH1 R132H:", ["Non testato", "Positivo", "Negativo"], index=0)
atrx = st.radio("ATRX:", ["Non testato", "Perdita", "Conservato"], index=0)
gfap = st.radio("GFAP:", ["Non testato", "Positivo", "Negativo"], index=0)

# 3️⃣ Profilo molecolare
st.subheader("3️⃣ Profilo molecolare")
mgmt = st.radio("Metilazione MGMT:", ["Non testato", "Metilato", "Non metilato"], index=0)
tert = st.radio("Mutazione TERT:", ["Non testato", "Presente", "Assente"], index=0)

# 4️⃣ Diagnosi suggerita
st.subheader("4️⃣ Diagnosi suggerita")
if idh1 == "Positivo" and atrx == "Perdita":
    st.success("✅ Diagnosi suggerita: Astrocitoma diffuso IDH-mutato, ATRX perso.")
elif idh1 == "Negativo" and tert == "Presente":
    st.warning("⚠️ Probabile glioblastoma IDH-wildtype.")
else:
    st.info("🔬 Pattern non definito: considerare ulteriori test molecolari e correlazione clinica.")

# 📚 Riferimenti bibliografici
with st.expander("📚 Riferimenti bibliografici"):
    st.markdown("""
- WHO Classification of Tumours Editorial Board. *Central Nervous System Tumours*, 5th ed., IARC, Lyon, 2021.  
- Louis DN et al. The 2021 WHO Classification of Tumors of the Central Nervous System: a summary. *Neuro-Oncology*, 2021.  
- Brat DJ, Aldape K, et al. Molecular Pathology of CNS Tumors. *J Neuropathol Exp Neurol*. 2021.

📄 👉 [Scarica WHO CNS5 2021 (Brain)](assets/Brain2021.pdf)
""")

# Footer
st.markdown("---")
st.caption("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")
