from .all_api import *
from typing import List

LIMIT_ERROR_SOURCE = 2

func_list = [
    price_from_binance,
    price_from_coingecko,
    price_from_coinmarketcap,
    price_from_kraken,
    price_from_okx
    ]

def find_price(symbol: str) -> List[float]:
    error_count = 0
    price_list = []
    for f in func_list:
        ask_price = f(symbol)
        #print(f,ask_price)
        if ask_price == 'error':
            error_count=error_count+1
        else:
            price_list.append(ask_price)
        if error_count > LIMIT_ERROR_SOURCE:
            raise Exception("'Not enough source.")
    return price_list
