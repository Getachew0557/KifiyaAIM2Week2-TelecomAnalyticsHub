# Enhancing Telecom Business Insights through Comprehensive Data Analysis and Machine Learning Techniques for Optimal Investment Decisions

## Executive Summary

In the highly competitive telecom sector, understanding customer behavior and engagement is crucial for making informed investment decisions. This project involves a comprehensive analysis of telecom data for TellCo, a mobile service provider in the Republic of Pefkakia. Leveraging advanced data analysis and machine learning techniques, the project aims to identify opportunities for growth, optimize service offerings, and support strategic investment decisions.

## Project Overview

The objective of this project is to analyze the data provided by TellCo to identify opportunities for growth and to assess whether TellCo is a worthy investment. The analysis is divided into four primary tasks:

1. **User Overview Analysis**: Understanding customer behavior and usage patterns.
2. **User Engagement Analysis**: Evaluating user engagement metrics and clustering users based on engagement.
3. **Experience Analysis**: Analyzing user experience metrics, including network performance and device characteristics.
4. **Satisfaction Analysis**: Combining engagement and experience metrics to compute satisfaction scores and predict customer satisfaction.

## Dataset Description

- **Data Source**: xDR records from TellCo.
- **Attributes**: Includes user activity data on various applications (e.g., Social Media, Google, Email, YouTube, Netflix, Gaming) and network performance metrics (e.g., TCP retransmission, RTT, Throughput).
- **Schema**: Detailed description of attributes and SQL schema.

## Project Setup

### Prerequisites

- Python 3.8+
- PostgreSQL Database
- Docker (for containerization)
- GitHub Actions (for CI/CD)

### Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/telecom-insights-project.git
    cd telecom-insights-project
    ```

2. **Setup Virtual Environment**:

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Database Setup**:
    - Import the provided SQL schema into your PostgreSQL database.
    - Configure the connection settings in your project configuration files.

5. **Run Tests**:

    ```bash
    pytest
    ```

6. **Build Docker Image**:

    ```bash
    docker build -t telecom-insights .
    ```

7. **Run Docker Container**:

    ```bash
    docker run -p 8501:8501 telecom-insights
    ```

## Tasks and Methodologies

### Task 1 - User Overview Analysis

- **Objective**: Analyze user behavior and handset usage to identify top devices and manufacturers.
- **Sub-tasks**:
  - Identify top 10 handsets and top 3 manufacturers.
  - Analyze the top 5 handsets per manufacturer.
  - Provide recommendations based on the findings.

- **Deliverables**:
  - Python scripts for data aggregation and analysis.
  - EDA reports and visualizations.

### Task 2 - User Engagement Analysis

- **Objective**: Assess user engagement based on session frequency, duration, and traffic.
- **Sub-tasks**:
  - Aggregate metrics per customer and classify users into engagement clusters using k-means clustering.
  - Analyze engagement metrics and identify top engaged users and applications.
  - Optimize clustering parameters and interpret findings.

- **Deliverables**:
  - Python scripts for engagement metrics calculation and clustering.
  - Visualizations and interpretations.

### Task 3 - Experience Analysis

- **Objective**: Evaluate user experience based on network parameters and device characteristics.
- **Sub-tasks**:
  - Aggregate and analyze TCP retransmission, RTT, throughput, and handset type.
  - Compute and list top and bottom values for key metrics.
  - Perform k-means clustering based on experience metrics.

- **Deliverables**:
  - Python scripts for experience analysis and clustering.
  - Insights and visualizations.

### Task 4 - Satisfaction Analysis

- **Objective**: Determine customer satisfaction based on engagement and experience scores.
- **Sub-tasks**:
  - Compute engagement and experience scores using Euclidean distance.
  - Build a regression model to predict satisfaction scores.
  - Perform clustering on satisfaction scores and export results.

- **Deliverables**:
  - Python scripts for satisfaction score calculation and regression modeling.
  - Visualizations and final report.

## Dashboard Development

- **Objective**: Develop an interactive dashboard using Streamlit to visualize insights.
- **Features**:
  - User-friendly navigation and clear data visualizations.
  - Interactive widgets for data exploration.

- **Deliverables**:
  - Streamlit dashboard accessible via a public URL.

## Conclusion

This project aims to provide a comprehensive analysis of TellCo's telecom data, offering insights into user behavior, engagement, experience, and satisfaction. The findings will inform investment decisions and strategic recommendations. Through meticulous analysis and advanced visualization, we seek to enhance understanding and drive profitable investment outcomes.

## Contact

For any questions or further information, please contact [Getachew Getu](mailto:getachewgetu2010@gmail.com).
