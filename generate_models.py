"""
Model Generation Script for Water Stress Index Prediction

This script trains and saves:
1. Random Forest model for WSI prediction
2. StandardScaler for feature normalization

Run this script to generate pkl files needed by app.py
Usage: python generate_models.py
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import os

def generate_models():
    """Generate and save ML models for WSI prediction"""
    
    print("=" * 60)
    print("Water Stress Index Model Generation")
    print("=" * 60)
    
    # Load dataset
    print("\n📂 Loading dataset...")
    df = pd.read_csv("dataset.csv")
    print(f"✅ Loaded {len(df)} villages")
    
    # Feature engineering for training data
    print("\n🔧 Performing feature engineering...")
    
    # Create synthetic target variable (WSI) based on features
    # WSI = f(rainfall_deviation, groundwater_depth, population, storage_ratio)
    
    rainfall_deviation = (df['rainfall_current'] - df['rainfall_average']) / df['rainfall_average']
    storage_ratio = df['current_storage'] / df['storage_capacity']
    normalized_population = (df['population'] - df['population'].min()) / (
        df['population'].max() - df['population'].min()
    )
    normalized_depth = (df['groundwater_depth'] - df['groundwater_depth'].min()) / (
        df['groundwater_depth'].max() - df['groundwater_depth'].min()
    )
    
    # Generate synthetic WSI target
    # Logic: Lower rainfall, deeper groundwater, larger population, lower storage = higher stress
    wsi = (
        (1 - storage_ratio) * 0.4 +  # Storage capacity impact (40%)
        (normalized_depth) * 0.3 +   # Groundwater depth (30%)
        (normalized_population) * 0.2 +  # Population impact (20%)
        (np.maximum(-rainfall_deviation, 0)) * 0.1  # Rainfall deficit (10%)
    )
    
    # Normalize WSI to 0-1 range
    wsi = (wsi - wsi.min()) / (wsi.max() - wsi.min())
    
    df['WSI_target'] = wsi
    
    print("✅ Feature engineering complete")
    
    # Prepare features for model training
    print("\n🤖 Preparing training data...")
    
    feature_columns = [
        'rainfall_current',
        'rainfall_average',
        'groundwater_depth',
        'population',
        'current_storage'
    ]
    
    X = df[feature_columns].copy()
    y = df['WSI_target'].copy()
    
    print(f"✅ Features: {feature_columns}")
    print(f"✅ Training samples: {len(X)}")
    
    # Create and fit scaler
    print("\n📊 Creating StandardScaler...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("✅ Scaler fitted and transformed")
    
    # Split data
    print("\n✂️  Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    print(f"✅ Train: {len(X_train)}, Test: {len(X_test)}")
    
    # Train Random Forest model
    print("\n🌲 Training Random Forest model...")
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    print("✅ Model training complete")
    
    # Evaluate model
    print("\n📈 Model Evaluation:")
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    
    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
    
    print(f"   Train R² Score: {train_r2:.4f}")
    print(f"   Test R² Score:  {test_r2:.4f}")
    print(f"   Train RMSE:     {train_rmse:.4f}")
    print(f"   Test RMSE:      {test_rmse:.4f}")
    
    # Feature importance
    print("\n📊 Feature Importance:")
    feature_importance = pd.DataFrame({
        'Feature': feature_columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    for idx, row in feature_importance.iterrows():
        print(f"   {row['Feature']}: {row['Importance']:.4f}")
    
    # Save models
    print("\n💾 Saving models...")
    
    model_path = "random_forest.pkl"
    scaler_path = "scaler.pkl"
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"✅ Saved: {model_path}")
    
    with open(scaler_path, 'wb') as f:
        pickle.dump(scaler, f)
    print(f"✅ Saved: {scaler_path}")
    
    # Verify files
    print("\n🔍 Verification:")
    if os.path.exists(model_path) and os.path.exists(scaler_path):
        model_size = os.path.getsize(model_path) / 1024
        scaler_size = os.path.getsize(scaler_path) / 1024
        print(f"✅ {model_path} ({model_size:.2f} KB)")
        print(f"✅ {scaler_path} ({scaler_size:.2f} KB)")
    else:
        print("❌ Error saving files!")
        return False
    
    # Test prediction
    print("\n🧪 Testing predictions...")
    all_pred = model.predict(X_scaled)
    print(f"✅ Predictions generated for all {len(all_pred)} villages")
    print(f"   Min WSI: {all_pred.min():.4f}")
    print(f"   Max WSI: {all_pred.max():.4f}")
    print(f"   Mean WSI: {all_pred.mean():.4f}")
    print(f"   Std WSI: {all_pred.std():.4f}")
    
    print("\n" + "=" * 60)
    print("✅ Model generation complete!")
    print("   Ready to use with app.py")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    try:
        generate_models()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
