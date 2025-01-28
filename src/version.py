"""
Version Module
--------------
This script retrieves the latest game version from the League of Legends Data Dragon API.
It saves the latest version to a file 'VERSION.txt' and returns the version from the file if the API call fails.
"""

import requests
import os
from config import VERSIONS_URL

# Path to the VERSION.txt file
VERSION_FILE_PATH = "VERSION.txt"

def get_latest_version():
    """
    Fetch the latest game version from the API.

    Returns:
        str: Latest version as a string, or the version from VERSION.txt if the request fails.

    Assumption:
        VERSION.txt file will always be available and will always have the latest valid call to the API.
    """
    try:
        # Make a request to fetch the latest version from the API
        response = requests.get(VERSIONS_URL)
        response.raise_for_status()  # Will raise an exception for bad responses
        versions = response.json()
        latest_version = versions[0]  # Get the most recent version

        # Save the latest version to VERSION.txt
        save_latest_version(latest_version)

        return latest_version
    except requests.RequestException as e:
        print(f"Error fetching latest version: {e}")
        return read_version_from_file()  # Return version from VERSION.txt if there's an error

def save_latest_version(version):
    """
    Save the latest version to the VERSION.txt file.
    """
    with open(VERSION_FILE_PATH, 'w') as file:
        file.write(version)

def read_version_from_file():
    """
    Read the version from VERSION.txt.
    Returns the version from the file.
    """
    try:
        if os.path.exists(VERSION_FILE_PATH):
            with open(VERSION_FILE_PATH, 'r') as file:
                version = file.read().strip()
                if version:  # If the file is not empty
                    return version
        return None  # If file is empty returns nothing due to assumption
    except Exception as e:
        print(f"Error reading version from file: {e}")
        return None
