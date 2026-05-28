import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ORIGINAL DATA
data = {
    "height": 0,
    "weight": 0
}

# ENERGY DATA
ENERGY = {
    "ENERGY": 0
}

# MOOD DATA
MOOD = {
    "MOOD": "neutral",
    "CONFIDENCE": 0
}

@app.route("/")
def home():
    return render_template("index.html")

# =========================
# UPDATE ALL DATA
# =========================
@app.route("/update", methods=["POST"])
def update():

    global data
    global ENERGY
    global MOOD

    content = request.json

    # ORIGINAL DATA
    data["height"] = content.get("height", data["height"])
    data["weight"] = content.get("weight", data["weight"])

    # ENERGY
    ENERGY["ENERGY"] = content.get(
        "ENERGY",
        ENERGY["ENERGY"]
    )

    # MOOD
    MOOD["MOOD"] = content.get(
        "MOOD",
        MOOD["MOOD"]
    )

    MOOD["CONFIDENCE"] = content.get(
        "CONFIDENCE",
        MOOD["CONFIDENCE"]
    )

    return jsonify({
        "status": "ok"
    })

# =========================
# ROUTES
# =========================
@app.route("/data")
def get_data():
    return jsonify(data)

@app.route("/energy")
def get_energy():
    return jsonify(ENERGY)

@app.route("/mood")
def get_mood():
    return jsonify(MOOD)

# =========================
# RUN
# =========================
if __name__ == "__main__":

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
