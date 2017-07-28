import requests

url = "https://api.telegram.org/bot346848783:AAFSCGeP1nbUsq84jWQyqC_0cxMRq6kwoWI/"


def get_update_json(request):
    response = requests.get(request+'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results)-1
    return results[total_updates]


print(get_update_json(url))
print('\n\n')
print(last_update(get_update_json(url)))


#print(TelegramBot.getUpdates())

# Use this token to access the HTTP API:
# 346848783:AAFSCGeP1nbUsq84jWQyqC_0cxMRq6kwoWI