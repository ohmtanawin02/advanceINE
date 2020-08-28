import requests


r = requests.post('https://restcountries.eu/rest/v2/regionalbloc/asean',auth = ("name", "Thailand"))
print(r)


#print(type(data))

#print(data)
