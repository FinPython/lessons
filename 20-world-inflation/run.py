import requests, json
from datetime import datetime
import matplotlib.pyplot as plt

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0'],"startyear":"2010", "endyear":"2022"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
print(p.text)
json_data = json.loads(p.text)['Results']['series'][0]['data']
x = []; y = []
print(json_data)
for i in json_data:
    s = str(i['periodName']) + ', ' + i['year']
    d = datetime.strptime(s, '%B, %Y')
    x.append(d)
    y.append(i['value'])
x.reverse(); y.reverse()

fig, ax = plt.subplots()
plt.style.use('seaborn-whitegrid')
plt.yticks(fontsize=8)
ax.plot(x, y, linewidth=2.0)
plt.show()
