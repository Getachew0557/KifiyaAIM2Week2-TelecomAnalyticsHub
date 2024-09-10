import streamlit as st

def show_task_2_description():
    # Introduction
    st.header('Introduction')
    st.write("""
    As telecom brands are the data providers of all online activities, meeting user requirements and creating an engaging user experience is crucial. Improving Quality of Service (QoS) to leverage mobile platforms and attract more users is beneficial, but business success is determined by user engagement and activity on available apps.

    Tracking user activities through database sessions is a good starting point to assess user engagement for overall applications and individual apps. Determining the level of engagement can help technical teams concentrate network resources based on engagement scores.
    """)

    # Objective
    st.header('Objective')
    st.write("""
    The current dataset aims to track user engagement using the following metrics:
    - **Sessions Frequency**
    - **Duration of the Session**
    - **Total Session Traffic (Download and Upload in bytes)**

    The analysis involves aggregating these metrics, normalizing them, and applying clustering algorithms to classify users based on engagement levels.
    """)

    # Completed Tasks

    st.subheader('Task 2.1: Perform User Engagement Analysis')

    st.write("""
    **1. Aggregate Metrics:**
    - Aggregated the metrics per customer ID (MSISDN) and reported the top 10 customers for each engagement metric.

    **2. Normalization and Clustering:**
    - Normalized each engagement metric and performed k-means clustering (k=3) to classify customers into three engagement groups.
    - Computed minimum, maximum, average, and total non-normalized metrics for each cluster.
    - Results were interpreted visually with accompanying explanations.

    **3. Top Engaged Users Per Application:**
    - Aggregated total traffic per application and derived the top 10 most engaged users for each application.

    **4. Plot Most Used Applications:**
    - Plotted the top 3 most used applications using appropriate charts.

    **5. K-Means Clustering and Optimization:**
    - Applied k-means clustering algorithm to group users based on engagement metrics.
    - Determined the optimized value of k using the elbow method.
    - Interpreted the findings from clustering results.
    """)

    # Conclusion
    st.header('Conclusion')
    st.write("""
    The User Engagement Analysis provided insights into user engagement levels across different applications. The analysis included metric aggregation, normalization, clustering, and visualization of engagement patterns. Key findings from the k-means clustering and application usage were reported to guide business decisions.

    For detailed results and interactive visualizations, please refer to the Streamlit app where the data and charts are displayed interactively.
    """)