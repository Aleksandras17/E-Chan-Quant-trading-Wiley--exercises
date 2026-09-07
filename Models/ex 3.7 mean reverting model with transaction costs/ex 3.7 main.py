import sys 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sys.path.append("C:/Users/alex/Documents/quant book")

from run_backtest import run_backtest

start_date = '2006-01-01'
end_date = '2006-12-31'

#The main issue with previous data sets was that out of almost 7000 stocks, only 400 existed in 2006
#Using the data gathered from E. Chans files

close = pd.read_csv("close.csv", index_col=0)





positions = pd.read_csv("positions.csv", index_col = 0).loc[start_date:end_date]





p_and_l = run_backtest(close, positions, apply_t_costs = True)
sharpe = 252**0.5 * (p_and_l.mean()/p_and_l.std())
print(sharpe)

percentage_return = (p_and_l+1).cumprod()-1
percentage_return.plot()


plt.show()