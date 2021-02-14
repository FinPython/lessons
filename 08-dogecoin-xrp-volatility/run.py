import pandas as pd
import matplotlib.pyplot as plt

# base url
url = 'https://query1.finance.yahoo.com/v7/finance/download/{asset}?period1=1581614915&period2=1613237315&interval=1d&events=history&includeAdjustedClose=true'

# pull feed
df_doge = pd.read_csv(url.format(asset='DOGE-USD'))
df_xrp = pd.read_csv(url.format(asset='XRP-USD'))

# show size of each df (rows, columns)
print('-- shapes')
print('doge shape',df_doge.shape)
print('xrp shape',df_xrp.shape)

# show rows with nulls prices
print('-- rows with null prices')
print(df_doge[df_doge['Open'].isna()])
print(df_xrp[df_doge['Open'].isna()])

# remove rows null prices
df_doge = df_doge.dropna(axis=0, subset=['Open'])
df_xrp = df_xrp.dropna(axis=0, subset=['Open'])

# show size of each df (rows, columns)
print('doge shape after scrub',df_doge.shape)
print('xrp shape after scrub',df_xrp.shape)

# calc rolling 30 day standard deviation
df_doge['Rolling 30 Vol'] = df_doge['Open'].rolling(30).std()
df_xrp['Rolling 30 Vol'] = df_xrp['Open'].rolling(30).std()

# plot both series
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(df_doge['Date'],df_doge['Rolling 30 Vol'],'y-')
ax2.plot(df_xrp['Date'],df_xrp['Rolling 30 Vol'],'b-')

plt.title('DOGE & XRP 30 day rolling vol')
plt.grid(True)
plt.legend(loc=2)
ax1.set_xlabel('Time->')

ax1.set_ylabel('DOGE',color='y')
ax2.set_ylabel('XRP',color='b')
plt.show()