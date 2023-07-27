import ccxt
import talib
from bybit import bybit
from openai import OpenAI

# Définissez vos clés API
OPENAI_API_KEY = 'votre_clé_api_openai'
BYBIT_API_KEY = 'votre_clé_api_bybit'
BYBIT_API_SECRET = 'votre_secret_api_bybit'

class TradingStrategy:
    def __init__(self):
        self.openai = OpenAI(api_key=OPENAI_API_KEY)
        self.bybit = bybit(test=False, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)
        self.exchange = ccxt.bybit({
            'apiKey': BYBIT_API_KEY,
            'secret': BYBIT_API_SECRET,
        })

    def get_trading_action(self, market_data, symbol):
        prompt = self._create_prompt(market_data)
        response = self.openai.Completion.create(engine="davinci-codex", prompt=prompt, max_tokens=100)
        action = self._parse_response(response)
        self.execute_trade(action, symbol)
        return action

    def _create_prompt(self, market_data):
        # Formatez les données du marché en une chaîne de caractères
        market_data_str = "\n".join(f"{key}: {value}" for key, value in market_data.items())
        
        # Créez le prompt pour GPT-3
        prompt = (
            f"Les données actuelles du marché sont :\n"
            f"{market_data_str}\n"
            f"Compte tenu de ces informations, quelle action de trading recommanderiez-vous ?"
        )
        
        return prompt

    def _parse_response(self, response):
        # Obtenez le texte généré par GPT-3
        gpt3_text = response.choices[0].text.strip()

        # Déterminez l'action de trading
        if "acheter" in gpt3_text.lower():
            action = "Acheter"
        elif "vendre" in gpt3_text.lower():
            action = "Vendre"
        else:
            action = "Ne rien faire"

        return action

    def execute_trade(self, action, symbol):
        if action == "Acheter":
            # Place a buy order
            self.bybit.place_active_order(symbol=symbol, side="Buy", order_type="Market", qty=1, time_in_force="GoodTillCancel")
        elif action == "Vendre":
            # Place a sell order
            self.bybit.place_active_order(symbol=symbol, side="Sell", order_type="Market", qty=1, time_in_force="GoodTillCancel")
