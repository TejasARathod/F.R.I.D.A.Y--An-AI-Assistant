
import requests

complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q=Pune&appid=0b3b598b540995e9755cdf8ab184dcaa'
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']

temp = "Current temperature is {:.2f} degree Celsius ".format(temp_city)
desc = "Current weather description is "+ str(weather_desc)
hum =  "Current Humidity is " + str(hmdt) + '%'
wind = "Current wind speed is " + str(wind_spd) + 'kmph'

print(temp)
print(desc)
print(hum)
print(wind)

