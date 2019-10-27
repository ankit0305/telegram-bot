import requests

class Pic:
	def dogpic(self):
		contents = requests.get('https://random.dog/woof.json').json()    
		url = contents['url']
		return url