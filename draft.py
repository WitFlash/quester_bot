from urllib import request

url = 'http://agame.com.ua/gallery'
r = request.urlopen(url)
print(r.geturl())
print(r.info())
print(r.getcode())










#print(TelegramBot.getUpdates())

# Use this token to access the HTTP API:
# 346848783:AAFSCGeP1nbUsq84jWQyqC_0cxMRq6kwoWI