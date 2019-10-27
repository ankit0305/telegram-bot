from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()
matches=c.matches()
class Cricket:
	def match():
		js=json.dumps(matches,indent=4)
		di=json.loads(js)
		return di["team2"]