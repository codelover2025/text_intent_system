from flask import Flask, Blueprint, request, jsonify
from auth import verify_key
from rules import rule_based_intent
from model import load_model, predict
from utils import clean_text

api_bp = Blueprint("api", __name__)  # Initialize the blueprint
model = None  # Initialize model variable

# Load the model only once when the app starts
def load_model_once():
    global model
    if model is None:
        try:
            model = load_model()  # This should load the model
            print("Model loaded successfully!")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise e

@api_bp.route("/predict", methods=["POST"])
def predict_intent():
    load_model_once()  # Ensure the model is loaded before making a prediction
    
    data = request.get_json()
    key = data.get("key")
    guid = data.get("guid")
    text = data.get("text")

    if not all([key, guid, text]):
        return jsonify({"error": "Missing key, guid, or text"}), 400

    if not verify_key(key):
        return jsonify({"error": "Invalid API key"}), 403

    # Rule-based filter
    intent = rule_based_intent(text)
    
    # If rule fails, use ML
    if intent is None:
        intent = predict(model, text)  # Now the model should be loaded and ready to use

    return jsonify({
        "guid": guid,
        "text": text,
        "intent": intent
    })

# Create the app using the blueprint
def create_app():
    app = Flask(__name__)  # Initialize the Flask app
    app.register_blueprint(api_bp, url_prefix='/api')  # Register blueprint with a URL prefix
    return app
