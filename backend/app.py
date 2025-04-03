# app.py - chillamp-selector2.0 (version claire et minimaliste)

import os
from flask import Flask, request, jsonify, send_file, send_from_directory
from preset_engine import get_presets_for_combination
from pdf_generator import generate_preset_pdf_flask
from base_bassistes import base_bassistes
from effets_details import effets_details
from amplis_basse_etendus import amplis_basse

app = Flask(__name__)

# --- API de génération de preset JSON ---
@app.route("/api/preset", methods=["POST"])
def generate_preset():
    data = request.get_json()
    preset = get_presets_for_combination(
        data.get("bassiste"),
        data.get("basse"),
        data.get("ampli"),
        data.get("effets", []),
        data.get("baffle")
    )
    return jsonify(preset)

# --- API de génération de preset PDF ---
@app.route("/api/preset/pdf", methods=["POST"])
def generate_preset_pdf():
    data = request.get_json()
    preset = get_presets_for_combination(
        data.get("bassiste"),
        data.get("basse"),
        data.get("ampli"),
        data.get("effets", []),
        data.get("baffle")
    )
    pdf_buffer = generate_preset_pdf_flask(preset)
    return send_file(pdf_buffer, as_attachment=True, download_name="preset_chillamp.pdf", mimetype="application/pdf")

# --- Routes de données ---
@app.route("/api/liste_bassistes")
def list_bassistes():
    return jsonify(sorted(base_bassistes.keys()))

@app.route("/api/liste_amplis")
def list_amplis():
    return jsonify(sorted(amplis_basse.keys()))

@app.route("/api/liste_baffles")
def list_baffles():
    return jsonify(["Chillamp Classic 1x15", "Chillamp Classic 4x12", "Chillamp Neo 1x10", "Ampeg SVT 8x10", "Aguilar DB 112"])

@app.route("/api/liste_basses")
def list_basses():
    return jsonify(["Fender Precision", "Fender Jazz", "Music Man StingRay", "Squier Vintage Modified", "Yamaha BB434"])

@app.route("/api/liste_effets")
def list_effets():
    return jsonify(list(effets_details.keys()))

# --- Serveur du frontend ---
@app.route("/")
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

