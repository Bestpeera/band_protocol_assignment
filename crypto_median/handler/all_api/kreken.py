import requests

def price_from_kraken(symbol:str) -> float:
    url='https://api.kraken.com/0/public/Ticker?pair='+symbol+'USD'
    response = requests.get(url)
    try:
        for key in response.json()['result'].keys():
            ask_price = float(response.json()['result'][key]['a'][0])
        #print(ask_price)
        return ask_price
    except Exception as e:
        #print(e)
        return 'error'