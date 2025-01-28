"""
Read Module
-----------
This script reads champions and skins data from JSON files in the `data` directory.
It ensures the data is imported and available for other scripts.
"""

import json
from pathlib import Path

# Define paths to the JSON files
DATA_DIR = Path("data")
CHAMPIONS_FILE = DATA_DIR / "champions.json"
SKINS_FILE = DATA_DIR / "skins.json"

def load_json(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (Path): Path to the JSON file.
    
    Returns:
        dict: Data loaded from the JSON file.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return {}

def load_skins():
    """
    Dynamically load skins data from the JSON file.
    
    Returns:
        dict: Skins data.
    """
    print("Loading skins data...")
    return load_json(SKINS_FILE)

def load_champions():
    """
    Dynamically load champions data from the JSON file.
    
    Returns:
        dict: Champions data.
    """
    print("Loading champions data...")
    return load_json(CHAMPIONS_FILE)
