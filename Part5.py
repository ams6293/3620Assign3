class Math:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        return self.x + other.x


num1 = Math(1)
num2 = Math(3)

print(num1 * num2)
