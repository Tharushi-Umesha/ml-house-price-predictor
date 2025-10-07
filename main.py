from src.data_preprocessing import load_and_preprocess_data
from src.model_training import train_and_evaluate

def main():
    print("🏠 Starting House Price Prediction Project...")
    filepath = "data/train.csv"
    
    X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data(filepath)
    train_and_evaluate(preprocessor, X_train, X_test, y_train, y_test)
    print("\n🎉 Training complete!")

if __name__ == "__main__":
    main()
