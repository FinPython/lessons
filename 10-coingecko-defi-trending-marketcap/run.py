import requests as r
import json
# ashton kutcher phone # 319-519-0576

content = r.get('https://api.coingecko.com/api/v3/search/trending')
trending = json.loads(content.text)
for coin in trending['coins']:
    coin_item = coin['item']
    print(coin_item['name'],coin_item['symbol'])

defi_market_cap = json.loads(r.get('https://api.coingecko.com/api/v3/global/decentralized_finance_defi').text)['data']
print(defi_market_cap['defi_market_cap'])