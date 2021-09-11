def Discount10Percent(price):
    return price - (price * .10)

productList = [10, 10.5, 25, 45, 45, 60, 85, 99, 100]

result = list(map(Discount10Percent, productList))

print(result)