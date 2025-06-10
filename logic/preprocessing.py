import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Generalized IQR-based outlier removal
def remove_outliers_all_numeric(df, method="remove", iqr_multiplier=1.5):
    df_out = df.copy()
    numeric_cols = df_out.select_dtypes(include=['number']).columns
    removed_log = {}

    for col in numeric_cols:
        Q1 = df_out[col].quantile(0.25)
        Q3 = df_out[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - iqr_multiplier * IQR
        upper_bound = Q3 + iqr_multiplier * IQR

        if method == "remove":
            original_len = len(df_out)
            df_out = df_out[(df_out[col] >= lower_bound) & (df_out[col] <= upper_bound)]
            removed = original_len - len(df_out)
            if removed > 0:
                removed_log[col] = removed
        elif method == "cap":
            df_out[col] = df_out[col].clip(lower=lower_bound, upper=upper_bound)
        else:
            raise ValueError("Method must be 'remove' or 'cap'")
    
    return df_out, removed_log

# Preprocessing pipeline
def preprocess_dataset(df, target_column=None, drop_null_cols=False, impute=False, encode=False,
                       scale=False, scaler_type='standard', handle_outliers=False,
                       outlier_method="remove", outlier_iqr_multiplier=1.5):
    df = df.copy()
    log = {"dropped_columns": [], "imputed_numeric": [], "imputed_categorical": [],
           "encoded": [], "scaled": [], "outliers_removed": []}

    # Ensure numeric types
    df = df.apply(pd.to_numeric, errors='ignore')

    # Remove outliers from all numeric columns
    if handle_outliers:
        original_len = len(df)
        df, removed_log = remove_outliers_all_numeric(df, method=outlier_method, iqr_multiplier=outlier_iqr_multiplier)
        for col, count in removed_log.items():
            st.write(f"Removed {count} outlier rows from '{col}' column")
        log["outliers_removed"].append(removed_log)

    # Separate target column if provided
    if target_column and target_column in df.columns:
        target_series = df[target_column]
        if target_series.isnull().sum() > 0 and impute:
            imputer_target = SimpleImputer(strategy="mean")
            target_series = imputer_target.fit_transform(target_series.values.reshape(-1, 1))
        df = df.drop(columns=[target_column])
    else:
        target_series = None

    # Convert object cols to category
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("category")

    # Drop columns with >50% missing values
    if drop_null_cols:
        threshold = int(0.5 * len(df))
        dropped_cols = df.columns[df.isnull().sum() >= threshold].tolist()
        df.drop(columns=dropped_cols, inplace=True)
        log["dropped_columns"] = dropped_cols

    # Convert bools to int
    for col in df.select_dtypes(include="bool").columns:
        df[col] = df[col].astype("int64")

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    category_cols = df.select_dtypes(include=["category"]).columns.tolist()

    # Impute missing values
    if impute:
        if numeric_cols:
            imputer_num = SimpleImputer(strategy="mean")
            df[numeric_cols] = imputer_num.fit_transform(df[numeric_cols])
            log["imputed_numeric"] = numeric_cols
        if category_cols:
            imputer_cat = SimpleImputer(strategy="most_frequent")
            df[category_cols] = imputer_cat.fit_transform(df[category_cols])
            log["imputed_categorical"] = category_cols

    # Encode categorical variables
    if encode and category_cols:
        df = pd.get_dummies(df, columns=category_cols, drop_first=True)
        log["encoded"] = category_cols

    # Scale numeric columns
    if scale and numeric_cols:
        scaler = MinMaxScaler() if scaler_type == 'minmax' else StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        log["scaled"] = numeric_cols

    # Reattach target column
    if target_series is not None:
        if target_series.dtype.name == 'category' or target_series.dtype == object:
            le = LabelEncoder()
            target_series = le.fit_transform(target_series)
        df[target_column] = target_series

    return df, log["dropped_columns"], log
