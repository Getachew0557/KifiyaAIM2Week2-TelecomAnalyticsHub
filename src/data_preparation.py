import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the telecom data by handling missing values and dropping unnecessary columns."""
    
    # Fill missing values for numeric columns with median
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())

    # Fill missing values for categorical columns with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Handle missing values in unique identifiers (e.g., IMEI, IMSI)
    unique_identifiers = ['IMEI', 'IMSI', 'MSISDN/Number']
    for col in unique_identifiers:
        df[col] = df[col].fillna('Unknown')

    # Drop columns with more than 50% missing values
    threshold = 0.5
    cols_to_drop = [col for col in df.columns if (df[col].isnull().mean() > threshold)]
    df = df.drop(columns=cols_to_drop)
    
    return df

def save_cleaned_data(df: pd.DataFrame, output_path: str):
    """Saves the cleaned dataframe to a CSV file."""
    df.to_csv(output_path, index=False)
