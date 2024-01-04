import requests
import time
import config


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'
API_FOXS_URL = 'https://randomfox.ca/floof/'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
DESCRIPTION_TEXT = 'напиши кто нравится: котик, песик, лисичка'

BOT_TOKEN = config.TOKEN

offset = -2
counter = 0
response: requests.Response
url_link: str

while 1: # counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            flag = 0
            print("result: ", result)
            text_message = result['message']['text'].lower()
            print("result text: ", text_message)
            offset = result['update_id']
            print("offset: ", offset)
            chat_id = result['message']['from']['id']
            print("chat_id: ", chat_id)

            # if  text_message == 'стоп' or text_message == 'stop':
                # requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={"finish..."}')
                # result['message']['text'] = ""
                # exit()
            if text_message == 'котик':
                response = requests.get(API_CATS_URL)
                url_link = response.json()[0]['url']
                flag = 1
            elif  text_message == 'песик' or text_message == 'пёсик':
                response = requests.get(API_DOGS_URL)
                url_link = response.json()['url']
                flag = 1
            elif  text_message == 'лисичка':
                response = requests.get(API_FOXS_URL)
                url_link = response.json()['image']
                flag = 1
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={DESCRIPTION_TEXT}')

            if flag == 1 and response.status_code == 200:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={url_link}')
            elif flag == 1 and response.status_code != 200:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
