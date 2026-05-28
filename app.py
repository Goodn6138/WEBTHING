import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

data = {
    "height": 0,
    "weight": 0
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    global data
    content = request.json

    data["height"] = content.get("height", 0)
    data["weight"] = content.get("weight", 0)

    return jsonify({"status": "ok"})

@app.route("/data")
def get_data():
    return jsonify(data)

# REQUIRED for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
