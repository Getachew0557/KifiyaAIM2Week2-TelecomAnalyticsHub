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

def describe_variables(df: pd.DataFrame):
    """Describes all relevant variables and associated data types."""
    print("Descriptive Statistics:")
    print(df.describe(include='all'))
    print("\nData Types:")
    print(df.dtypes)

def variable_transformation(df: pd.DataFrame):
    """Performs variable transformation and segmentation."""
    # Segment users into deciles based on total session duration
    user_data = aggregate_user_data(df)
    user_data['decile_class'] = pd.qcut(user_data['total_session_duration'], 10, labels=False)
    
    # Compute total data (DL+UL) per decile class
    decile_data = user_data.groupby('decile_class').agg({
        'total_download_data': 'sum',
        'total_upload_data': 'sum'
    })
    
    print("\nDecile Data:")
    print(decile_data)

def analyze_basic_metrics(df: pd.DataFrame):
    """Analyzes basic metrics of the dataset."""
    print("\nBasic Metrics:")
    print(df[['Total DL (Bytes)', 'Total UL (Bytes)']].describe())

def univariate_analysis(df: pd.DataFrame):
    """Conducts univariate analysis - both graphical and non-graphical."""
    print("\nNon-Graphical Univariate Analysis:")
    print(df[['Total DL (Bytes)', 'Total UL (Bytes)']].agg(['mean', 'median', 'std', 'var']))
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(df['Total DL (Bytes)'], kde=True)
    plt.title('Histogram of Total Download Data')

    plt.subplot(1, 2, 2)
    sns.histplot(df['Total UL (Bytes)'], kde=True)
    plt.title('Histogram of Total Upload Data')

    plt.tight_layout()
    plt.show()

def bivariate_analysis(df: pd.DataFrame):
    """Conducts bivariate analysis - relationship between applications and total DL+UL data."""
    app_cols = ['Social Media DL (Bytes)', 'Google DL (Bytes)', 'Email DL (Bytes)',
                'Youtube DL (Bytes)', 'Netflix DL (Bytes)', 'Gaming DL (Bytes)',
                'Other DL (Bytes)']
    df['Total Data DL'] = df[app_cols].sum(axis=1)

    plt.figure(figsize=(14, 8))
    for col in app_cols:
        sns.scatterplot(x=df[col], y=df['Total Data DL'], label=col)
    plt.title('Scatter plot of Application DL Data vs Total Data DL')
    plt.xlabel('Application DL (Bytes)')
    plt.ylabel('Total Data DL (Bytes)')
    plt.legend()
    plt.show()