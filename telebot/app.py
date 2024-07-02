import requests


BOT_TOKEN = '7486980868:AAH88FIlMU9-KWYLmjKp3L2H_qAvHo05YLw'


API_METHOD = 'setWebhook'
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/{API_METHOD}"

request_data = {
    'url': 'https://functions.yandexcloud.net/d4etclimd8asjpvvarim'
}

response_data = requests.post(API_URL, request_data)

print(response_data.json())