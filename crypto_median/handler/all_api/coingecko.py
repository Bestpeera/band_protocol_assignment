import requests

def price_from_coingecko(symbol:str) -> float:
    url='https://api.coingecko.com/api/v3/search?query='+symbol
    response = requests.get(url)
    symbol_fullname = response.json()["coins"][0]['id']
    #print(symbol_fullname)
    #symbol_fullname = symbol_fullname".replace(' ','-')
    url='https://api.coingecko.com/api/v3/simple/price?ids='+symbol_fullname+'&vs_currencies=usd'
    response = requests.get(url)
    ask_price = response.json()[symbol_fullname]['usd']
    #print(ask_price)
    return ask_price