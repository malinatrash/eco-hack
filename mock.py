from faker import Faker
from random import uniform
from datetime import datetime
import json

# Создаем объект Faker
fake = Faker('ru_RU')

# Координаты города Иркутска (долгота, широта)
irkutsk_coordinates = (104.2807, 52.2864)

# Генерируем 10000 тестовых шумов для города Иркутска
noises = []
for _ in range(10000):
    # Генерируем случайные координаты в пределах города
    latitude = uniform(52.15, 52.4)  # Примерные границы широты Иркутска
    longitude = uniform(103.85, 104.45)  # Примерные границы долготы Иркутска

    # Генерируем случайный уровень шума в децибелах
    decibels = uniform(40, 100)

    # Генерируем случайную частоту
    frequency = uniform(50, 20000)

    # Генерируем случайную дату и время
    timestamp = fake.date_time_this_year()

    # Добавляем шум в список
    noises.append({
        'latitude': latitude,
        'longitude': longitude,
        'decibels': decibels,
        'frequency': frequency,
        'datetime': timestamp.strftime('%Y-%m-%d %H:%M:%S')
    })

# Сохраняем тестовые данные в JSON файл
with open('noises_irkutsk.json', 'w') as f:
    json.dump(noises, f, ensure_ascii=False, indent=4)

print("Тестовые данные успешно сгенерированы и сохранены в файл 'noises_irkutsk.json'")
