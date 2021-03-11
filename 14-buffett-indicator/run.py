import requests
from bs4 import BeautifulSoup

def get_value(url,html_class,multiplier=1000000000):
    p = requests.get(url)
    soup = BeautifulSoup(p.content,'html.parser')
    r = soup.find_all('span', attrs={"class":html_class})
    return float(r[0].text.replace(',','')) * multiplier


gdp_current_adjustment = 1.084 # Atlanta FR
gdp = get_value('https://fred.stlouisfed.org/series/GDP',
                'series-meta-observation-value')
gdp = gdp * gdp_current_adjustment

w5000 = get_value('https://markets.ft.com/data/indices/tearsheet/summary?s=W5000FLT:PSE',                         'mod-ui-data-list__value')

buffet_indicator = w5000 / gdp
print('GDP:',gdp)
print('W5000:',w5000)
print('BI:',buffet_indicator)


