import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Loads telecom data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
