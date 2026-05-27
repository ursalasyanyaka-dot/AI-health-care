from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Clinic Finder API! Visit /clinics to get the list of clinics."

@app.route("/clinics/<district>")

def get_clinics(district):
    #build the path relative to app.py
    file_path = os.path.join(os.path.dirname(__file__), "clinics.json")
    #Load clinics.json
    with open(file_path, "r") as file:
        clinics = json.load(file)
    filtered = [c for c in clinics if c["district"].lower() == district.lower()]
    if not filtered:
        return jsonify({"message": f"No clinics found in {district}"}), 404
    
    return jsonify(filtered)



if __name__ == "__main__":
    app.run(debug=True)
    


