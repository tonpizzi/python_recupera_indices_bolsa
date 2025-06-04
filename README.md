# Python Scraping Stock Indexes
This project aims to collect stock market index data using web scraping techniques in Python.

## Technologies Used
- Python
- Scraping libraries (`requests`, `BeautifulSoup`)
- Modular structure with folders like `config`, `data`, `framework`, `logs`, `utils`

## Project Structure
python_scraping_stock_indexes/
├── config/ # Project settings
├── data/ # Collected data
├── framework/ # Main scraping logic
├── logs/ # Log files
├── utils/ # Helper functions
│ └── stock_scraper.py # Core scraping module
└── main.py # Entry point script


## About `stock_scraper.py`
The `stock_scraper.py` module is responsible for extracting stock market index data using web scraping techniques. It uses `requests` and `BeautifulSoup` to collect and structure information such as index names, current values, and percentage changes. This script includes error handling to deal with changes in page structure or connectivity issues.

## How to Use
1. Clone the repository:
   git clone https://github.com/tonpizzi/python_scraping_stock_indexes.git
   cd python_scraping_stock_indexes

2. Install dependencies:
   pip install -r requirements.txt

3. Run the main script:
   python main.py

License
This project is licensed under the MIT License.
