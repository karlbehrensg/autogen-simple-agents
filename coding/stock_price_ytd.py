# filename: stock_price_ytd.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define the ticker symbols
tickers = ['META', 'TSLA']

# Get the current year
current_year = datetime.now().year

# Download the stock data
data = yf.download(tickers, start=f'{current_year}-01-01', end=datetime.now().strftime('%Y-%m-%d'))

# Calculate the YTD gain
ytd_gain = {}
for ticker in tickers:
    ytd_gain[ticker] = (data['Adj Close'][ticker][-1] / data['Adj Close'][ticker][0] - 1) * 100

# Print the YTD gain
for ticker, gain in ytd_gain.items():
    print(f'The YTD gain for {ticker} is {gain:.2f}%')

# Plot the stock price change YTD
data['Adj Close'].plot()
plt.title('Stock Price Change YTD')
plt.ylabel('Price ($)')
plt.grid(True)
plt.savefig('stock_price_ytd.png')