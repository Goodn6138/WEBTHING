import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ORIGINAL DATA (UNCHANGED)
data = {
    "height": 0,
    "weight": 0
}

# NEW ENERGY DICTIONARY
ENERGY = {
    "ENERGY": 0
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():

    global data
    global ENERGY

    content = request.json

    # ORIGINAL DATA
    data["height"] = content.get("height", 0)
    data["weight"] = content.get("weight", 0)

    # NEW ENERGY DATA
    ENERGY["ENERGY"] = content.get("ENERGY", 0)

    return jsonify({"status": "ok"})

@app.route("/data")
def get_data():
    return jsonify(data)

# OPTIONAL ENERGY ENDPOINT
@app.route("/energy")
def get_energy():
    return jsonify(ENERGY)

# REQUIRED for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
