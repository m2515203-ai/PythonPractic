# Задача 6.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

def count_it(sequence):
    count_dict = {}
    for char in sequence:
        if char.isdigit():
            num = int(char)
            count_dict[num] = count_dict.get(num, 0) + 1
    if not count_dict:
        return {}
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    return dict(sorted_items[:3])


example_sequence = "1234512345123456789012345"
result = count_it(example_sequence)

print(f"Входная строка: '{example_sequence}'")
print(f"3 самых частых числа: {result}")
