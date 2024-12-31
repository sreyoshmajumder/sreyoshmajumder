import requests

city_name = 'delhi'
API_Key = 'f3bf687659dff27e8d6987248c86bf5e'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

print('WEATHER UPDATING .....................')
response = requests.get(url)
if response.status_code == 200:
   data = response.json()
   print(data)
   print('Current Temperature is :- ',data['main']['temp'])