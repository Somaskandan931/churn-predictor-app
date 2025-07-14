from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from joblib import load
import traceback

from backend.explain_utils import ExplainabilityHelper
from backend.preprocess_utils import preprocess_input

# === Initialize Flask app ===
app = Flask(__name__)
CORS(app)  # Optional: CORS(app, origins=["http://localhost:3000"]) to restrict

# === Paths ===
MODEL_PATH = 'C:/Users/somas/PycharmProjects/OnSource_Churn_AI/models/xgb_churn_model.joblib'
COLUMNS_PATH = 'C:/Users/somas/PycharmProjects/OnSource_Churn_AI/models/train_columns.joblib'

# === Load model and training metadata ===
try:
    print("📦 Loading model and training metadata...")
    model = load(MODEL_PATH)
    train_columns = load(COLUMNS_PATH)
    explainer = ExplainabilityHelper(model)
    print("✅ Model and columns loaded successfully.")
except Exception as e:
    raise RuntimeError(f"❌ Failed to load model or columns: {e}")

# === Prediction Endpoint ===
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data received'}), 400

        print("📥 Incoming request:", data)

        # Preprocess
        input_processed = preprocess_input(data, train_columns)
        print("✅ Preprocessed input shape:", input_processed.shape)

        # Predict
        pred = int(model.predict(input_processed)[0])
        prob = float(model.predict_proba(input_processed)[0][1])  # Convert to native float

        print(f"🔮 Prediction: {pred}, Probability: {prob:.4f}")

        # SHAP explanation
        explanation_raw = explainer.get_shap_explanation(input_processed, top_n=5)

        # Convert explanation numeric values to native Python types for JSON serialization
        explanation = [
            {
                'feature': item.get('feature'),
                'impact': float(item.get('impact')) if item.get('impact') is not None else None
            }
            for item in explanation_raw
        ]

        return jsonify({
            'prediction': pred,
            'probability': round(prob, 4),
            'explanation': explanation
        })

    except Exception as e:
        print("❌ Exception during prediction:\n", traceback.format_exc())
        return jsonify({'error': str(e)}), 500

# === Health Check ===
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'}), 200

# === Run the Server ===
if __name__ == '__main__':
    app.run(debug=True, port=5000)
