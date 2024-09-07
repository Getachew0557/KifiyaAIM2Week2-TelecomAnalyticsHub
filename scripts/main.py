import os
import sys
import pandas as pd

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from load_data import load_data
from data_preparation import clean_data, save_cleaned_data
from exploratory_analysis import (aggregate_user_data, correlation_analysis, pca_analysis,
                                   describe_variables, variable_transformation, analyze_basic_metrics,
                                   univariate_analysis, bivariate_analysis)

def main():
    # File paths
    data_path = '../data/cleaned_week2_challenge_data_source.csv'
    cleaned_data_path = '../data/cleaned_telecom_data.csv'

    # Load the data
    print("Loading data...")
    df = load_data(data_path)
    if df is None:
        print("Data loading failed.")
        return

    # Clean the data
    print("Cleaning data...")
    cleaned_df = clean_data(df)
    save_cleaned_data(cleaned_df, cleaned_data_path)

    # Perform EDA - User Data Aggregation
    print("Aggregating user data...")
    user_data = aggregate_user_data(cleaned_df)
    print("Aggregated User Data:")
    print(user_data.head())

    # Perform Descriptive Analysis
    print("Describing variables...")
    describe_variables(cleaned_df)

        # Perform Variable Transformation
    print("Performing variable transformation...")
    variable_transformation(cleaned_df)

    # Perform Basic Metrics Analysis
    print("Analyzing basic metrics...")
    analyze_basic_metrics(cleaned_df)

    # Perform Univariate Analysis
    print("Performing univariate analysis...")
    univariate_analysis(cleaned_df)

    # Perform Bivariate Analysis
    print("Performing bivariate analysis...")
    bivariate_analysis(cleaned_df)

    # Perform Correlation Analysis
    print("Performing correlation analysis...")
    correlation_analysis(cleaned_df)

    # Perform PCA
    print("Performing PCA...")
    explained_variance = pca_analysis(cleaned_df)
    print(f"Explained Variance by PCA Components: {explained_variance}")

if __name__ == "__main__":
    main()
