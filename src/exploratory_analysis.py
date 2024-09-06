import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def aggregate_user_data(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregates user data for the telecom dataset."""
    user_data = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',   # Number of xDR sessions
        'Dur. (ms)': 'sum',     # Total session duration
        'Total DL (Bytes)': 'sum',   # Total download data
        'Total UL (Bytes)': 'sum',   # Total upload data
        'Social Media DL (Bytes)': 'sum',
        'Google DL (Bytes)': 'sum',
        'Email DL (Bytes)': 'sum',
        'Youtube DL (Bytes)': 'sum',
        'Netflix DL (Bytes)': 'sum',
        'Gaming DL (Bytes)': 'sum',
        'Other DL (Bytes)': 'sum'
    }).rename(columns={
        'Bearer Id': 'number_of_xDR_sessions',
        'Dur. (ms)': 'total_session_duration',
        'Total DL (Bytes)': 'total_download_data',
        'Total UL (Bytes)': 'total_upload_data'
    })

    return user_data

def correlation_analysis(df: pd.DataFrame):
    """Performs correlation analysis on specific columns."""
    app_cols = ['Social Media DL (Bytes)', 'Google DL (Bytes)', 'Email DL (Bytes)',
                'Youtube DL (Bytes)', 'Netflix DL (Bytes)', 'Gaming DL (Bytes)',
                'Other DL (Bytes)']
    correlation_matrix = df[app_cols].corr()
    
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Application Data')
    plt.show()

def pca_analysis(df: pd.DataFrame):
    """Performs Principal Component Analysis (PCA) for dimensionality reduction."""
    pca = PCA(n_components=2)
    app_cols = ['Social Media DL (Bytes)', 'Google DL (Bytes)', 'Email DL (Bytes)',
                'Youtube DL (Bytes)', 'Netflix DL (Bytes)', 'Gaming DL (Bytes)',
                'Other DL (Bytes)']
    
    pca_result = pca.fit_transform(df[app_cols].fillna(0))
    explained_variance = pca.explained_variance_ratio_

    plt.scatter(pca_result[:, 0], pca_result[:, 1])
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA of Application Data')
    plt.show()

    return explained_variance
