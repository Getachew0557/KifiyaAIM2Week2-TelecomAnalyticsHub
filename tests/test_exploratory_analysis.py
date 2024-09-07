import pandas as pd
from src.exploratory_analysis import aggregate_user_data

def test_aggregate_user_data():
    # Create sample dataframe for aggregation
    data = {
        'MSISDN/Number': [12345, 12345, 67890],
        'Bearer Id': [1, 1, 1],
        'Dur. (ms)': [1000, 2000, 1500],
        'Total DL (Bytes)': [100, 200, 150],
        'Total UL (Bytes)': [50, 75, 100]
    }
    df = pd.DataFrame(data)
    
    # Perform aggregation
    user_data = aggregate_user_data(df)
    
    # Test if aggregation is correct
    assert user_data.loc[12345, 'total_session_duration'] == 3000
    assert user_data.loc[67890, 'total_download_data'] == 150
