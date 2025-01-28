"""
Champions Module
----------------
This script retrieves the current version and total number of champions
in League of Legends from the Data Dragon API.
"""

import requests
import json
import config  # Importing sensitive data from config.py
import version  # Importing the version module

def get_champions_data():
    """
    Fetch the latest champions data from the Data Dragon API.
    
    Returns:
        dict: A dictionary containing information about all champions.
    """
    try:
        # Fetch current version and champion data
        response = requests.get(f"{config.API_BASE_URL}/{version.get_latest_version()}/data/en_US/champion.json")
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()
        return data['data']
    except requests.RequestException as e:
        print(f"Error fetching champions data: {e}")
        return {}

def parse_champions(champions_data):
    """
    Parse champions data into a formatted dictionary.
    
    Args:
        champions_data (dict): Raw champions data from the API.
        
    Returns:
        dict: Formatted champions data.
    """
    champions = {}
    for champion_id, info in champions_data.items():
        champions[info['id']] = [
            {'key': info['key']},
            {'name': info['name']},
            {'title': info['title']}
        ]
    return champions

if __name__ == "__main__":
    # For testing purposes only. 
    # Fetches the information from the API and prints the total number of champions
    print("Fetching League of Legends champions...")
    champions_data = get_champions_data()
    champions = parse_champions(champions_data)
    
    if champions:
        print(f"Champions retrieved successfully. Total: {len(champions)}")
    else:
        print("Failed to retrieve champions data.")
