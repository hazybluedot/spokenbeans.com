
def getRetailPrice(wholesale, weight, markup):
    "Given wholesale price, weight (float),  markup percent, calculate retail price"
    wholesale = float(wholesale)
    weight = float(weight)
    markup = float(markup)
    return round(weight*wholesale*(markup+1),2)

def addTax(price, tax):
    price = float(price)
    tax = float(tax)
    return round(price*(1+tax),2)
