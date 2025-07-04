# diagnostic_assistant_interactive.py

import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="CNS Tumour Diagnostic Assistant",
    page_icon="🧠",
    layout="centered"
)

# Sidebar: flowchart e riferimenti
st.sidebar.image(
    "assets/flowchart_who_cns5.png",
    caption="WHO CNS5 Tumours Flowchart",
    use_container_width=True
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Riferimento**: WHO Classification of Tumours of the Central Nervous System, 5th Ed. (2021).")

# Header
st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5")
st.caption("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")

st.write("**Benvenuto!** Segui i passaggi per navigare l’algoritmo diagnostico basato sulla classificazione WHO CNS5 (2021).")

# Step 1: Età
age_group = st.radio(
    "1️⃣ Fascia d'età del paziente:",
    ["Adulto", "Pediatrico"],
    index=0
)

# Step 2: Pattern di crescita
if age_group == "Adulto":
    st.subheader("👉 Tumori cerebrali dell’adulto")

    pattern = st.radio(
        "2️⃣ Pattern di crescita:",
        ["Diffuso", "Non diffuso"]
    )

    if pattern == "Diffuso":
        st.subheader("🔬 Analisi molecolare")
        
        idh = st.radio("IDH status:", ["IDH-mutato", "IDH-wildtype"])
        
        if idh == "IDH-mutato":
            atrx = st.radio("ATRX:", ["Perdita", "Conservato"])
            
            if atrx == "Perdita":
                st.success("**Diagnosi suggerita:** Astrocitoma diffuso IDH-mutato.")
                st.info("Suggeriti: TP53, grading istologico.")
            
            else:
                codeletion = st.radio("1p/19q codelezione:", ["Presente", "Assente"])
                if codeletion == "Presente":
                    st.success("**Diagnosi suggerita:** Oligodendroglioma IDH-mutato, 1p/19q codeleted.")
                else:
                    st.warning("Possibile astrocitoma IDH-mutato con ATRX conservato: confermare TP53.")
        
        else:  # IDH-wildtype
            st.warning("Considera GBM IDH-wildtype: AAP, TERT, EGFR?")
            st.info("Suggeriti: MGMT, TERT, EGFR, imaging clinico.")
    
    else:
        st.info("Per pattern **non diffusi**, considera entità come pilocitoma, ganglioglioma, pleomorfo, etc.")
        st.write("Consulta le entità circoscritte nel WHO CNS5.")

else:
    st.warning("🚧 *Sezione tumori pediatrici in sviluppo.*")

# Footer
st.markdown("---")
st.caption("📚 *Riferimento bibliografico*: WHO CNS5 2021 | Educational use only.")
