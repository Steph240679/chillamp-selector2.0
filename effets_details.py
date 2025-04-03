# effets_details.py (version allégée pour chillamp-selector2.0)

effets_details = {
    "Darkglass Hyper Luminal": {
        "description": "Compresseur hybride avec circuits analogiques et contrôle digital.",
        "controls": {
            "Blend": {"type": "knob", "plage": "0-100", "effet": "mélange signal sec/compressé"},
            "Time": {"type": "knob", "plage": "0-100", "effet": "durée d'attaque et de relâchement"},
            "Output": {"type": "knob", "plage": "0-100", "effet": "niveau de sortie final"},
            "Ratio": {"type": "knob", "plage": "1:1 à ∞:1", "effet": "taux de compression"},
            "Mode": {"type": "switch", "plage": "BUS / FET / SYM", "effet": "type de compression"}
        }
    },
    "Way Huge Pork Loin": {
        "description": "Overdrive crèmeux avec EQ interne.",
        "controls": {
            "Volume": {"type": "knob", "plage": "0-100", "effet": "volume de sortie"},
            "Tone": {"type": "knob", "plage": "0-100", "effet": "balance fréquences aiguës"},
            "Drive": {"type": "knob", "plage": "0-100", "effet": "niveau de saturation"}
        }
    },
    "Boss CEB-3": {
        "description": "Chorus spécialement conçu pour les basses.",
        "controls": {
            "Effect Level": {"type": "knob", "plage": "0-100", "effet": "mélange entre son clair et chorus"},
            "Low Filter": {"type": "knob", "plage": "0-100", "effet": "filtre de fréquence pour les graves"},
            "Rate": {"type": "knob", "plage": "0-100", "effet": "vitesse de modulation"},
            "Depth": {"type": "knob", "plage": "0-100", "effet": "profondeur du chorus"}
        }
    },
    "EBS OctaBass": {
        "description": "Octaver analogique avec suivi précis.",
        "controls": {
            "Normal": {"type": "knob", "plage": "0-100", "effet": "volume du signal d'origine"},
            "Octave": {"type": "knob", "plage": "0-100", "effet": "volume du signal à l'octave inférieure"},
            "Range": {"type": "switch", "plage": "High / Mid / Low", "effet": "réponse adaptée aux fréquences jouées"}
        }
    },
    "Empress ParaEQ": {
        "description": "EQ paramétrique haute qualité pour basse ou guitare.",
        "controls": {
            "Gain Low": {"type": "knob", "plage": "-15dB à +15dB", "effet": "niveau de l’égalisation basse"},
            "Freq Low": {"type": "knob", "plage": "35Hz à 500Hz", "effet": "fréquence de l’égalisation basse"},
            "Gain Mid": {"type": "knob", "plage": "-15dB à +15dB", "effet": "niveau de l’égalisation médium"},
            "Freq Mid": {"type": "knob", "plage": "200Hz à 5kHz", "effet": "fréquence de l’égalisation médium"},
            "Q Mid": {"type": "switch", "plage": "Narrow / Medium / Wide", "effet": "largeur de bande du mid"},
            "Boost Switch": {"type": "switch", "plage": "On/Off", "effet": "active un boost de 30dB"}
        }
    }
}
