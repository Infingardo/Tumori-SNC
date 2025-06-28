import streamlit as st

st.set_page_config(page_title="CNS Tumour Diagnostic Assistant", page_icon="🧠")

st.title("🧠 CNS Tumour Diagnostic Assistant")
st.subheader("WHO CNS5 (2021) – Diagnosi guidata (versione demo)")

# Selezione età
age_group = st.radio(
    "1️⃣ Fascia d'età del paziente:",
    ["Adulto", "Pediatrico"],
    index=0
)

if age_group == "Adulto":
    st.write("👉 Tumori cerebrali dell'adulto")
    
    infiltration = st.radio(
        "2️⃣ Pattern di crescita:",
        ["Diffuso", "Non diffuso"]
    )
    
    if infiltration == "Diffuso":
        st.write("👉 Analisi molecolare")
        
        idh_status = st.radio("IDH status:", ["IDH-mutato", "IDH-wildtype"])
        
        if idh_status == "IDH-mutato":
            atrx_status = st.radio("ATRX:", ["Perdita", "Conservato"])
            if atrx_status == "Perdita":
                st.success("🔬 **Diagnosi suggerita:** Astrocitoma diffuso IDH-mutato (probabile).")
                st.info("Suggeriti: valutazione TP53, grading istologico.")
            else:
                codeletion = st.radio("1p/19q codelezione:", ["Presente", "Assente"])
                if codeletion == "Presente":
                    st.success("🔬 **Diagnosi suggerita:** Oligodendroglioma IDH-mutato, 1p/19q codeleted.")
                else:
                    st.warning("Possibile astrocitoma IDH-mutato con ATRX conservato: confermare con TP53.")
        
        else:  # IDH-wildtype
            st.warning("Considera gli high-grade: GBM IDH-wildtype? AAP e alterazioni TERT/EGFR?")
            st.info("Suggeriti: MGMT, TERT, EGFR, + imaging clinico.")
            
    else:
        st.write("👉 Per forme non diffuse, vanno considerate entità circoscritte (es. piloide, ganglioglioma).")
        st.info("Consulta la sezione corrispondente nel WHO CNS5.")
        
else:
    st.warning("🚧 Sezione tumori pediatrici in sviluppo.")

# Footer
st.caption("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")
