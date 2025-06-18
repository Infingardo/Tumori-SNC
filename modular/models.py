
"""Data models and static dataset for CNS Tumour Assistant (WHO CNS5 2021)."""
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class DiagnosticEntity:
    name: str
    pattern: str
    morphology: Dict[str, Any]          # e.g. {"necrosis": (0,1)}
    ihc: Dict[str, str]                 # marker -> expected ("pos","neg","loss","retain")
    mol: Dict[str, str]                 # flag -> expected ("pos","neg")
    site: str | None = None             # e.g. "midline", "emisferica"

# ---------------- ENTITIES ----------------
ENTITIES: Dict[str, DiagnosticEntity] = {
    # Adult diffuse
    "Astrocitoma IDH‑mutato": DiagnosticEntity(
        name="Astrocitoma IDH‑mutato",
        pattern="diffuse",
        morphology={"necrosis": (0,1), "microvascular": (0,1)},
        ihc={"IDH1_R132H": "pos", "ATRX": "loss"},
        mol={"IDH_mut": "pos", "Code1p19q": "neg"},
    ),
    "Oligodendroglioma IDH‑mut 1p/19q": DiagnosticEntity(
        name="Oligodendroglioma IDH‑mut 1p/19q",
        pattern="diffuse",
        morphology={"necrosis": (0,1), "microvascular": (0,1)},
        ihc={"IDH1_R132H": "pos", "ATRX": "retain"},
        mol={"IDH_mut": "pos", "Code1p19q": "pos"},
    ),
    "Glioblastoma IDH‑wt": DiagnosticEntity(
        name="Glioblastoma IDH‑wt",
        pattern="diffuse",
        morphology={"necrosis": (2,3), "microvascular": (1,1)},
        ihc={"IDH1_R132H": "neg"},
        mol={"EGFR_amp": "pos"},
    ),
    # Pediatric diffuse
    "Diffuse midline glioma H3 K27‑alt": DiagnosticEntity(
        name="Diffuse midline glioma H3 K27‑altered",
        pattern="diffuse",
        site="midline",
        morphology={},
        ihc={"H3K27M": "pos"},
        mol={"H3K27M_mut": "pos"},
    ),
    "Diffuse hemispheric glioma H3 G34‑mut": DiagnosticEntity(
        name="Diffuse hemispheric glioma H3 G34‑mut",
        pattern="diffuse",
        site="emisferica",
        morphology={},
        ihc={"H3G34": "pos", "ATRX": "loss"},
        mol={"H3G34_mut": "pos"},
    ),
    # Circumscribed
    "Astrocitoma pilocitico": DiagnosticEntity(
        name="Astrocitoma pilocitico",
        pattern="circumscribed",
        morphology={"rosenthal": 1},
        ihc={},
        mol={"KIAA1549_BRAF_fusion": "pos"},
    ),
    "PXA": DiagnosticEntity(
        name="Xantoastrocitoma pleomorfo",
        pattern="circumscribed",
        morphology={"xanthomatous": 1},
        ihc={"BRAF_V600E": "pos"},
        mol={"BRAF_V600E_mut": "pos"},
    ),
    "Ganglioglioma": DiagnosticEntity(
        name="Ganglioglioma",
        pattern="circumscribed",
        morphology={},
        ihc={"BRAF_V600E": "pos"},
        mol={"BRAF_V600E_mut": "pos"},
    ),
    # Ependymal
    "Ependimoma ZFTA‑fusion": DiagnosticEntity(
        name="Ependimoma ZFTA‑fusion",
        pattern="ependymal",
        morphology={},
        ihc={"L1CAM": "pos"},
        mol={"ZFTA_fusion": "pos"},
    ),
    "Ependimoma PFA": DiagnosticEntity(
        name="Ependimoma PFA",
        pattern="ependymal",
        morphology={},
        ihc={"H3K27me3": "loss"},
        mol={"EZHIP_over": "pos"},
    ),
    # Embryonal
    "Medulloblastoma WNT": DiagnosticEntity(
        name="Medulloblastoma WNT",
        pattern="embryonal",
        morphology={},
        ihc={"beta_catenin": "pos", "YAP1": "pos"},
        mol={"CTNNB1_mut": "pos"},
    ),
    "AT/RT": DiagnosticEntity(
        name="Atypical Teratoid/Rhabdoid Tumour",
        pattern="embryonal",
        morphology={},
        ihc={"INI1": "loss"},
        mol={"SMARCB1_del": "pos"},
    ),
}
