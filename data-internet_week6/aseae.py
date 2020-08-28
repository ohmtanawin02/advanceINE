import requests
get_response = requests.get(url='https://restcountries.eu/rest/v2/regionalbloc/asean')
post_data = {'name':'Thailand', 'name':'Myanmar'}
# POST some form-encoded data:
post_response = requests.post(url='https://restcountries.eu/rest/v2/regionalbloc/asean', data=post_data)
print(post_response.json)