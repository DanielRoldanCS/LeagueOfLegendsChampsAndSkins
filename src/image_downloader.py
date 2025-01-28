"""
Image Downloader Module
-----------------------
Downloads champion skin images and saves them in the appropriate directory.
"""

import os
import urllib.request
from pathlib import Path
import config

def download_skin_images(skins):
    """
    Download skin images for each champion.

    Args:
        skins (dict): Dictionary of champion skins.
    """
    for champion_name, skin_list in skins.items():
        # Create directory for the champion
        champion_dir = Path(f"ChampionImages/{champion_name}")
        champion_dir.mkdir(parents=True, exist_ok=True)

        for skin in skin_list:
            skin_filename = f"{champion_name}_{skin['num']}.jpg"
            skin_path = champion_dir / skin_filename

            if not skin_path.exists():
                print(f"Downloading {skin_filename}...")
                try:
                    urllib.request.urlretrieve(
                        f"{config.SPLASH_BASE_URL}/{skin_filename}",
                        skin_path
                    )
                except Exception as e:
                    print(f"Failed to download {skin_filename}: {e}")