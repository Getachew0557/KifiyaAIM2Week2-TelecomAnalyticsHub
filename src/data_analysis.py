import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics.pairwise import euclidean_distances

def perform_data_analysis(df):
    # Aggregate per customer
    agg_df = df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'TCP UL Retrans. Vol (Bytes)': 'mean',
        'Avg RTT DL (ms)': 'mean',
        'Avg RTT UL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Avg Bearer TP UL (kbps)': 'mean',
        'IMEI': 'first',  # Assuming one device per user
        'IMSI': 'first'   # Assuming one IMSI per user
    }).reset_index()

    print(agg_df.head())

    # Top 10 TCP, RTT, and Throughput Values
    top_10_tcp = df['TCP DL Retrans. Vol (Bytes)'].nlargest(10)
    bottom_10_tcp = df['TCP DL Retrans. Vol (Bytes)'].nsmallest(10)
    top_10_rtt = df['Avg RTT DL (ms)'].nlargest(10)
    bottom_10_rtt = df['Avg RTT DL (ms)'].nsmallest(10)
    top_10_throughput = df['Avg Bearer TP DL (kbps)'].nlargest(10)
    bottom_10_throughput = df['Avg Bearer TP DL (kbps)'].nsmallest(10)

    print("Top 10 TCP values:\n", top_10_tcp)
    print("Bottom 10 TCP values:\n", bottom_10_tcp)
    print("Top 10 RTT values:\n", top_10_rtt)
    print("Bottom 10 RTT values:\n", bottom_10_rtt)
    print("Top 10 Throughput values:\n", top_10_throughput)
    print("Bottom 10 Throughput values:\n", bottom_10_throughput)

    # Plot Throughput Distribution
    throughput_distribution = df.groupby('IMEI')['Avg Bearer TP DL (kbps)'].mean()
    tcp_retransmission_distribution = df.groupby('IMEI')['TCP DL Retrans. Vol (Bytes)'].mean()

    print(throughput_distribution.describe())
    print(tcp_retransmission_distribution.describe())

    plt.figure(figsize=(12, 6))
    plt.hist(throughput_distribution, bins=30, edgecolor='k', alpha=0.7)
    plt.title('Distribution of Average Throughput per Handset Type')
    plt.xlabel('Average Throughput (kbps)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # K-means clustering
    features = agg_df[['TCP DL Retrans. Vol (Bytes)', 'Avg RTT DL (ms)', 'Avg Bearer TP DL (kbps)']]
    kmeans = KMeans(n_clusters=3, random_state=0).fit(features)
    agg_df['Experience Cluster'] = kmeans.labels_

    print("Cluster Descriptions:\n", agg_df.groupby('Experience Cluster').mean())

    # Cluster Visualization
    plt.figure(figsize=(10, 7))
    plt.scatter(agg_df['TCP DL Retrans. Vol (Bytes)'], agg_df['Avg RTT DL (ms)'], 
                c=agg_df['Experience Cluster'], cmap='viridis', alpha=0.5)
    plt.title('Customer Clustering Based on TCP Retransmission and RTT')
    plt.xlabel('Average TCP Retransmission (Bytes)')
    plt.ylabel('Average RTT (ms)')
    plt.colorbar(label='Cluster')
    plt.grid(True)
    plt.show()

    # Engagement and Experience Scores
    worst_experience_cluster_center = kmeans.cluster_centers_[2]
    agg_df['Engagement Score'] = euclidean_distances(
        agg_df[['TCP DL Retrans. Vol (Bytes)', 'Avg RTT DL (ms)', 'Avg Bearer TP DL (kbps)']],
        [worst_experience_cluster_center]
    ).flatten()

    agg_df['Experience Score'] = agg_df['Engagement Score']
    agg_df['Satisfaction Score'] = agg_df[['Engagement Score', 'Experience Score']].mean(axis=1)

    print("Satisfaction Score:\n", agg_df[['MSISDN/Number', 'Satisfaction Score']].head(10))

    # Regression Analysis
    X = agg_df[['Engagement Score', 'Experience Score']]
    y = agg_df['Satisfaction Score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regression_model = LinearRegression()
    regression_model.fit(X_train, y_train)
    y_pred = regression_model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Model MSE: {mse}")
    print(f"Model R² Score: {r2}")

    # Additional Clustering on Engagement & Experience Scores
    kmeans_2 = KMeans(n_clusters=2, random_state=42)
    agg_df['Engagement_Experience Cluster'] = kmeans_2.fit_predict(agg_df[['Engagement Score', 'Experience Score']])

    print("Cluster centers:\n", kmeans_2.cluster_centers_)
    print("Average Satisfaction & Experience Scores per Cluster:\n", agg_df.groupby('Engagement_Experience Cluster')[['Satisfaction Score', 'Experience Score']].mean())

    return agg_df
