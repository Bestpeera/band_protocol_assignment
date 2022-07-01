from typing import List
from .calculator import calculate_median
from .handler import find_price

def find_median_of_symbols(symbols: List[str]) -> float:
    symbols = list(set(symbols))
    for symbol in symbols:
        try:
            price_list=find_price(symbol)
            med=calculate_median(price_list)
            print(symbol,med)
        except Exception as e:
            raise e
#print(find_median_of_symbols(["CAKE"]))