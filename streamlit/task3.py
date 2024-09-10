import streamlit as st

def show_task_3_description():
    # Introduction
    st.header('Introduction')
    st.write("""
    The telecommunications industry has undergone significant changes in the past decade, with mobile devices becoming integral to daily life. The success of mobile services heavily relies on understanding consumer needs and perceptions. Tracking and evaluating customer experience is essential for optimizing products and services to meet evolving expectations.

    In this analysis, we focus on network parameters such as TCP retransmission, Round Trip Time (RTT), Throughput, and handset types to conduct a thorough user experience analysis.
    """)

    # Objective
    st.header('Objective')
    st.write("""
    The goal of this analysis is to evaluate user experience based on the following metrics:
    - **Average TCP Retransmission**
    - **Average RTT**
    - **Handset Type**
    - **Average Throughput**

    We will aggregate data, identify key metrics, analyze distributions, and perform clustering to segment users based on their experience.
    """)

    # Completed Tasks

    st.subheader('Task 3.1: Aggregate Information Per Customer')
    st.write("""
    Aggregated the following metrics per customer, treating missing values and outliers by replacing them with the mean or mode of the corresponding variable:
    - **Average TCP Retransmission**
    - **Average RTT**
    - **Handset Type**
    - **Average Throughput**
    """)

    st.subheader('Task 3.2: Top, Bottom, and Most Frequent Values')
    st.write("""
    Computed and listed the top 10, bottom 10, and most frequent values for:
    - **TCP Values**
    - **RTT Values**
    - **Throughput Values**
    """)

    st.subheader('Task 3.3: Distribution and Average Analysis')
    st.write("""
    - **Distribution of Average Throughput Per Handset Type:**
    Analyzed and visualized the distribution of average throughput for different handset types.

    - **Average TCP Retransmission Per Handset Type:**
    Reported and interpreted the average TCP retransmission for each handset type.
    """)

    st.subheader('Task 3.4: K-Means Clustering Analysis')
    st.write("""
    Performed k-means clustering (k=3) using the experience metrics to segment users into different experience groups. Each cluster was described based on the aggregated metrics.
    """)

    # Conclusion
    st.header('Conclusion')
    st.write("""
    The Experience Analytics provided valuable insights into user experiences across different handset types and network parameters. The analysis included metric aggregation, identification of key values, and clustering to segment users based on their experiences.

    For detailed results and interactive visualizations, please refer to the Streamlit app where the data and charts are displayed interactively.
    """)