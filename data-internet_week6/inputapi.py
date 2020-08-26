import requests
response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
exchange_rates = eval(response.text)["rates"]
print(response.text)
cash = int(input("Money"))
money = (input("Currency"))
money_afterchange = exchange_rates[money] * cash
print(money_afterchange)