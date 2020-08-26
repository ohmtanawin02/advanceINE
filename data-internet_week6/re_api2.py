import requests
response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
exchange_rates = eval(response.text)["rates"]
print(response.text)
my_money = 1000
print(exchange_rates["JPY"]*my_money)