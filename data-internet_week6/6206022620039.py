import requests

payload = {"population": "65327652"}
response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/asean',params=payload)
print(response.text)
#data = response.json()


#print(type(data))

#print(data)
