import requests
import time
import config

# long polling со стороны клиента
# getUpdates?offset={offset + 1}&timeout={timeout}').json()
# 0 < timeout < 100    !!!

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = config.TOKEN
offset = -2
timeout = 60
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')