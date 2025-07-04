
import streamlit as st
import os

st.set_page_config(
    page_title="🧠 Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Assistente Diagnostico Tumori SNC – WHO CNS5 (Extended Plus)")
st.caption("Educational demo – Non usare per scopi clinici. Filippo x ChatGPT 2025 🧬")

# 1️⃣ Caratteristiche clinico-morfologiche
st.subheader("1️⃣ Caratteristiche clinico-morfologiche")

sede = st.selectbox("Seleziona la sede:", [
    "Seleziona...", 
    "Lobo frontale", 
    "Lobo parietale", 
    "Lobo temporale",
    "Lobo occipitale",
    "Cervelletto", 
    "Tronco encefalico",
    "Midollo spinale",
    "Regione sellare",
    "Ventricoli"
])

pattern = st.radio("Pattern di crescita:", ["Diffuso", "Circostritto"])
fascia_eta = st.radio("Fascia d'età:", ["Pediatrico (<18 anni)", "Adulto (18-65 anni)", "Anziano (>65 anni)"])

if sede != "Seleziona...":
    st.info(f"📍 Sede selezionata: {sede}")

# Ipotesi diagnostica base con logica espansa
def genera_ipotesi_iniziale(fascia_eta, pattern, sede):
    if fascia_eta == "Adulto (18-65 anni)" and pattern == "Diffuso":
        return "🟢 Ipotesi iniziale: Astrocitoma diffuso o Oligodendroglioma."
    elif fascia_eta == "Pediatrico (<18 anni)" and pattern == "Circostritto":
        if sede == "Cervelletto":
            return "🟢 Ipotesi iniziale: Medulloblastoma."
        else:
            return "🟢 Ipotesi iniziale: Possibile PNET o tumore embrionale."
    elif fascia_eta == "Anziano (>65 anni)" and pattern == "Diffuso":
        return "🟠 Ipotesi iniziale: Probabile Glioblastoma IDH-wildtype."
    else:
        return "ℹ️ Ipotesi: valutare correlazione con imaging e clinica."

ipotesi = genera_ipotesi_iniziale(fascia_eta, pattern, sede)
st.success(ipotesi) if "🟢" in ipotesi else st.warning(ipotesi) if "🟠" in ipotesi else st.info(ipotesi)

# Mostra immagine rosetta se pattern circoscritto (con controllo file)
if pattern == "Circostritto":
    if os.path.exists("assets/rosetta.png"):
        st.image(
            "assets/rosetta.png",
            caption="Rosette di Homer-Wright, Flexner-Wintersteiner e pseudorosette di ependimoma.",
            use_container_width=True
        )
    else:
        st.warning("📸 Immagine rosetta non disponibile (assets/rosetta.png)")

# 2️⃣ Pannello Immunoistochimico
st.subheader("2️⃣ Pannello IIC di base")

col1, col2 = st.columns(2)

with col1:
    idh1 = st.radio("IDH1 R132H:", ["Non testato", "Positivo", "Negativo"], index=0)
    atrx = st.radio("ATRX:", ["Non testato", "Perdita", "Conservato"], index=0)
    gfap = st.radio("GFAP:", ["Non testato", "Positivo", "Negativo"], index=0)

with col2:
    p53 = st.radio("p53:", ["Non testato", "Positivo", "Negativo"], index=0)
    ki67 = st.radio("Ki-67 (%):", ["Non testato", "<5%", "5-15%", ">15%"], index=0)
    egfr = st.radio("EGFR:", ["Non testato", "Amplificato", "Non amplificato"], index=0)

# 3️⃣ Profilo molecolare
st.subheader("3️⃣ Profilo molecolare")

col3, col4 = st.columns(2)

with col3:
    mgmt = st.radio("Metilazione MGMT:", ["Non testato", "Metilato", "Non metilato"], index=0)
    tert = st.radio("Mutazione TERT:", ["Non testato", "Presente", "Assente"], index=0)

with col4:
    codelezione_1p19q = st.radio("Codelezione 1p/19q:", ["Non testato", "Presente", "Assente"], index=0)
    h3k27me3 = st.radio("H3K27me3:", ["Non testato", "Perdita", "Conservato"], index=0)

# 4️⃣ Diagnosi suggerita con logica espansa
st.subheader("4️⃣ Diagnosi suggerita")

def genera_diagnosi(idh1, atrx, gfap, tert, codelezione_1p19q, p53, fascia_eta):
    diagnosi = []
    
    if idh1 == "Positivo":
        if atrx == "Perdita":
            diagnosi.append("✅ Astrocitoma diffuso IDH-mutato")
        elif codelezione_1p19q == "Presente":
            diagnosi.append("✅ Oligodendroglioma IDH-mutato, 1p/19q codeleto")
        else:
            diagnosi.append("✅ Glioma IDH-mutato (specificare con ulteriori test)")
    
    elif idh1 == "Negativo":
        if tert == "Presente" and fascia_eta in ["Adulto (18-65 anni)", "Anziano (>65 anni)"]:
            diagnosi.append("⚠️ Glioblastoma IDH-wildtype")
        else:
            diagnosi.append("⚠️ Glioma IDH-wildtype (considerare ulteriori test)")
    
    else:
        diagnosi.append("🔬 Test IDH necessario per classificazione WHO CNS5")
    
    return diagnosi

diagnosi_list = genera_diagnosi(idh1, atrx, gfap, tert, codelezione_1p19q, p53, fascia_eta)

for diagnosi in diagnosi_list:
    if "✅" in diagnosi:
        st.success(diagnosi)
    elif "⚠️" in diagnosi:
        st.warning(diagnosi)
    else:
        st.info(diagnosi)

# 5️⃣ Raccomandazioni terapeutiche (se applicabile)
if mgmt == "Metilato" and "Glioblastoma" in str(diagnosi_list):
    st.subheader("5️⃣ Considerazioni terapeutiche")
    st.success("💊 MGMT metilato: possibile beneficio da temozolomide")

# 6️⃣ Controllo completezza dati
st.subheader("6️⃣ Controllo completezza")

test_essenziali = [idh1, atrx, gfap]
test_opzionali = [mgmt, tert, codelezione_1p19q, p53, ki67, egfr, h3k27me3]

essenziali_completati = sum(1 for test in test_essenziali if test != "Non testato")
opzionali_completati = sum(1 for test in test_opzionali if test != "Non testato")

st.metric("Test essenziali completati", f"{essenziali_completati}/3")
st.metric("Test opzionali completati", f"{opzionali_completati}/7")

if essenziali_completati < 3:
    st.warning("⚠️ Completare i test essenziali per diagnosi definitiva")

# 📚 Riferimenti bibliografici
with st.expander("📚 Riferimenti bibliografici"):
    st.markdown("""
    - WHO Classification of Tumours Editorial Board. *Central Nervous System Tumours*, 5th ed., IARC, Lyon, 2021.
    - Louis DN et al. The 2021 WHO Classification of Tumors of the Central Nervous System: a summary. *Neuro-Oncology*, 2021.
    - Brat DJ, Aldape K, et al. Molecular Pathology of CNS Tumors. *J Neuropathol Exp Neurol*. 2021.
    - Eckel-Passow JE et al. Glioma Groups Based on 1p/19q, IDH, and TERT Promoter Mutations. *NEJM*, 2015.
    """)
    
    # Controllo esistenza file PDF
    if os.path.exists("assets/Brain2021.pdf"):
        st.markdown("📄 👉 [Scarica WHO CNS5 2021 (Brain)](assets/Brain2021.pdf)")
    else:
        st.warning("📄 File Brain2021.pdf non disponibile in assets/")

# Footer
st.markdown("---")
st.caption("Educational demo – Non usare per scopi clinici. Versione Filippo x ChatGPT 2025 🧬")

# Debug info (rimuovere in produzione)
if st.checkbox("Mostra info debug"):
    st.json({
        "sede": sede,
        "pattern": pattern,
        "fascia_eta": fascia_eta,
        "idh1": idh1,
        "atrx": atrx,
        "gfap": gfap,
        "mgmt": mgmt,
        "tert": tert
    })
