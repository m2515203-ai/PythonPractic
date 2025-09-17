
import math

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Арифметические операции
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {round(a / b, 2)}" if b != 0 else "Бесконечность")
print(f"{a} // {b} = {a // b}" if b != 0 else "Бесконечность")
print(f"{a} % {b} = {a % b}" if b != 0 else "Бесконечность")
print(f"{a} ** {b} = {a ** b}")
print(f"log10({a}) = {round(math.log10(a), 2)}" if a > 0 else "Логарифм нуля (log 0) не определён")

# Операции сравнения
print(f"{a} < {b} = {a < b}")
print(f"{a} <= {b} = {a <= b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} >= {b} = {a >= b}")
print(f"{a} != {b} = {a != b}")
print(f"{a} == {b} = {a == b}")