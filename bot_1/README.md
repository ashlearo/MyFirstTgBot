## main.py

Бот на полученное сообщения отправляет ответ

## main2.py
Бот присылает картинку животного в зависимости от полученного сообщения

## main3.py
- polling со стороны клиента, то есть бота
- updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
- timeout == 0    !!!
- или:
- updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

## main4.py
- long polling со стороны клиента
- updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
- 0 < timeout < 100    !!!

## config.py
в файле config.py положить токен:
TOKEN = 'токен бота'
