import pandas as pd
import requests as r

url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-02-15&currency={}'

resp_USD = r.get(url.format('USD')).text
resp_CNY = r.get(url.format('CNY')).text
resp_IDR = r.get(url.format('IDR')).text


df_USD = pd.read_json(resp_USD)
df_IDR = pd.read_json(resp_IDR)
df_CNY = pd.read_json(resp_CNY)


df_global = pd.DataFrame()
df_global['USD'] = df_USD['bpi']
df_global['IDR'] = df_IDR['bpi']
df_global['CNY'] = df_CNY['bpi']

df_global = df_global.drop(df_global.tail(2).index)
print(df_global)