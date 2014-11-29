
import requests
import json
import date_test
from stage4 import datestamp







data = {'token':'hGO8rPbdnQ', 'datestamp': datestamp('85915058', '2007-05-22T12:18:00.000Z')}

r = requests.post('http://challenge.code2040.org/api/validatetime', data=json.dumps(data))
jsonData = r.json()

print(jsonData)
