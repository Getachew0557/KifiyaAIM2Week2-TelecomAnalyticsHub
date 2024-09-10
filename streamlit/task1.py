import streamlit as st


def show_task_1_description():
    # Introduction
    st.header('Introduction')
    st.write("""
    Understanding customer behavior is crucial for businesses aiming to tailor their services and improve efficiency. Exploratory Data Analysis (EDA) serves as a foundational step in the data science process, helping to uncover initial insights and guide further analysis. This report outlines the completed tasks for the User Overview Analysis of a telecom dataset, focusing on user behavior across various applications.
    """)

    # Objective
    st.header('Objective')
    st.write("""
    The primary objective of this analysis is to gain a comprehensive understanding of user behavior based on xDR (data sessions Detail Record) across different applications. This involves exploring user interactions with applications such as Social Media, Google, Email, YouTube, Netflix, Gaming, and others. The analysis aims to identify patterns, anomalies, and key insights to inform marketing strategies and improve service offerings.
    """)

    # Completed Tasks
    st.header('Completed Tasks')

    st.subheader('Task 1.1: Aggregate User Behavior Data')
    st.write("""
    The following aggregations were performed for each user:
    - **Number of xDR Sessions:** Count of sessions per user.
    - **Session Duration:** Total time spent in each session.
    - **Total Download (DL) and Upload (UL) Data:** Cumulative data volume for both download and upload.
    - **Total Data Volume:** Overall data usage (in bytes) for each application.
    """)

    st.subheader('Task 1.2: Exploratory Data Analysis')

    st.write("""
    **1. Variable Description and Data Types:**
    - Detailed descriptions of all relevant variables and their associated data types were provided, highlighting key attributes of the dataset.

    **2. Variable Transformations:**
    - Users were segmented into the top five decile classes based on the total duration of sessions. The total data (DL + UL) was computed for each decile class to understand data consumption patterns.

    **3. Basic Metrics Analysis:**
    - The dataset was analyzed for basic metrics such as mean, median, etc. The importance of these metrics in achieving the global objectives was explained, helping to understand overall trends and central tendencies.

    **4. Univariate Analysis:**
    - **Non-Graphical Analysis:** Dispersion parameters (variance, standard deviation) for each quantitative variable were computed, and their interpretations were provided.
    - **Graphical Analysis:** Suitable plotting options for each variable were identified, and findings were interpreted to reveal distribution patterns and outliers.

    **5. Bivariate Analysis:**
    - Relationships between each application and total DL + UL data were explored using appropriate methods, providing insights into how different applications contribute to overall data usage.

    **6. Correlation Analysis:**
    - A correlation matrix was computed for variables including Social Media data, Google data, Email data, YouTube data, Netflix data, Gaming data, and Other data. Interpretations of these correlations were provided to understand relationships between various data channels.

    **7. Dimensionality Reduction:**
    - Principal Component Analysis (PCA) was performed to reduce the dimensions of the data. Key results were interpreted in four bullet points, summarizing the most significant components and their implications.
    """)

    # Placeholder for data display (if applicable)
    # Example: df = pd.read_csv('path_to_your_data.csv')  # Replace with actual data path
    # st.write(df.head())  # Display the first few rows of the DataFrame

    # You can also use st.image to include images or graphs if you have any visualizations
    # Example:
    # st.image('path_to_your_plot.png', caption='Exploratory Data Analysis Plot')  # Replace with actual image path

    # Conclusion
    st.header('Conclusion')
    st.write("""
    The User Overview Analysis provided valuable insights into user behavior and data usage across various applications. The findings from this analysis will inform marketing strategies and help tailor services to better meet user needs. The results and visualizations are available for further review and interpretation in the accompanying Python script and presentation slides.

    For additional details or to view the Streamlit app showcasing these results, please refer to the app interface where the data and visualizations are displayed interactively.
    """)
