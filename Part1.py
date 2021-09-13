

def Discount10Percent(price):
    return (price * 0.10)


def Discount5Percent(price):
    return (price * 0.05)


price = float(input("Enter in the starting price: "))
print(round(price - Discount10Percent(price) - Discount5Percent(price), 2))
