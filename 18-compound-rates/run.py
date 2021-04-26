import requests, json
from prettytable import PrettyTable

url = 'https://api.compound.finance/api/v2/ctoken'
payload = '{ "addresses": [] "block_timestamp":}'
r = requests.post(url,data=payload)
market = json.loads(r.content)['cToken']
comp_table = PrettyTable(['Token','Lend','Borrow'])
for m in market:
    comp_table.add_row([m['underlying_name'],
    float(m['supply_rate']['value']),
    float(m['borrow_rate']['value'])])
print(comp_table)