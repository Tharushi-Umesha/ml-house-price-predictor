import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_and_preprocess_data(filepath):
    """Load data, preprocess it, and return X_train, X_test, y_train, y_test."""
    df = pd.read_csv(filepath)
    
    if 'Id' in df.columns:
        df = df.drop(columns=['Id'])
    
    y = df['SalePrice']
    X = df.drop(columns=['SalePrice'])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    numeric_features = X_train.select_dtypes(include=['int64','float64']).columns.tolist()
    cat_features = X_train.select_dtypes(include=['object']).columns.tolist()
    
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    cat_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))

    ])
    
    preprocessor = ColumnTransformer([
        ('num', numeric_transformer, numeric_features),
        ('cat', cat_transformer, cat_features)
    ])
    
    return X_train, X_test, y_train, y_test, preprocessor
