import requests

payload = {"name": "Thailand"}
r = requests.post('https://restcountries.eu/rest/v2/regionalbloc/asean',data=payload)
r_dict = r.json()
print(r_dict["name"])
#data = response.json()

#lalala
#print(type(data))

#print(data)
