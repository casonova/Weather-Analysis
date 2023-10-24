import os
import pandas as pd

def import_csv_file(file_path):
    # Check if file exists
    if os.path.exists(file_path):
        # Read CSV file
        data = pd.read_csv(file_path)
        # Return data
        return data
    # Return None if file not found
    else:
        return None