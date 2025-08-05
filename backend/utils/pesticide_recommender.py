import json

# Load pesticides data
with open("data/pesticides.json") as f:
    pesticide_data = json.load(f)

def recommend_pesticide(crop, disease):
    # Example logic: find pesticide that matches both crop and disease
    recommendations = []
    for item in pesticide_data.get("pesticides", []):
        if crop in item.get("crops", []) and disease in item.get("targets", []):
            recommendations.append(item["name"])
    return {
        "crop": crop,
        "disease": disease,
        "recommended_pesticides": recommendations
    }
