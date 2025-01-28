# LeagueOfLegendsChampsAndSkins

LeagueOfLegendsChampsAndSkins is a Python-based project designed to interact with the League of Legends Data Dragon API. It retrieves information about champions and their skins, stores the data in JSON files, and downloads splash art images for each champion and skin.

## Features

- Fetches the latest version of the game dynamically.
- Retrieves information about all champions, including their IDs, names, and titles.
- Fetches skin data for each champion, including unique skin numbers and names.
- Downloads high-quality splash art images for each skin.
- Stores retrieved data in JSON files for persistent storage.


## Requirements

- Python 3.7+
- Internet connection (to fetch data from the API)

### Python Libraries

The following Python libraries are required for this project:

- `requests`: For making HTTP requests to the API.
- `os`: For file and directory management.
- `json`: For working with JSON data.
- `pathlib`: For handling file paths.

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/DanielRoldanCS/LeagueOfLegendsChampsAndSkins.git
cd LeagueOfLegendsChampsAndSkins
```

2. Copy the example configuration file and modify it with your API links:

```bash
cp config.example.py config.py
```

Open config.py and replace any placeholders with your specific links.

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the project:

```bash
python main.py
```

## How It Works

1. **Fetching Data**:
   - The project retrieves the latest game version using `version.py`.
   - It fetches champion and skin data using `champions.py` and `skins.py`.

2. **Data Storage**:
   - Retrieved data is stored in JSON files (`champions.json` and `skins.json`) located in the `data/` directory.

3. **Image Downloading**:
   - High-quality splash art images for each skin are downloaded to the `ChampionImages/` directory.

## Example Output

- JSON data for champions:

```json
{
    "Aatrox": [
        {"key": "266"},
        {"name": "Aatrox"},
        {"title": "the Darkin Blade"}
    ],
    ...
}
```

- JSON data for skins:

```json
{
    "Aatrox": [
        {"num": 0, "name": "Classic Aatrox"},
        {"num": 1, "name": "Justicar Aatrox"},
        ...
    ]
}
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Riot Games for providing the League of Legends Data Dragon API.

