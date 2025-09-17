a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

minimum = min(a, b, c)
maximum = max(a, b, c)
middle = a + b + c - minimum - maximum

print(minimum, middle, maximum)
