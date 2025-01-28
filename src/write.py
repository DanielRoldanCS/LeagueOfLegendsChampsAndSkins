"""
Write Module
------------
This script writes champion and skin data to JSON files.
"""

import json
from pathlib import Path
import champions
import skins

def save_data_to_file(data, filename):
    """
    Save data to a JSON file in the `data/` directory.

    Args:
        data (dict): Data to be saved.
        filename (str): Name of the file to save the data.
    """
    try:
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)  # Ensure the directory exists
        file_path = data_dir / filename

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing data to file: {e}")

def write_data_to_files():
        print("Writing champion and skin data to files...")

        # Fetch data from modules
        champions_data = champions.parse_champions(champions.get_champions_data())
        skins_data = skins.fetch_skins_data(champions_data)

        # Save data to files
        save_data_to_file(champions_data, "champions.json")
        save_data_to_file(skins_data, "skins.json")