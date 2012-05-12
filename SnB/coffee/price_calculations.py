from SnB.coffee.models import Origin
import numpy as np

def getCyclistPrice():
    origin_list = Origin.objects.filter(blend=False, available=True, decaf=False)
    prices = []
    for origin in origin_list:
        prices.append(origin.wholesaleprice)
    avg = np.average(prices)
    std = np.std(prices)
    cyclist_wholesale = np.min(np.max(prices),avg+0.5*std)
    return cyclist_wholesale
