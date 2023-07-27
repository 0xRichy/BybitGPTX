import requests
from config import Config

class BybitAPI:
    BASE_URL = "https://api.bybit.com"

    def __init__(self):
        self.api_key = Config.BYBIT_API_KEY
        self.api_secret = Config.BYBIT_API_SECRET

    def get_market_data(self, symbol):
        endpoint = "/v2/public/tickers"
        params = {"symbol": symbol}
        response = requests.get(self.BASE_URL + endpoint, params=params)
        return response.json()

    # Ajoutez d'autres méthodes pour passer des ordres, etc.
