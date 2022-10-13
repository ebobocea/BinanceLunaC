import requests
import json

response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=LUNCBUSD")
ticket = json.loads(response.text)
print(f'LUNC:{ticket["price"]}')
