from SnB.coffee.models import Origin
import numpy as np
#from sys import stderr

def getCyclistPrice():
    origin_list = Origin.objects.filter(blend=False, available=True, decaf=False)
    prices = []
    for origin in origin_list:
        prices.append(float(origin.wholesaleprice))
    avg = np.average(prices)
    std = np.std(prices)
    #stderr.write("Prices: %r\n" % prices)
    #stderr.write("avg: %0.2f, std: %0.2f\n" % (avg,std))
    cyclist_wholesale = np.min(np.max(prices), avg+0.5*std)
    return cyclist_wholesale
