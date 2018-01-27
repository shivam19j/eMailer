import requests

def get_weather_forecast():
	url = 'http://api.openweathermap.org/data/2.5/find?q=London,uk&units=imperial&appid=81344c0a0e3fb694da728580f8f9a1e0'
	weather_request = requests.get(url)
	weather_json = weather_request.json()
	# print(weather_json)

	description = weather_json['list'][0]['weather'][0]['description']
	print(description)

	temp_min = weather_json['list'][0]['main']['temp_min']
	# print(temp_min)

	temp_max = weather_json['list'][0]['main']['temp_max']
	# print(temp_max)

	forecast = 'The forecast for today is ' + description
	forecast += ' with a high of ' + str(int(temp_max))
	forecast += ' and a low of ' + str(int(temp_min)) 

	return forecast