from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, template_folder='.', static_folder='.')

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)

# Load model and scaler
MODEL_PATH = os.path.join(SCRIPT_DIR, 'wsi_model.pkl')
SCALER_PATH = os.path.join(SCRIPT_DIR, 'scaler.pkl')
DATASET_PATH = os.path.join(PARENT_DIR, 'dataset.csv')

# Load dataset for village list and existing data
try:
    df = pd.read_csv(DATASET_PATH)
except FileNotFoundError:
    df = pd.DataFrame()

# Load model and scaler if they exist
if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
else:
    model = None
    scaler = None
    print("Warning: Model files not found. Train the model first using app.py")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/villages', methods=['GET'])
def get_villages():
    """Get all villages and their current data"""
    if df.empty:
        return jsonify({'error': 'Dataset not found'}), 404
    
    villages_data = []
    for _, row in df.iterrows():
        village_info = {
            'village_name': row['village_name'],
            'rainfall_current': float(row['rainfall_current']),
            'rainfall_average': float(row['rainfall_average']),
            'groundwater_depth': float(row['groundwater_depth']),
            'population': int(row['population']),
            'storage_capacity': int(row['storage_capacity']),
            'current_storage': int(row['current_storage']),
            'latitude': float(row['latitude']),
            'longitude': float(row['longitude']),
            'wsi': calculate_wsi(row['storage_capacity'], row['current_storage'])
        }
        villages_data.append(village_info)
    
    return jsonify(villages_data)

@app.route('/api/predict', methods=['POST'])
def predict():
    """Predict WSI based on input parameters"""
    if model is None or scaler is None:
        return jsonify({'error': 'Model not trained yet. Please run app.py first.'}), 500
    
    try:
        data = request.json
        
        # Extract features in correct order
        features = [
            float(data.get('rainfall_current', 0)),
            float(data.get('rainfall_average', 0)),
            float(data.get('groundwater_depth', 0)),
            float(data.get('population', 0)),
            float(data.get('storage_capacity', 0)),
            float(data.get('current_storage', 0))
        ]
        
        # Scale features
        features_scaled = scaler.transform([features])
        
        # Make prediction
        wsi_prediction = model.predict(features_scaled)[0]
        
        # Interpret WSI
        interpretation = interpret_wsi(wsi_prediction)
        
        return jsonify({
            'wsi': float(wsi_prediction),
            'interpretation': interpretation,
            'features': {
                'rainfall_current': features[0],
                'rainfall_average': features[1],
                'groundwater_depth': features[2],
                'population': features[3],
                'storage_capacity': int(features[4]),
                'current_storage': int(features[5])
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/village/<name>', methods=['GET'])
def get_village_detail(name):
    """Get detailed information for a specific village"""
    if df.empty:
        return jsonify({'error': 'Dataset not found'}), 404
    
    village = df[df['village_name'].str.lower() == name.lower()]
    if village.empty:
        return jsonify({'error': 'Village not found'}), 404
    
    row = village.iloc[0]
    detail = {
        'village_name': row['village_name'],
        'rainfall_current': float(row['rainfall_current']),
        'rainfall_average': float(row['rainfall_average']),
        'groundwater_depth': float(row['groundwater_depth']),
        'population': int(row['population']),
        'storage_capacity': int(row['storage_capacity']),
        'current_storage': int(row['current_storage']),
        'latitude': float(row['latitude']),
        'longitude': float(row['longitude']),
        'wsi': calculate_wsi(row['storage_capacity'], row['current_storage'])
    }
    return jsonify(detail)

def calculate_wsi(storage_capacity, current_storage):
    """Calculate Water Stress Index"""
    return (storage_capacity - current_storage) / storage_capacity

def interpret_wsi(wsi):
    """Interpret WSI value"""
    if wsi < 0.3:
        return "Low Water Stress - Good water availability"
    elif wsi < 0.6:
        return "Moderate Water Stress - Adequate water reserves"
    elif wsi < 0.8:
        return "High Water Stress - Limited water reserves"
    else:
        return "Critical Water Stress - Severe water shortage"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
