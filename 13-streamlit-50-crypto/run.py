import streamlit as st
import pandas_datareader.data as web
from datetime import datetime as dt, timedelta as td

st.title('FinPython Crypto Tracker')
opts = st.selectbox('Select Pair', 
    ('BTC-USD', 'ETH-USD', 'BNB-USD','XRP-USD','LINK-USD','DOGE-USD','EOS-USD','BSV-USD'))
prices = web.get_data_yahoo(opts, start=dt.now() - td(days=365), end=dt.now())
st.line_chart(prices)