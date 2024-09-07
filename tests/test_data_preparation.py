import pandas as pd
from src.data_preparation import clean_data

def test_clean_data():
    # Create sample dataframe with missing values
    data = {
        'Dur. (ms)': [1000, 2000, None],
        'Total DL (Bytes)': [100, None, 300],
        'Handset Type': ['iPhone', None, 'Samsung'],
        'MSISDN/Number': [12345, None, 67890]
    }
    df = pd.DataFrame(data)
    
    # Clean the data
    cleaned_df = clean_data(df)
    
    # Test if missing values are filled
    assert cleaned_df['Dur. (ms)'].isnull().sum() == 0
    assert cleaned_df['Total DL (Bytes)'].isnull().sum() == 0
    assert cleaned_df['Handset Type'].isnull().sum() == 0
    assert cleaned_df['MSISDN/Number'].isnull().sum() == 0
