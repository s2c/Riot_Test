import requests

import json


def get_data():
data_file = open(test,"w")
debugger(i)
#for i in xrange(1,11):
url = 'https://s3-us-west-1.amazonaws.com/riot-api/seed_data/matches1.json'
r = requests.get(url)
data = r.json()
debugger(i)
json.dump(data,data_file,indent=4)
data_file.close()
