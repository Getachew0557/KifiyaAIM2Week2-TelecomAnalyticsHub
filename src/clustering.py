from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pandas as pd
from typing import Tuple

from sklearn.metrics import euclidean_distances

def perform_clustering(df: pd.DataFrame):
    # Aggregating metrics for clustering
    metrics = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',
        'Dur. (ms)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum'
    }).rename(columns={
        'Bearer Id': 'session_frequency',
        'Dur. (ms)': 'session_duration',
        'Total DL (Bytes)': 'total_dl',
        'Total UL (Bytes)': 'total_ul'
    })

    # Normalize Metrics
    scaler = StandardScaler()
    metrics_scaled = scaler.fit_transform(metrics)

    # K-means Clustering (k=3)
    kmeans = KMeans(n_clusters=3, random_state=0)
    metrics['cluster'] = kmeans.fit_predict(metrics_scaled)

    # Compute and Report Cluster Metrics
    cluster_summary = metrics.groupby('cluster').agg({
        'session_frequency': ['min', 'max', 'mean', 'sum'],
        'session_duration': ['min', 'max', 'mean', 'sum'],
        'total_dl': ['min', 'max', 'mean', 'sum'],
        'total_ul': ['min', 'max', 'mean', 'sum']
    })
    print("Cluster Summary:")
    print(cluster_summary)

def plot_elbow_method(df: pd.DataFrame):
    metrics = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',
        'Dur. (ms)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum'
    }).rename(columns={
        'Bearer Id': 'session_frequency',
        'Dur. (ms)': 'session_duration',
        'Total DL (Bytes)': 'total_dl',
        'Total UL (Bytes)': 'total_ul'
    })

    # Normalize Metrics
    scaler = StandardScaler()
    metrics_scaled = scaler.fit_transform(metrics)

    # Optimal Number of Clusters using Elbow Method
    inertia = []
    num_clusters = min(10, len(metrics))  # Adjust k to be less than or equal to the number of samples
    for k in range(1, num_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=0)
        kmeans.fit(metrics_scaled)
        inertia.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, num_clusters + 1), inertia, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.xticks(range(1, num_clusters + 1))
    plt.grid(True)
    plt.savefig('../data/elbow_method.png')
    plt.show()
