from profils_sonores import profils_sonores
from amplis_basse_etendus import amplis_basse

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
        reglages[bande] = max(0, min(100, base + delta))  # clamp 0-100

    return reglages
