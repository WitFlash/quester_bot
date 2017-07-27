from urllib import request

url = 'http://agame.com.ua/gallery'
r = request.urlopen(url)
print(r.geturl())
print(r.info())
print(r.getcode())
















'''
from urllib import request
url = 'http://www.restapitutorial.com/httpstatuscodes.html'
r = request.urlopen(url).getcode()
get_url = request.urlopen(url).geturl()
info = request.urlopen(url).info()
print(url, get_url, info, 'Response: ' + str(r), sep='\n')
'''