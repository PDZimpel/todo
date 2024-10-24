import requests
import datetime as dt
import json

BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api-key.txt", 'r').read()


def kelvinToCelsiusFahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


LOC = "Campo Grande"
url = (BASE_URL+"appid=" + API_KEY+"&q="+LOC)
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvinToCelsiusFahrenheit(temp_kelvin)
feels_kelvin = response['main']['feels_like']
feels_celsius, feels_fahrenheit = kelvinToCelsiusFahrenheit((feels_kelvin))
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


