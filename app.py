import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os

# Function to load and preprocess data
def load_and_preprocess_data(file_path='dataset.csv'):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found. Please ensure it's in the correct directory.")

    df = pd.read_csv(file_path)

    # Handle missing values (if any - based on previous check, there were none)
    if df.isnull().sum().sum() > 0:
        print("Missing values detected. Consider imputation or removal.")
        # Example: df.dropna(inplace=True)
        # Example: df.fillna(df.mean(), inplace=True)

    # Calculate WSI
    df['WSI'] = (df['storage_capacity'] - df['current_storage']) / df['storage_capacity']

    # Define features and target
    features = ['rainfall_current', 'rainfall_average', 'groundwater_depth', 'population', 'storage_capacity', 'current_storage']
    X = df[features]
    y = df['WSI']

    return X, y

# Function to train and evaluate the model
def train_and_evaluate_model(X, y, test_size=0.2, random_state=42):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the model
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train_scaled, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"R-squared (R^2) Score: {r2:.4f}")

    return model, scaler, X_test, y_test, y_pred

# Main execution block
if __name__ == '__main__':
    print("Starting model pipeline...")

    # Step 1 & 2: Load data and handle missing values
    try:
        X, y = load_and_preprocess_data('../dataset.csv')
        print("Data loaded and preprocessed successfully.")
    except FileNotFoundError as e:
        print(e)
        print("Please upload 'dataset.csv' first if running in an environment like Google Colab.")
        exit() # Exit if the file is not found

    # Step 3, 4, 5, 6: Split, Scale, Train, and Evaluate
    model, scaler, X_test, y_test, y_pred = train_and_evaluate_model(X, y)
    print("Model trained and evaluated.")

    # Step 7: Save the trained model and scaler
    model_filename = 'wsi_model.pkl'
    scaler_filename = 'scaler.pkl'
    joblib.dump(model, model_filename)
    joblib.dump(scaler, scaler_filename)
    print(f"Model '{model_filename}' and Scaler '{scaler_filename}' saved successfully.")

    # Step 8: Print sample predictions
    print("\nSample Predictions (first 5 of test data):")
    for i in range(min(5, len(y_test))):
        print(f"Actual: {y_test.iloc[i]:.4f}, Predicted: {y_pred[i]:.4f}")

    print("\nModel pipeline completed. The model and scaler are ready for API integration.")
