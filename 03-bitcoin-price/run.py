import json, requests as r
content = r.get('https://api.gdax.com/products/btc-usd/book')
price = json.loads(content.text)
bid = float(price['bids'][0][0])
ask = float(price['asks'][0][0])
spread = ask - bid
print(spread)