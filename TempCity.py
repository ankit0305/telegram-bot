import requests

TOKEN=""
location="thiruvananthapuram"

class TempCity:
	def temp(self):
		url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, TOKEN)
		r=requests.get(url)
		return r.json()
