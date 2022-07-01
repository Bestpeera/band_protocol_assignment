import requests

def price_from_binance(symbol:str) -> float:
    if symbol == "BUSD":
        return 1.0
    url='https://www.binance.com/api/v3/ticker/price?symbol='+symbol+"BUSD"
    response = requests.get(url)
    try:
        ask_price = float(response.json()['price'])
        #print(ask_price)
        return ask_price
    except Exception as e:
        return 'error'