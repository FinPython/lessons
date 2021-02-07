import yfinance as yf
import matplotlib.pyplot as plt

gamestop_series = yf.download('GME','2020-10-01','2021-02-05')
gamestop_series['Adj Close'].plot()
plt.show()