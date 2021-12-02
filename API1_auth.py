import requests
import codecs
import json

from requests.models import Response
request = requests.get(
    'https://api.mapbox.com/directions/v5/mapbox/driving/-84.518641%2C39.13427%3B-84.512023%2C39.102779?alternatives=true&geometries=geojson&steps=true&access_token=pk.eyJ1IjoiYWtobWVsIiwiYSI6ImNrcjJmejlzZjFkd3MyeXM2dGtvYzVlY3UifQ.Z9lBfH4_hmvK_Fz2JXjvfQ')
print(request.text)
json_2 = request.json()
with open('data_maps.json', 'w') as f:
  json.dump(json_2, f)

