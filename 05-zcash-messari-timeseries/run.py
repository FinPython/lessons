import requests as r
import json
import matplotlib.pyplot as plt

content = r.get('https://data.messari.io/api/v1/assets/zcash/metrics/price/time-series?start=2021-01-10&end=2021-02-07&interval=1d&columns=open')
values = json.loads(content.text)['data']['values']
x= list(map (lambda v: v[0], values))
y= list(map (lambda v: v[1], values))
plt.title('ZCash')
plt.plot(x,y)
plt.show()