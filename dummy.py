import requests


url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperials&appid=4dff3bbc561ffeb5f1a85a5a1003c3ed'
city = 'Thirunelveli'
r= requests.get(url.format(city)).json()

if 'name' not in r:
        print('City not found')

print(r)

# print(r['name'])
# print(r['main']['temp'])
