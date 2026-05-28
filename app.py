from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# store latest sensor data
data = {
    "height": 0,
    "weight": 0
}

# homepage
@app.route("/")
def home():
    return render_template("index.html")

# Arduino sends data here
@app.route("/update", methods=["POST"])
def update():
    global data
    content = request.json

    data["height"] = content.get("height", 0)
    data["weight"] = content.get("weight", 0)

    return jsonify({"status": "ok"})

# frontend fetches data here
@app.route("/data")
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
