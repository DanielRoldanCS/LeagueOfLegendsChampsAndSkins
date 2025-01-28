"""
Skins Module
------------
This script retrieves champion skins data from the League of Legends Data Dragon API
and formats to be processed.
"""

import json
import requests
import config
import champions
import version

def fetch_skins_data(champions_dict):
    """
    Fetch skin data for each champion from the Data Dragon API.

    Args:
        champions_dict (dict): Dictionary containing champion information.

    Returns:
        dict: Dictionary containing skin data for all champions.
    """
    skins = {}
    versionGet = version.get_latest_version()

    for champion_id, champion_info in champions_dict.items():
        try:
            # Fetch data for each champion
            url = f"{config.API_BASE_URL}/{versionGet}/data/en_US/champion/{champion_id}.json"
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors

            data = response.json()
            champion_name = data['data'][champion_id]['id']
            champion_skins = data['data'][champion_id]['skins']

            # Add skins to the dictionary
            skins[champion_name] = champion_skins
        except requests.RequestException as e:
            print(f"Error fetching skins for {champion_id}: {e}")

    return skins

if __name__ == "__main__":
    # For testing purposes only. 
    # Fetches the information from the API and prints the total number of champions
    # It also prints the total number of skins per champion available in the API
    print("Fetching champion skins...")
    champions_dict = champions.parse_champions(champions.get_champions_data())
    skins_data = fetch_skins_data(champions_dict)

    # Print the number of champions and skins retrieved
    print(f"Total champions processed: {len(skins_data)}")
    for champ, skins in skins_data.items():
        print(f"{champ}: {len(skins)} skins")
