# CommentScraper
 
The project includes various Python scripts for web scraping, particularly targeting Instagram and possibly Twitter (X). Here’s a draft README file based on a review of the extracted files:

---

## Overview

**CommentScraper** is a Python-based tool for scraping social media comments, designed to extract and analyze comments from Instagram and Twitter (X) posts. This tool utilizes browser automation and sentiment analysis techniques to collect user feedback on specific topics.

## Features

- **Instagram Scraping**: Captures posts and comments using automated login and navigational scripts.
- **Twitter (X) Scraping**: Currently under development.
- **Sentiment Analysis**: Performs basic sentiment analysis on collected comments to categorize user sentiment.
- **CSV Output**: Saves collected data to CSV files for easy review and further processing.

## Folder Structure

```
CommentScraper/
├── Instagram/
│   ├── browser_setup.py       # Sets up the browser environment
│   ├── Creds.py               # Credentials configuration
│   ├── find_posts.py          # Locates and fetches Instagram posts
│   ├── Login.py               # Handles Instagram login automation
│   ├── main.py                # Main script for running the Instagram scraper
│   ├── scraper.py             # Core scraping logic
│   ├── sentiment_analysis.py  # Analyzes sentiment in comments
│   └── text_processing.py     # Processes text data for analysis
├── X/
│   ├── Creds.py               # Twitter (X) credentials
│   └── XScrapy.py             # Scraper script for Twitter
├── anatelgovbr_posts.csv      # Example data file
├── InstagramScraperDone.csv   # Output sample from Instagram scraper
├── LICENSE                    # License information
└── README.md                  # Documentation
```

## Requirements

- Python 3.10+
- Selenium for browser automation
- pandas for data handling
- NLP libraries such as spaCy (for sentiment analysis)

## Setup and Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Browser setup**:
   - Ensure that you have Chrome and the appropriate ChromeDriver installed.
   - Update the `browser_setup.py` script with your ChromeDriver path if needed.

3. **Configure credentials**:
   - Update `Creds.py` files in both `Instagram` and `X` folders with your login information.
   - the `INSTAGRAM_LOGIN_PATH` and `INSTAGRAM_POST_PATH` are needed for the application to work properly
   - the `Creds.py` files need to look something like this
   ```python
   USERNAME = 'YOUR_USERNAME'
   PASSWORD = 'YOUR_PASSWORD'
   FIND_USER = 'SOME_USER'
   CSV_PATH = f'{FIND_USER}_posts.csv'
   INSTAGRAM_LOGIN_PATH = 'https://www.instagram.com/accounts/login/'
   INSTAGRAM_POST_PATH = 'https://www.instagram.com/p/'
   FINAL_FILE = 'InstagramScraperDone.csv'

## Usage

### Instagram Scraper

Run the Instagram scraper with:
```bash
python Instagram/main.py
```
This will automate the process of logging in, finding posts, extracting comments, and performing sentiment analysis.

### Twitter Scraper (*this is still not working*)

Run the Twitter scraper with:
```bash
python X/XScrapy.py
```

## Contributing

Contributions are welcome! Please follow the [Contributor’s Guide](CONTRIBUTING.md) and ensure all new code includes proper documentation and testing.

## TODO LIST
- [ ] Twitter scrap
- [ ] Facebook scrap
- [ ] Unify sentiment analysis for all social media
- [ ] Improve performance

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.
