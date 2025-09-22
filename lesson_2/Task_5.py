# Задача 5.
# Создайте список словарей с именами и фамилиями.
# Выведите на экран новый список, в котором будут люди с определенными именем (задается юзером).

people = [
    {"name": "Иван", "surname": "Иванов"},
    {"name": "Петр", "surname": "Петров"},
    {"name": "Мария", "surname": "Сидорова"},
    {"name": "Иван", "surname": "Кузнецов"},
    {"name": "Анна", "surname": "Иванова"},
    {"name": "Петр", "surname": "Смирнов"},
    {"name": "Ольга", "surname": "Петрова"},
    {"name": "Иван", "surname": "Попов"}
]

print("Исходный список людей:")
for i, person in enumerate(people, 1):
    print(f"{i}. {person['name']} {person['surname']}")

search_name = input("\nВведите имя для поиска: ").strip()
filtered_people = list(filter(lambda p: p["name"].lower() == search_name.lower(), people))

if filtered_people:
    print(f"\nЛюди с именем '{search_name}':")
    for i, person in enumerate(filtered_people, 1):
        print(f"{i}. {person['name']} {person['surname']}")
else:
    print(f"\nЛюдей с именем '{search_name}' не найдено.")
