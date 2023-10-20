import psutil
import requests


def send_alarm(url, message):
    headers = {'Content-Type': 'application/json'}
    data = {'message': message}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Аларм успешно отправлен")
    else:
        print("Ошибка отправки аларма")


threshold = 80
"""Пороговое значение аларма в 80%"""

memory_usage = psutil.virtual_memory().percent

if memory_usage > threshold:
    api_url = 'http://example.com/alarm'
    message = f"Потребление памяти превысило пороговое значение: {memory_usage}%"
    send_alarm(api_url, message)
