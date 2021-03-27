#!pip install pyfolio
import pyfolio as pf
import pandas as pd
import pandas_datareader as web

snow = web.get_data_yahoo('SNOW',start='2020-03-26',end='2021-03-27')
snow['% Returns'] = snow['Adj Close'].pct_change()
pf.create_simple_tear_sheet(snow['% Returns'])