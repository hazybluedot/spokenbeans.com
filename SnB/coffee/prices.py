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

def getRetailPrice(wholesale, weight, markup):
    "Given wholesale price, weight (float),  markup percent, calculate retail price"
    wholesale = float(wholesale)
    weight = float(weight)
    markup = float(markup)
    return round(weight*wholesale*(markup+1),2)

def getBothPrices(wholesale):
    price_list = ()
    price_list += ( addTax(getRetailPrice(float(wholesale), 0.77, 0.75), 0.025), )
    price_list += ( addTax(getRetailPrice(float(wholesale), 0.38, 0.85), 0.025), )
    return price_list

def addTax(price, tax):
    price = float(price)
    tax = float(tax)
    return round(price*(1+tax),2)
