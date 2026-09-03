import yfinance as yf 
import pandas as pd

def validity(close_price):
    validity_matrix = (close_price>=5) & (close_price<=2000)
    return(validity_matrix)

def strategy(daily_return, validity_matrix):
    stock_num = val_matrix.sum(axis=0)
    mean_return = daily_return.sum(axis=0)/stock_num
    weights = -1/stock_num * (daily_return-mean_return) * validity_matrix

    return weights.fillna(0, inplace=True).shift(-1)



start_date = '2006-01-01'
end_date = '2006-12-31'

# with open("C:/Users/alex/Documents/quant book/Models/ex 3.7 mean reverting model with transaction costs/sp500_400_historical_tickers.txt") as f:
#     ticker_names = [line.strip() for line in f if line.strip()]


# Code that was previously used to load the tickers
# tickers = yf.download(ticker_names, start_date, end_date, auto_adjust=True)
# tickers.to_csv("tickers.csv")

tickers = pd.read_csv("tickers.csv", header=[0,1], index_col = 0)

close_price = tickers["Close"].iloc[1:].dropna(axis=1)
open_price = tickers["Open"].iloc[1:].dropna(axis=1).pct_change()
close_return = close_price.pct_change()

val_matrix = validity(close_price)

weights = strategy(close_return, val_matrix)

print(weights)

weights.to_csv("positions.csv")