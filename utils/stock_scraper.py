
import requests
from bs4 import BeautifulSoup
from framework.logger import setup_logger

def get_top_gainers():
    url = "https://br.tradingview.com/markets/stocks-brazil/market-movers-gainers/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        logger = setup_logger()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table')
        if not table:
            logger.error("Tabela de maiores altas não encontrada.")
            return []

        rows = table.find('tbody').find_all('tr')
        top_gainers = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 5:
                ticker = columns[0].get_text(strip=True)
                name = columns[1].get_text(strip=True)
                price = columns[2].get_text(strip=True)
                change_percent = columns[4].get_text(strip=True)
                top_gainers.append({
                    "ticker": ticker,
                    "name": name,
                    "price": price,
                    "change_percent": change_percent
                })

        logger.info(f"{len(top_gainers)} ações recuperadas com sucesso.")
        return top_gainers

    except Exception as e:
        logger.error(f"Erro ao recuperar dados de maiores altas: {e}")
        return []
