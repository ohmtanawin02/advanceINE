import requests

response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/asean?fields=name')

data = response.json()


print(type(data))

print(data)
