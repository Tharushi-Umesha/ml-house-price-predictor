# predict.py
import pandas as pd
from joblib import load

def predict_new_data(model_path, data_path):
    """Load model and make predictions on new data."""
    # Load the trained model
    model = load(model_path)
    print("💾 Model loaded successfully.")
    
    # Load new data
    new_data = pd.read_csv(data_path)
    print(f"📊 Loaded {len(new_data)} rows of new data.")

    # Make predictions
    predictions = model.predict(new_data)
    
    # Add predictions to the dataframe
    new_data['Predicted_SalePrice'] = predictions
    
    # Save predictions to CSV
    output_file = "predictions.csv"
    new_data.to_csv(output_file, index=False)
    print(f"✅ Predictions saved to '{output_file}'.")

if __name__ == "__main__":
    model_path = "model/house_price_model.joblib"
    data_path = "data/new_houses.csv"  # <-- replace with your new data file
    
    predict_new_data(model_path, data_path)
