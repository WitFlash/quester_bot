import requests
from time import sleep

url = "https://api.telegram.org/bot346848783:AAFSCGeP1nbUsq84jWQyqC_0cxMRq6kwoWI/"

def get_update_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results)-1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_msg(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)

def main():
    update_id = last_update(get_update_json(url))['update_id']
    while True:
        if update_id == last_update(get_update_json(url))['update_id']:
            send_msg(get_chat_id(last_update(get_update_json(url))), 'test')
            update_id += 1

if __name__ == '__main__':
    main()


#chat_id = get_chat_id(last_update(get_update_json(url)))
#send_msg(chat_id, "It's my first message!")