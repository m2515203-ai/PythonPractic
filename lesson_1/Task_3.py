import math

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

numerator = (x**5 + 7)
denominator = abs(-6) * y
fraction = numerator / denominator
result = math.pow(fraction, 1/3) / (7 - z % y)

print(round(result, 3))