# pdf_generator.py pour chillamp-selector2.0 avec effets enrichis

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import io

def _draw_preset_content(c, preset):
    width, height = A4
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"Preset : {preset['bassiste']}")

    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Généré le : {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Basse")
    y = draw_dict_block(c, preset["basse"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Ampli")
    y = draw_dict_block(c, preset["ampli"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Effets")

    for effet in preset["effets"]:
        nom_effet = effet.get("nom", "Effet inconnu")
        description = effet.get("description", "")
        controls = effet.get("controls", {})

        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60, y, nom_effet)

        if description:
            y -= 15
            c.setFont("Helvetica-Oblique", 11)
            c.drawString(70, y, description)

        if controls:
            y -= 15
            c.setFont("Helvetica", 11)
            c.drawString(70, y, "Contrôles :")
            for ctrl_nom, ctrl_data in controls.items():
                y -= 15
                ligne = f"- {ctrl_nom} ({ctrl_data.get('type')}): {ctrl_data.get('plage')} → {ctrl_data.get('effet')}"
                c.drawString(80, y, ligne)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Baffle")
    y = draw_dict_block(c, preset["baffle"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Chaîne du signal")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(60, y, " ➔ ".join(preset["chaine_signal"]))
    return c

def draw_dict_block(c, data, y, indent=60):
    c.setFont("Helvetica", 12)
    for key, value in data.items():
        y -= 20
        if isinstance(value, dict):
            c.drawString(indent, y, f"{key} :")
            y = draw_dict_block(c, value, y, indent + 20)
        else:
            c.drawString(indent, y, f"{key} : {value}")
    return y

def generate_preset_pdf(preset, filename="preset.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    _draw_preset_content(c, preset)
    c.save()

def generate_preset_pdf_flask(preset):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    try:
        _draw_preset_content(c, preset)
        c.save()
        buffer.seek(0)
        return buffer
    except Exception as e:
        print("Erreur PDF :", e)
        raise
