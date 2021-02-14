import requests as r
import pandas as pd
import json

defi_market_cap = json.loads(r.get('https://api.coingecko.com/api/v3/global/decentralized_finance_defi').text)['data']
print(defi_market_cap['defi_market_cap'])
