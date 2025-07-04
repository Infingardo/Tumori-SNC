import streamlit as st

st.set_page_config(page_title="Assistente Diagnostico Tumori SNC", page_icon="🧠")

# Titolo
st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5")
st.write("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")

# Sidebar con flowchart WHO
st.sidebar.image("assets/flowchart_who_cns5.png",
                 caption="WHO CNS5 Tumours Flowchart",
                 use_container_width=True)

# 1️⃣ Fascia d'età e sede
st.subheader("📌 Informazioni di base")
age_group = st.radio("Fascia d'età del paziente:", ["Adulto", "Pediatrico"], index=0)
site = st.selectbox("Sede anatomica principale:", ["Lobo frontale", "Lobo temporale", "Cervelletto", "Tronco encefalico", "Midollo spinale"])

# 2️⃣ Caratteristiche macroscopiche (esempio)
st.subheader("🧩 Caratteristiche macroscopiche")
macro = st.checkbox("Aspetto necrotico-emorragico")
borders = st.checkbox("Margini infiltranti")

# 3️⃣ Pattern microscopici con rosette
st.subheader("🔬 Caratteristiche microscopiche")
pattern = st.radio(
    "Pattern morfologico osservato:",
    [
        "Nessun pattern definito",
        "Rosette di Homer-Wright",
        "Rosette di Flexner-Wintersteiner",
        "Rosette perivascolari"
    ]
)

if pattern != "Nessun pattern definito":
    st.image("assets/rosetta.png",
             caption=f"Pattern morfologico: {pattern}",
             use_container_width=True)

# 4️⃣ Pannello IIC di base
st.subheader("🧪 Pannello Immunoistochimico")
idh1 = st.radio("IDH1 R132H:", ["Non testato", "Positivo", "Negativo"], index=0)
atrx = st.radio("ATRX:", ["Non testato", "Perdita", "Conservato"], index=0)
gfap = st.radio("GFAP:", ["Non testato", "Positivo", "Negativo"], index=0)

# 5️⃣ Analisi molecolare semplificata
st.subheader("🧬 Profilo molecolare")
mgmt = st.radio("Metilazione MGMT:", ["Non testato", "Metilato", "Non metilato"], index=0)
tert = st.radio("Mutazione TERT:", ["Non testato", "Presente", "Assente"], index=0)

# 6️⃣ Diagnosi suggerita (esempio logico)
st.subheader("🔍 Diagnosi suggerita")
if idh1 == "Positivo" and atrx == "Perdita":
    st.success("Astrocitoma diffuso IDH-mutato, ATRX perso.")
elif idh1 == "Negativo" and tert == "Presente":
    st.warning("Probabile glioblastoma IDH-wildtype.")
else:
    st.info("Pattern non definito: considera ulteriori test molecolari e correlazione clinica.")

# Link PDF bibliografia
with st.expander("📚 Riferimenti bibliografici"):
    st.markdown("[Scarica WHO CNS5 2021 (Brain)](assets/Brain2021.pdf)")

# Footer
st.caption("---")
st.caption("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")
