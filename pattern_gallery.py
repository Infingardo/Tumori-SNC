# pattern_gallery.py

import streamlit as st
import os

# Path base (directory dove si trova questo file)
BASE_DIR = os.path.dirname(__file__)

# Dizionario dei pattern morfologici
PATTERNS = {
    "Homer-Wright": {
        "file": "rosetta.png",
        "caption": "Rosette di Homer-Wright — pattern di differenziazione neuroblastica"
    },
    "Flexner-Wintersteiner": {
        "file": "flexner.png",
        "caption": "Rosette di Flexner-Wintersteiner — tipiche del retinoblastoma"
    },
    "Pseudorosette Perivascolare": {
        "file": "pseudorosetta.png",
        "caption": "Pseudorosette perivascolari — pattern di ependimoma"
    }
}

def show_pattern_selector():
    """Mostra un selettore di pattern con immagine e didascalia dinamica."""
    st.subheader("Galleria Pattern Morfologici")
    
    selected = st.selectbox("Scegli il pattern:", list(PATTERNS.keys()))

    pattern_info = PATTERNS[selected]
    image_path = os.path.join(BASE_DIR, "assets", pattern_info["file"])

    st.image(image_path, caption=pattern_info["caption"], use_container_width=True)

    return selected
