import yfinance as yf
import matplotlib.pyplot as plt

zm = yf.Ticker('ZM')
zm_options = zm.option_chain('2021-02-19')
df_zm_calls = zm_options.calls

plt.plot(df_zm_calls['strike'],df_zm_calls['impliedVolatility'])
plt.show()

df_zm_puts = zm_options.puts
plt.plot(df_zm_puts['strike'],df_zm_puts['impliedVolatility'])
plt.show()