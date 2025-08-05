from flask import Blueprint, request, jsonify
import joblib
import json
import numpy as np
from keras.models import load_model
from utils.pesticide_recommender import recommend_pesticide

api_bp = Blueprint("api", __name__)

# Load soil classifier
soil_model = joblib.load("models/soil_classifier.pkl")

# Load disease model
disease_model = load_model("models/plant_disease_recog_model_pwp.keras")

# Load disease info
with open("data/plant_diseases.json") as f:
    disease_data = json.load(f)

@api_bp.route("/soil/predict", methods=["POST"])
def predict_soil():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)
    prediction = soil_model.predict(features)[0]
    return jsonify({"soil_type": int(prediction)})

@api_bp.route("/disease/info", methods=["GET"])
def disease_info():
    disease_key = request.args.get("disease")
    info = disease_data["diseases"].get(disease_key, {})
    return jsonify(info)

@api_bp.route("/pesticide/recommend", methods=["POST"])
def recommend():
    data = request.json
    crop = data.get("crop")
    disease = data.get("disease")
    recommendation = recommend_pesticide(crop, disease)
    return jsonify(recommendation)
