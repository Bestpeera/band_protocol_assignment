from typing import List
import statistics

def calculate_median(price_list: List[float]) -> float:
    no_outlier_list = []
    try:
        sd = statistics.stdev(price_list)
        mean = statistics.mean(price_list)
        for price in price_list:
            if price>=mean-(2*sd) and price<=mean+(2*sd):
                no_outlier_list.append(price)
        med = statistics.median(no_outlier_list)
    except Exception as e:
        raise e
    return med