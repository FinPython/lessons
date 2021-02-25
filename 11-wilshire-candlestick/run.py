import pandas as pd
import mplfinance as mpf

df = pd.read_csv('data/wilshire5000tmc.csv',index_col=0,parse_dates=True)
df.index.name = 'Date'
# Rename Price column to Close
df = df.rename(columns={'Price':'Close'})

# Remove all commas in numbers
df = df.replace(',','',regex=True)

# Convert string to float
for n in ['Open','High','Low','Close']: 
    df[n] = df[n].astype(float)

mpf.plot(df,type='candle',mav=5)