import os
import sys
import pytest
import pandas as pd
import matplotlib.pyplot as plt
from exploratory_analysis import aggregate_user_data, correlation_analysis, pca_analysis, describe_variables, variable_transformation, analyze_basic_metrics, univariate_analysis, bivariate_analysis

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

@pytest.fixture
def sample_dataframe():
    """Create a sample dataframe for testing."""
    data = {
        'MSISDN/Number': ['555-1234', '555-5678', '555-0000'],
        'Bearer Id': [1, 2, 3],
        'Dur. (ms)': [100, 200, 300],
        'Total DL (Bytes)': [500, 600, 700],
        'Total UL (Bytes)': [150, 250, 350],
        'Social Media DL (Bytes)': [50, 60, 70],
        'Google DL (Bytes)': [10, 20, 30],
        'Email DL (Bytes)': [5, 10, 15],
        'Youtube DL (Bytes)': [20, 30, 40],
        'Netflix DL (Bytes)': [15, 25, 35],
        'Gaming DL (Bytes)': [25, 35, 45],
        'Other DL (Bytes)': [10, 20, 30]
    }
    return pd.DataFrame(data)

def test_aggregate_user_data(sample_dataframe):
    aggregated_df = aggregate_user_data(sample_dataframe)
    
    assert 'number_of_xDR_sessions' in aggregated_df.columns
    assert 'total_session_duration' in aggregated_df.columns
    assert 'total_download_data' in aggregated_df.columns
    assert aggregated_df.shape[0] == 3  # Ensure all rows are included

def test_correlation_analysis(sample_dataframe):
    try:
        correlation_analysis(sample_dataframe)
    except Exception as e:
        pytest.fail(f"Correlation analysis failed: {e}")

def test_pca_analysis(sample_dataframe):
    try:
        explained_variance = pca_analysis(sample_dataframe)
        assert len(explained_variance) == 2
    except Exception as e:
        pytest.fail(f"PCA analysis failed: {e}")

def test_describe_variables(sample_dataframe):
    try:
        describe_variables(sample_dataframe)
    except Exception as e:
        pytest.fail(f"Describe variables failed: {e}")

def test_variable_transformation(sample_dataframe):
    try:
        variable_transformation(sample_dataframe)
    except Exception as e:
        pytest.fail(f"Variable transformation failed: {e}")

def test_analyze_basic_metrics(sample_dataframe):
    try:
        analyze_basic_metrics(sample_dataframe)
    except Exception as e:
        pytest.fail(f"Analyze basic metrics failed: {e}")

def test_univariate_analysis(sample_dataframe):
    try:
        univariate_analysis(sample_dataframe)
    except Exception as e:
        pytest.fail(f"Univariate analysis failed: {e}")

def test_bivariate_analysis(sample_dataframe):
    try:
        bivariate_analysis(sample_dataframe)
    except Exception as e:
        pytest.fail(f"Bivariate analysis failed: {e}")
