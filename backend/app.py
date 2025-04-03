from flask import Flask, request, jsonify, send_file, send_from_directory
from preset_engine import get_presets_for_combination
from pdf_generator import generate_preset_pdf_flask
from base_bassistes import base_bassistes
from profils_sonores import profils_sonores
from effets_details import effets_details
from amplis_basse_etendus import amplis_basse

app = Flask(__name__)

@app.route("/api/preset", methods=["POST"])
def generate_preset():
    data = request.get_json()
    bassiste = data.get("bassiste")
    basse = data.get("basse")
    ampli = data.get("ampli")
    effets = data.get("effets", [])
    baffle = data.get("baffle")

    preset = get_presets_for_combination(bassiste, basse, ampli, effets, baffle)
    return jsonify(preset)

@app.route("/api/preset/pdf", methods=["POST"])
def generate_preset_pdf():
    data = request.get_json()
    bassiste = data.get("bassiste")
    basse = data.get("basse")
    ampli = data.get("ampli")
    effets = data.get("effets", [])
    baffle = data.get("baffle")

    preset = get_presets_for_combination(bassiste, basse, ampli, effets, baffle)
    pdf_buffer = generate_preset_pdf_flask(preset)
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="preset_chillamp.pdf",
        mimetype="application/pdf"
    )

@app.route("/")
def serve_frontend():
    return send_from_directory("../frontend", "index.html")
