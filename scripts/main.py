import os
import pandas as pd
from src.load_data import load_data
from src.data_preparation import clean_data, save_cleaned_data
from src.exploratory_analysis import aggregate_user_data, correlation_analysis, pca_analysis

df = '../data/Week2_challenge_data_source.xlsx'
data = pd.read_excel(df)
# Save the loaded data to CSV for further access
data.to_csv('../data/cleaned_week2_challenge_data_source.csv', index=False)

# Reload the cleaned CSV data
data_path = pd.read_csv('../data/cleaned_week2_challenge_data_source.csv')
cleaned_data_path = '../data/cleaned_telecom_data.csv'


def main():
    # 1. Load the data
    df = load_data(data_path)
    if df is None:
        return
    
    # 2. Clean the data
    cleaned_df = clean_data(df)
    save_cleaned_data(cleaned_df, cleaned_data_path)

    # 3. Perform EDA - User Data Aggregation
    user_data = aggregate_user_data(cleaned_df)
    print("Aggregated User Data:")
    print(user_data.head())

    # 4. Perform Correlation Analysis
    correlation_analysis(cleaned_df)

    # 5. Perform PCA
    explained_variance = pca_analysis(cleaned_df)
    print(f"Explained Variance by PCA Components: {explained_variance}")

if __name__ == "__main__":
    main()
