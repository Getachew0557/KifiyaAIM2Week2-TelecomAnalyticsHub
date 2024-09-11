import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch MySQL connection parameters from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

def export_to_mysql(df, table_name):
    """
    Exports the given DataFrame to a MySQL table.
    """
    connection = None
    cursor = None
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        cursor = connection.cursor()

        # Loop through the DataFrame and insert each row into the MySQL table
        for index, row in df.iterrows():
            sql = f"INSERT INTO {table_name} (MSISDN, engagement_score, experience_score, satisfaction_score) " \
                  f"VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (row['MSISDN/Number'], row['Engagement Score'], row['Experience Score'], row['Satisfaction Score']))

        # Commit the transaction
        connection.commit()
        print(f"Data successfully exported to {table_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close cursor and connection if they were initialized
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
