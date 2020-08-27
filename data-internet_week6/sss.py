import requests

url = 'https://restcountries.eu/rest/v2/regionalbloc/asean'
myobj = {'name':'Myanmar'}

x = requests.post(url, data = myobj)

#print the response text (the content of the requested file):

print(x.text)