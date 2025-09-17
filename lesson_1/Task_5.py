a = float(input("Введите a: "))
b = float(input("Введите b: "))
m = float(input("Введите m: "))
n = float(input("Введите n: "))

if a == 0:
    if b == 0:
        print("Бесконечное число решений")
    else:
        print("Нет решений")
else:
    x = -b / a
    if m <= x <= n:
        print(f"Решение {x} попадает в отрезок [{m}; {n}]")
    else:
        print(f"Решение {x} не попадает в отрезок [{m}; {n}]")
