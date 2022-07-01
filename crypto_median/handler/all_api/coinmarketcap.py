import requests
from requests import Session,Timeout,TooManyRedirects
import time

def price_from_coinmarketcap(symbol:str) -> float:
    def find_slug(symbol:str) -> str:
        API_KEY = '59769d5a-7321-4ae8-8f5f-bfd77559389a'
        url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        parameters = {
            'symbol':symbol
            }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY
            }
        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            if response.status_code == 429:
                time.sleep(60)
            slug = response.json()["data"][0]["slug"]
            return slug
        except Exception as e:
            return 'error'

    API_KEY = '59769d5a-7321-4ae8-8f5f-bfd77559389a'
    slug = find_slug(symbol)
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'slug':slug,
        'convert':'USD'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
        }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        if response.status_code == 429:
            print('hell2')
        for key in response.json()['data'].keys():
            ask_price = float(response.json()["data"][key]['quote']['USD']['price'])
    except Exception as e:
        return 'error'
    return ask_price