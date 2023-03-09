import requests
city = "Moscow,RU"
appid = "1df7ead22466bee19cfb42e4122c41e9"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Скорость ветра:", data['wind']['speed'])
print("Дальность", data['visibility'])
