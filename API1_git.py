import requests
import codecs
import json

username = input("Enter the github username:")
request = requests.get('https://api.github.com/users/username/repos')
json_1 = request.json()

for i in range(0,len(json_1)):
  print("Project Number:",i+1)
  print("Project Name:",json_1[i]['name'])
  print("Project URL:",json_1[i]['svn_url'],"\n")

with open('data.json', 'w') as f:
  json.dump(json_1, f)
