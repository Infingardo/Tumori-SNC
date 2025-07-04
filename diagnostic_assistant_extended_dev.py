import streamlit as st

st.set_page_config(page_title="CNS Tumour Diagnostic Assistant", page_icon="🧠")

st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)")
st.caption("Educational demo – Non usare per scopi clinici. Filippo x ChatGPT 2025 🧬")

# 1️⃣ Caratteristiche clinico-morfologiche
st.subheader("1️⃣ Caratteristiche clinico-morfologiche")

sede = st.selectbox("Seleziona la sede:", ["Lobo frontale", "Lobo temporale", "Tronco encefalico"])
pattern = st.radio("Pattern di crescita:", ["Diffuso", "Circospetto"])
eta = st.radio("Fascia d'età:", ["Pediatrico", "Adulto"])

# Ipotesi diagnostica preliminare
if pattern == "Diffuso" and eta == "Adulto":
    st.success("🟢 Considerare Astrocitoma diffuso o Oligodendroglioma.")
elif pattern == "Circospetto" and eta == "Pediatrico":
    st.warning("🟠 Valutare ganglioglioma o tumori embrionali.")
else:
    st.info("🔵 Diagnosi ampia: considerare correlazione clinico-radiologica.")

# Immagine istologica di esempio
st.image(
    "assets/sample_histology.png",  # oppure 'rosetta.png'
    caption="Sezione istologica esemplificativa – H&E",
    use_container_width=True
)

# 4️⃣ Pannello IIC di base
st.subheader("🧪 Pannello Immunoistochimico")
idh1 = st.radio("IDH1 R132H:", ["Non testato", "Positivo", "Negativo"], index=0)
atrx = st.radio("ATRX:", ["Non testato", "Perdita", "Conservato"], index=0)
gfap = st.radio("GFAP:", ["Non testato", "Positivo", "Negativo"], index=0)

# 5️⃣ Analisi molecolare semplificata
st.subheader("🧬 Profilo molecolare")
mgmt = st.radio("Metilazione MGMT:", ["Non testato", "Metilato", "Non metilato"], index=0)
tert = st.radio("Mutazione TERT:", ["Non testato", "Presente", "Assente"], index=0)

# 6️⃣ Diagnosi suggerita
st.subheader("🔍 Diagnosi suggerita")
if idh1 == "Positivo" and atrx == "Perdita":
    st.success("Astrocitoma diffuso IDH-mutato, ATRX perso.")
elif idh1 == "Negativo" and tert == "Presente":
    st.warning("Probabile glioblastoma IDH-wildtype.")
else:
    st.info("Pattern non definito: considera ulteriori test molecolari e correlazione clinica.")

# 📚 Riferimenti bibliografici (link PDF)
with st.expander("📚 Riferimenti bibliografici"):
    st.markdown("[Scarica WHO CNS5 2021 (Brain)](assets/Brain2021.pdf)")

# Footer
st.caption("---")
st.caption("Educational demo – Non usare per scopi clinici. Filippo x ChatGPT 2025 🧬")
