# preset_engine.py - version chillamp-selector2.0 avec enrichissement effets

from base_bassistes import base_bassistes
from profils_sonores import profils_sonores
from amplis_basse_etendus import amplis_basse
from effets_details import effets_details

def adapter_eq_ampli(ampli_nom, profil_cible):
    if ampli_nom not in amplis_basse:
        raise ValueError(f"Ampli inconnu : {ampli_nom}")

    ampli_data = amplis_basse[ampli_nom]
    eq_bandes = ampli_data["eq"]
    neutral = ampli_data["neutral"]
    tendance = profils_sonores[profil_cible]["tendance"]

    reglages = {}
    for bande in eq_bandes:
        bande_lower = bande.lower()
        if "low" in bande_lower or "bass" in bande_lower:
            delta = tendance["bass"]
        elif "mid" in bande_lower:
            delta = tendance["mid"]
        elif "high" in bande_lower or "treble" in bande_lower:
            delta = tendance["treble"]
        else:
            delta = 0

        base = neutral.get(bande, 50)
        reglages[bande] = max(0, min(100, base + delta))

    return reglages

def get_presets_for_combination(bassiste, basse, ampli, effets, baffle):
    if bassiste not in base_bassistes:
        raise ValueError(f"Bassiste '{bassiste}' non trouvé.")

    # Extraction du profil sonore à partir du caractère
    profil_sonore = base_bassistes[bassiste]["caractere"].split('.')[-1].strip()

    # Génération des réglages par module
    reglage_ampli = adapter_eq_ampli(ampli, profil_sonore)

    # Enrichissement des effets sélectionnés
    effets_configures = []
    for effet in effets:
        details = effets_details.get(effet, {})
        effets_configures.append({
            "nom": effet,
            "description": details.get("description", ""),
            "controls": details.get("controls", {})
        })

    return {
        "bassiste": bassiste,
        "basse": {
            "modele": basse,
            "type": "active",
            "reglages": {
                "volume": 80,
                "tone": 60
            }
        },
        "ampli": {
            "modele": ampli,
            "reglages": reglage_ampli
        },
        "effets": effets_configures,
        "baffle": {
            "modele": baffle,
            "profil": "standard"
        },
        "chaine_signal": [basse] + effets + [ampli, baffle]
    }
