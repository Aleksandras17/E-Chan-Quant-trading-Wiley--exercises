import pandas as pd 
import numpy as np

def run_backtest(enter_price, positions, apply_t_costs=False, t_costs = 0.0005):
    enter_price = enter_price.pct_change()
    enter_price = enter_price.loc[positions.index]
    
    p_and_l = (enter_price*positions).sum(axis=1)

    if apply_t_costs == True:
        positions_shift = positions.shift(1)
        positions_shift.iloc[0] = np.zeros(positions.shape[1])
        turnover = (positions-positions_shift).abs()
        costs = turnover.mul(t_costs)
        p_and_l = p_and_l - costs.sum(axis=1) 
    return p_and_l

