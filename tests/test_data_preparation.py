import os
import sys
import pytest
import pandas as pd

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from data_preparation import clean_data, save_cleaned_data

@pytest.fixture
def sample_dataframe():
    """Create a sample dataframe for testing."""
    data = {
        'IMEI': ['123', '456', None, '789'],
        'IMSI': ['ABC', 'DEF', 'GHI', None],
        'MSISDN/Number': [None, '555-1234', '555-5678', '555-0000'],
        'Bearer Id': [1, 2, None, 4],
        'Dur. (ms)': [100, 200, None, 400],
        'Total DL (Bytes)': [500, 600, None, 800],
        'Total UL (Bytes)': [150, None, 350, 450]
    }
    return pd.DataFrame(data)

def test_clean_data(sample_dataframe):
    cleaned_df = clean_data(sample_dataframe)
    
    # Check if 'IMEI', 'IMSI', and 'MSISDN/Number' columns are filled correctly
    assert cleaned_df['IMEI'].isnull().sum() == 0
    assert cleaned_df['IMSI'].isnull().sum() == 0
    assert cleaned_df['MSISDN/Number'].isnull().sum() == 0
    
    # Check if columns with more than 50% missing values are dropped
    assert 'Bearer Id' not in cleaned_df.columns
    assert 'Dur. (ms)' in cleaned_df.columns

def test_save_cleaned_data(sample_dataframe):
    output_path = 'test_cleaned_data.csv'
    clean_df = clean_data(sample_dataframe)
    save_cleaned_data(clean_df, output_path)
    
    # Check if the file is created
    assert os.path.exists(output_path)
    
    # Cleanup
    os.remove(output_path)
