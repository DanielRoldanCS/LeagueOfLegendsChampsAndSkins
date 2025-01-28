"""
Main Entry Point
----------------
This script runs the LeagueOfLegendsChampsAndSkins project by:
1. Fetching the latest version and champion data.
2. Writing champions and skins data to JSON files.
3. Downloading champion skin images.
"""

from write import write_data_to_files
from image_downloader import download_skin_images
from read import load_skins

def main():
    print("Welcome to the League of Legends Champs and Skins Downloader!")
    print("Fetching data and preparing resources...\n")

    # Step 1: Write champions and skins data to files
    write_data_to_files()

    # Step 2: Load skins data from file
    skins = load_skins()

    # Step 3: Download skin images
    print("\nStarting image downloads...")
    download_skin_images(skins)

    print("\nAll tasks completed successfully!")

if __name__ == "__main__":
    main()
