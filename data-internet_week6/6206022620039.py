import requests

parameter = {"name":"Thailand"}
response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/asean?fields=name;population;area',params=parameter)

data = response.json()


print(type(data))

print(data)
