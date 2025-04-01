# Phone Data Scraper

This script scrapes smartphone data from The Gioi Di Dong website (https://www.thegioididong.com/dtdd) for price analysis and prediction.

## Features

The scraper collects the following information for each smartphone:
- Brand name
- Product name
- Release date
- Processor
- RAM
- Internal storage
- Screen size
- Screen technology
- Screen refresh rate
- Number of rear cameras
- Main camera resolution
- Battery capacity
- Fast charging capability
- 5G support
- Price
- Product URL

## Requirements

- Python 3.7+
- Required packages listed in `requirements.txt`

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python phone_scraper.py
```

The script will:
1. Scrape all phone listings from The Gioi Di Dong website
2. Extract detailed specifications for each phone
3. Save the data to a CSV file with timestamp in the filename

## Output

The data will be saved in a CSV file named `phone_data_YYYYMMDD_HHMMSS.csv` in the same directory as the script.

## Notes

- The script includes delays between requests to be respectful to the website's servers
- Some phones might be missing certain specifications
- The script handles errors gracefully and continues scraping even if some phones fail 