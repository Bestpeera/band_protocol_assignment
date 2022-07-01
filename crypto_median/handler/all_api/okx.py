import requests

def price_from_okx(symbol:str) -> float:
    url='https://www.okx.com/api/v5/market/ticker?instId='+symbol+'-USD-SWAP'
    response = requests.get(url)
    #print(response.json())
    try:
        ask_price=float(response.json()['data'][0]['askPx'])
        #print(ask_price)
        return ask_price
    except Exception as e:
        #print(e)
        return 'error'