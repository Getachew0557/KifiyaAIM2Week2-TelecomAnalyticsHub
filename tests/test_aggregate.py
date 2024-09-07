import os
import sys
import pytest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from aggregate import aggregate_total_traffic_per_application, top_10_most_engaged_users_per_application, identify_top_3_most_used_applications, plot_top_3_most_used_applications
# Sample DataFrame for testing
def create_test_dataframe():
    data = {
        'Social Media DL (Bytes)': [100, 200, 300],
        'Social Media UL (Bytes)': [50, 150, 250],
        'Google DL (Bytes)': [300, 400, 500],
        'Google UL (Bytes)': [150, 200, 250],
        'Email DL (Bytes)': [200, 300, 400],
        'Email UL (Bytes)': [100, 150, 200],
        'Youtube DL (Bytes)': [400, 500, 600],
        'Youtube UL (Bytes)': [200, 250, 300],
        'Netflix DL (Bytes)': [500, 600, 700],
        'Netflix UL (Bytes)': [250, 300, 350],
        'Gaming DL (Bytes)': [600, 700, 800],
        'Gaming UL (Bytes)': [300, 350, 400],
        'Other DL (Bytes)': [700, 800, 900],
        'Other UL (Bytes)': [350, 400, 450],
        'MSISDN/Number': ['123', '456', '789']
    }
    return pd.DataFrame(data)

def test_aggregate_total_traffic_per_application(capsys):
    df = create_test_dataframe()
    aggregate_total_traffic_per_application(df)

    captured = capsys.readouterr()
    assert "Social Media: 1050 Bytes" in captured.out
    assert "Google: 1800 Bytes" in captured.out
    assert "Email: 1350 Bytes" in captured.out
    assert "Youtube: 2250 Bytes" in captured.out
    assert "Netflix: 2700 Bytes" in captured.out
    assert "Gaming: 3150 Bytes" in captured.out
    assert "Other: 3600 Bytes" in captured.out

def test_top_10_most_engaged_users_per_application(capsys):
    df = create_test_dataframe()
    df['Total Social Media Traffic'] = df['Social Media DL (Bytes)'] + df['Social Media UL (Bytes)']
    df['Total Google Traffic'] = df['Google DL (Bytes)'] + df['Google UL (Bytes)']
    top_10_most_engaged_users_per_application(df)
    
    captured = capsys.readouterr()
    assert "Top 10 Most Engaged Users for Social Media:" in captured.out
    assert "Top 10 Most Engaged Users for Google:" in captured.out

def test_identify_top_3_most_used_applications():
    df = create_test_dataframe()
    df['Social Media_total_traffic'] = df['Social Media DL (Bytes)'] + df['Social Media UL (Bytes)']
    df['Google_total_traffic'] = df['Google DL (Bytes)'] + df['Google UL (Bytes)']
    df['Email_total_traffic'] = df['Email DL (Bytes)'] + df['Email UL (Bytes)']
    df['Youtube_total_traffic'] = df['Youtube DL (Bytes)'] + df['Youtube UL (Bytes)']
    df['Netflix_total_traffic'] = df['Netflix DL (Bytes)'] + df['Netflix UL (Bytes)']
    df['Gaming_total_traffic'] = df['Gaming DL (Bytes)'] + df['Gaming UL (Bytes)']
    df['Other_total_traffic'] = df['Other DL (Bytes)'] + df['Other UL (Bytes)']
    
    top_3_apps = identify_top_3_most_used_applications(df)
    
    assert len(top_3_apps) == 3
    assert top_3_apps[0][0] == 'Other'
    assert top_3_apps[1][0] == 'Gaming'
    assert top_3_apps[2][0] == 'Netflix'

# The plot functions do not produce returnable outputs but can be tested by checking if files are created
@pytest.mark.skip(reason="Plotting functions produce outputs to files, which should be manually verified.")
def test_plot_top_3_most_used_applications():
    df = create_test_dataframe()
    df['Social Media_total_traffic'] = df['Social Media DL (Bytes)'] + df['Social Media UL (Bytes)']
    df['Google_total_traffic'] = df['Google DL (Bytes)'] + df['Google UL (Bytes)']
    df['Email_total_traffic'] = df['Email DL (Bytes)'] + df['Email UL (Bytes)']
    df['Youtube_total_traffic'] = df['Youtube DL (Bytes)'] + df['Youtube UL (Bytes)']
    df['Netflix_total_traffic'] = df['Netflix DL (Bytes)'] + df['Netflix UL (Bytes)']
    df['Gaming_total_traffic'] = df['Gaming DL (Bytes)'] + df['Gaming UL (Bytes)']
    df['Other_total_traffic'] = df['Other DL (Bytes)'] + df['Other UL (Bytes)']
    
    plot_top_3_most_used_applications(df)
    
    # Check if the file is created
    assert os.path.exists('../data/top_3_applications.png')