"""
GreenCheck - Plant and Soil Analysis System
Main Flask Application
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import logging
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'greencheck-secret-key-2024'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Enable CORS for frontend integration
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    """Main dashboard page"""
    return jsonify({
        "message": "Welcome to GreenCheck API",
        "version": "1.0.0",
        "endpoints": {
            "plant_analysis": "/api/analyze-plant",
            "soil_analysis": "/api/analyze-soil", 
            "pesticide_recommendation": "/api/recommend-pesticide",
            "chat": "/api/chat",
            "health": "/api/health"
        }
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/analyze-plant', methods=['POST'])
def analyze_plant():
    """Analyze plant image for disease detection"""
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Mock analysis result
        result = {
            "success": True,
            "result": {
                "disease": "early_blight",
                "confidence": 0.94,
                "crop_type": "tomato",
                "severity": "medium",
                "description": "Fungal disease causing brown spots with concentric rings on leaves"
            },
            "pesticide_recommendation": {
                "primary_recommendations": [
                    {
                        "name": "Copper Fungicide",
                        "type": "organic",
                        "application_rate": "1-2 tablespoons per gallon",
                        "safety_rating": "moderately_safe"
                    }
                ]
            },
            "timestamp": datetime.now().isoformat()
        }

        return jsonify(result)

    except Exception as e:
        logger.error(f"Error in plant analysis: {str(e)}")
        return jsonify({"error": "Analysis failed"}), 500

@app.route('/api/analyze-soil', methods=['POST'])
def analyze_soil():
    """Analyze soil image for health assessment"""
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Mock soil analysis result
        result = {
            "success": True,
            "result": {
                "soil_type": "loam",
                "ph_level": 6.8,
                "moisture_level": 0.65,
                "organic_matter": 0.45,
                "health_score": 0.88,
                "fertility": "excellent",
                "recommendations": [
                    "Maintain current organic matter levels",
                    "Continue balanced irrigation practices"
                ],
                "suitable_crops": ["tomatoes", "peppers", "lettuce"]
            },
            "timestamp": datetime.now().isoformat()
        }

        return jsonify(result)

    except Exception as e:
        logger.error(f"Error in soil analysis: {str(e)}")
        return jsonify({"error": "Analysis failed"}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chatbot conversations"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        # Mock chatbot response
        bot_response = "I can help you with plant diseases, soil health, and pesticide recommendations. What specific agricultural question do you have?"

        return jsonify({
            "success": True,
            "response": bot_response,
            "timestamp": datetime.now().isoformat()
        })

    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        return jsonify({"error": "Chat failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)