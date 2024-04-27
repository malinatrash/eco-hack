import json
import requests

# Открываем файл с данными о шуме
with open('noises_irkutsk.json', 'r') as f:
    noises = json.load(f)

# Адрес сервера
url = 'http://localhost:8000/api/noises/'

# Проходим по каждой записи о шуме и отправляем ее на сервер
for noise in noises:
    # Отправляем POST-запрос с данными о шуме
    response = requests.post(url, json=noise)

    # Проверяем статус ответа
    if response.status_code == 200:
        print("Данные успешно отправлены на сервер.")
    else:
        print("Произошла ошибка при отправке данных на сервер:", response.status_code)
