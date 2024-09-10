import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

#from load_data import load_data
from load_data import load_data_from_postgres
from data_preparation import clean_data, save_cleaned_data
from exploratory_analysis import (aggregate_user_data, correlation_analysis, pca_analysis,
                                   describe_variables, variable_transformation, analyze_basic_metrics,
                                   univariate_analysis, bivariate_analysis)
from clustering import perform_clustering, plot_elbow_method
from aggregate import (aggregate_total_traffic_per_application, top_10_most_engaged_users_per_application,
                       identify_top_3_most_used_applications, plot_top_3_most_used_applications)
from data_analysis import perform_data_analysis

def main():
    #data_path = '../data/cleaned_week2_challenge_data_source.csv'
    cleaned_data_path = '../data/cleaned_telecom_data.csv'
    # SQL query for loading data
    query = "SELECT * FROM xdr_data;"

    # Load the data from PostgreSQL
    print("Loading data...")
    #df = load_data(data_path)
    df = load_data_from_postgres(query)
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


    # Perform Clustering
    print("Performing clustering...")
    perform_clustering(cleaned_df)
    plot_elbow_method(cleaned_df)

    # Aggregate Total Traffic per Application
    print("Aggregating total traffic per application...")
    aggregate_total_traffic_per_application(cleaned_df)

    # Top 10 Most Engaged Users per Application
    print("Finding top 10 most engaged users per application...")
    top_10_most_engaged_users_per_application(cleaned_df)

    # Identify Top 3 Most Used Applications
    print("Identifying top 3 most used applications...")
    identify_top_3_most_used_applications(cleaned_df)

    # Plot Top 3 Most Used Applications
    print("Plotting top 3 most used applications...")
    plot_top_3_most_used_applications(cleaned_df)

    # Call the data analysis function at the end of the pipeline
    print("Performing data analysis...")
    analysis_results = perform_data_analysis(cleaned_df)
    print("Data Analysis Results:\n", analysis_results.head())

if __name__ == "__main__":
    main()
