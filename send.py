import json
import requests

with open('noises_irkutsk.json', 'r') as f:
    noises = json.load(f)

url = 'http://localhost:8000/api/noises/'

for noise in noises:
    response = requests.post(url, json=noise)

    if response.status_code == 200:
        print("Данные успешно отправлены на сервер.")
    else:
        print("Произошла ошибка при отправке данных на сервер:", response.status_code)
