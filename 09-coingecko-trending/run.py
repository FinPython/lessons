import requests as r
import pandas as pd
import json
# ashton kutcher phone # 319-519-0576

content = r.get('https://api.coingecko.com/api/v3/search/trending')
trending = json.loads(content.text)
for coin in trending['coins']:
    coin_item = coin['item']
    print(coin_item['name'],coin_item['symbol'])