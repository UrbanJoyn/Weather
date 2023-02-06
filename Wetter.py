import requests

API_KEY =""
BASE_URL = "https://home.openweathermap.org/api_keys"

city = input("Enter a City: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = data['main']['temp'] - 273,15
    print(temperature)
else:
    print('Error')
