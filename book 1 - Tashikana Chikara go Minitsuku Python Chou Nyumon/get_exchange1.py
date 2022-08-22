import requests
from datetime import datetime
today = datetime.now().strftime('%Y年%m月%d日')
api_url='http://api.coingecko.com/api/v3/exchange_rates'
ex_data=requests.get(api_url).json()
print(today + " $" + str(ex_data['rates']['btc']['value']) + " 的" + ex_data['rates']['btc']['name'] + '可兌換 NT$' + str(ex_data['rates']['twd']['value']))