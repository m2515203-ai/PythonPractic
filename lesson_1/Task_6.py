v = float(input("Скорость (км/ч): "))
t = float(input("Время (ч): "))
distance = v * t
position = int(distance % 122)
print(position)
