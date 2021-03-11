import requests
from bs4 import BeautifulSoup


def scrape_value(url,
        html_class,
        multiplier=1000000000):
    p = requests.get(url)
    soup = BeautifulSoup(p.content,'html.parser')
    r = soup.find_all('span', attrs={'class':html_class})
    return float(r[0].text.replace(',','')) * multiplier

# https://www.frbatlanta.org/cqer/research/gdpnow/archives.aspx
gdp_current_adjustment = 1.084 # Atlanta FRB

gdp = scrape_value(
    'https://fred.stlouisfed.org/series/GDP',
    'series-meta-observation-value')
gdp = gdp * gdp_current_adjustment

tmv = scrape_value(
    'https://markets.ft.com/data/indices/tearsheet/summary?s=W5000FLT:PSE',       'mod-ui-data-list__value')

buffet_indicator = tmv / gdp * 100
print('GDP:',gdp)
print('W5000:',tmv)
print('BI:',buffet_indicator)


