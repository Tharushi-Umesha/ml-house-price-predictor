import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
model = load("model/house_price_model.joblib")

st.title("🏠 House Price Prediction App")
st.write("Enter house features to predict its sale price:")

# User inputs for main features
LotArea = st.number_input("Lot Area", min_value=100, max_value=20000, value=8450)
OverallQual = st.number_input("Overall Quality (1-10)", min_value=1, max_value=10, value=7)
OverallCond = st.number_input("Overall Condition (1-10)", min_value=1, max_value=10, value=5)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2003)
ExterQual = st.selectbox("Exterior Quality", ["Ex", "Gd", "TA", "Fa", "Po"])

# Map categorical input if needed
exter_map = {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1}
ExterQual_mapped = exter_map[ExterQual]

# Create empty DataFrame with all features the model expects
all_columns = model.named_steps['preprocessor'].feature_names_in_
input_df = pd.DataFrame(columns=all_columns)
input_df.loc[0, "LotArea"] = LotArea
input_df.loc[0, "OverallQual"] = OverallQual
input_df.loc[0, "OverallCond"] = OverallCond
input_df.loc[0, "YearBuilt"] = YearBuilt
input_df.loc[0, "ExterQual"] = ExterQual_mapped

# Fill numeric columns with 0
numeric_cols = model.named_steps['preprocessor'].transformers_[0][2]  # numeric feature names
for col in numeric_cols:
    if pd.isna(input_df.loc[0, col]):
        input_df.loc[0, col] = 0

# Fill categorical columns with most frequent category from training
cat_cols = model.named_steps['preprocessor'].transformers_[1][2]  # categorical feature names
# Use "missing" as placeholder for simplicity
for col in cat_cols:
    if pd.isna(input_df.loc[0, col]):
        input_df.loc[0, col] = "missing"

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Sale Price: ${prediction:,.2f}")
