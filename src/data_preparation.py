import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the telecom data by handling missing values and dropping unnecessary columns."""
    
    # # Fill missing values for numeric columns with median
    # numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    # df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())

    # # Fill missing values for categorical columns with mode
    # categorical_cols = df.select_dtypes(include=['object']).columns
    # for col in categorical_cols:
    #     df[col] = df[col].fillna(df[col].mode()[0])

    # # Handle missing values in unique identifiers (e.g., IMEI, IMSI)
    # unique_identifiers = ['IMEI', 'IMSI', 'MSISDN/Number']
    # for col in unique_identifiers:
    #     df[col] = df[col].fillna('Unknown')

    # # Drop specific columns
    # #cols_to_drop = ['Bearer Id']
    # # Drop columns with more than 50% missing values
    # threshold = 0.5
    # cols_to_drop = [col for col in df.columns if (df[col].isnull().mean() > threshold)]
    # df = df.drop(columns=cols_to_drop)

    # Separate numeric and non-numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    non_numeric_cols = df.select_dtypes(include=['object']).columns

    # Impute missing numeric values with the mean
    imputer = SimpleImputer(strategy='mean')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

    # For non-numeric columns, you can fill with the most frequent value (mode) or a custom value
    df[non_numeric_cols] = df[non_numeric_cols].fillna(df[non_numeric_cols].mode().iloc[0])

    # Verify no more missing values
    print(df.isnull().sum())
    
    return df

def save_cleaned_data(df: pd.DataFrame, output_path: str):
    """Saves the cleaned dataframe to a CSV file."""
    df.to_csv(output_path, index=False)
def normalize_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize the engagement metrics using StandardScaler."""
    scaler = StandardScaler()
    metrics = df[['session_frequency', 'session_duration', 'total_dl', 'total_ul']]
    metrics_scaled = scaler.fit_transform(metrics)
    return pd.DataFrame(metrics_scaled, columns=metrics.columns)

def aggregate_user_traffic(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total traffic per application."""
    applications = ['Social Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']
    for app in applications:
        dl_col = f'{app} DL (Bytes)'
        ul_col = f'{app} UL (Bytes)'
        traffic_col = f'{app}_total_traffic'
        df[traffic_col] = df[dl_col] + df[ul_col]
    return df