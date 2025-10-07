# 🏠 House Price Predictor

A machine learning project that predicts house prices using a **Random Forest Regressor**. This project includes comprehensive data preprocessing, model training with evaluation metrics, and an interactive **Streamlit web application** for real-time predictions.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)

---

## 📋 Table of Contents
- [Features](#-features)
- [Demo](#-demo)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Performance](#-model-performance)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **Data Preprocessing**: Automatic handling of missing values and categorical features
- **Machine Learning Model**: Random Forest Regressor for accurate price predictions
- **Comprehensive Evaluation**: Multiple metrics including MAE, RMSE, and R² score
- **Model Persistence**: Save and load trained models using joblib
- **Batch Predictions**: Script for making predictions on new CSV datasets
- **Interactive Web App**: User-friendly Streamlit interface for real-time predictions
- **Modular Codebase**: Clean, organized, and easily extensible architecture

---

## 🎯 Demo

### Streamlit Web Application
The interactive web app allows users to input house features and receive instant price predictions.

![App Screenshot](https://via.placeholder.com/800x400?text=Streamlit+App+Screenshot)

---

## 📁 Project Structure

```
house-price-project/
│
├── app/
│   └── app.py                          # Streamlit web application
│
├── data/
│   ├── train.csv                       # Training dataset
│   └── new_houses.csv                  # Sample data for predictions
│
├── model/
│   └── house_price_model.joblib        # Saved trained model
│
├── src/
│   ├── data_preprocessing.py           # Data cleaning and feature engineering
│   └── model_training.py               # Model training and evaluation
│
├── main.py                             # Main script to train and evaluate model
├── predict.py                          # Script for batch predictions
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tharushi-Umesha/ml-house-price-predictor.git
   cd ml-house-price-predictor
   ```

2. **Create and activate a virtual environment**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### 1️⃣ Train the Model

Train the Random Forest model on your dataset:

```bash
python main.py
```

**What this does:**
- Loads and preprocesses the training data
- Trains a Random Forest Regressor
- Evaluates model performance with multiple metrics
- Saves the trained model to `model/house_price_model.joblib`

### 2️⃣ Make Batch Predictions

Predict prices for multiple houses from a CSV file:

```bash
python predict.py
```

**Requirements:**
- Prepare a CSV file (e.g., `data/new_houses.csv`)
- Ensure it contains the same feature columns as the training data (excluding `SalePrice`)
- Predictions will be saved to `predictions.csv`

### 3️⃣ Launch the Interactive Web App

Run the Streamlit application:

```bash
streamlit run app/app.py
```

**Features:**
- Enter house characteristics through an intuitive form
- Get instant price predictions
- View model confidence metrics
- No coding required!

The app will open automatically in your default browser at `http://localhost:8501`

---

## 📊 Model Performance

The Random Forest model is evaluated using industry-standard metrics:

| Metric | Description | Example Value |
|--------|-------------|---------------|
| **MAE** | Mean Absolute Error - Average prediction error | $17,408 |
| **RMSE** | Root Mean Squared Error - Penalizes large errors | $28,432 |
| **R² Score** | Coefficient of Determination - Model accuracy | 0.895 (89.5%) |

### Sample Output
```
Model Evaluation Results:
==========================
Mean Absolute Error (MAE): $17,408
Root Mean Squared Error (RMSE): $28,432
R² Score: 0.895

Model saved successfully to model/house_price_model.joblib
```

---

## 🛠️ Technologies Used

- **Python 3.8+** - Programming language
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning algorithms and tools
- **joblib** - Model serialization
- **Streamlit** - Web application framework

---

## 📦 Dependencies

All required packages are listed in `requirements.txt`:

```txt
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
joblib>=1.1.0
streamlit>=1.0.0
```

---

## 🎓 Key Concepts

### Random Forest Regressor
An ensemble learning method that constructs multiple decision trees during training and outputs the average prediction, resulting in improved accuracy and reduced overfitting.

### Feature Engineering
The project handles both numerical and categorical features, automatically encoding categorical variables and managing missing values for robust predictions.

### Model Persistence
Trained models are saved using joblib for efficient storage and quick loading, enabling deployment without retraining.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Tharushi Umesha**
- GitHub: [@Tharushi-Umesha](https://github.com/Tharushi-Umesha)

---

## 🌟 Acknowledgments

- Dataset source and inspiration
- scikit-learn documentation
- Streamlit community

---

## 📧 Contact

For questions or suggestions, please open an issue or contact the repository owner.

---

**⭐ If you find this project useful, please consider giving it a star!**
