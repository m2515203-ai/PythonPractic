# Требования к данным:
# - кол-во объектов (элементов словаря) должно быть не менее 3;
# - кол-во атрибутов объекта должно быть не менее 5;
# - по крайней мере 3 атрибута объекта должны иметь различный тип:
#   int, float, str и др.;
# - по крайней мере 1 атрибут объекта должен иметь тип list.


# Замените атрибуты словаря и др. на соответствующие своему варианту

db = [
    {
        "name": "Иванов Иван",
        "birthday": "01/12/2000",
        "height": 170,
        "weight": 70.5,
        "car": True,
        "languages": ["С++", "Python"]
    },
    {
        "name": "Сергеев Сергей",
        "birthday": "01/06/2001",
        "height": 180,
        "weight": 110.4,
        "car": False,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Николаева Мария",
        "birthday": "14/07/1998",
        "height": 180,
        "weight": 66.9,
        "car": True,
        "languages": ["C#", "C++", "C"]
    },
    {
        "name": "Петрова Анна",
        "birthday": "25/03/1999",
        "height": 165,
        "weight": 58.2,
        "car": False,
        "languages": ["Java", "JavaScript", "Python"]
    }
]

# Вывод содержимого базы данных
print(f"Содержимое базы данных ({len(db)}):")

for i, person in enumerate(db, 1):
    print(f"{i}.")
    print(f"Имя: {person['name']}")
    print(f"День рождения: {person['birthday']}")
    print(f"Рост (см.): {person['height']}")
    print(f"Вес (кг.): {person['weight']}")
    print(f"Есть машина: {person['car']}")
    print(f"Языки программирования: {person['languages']}")