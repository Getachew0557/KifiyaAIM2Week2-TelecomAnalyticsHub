

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
#from load_data import load_data_from_postgres, load_data_using_sqlalchemy

def show_overview():
    st.header("Situational Overview (Business Need)")
    st.write("""
    As an analyst for a wealthy investor specializing in undervalued assets, your role involves a thorough examination of business data to uncover opportunities that drive profitability. Your previous success with identifying a profitable delivery route for university students, which resulted in a 25% profit increase, demonstrated your ability to leverage data insights effectively.

    Your current task is to evaluate TellCo, a mobile service provider in the Republic of Pefkakia, using a telecommunication dataset to assess its growth potential and determine whether it is a worthwhile investment. The analysis will involve detailed exploration of user data to provide actionable insights that will guide the investment decision.
    """)
    #
    # st.subheader('Sample data from the dataset')
    # Define your SQL query
    #query = "SELECT * FROM xdr_data;"  # Replace with your actual table name

    # Load data from PostgreSQL
    #df = load_data_using_sqlalchemy(query)
    #df = pd.read_csv('../data/data.csv')

    # Display the first few rows of the dataset
    #st.write(df.head())
    

def show_completed_tasks():
    st.header("Completed Tasks")

    st.subheader("Task 1 - User Overview Analysis")
    st.write("""
    **Objective**: Understand user behavior and device preferences.

    - **Activities Completed**:
      - Identified the top 10 handsets used by customers.
      - Determined the top 3 handset manufacturers and the top 5 handsets for each.
      - Aggregated user data on session frequency, duration, and total data usage.
      - Conducted exploratory data analysis, including descriptive statistics, variable transformations, and graphical univariate analysis.
      - Performed bivariate and correlation analysis and dimensionality reduction using principal component analysis.

    **Outcome**: Provided insights into device popularity and user behavior, helping to understand user preferences and potential areas for targeted marketing.
    """)

    st.subheader("Task 2 - User Engagement Analysis")
    st.write("""
    **Objective**: Assess user engagement to optimize resource allocation.

    - **Activities Completed**:
      - Aggregated engagement metrics per customer: session frequency, duration, and total traffic.
      - Normalized metrics and applied k-means clustering to classify users into engagement groups.
      - Analyzed top engaged users and derived engagement clusters.
      - Plotted top used applications and optimized k-value for clustering.

    **Outcome**: Identified high-engagement users and applications, aiding in effective network resource allocation and marketing strategies.
    """)

    st.subheader("Task 3 - Experience Analysis")
    st.write("""
    **Objective**: Evaluate user experience based on network performance and device characteristics.

    - **Activities Completed**:
      - Aggregated data on TCP retransmission, RTT, throughput, and handset type.
      - Computed and listed top, bottom, and frequent values for TCP, RTT, and throughput.
      - Analyzed throughput and TCP retransmission by handset type.
      - Applied k-means clustering to segment users based on experience metrics.

    **Outcome**: Provided a detailed understanding of user experience and device performance, enabling targeted improvements in network quality.
    """)

    st.subheader("Task 4 - Satisfaction Analysis")
    st.write("""
    **Objective**: Measure and predict user satisfaction based on engagement and experience.

    - **Activities Completed**:
      - Assigned engagement and experience scores using Euclidean distance from clustering results.
      - Calculated satisfaction scores as the average of engagement and experience scores.
      - Built a regression model to predict satisfaction scores.
      - Applied k-means clustering to satisfaction and experience scores.
      - Exported the final dataset with scores to a local MySQL database.

    **Outcome**: Developed a comprehensive model to assess and predict user satisfaction, providing valuable insights into customer contentment and areas for improvement.
    """)

    st.subheader("Task 5 - Dashboard Development")
    st.write("""
    **Objective**: Create an interactive dashboard for visualizing data insights.

    - **Activities Completed**:
      - Designed a Streamlit dashboard with separate pages for each analysis task.
      - Incorporated visualizations for user overview, engagement, experience, and satisfaction.
      - Ensured dashboard usability, interactive elements, visual appeal, and deployment success.

    **Outcome**: Delivered an interactive, user-friendly dashboard that provides clear and actionable insights into TellCo's data, supporting informed investment decisions.
    """)

def show_next_steps():
    st.header("Next Steps")
    st.write("""
    - Review the dashboard and written report to finalize recommendations.
    - Discuss potential strategies for leveraging identified opportunities.
    - Consider further analysis or adjustments based on additional data or feedback.
    """)
