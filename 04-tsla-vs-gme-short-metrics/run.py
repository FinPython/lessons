import yfinance as yf
tsla = yf.Ticker('TSLA')
tsla_shares_outstanding = int(tsla.info['sharesOutstanding'])
print('shares outstanding',tsla_shares_outstanding)
tsla_shares_short = int(tsla.info['sharesShort'])
print('shares short',tsla_shares_short)
print('shares short / outstanding',tsla_shares_short / tsla_shares_outstanding)
tsla_short_pct_outstanding = float(tsla.info['shortPercentOfFloat'])
print('tsla short pct outstanding',tsla_short_pct_outstanding)
tsla_short_ratio = tsla.info['shortRatio']
print(tsla_short_ratio)

amc = yf.Ticker('AMC')
amc_short_pct_outstanding = float(amc.info['shortPercentOfFloat'])
print('amc short pct outstanding',amc_short_pct_outstanding)

gme = yf.Ticker('GME')
gme_short_pct_outstanding = float(gme.info['shortPercentOfFloat'])
print('gme short pct outstanding',gme_short_pct_outstanding)

