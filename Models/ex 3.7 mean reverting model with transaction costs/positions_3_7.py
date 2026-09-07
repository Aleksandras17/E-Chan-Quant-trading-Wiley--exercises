import yfinance as yf 
import pandas as pd

def validity(close_price):
    validity_matrix = (close_price>=5) & (close_price<=2000)
    return(validity_matrix)

def strategy(daily_return, validity_matrix, exposure=1):
    stock_num = validity_matrix.sum(axis=1)
    mean_return = (daily_return*validity_matrix).sum(axis=1)/stock_num
    weights = -(daily_return.sub(mean_return, axis=0)).div(stock_num, axis=0) * validity_matrix

    #Normalize weights for 100% gross exposure 

    gross_exposure = weights.abs().sum(axis=1)
    weights=weights.mul(exposure/gross_exposure, axis = 0)
    #Now the weights on day t are calculatedf using the return from t-1 to t, since i want these weights to be applied for the period t to t+1, I need to shift them by one.
    return weights.shift(1).fillna(0)



start_date = '2005-01-01'
end_date = '2006-12-31'





close_price = pd.read_csv('SPX_20071123.txt', sep='\t', header = 0, index_col=0)
close_price.index = pd.to_datetime(close_price.index, format = "%Y%m%d")

open_price = pd.read_csv('SPX_op_20071123.txt', sep='\t', header = 0, index_col = 0)
open_price.index = pd.to_datetime(open_price.index, format = "%Y%m%d")

close_price = close_price.loc[start_date:end_date]
open_price = open_price.loc[start_date:end_date]




close_price.to_csv("close.csv")
open_price.to_csv("open.csv")



close_return = close_price.pct_change()
val_matrix = validity(close_price)
weights = strategy(close_return, val_matrix)

val_matrix.to_csv("validity.csv")

weights.to_csv("positions.csv")