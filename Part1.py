

def Discount10Percent(price):
    return price - (price * .10)


def Discount5Percent(price):
    return price - (price * .5)


def BothDiscounts(Discount10, Discount5, arg):
    return Discount10(Discount5(arg))


print(BothDiscounts(Discount10Percent, Discount5Percent, 100))
