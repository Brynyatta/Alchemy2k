# -*- coding: utf-8 -*-
import pandas as pd
import numpy
import account

def strategies(trade_dataset,strats):
    
    ## Settings
    init_funds = 10000
    increments = 2000
    hold_as_baseline_case = 1 # Whether to show holding the stocks from start data until now
    ind_start = trade_dataset.index[0]
    ind_end = trade_dataset.index[-1]
    fund_evolution = [init_funds]
    
    # BUYING AT START AND HOLDING UNTIL NOW
    # Baseline Case
    if (hold_as_baseline_case == 1):
        fund_evolution = [init_funds]
        strat = account.trader(['HOLD'],init_funds)
        fund_evolution = numpy.zeros(ind_end-ind_start+1)
        fund_evolution[0] = init_funds
        investment = strat.invest(init_funds)
        shares_bought = (investment/trade_dataset.CLOSE[ind_start])
        
        profit = (trade_dataset.CLOSE[ind_end]-trade_dataset.CLOSE[ind_start])*shares_bought
        fund_evolution[-1] = (profit+investment)
        spacing = (fund_evolution[-1] - fund_evolution[0])/(ind_end-ind_start)
        for j in range(1,ind_end-ind_start):
            fund_evolution[j] = init_funds + j*spacing
        stratDF1 = pd.DataFrame({"quote_date": trade_dataset.Date, "Balance": fund_evolution})
        results = pd.DataFrame({"Data": [[stratDF1]],"Strategy": ["Buy & Hold"]})

    # STRATEGY 1 
    #1 Day, Shorting Allowed
    if int(strats[0]) == 1:
        fund_evolution = [init_funds]
        strat1 = account.trader(['1 Day, Shorting Allowed'],init_funds)
        for i in range(ind_start,ind_end):
            if trade_dataset.Pred_Down[i] == 1:
                investment = strat1.invest(increments)
                shares_bought = (investment/trade_dataset.CLOSE[i])
                profit = (trade_dataset.CLOSE[i]-trade_dataset.CLOSE[i+1])*shares_bought
                strat1.profit(profit+investment)
                fund_evolution.append(strat1.balance)
            elif trade_dataset.Pred_Sideways[i] == 1:
                investment = strat1.invest(0)
                fund_evolution.append(strat1.balance)
            elif trade_dataset.Pred_Up[i] == 1:
                investment = strat1.invest(increments)
                shares_bought = (investment/trade_dataset.CLOSE[i])
                profit = (trade_dataset.CLOSE[i+1]-trade_dataset.CLOSE[i])*shares_bought
                strat1.profit(profit+investment)
                fund_evolution.append(strat1.balance)
        stratDF2 = pd.DataFrame({"quote_date": trade_dataset.Date, "Balance": fund_evolution})
        data2 = pd.DataFrame({"Data": [[stratDF2]],"Strategy": ["1 Day, Shorting Allowed"]})
        results = results.append(data2, ignore_index=True)

    # STRATEGY 2
    #1 Day, Shorting NOT Allowed
    if int(strats[1]) == 1:
        fund_evolution = [init_funds]
        strat2 = account.trader(['1 Day, Shorting NOT Allowed'],init_funds)
        for j in range(ind_start,ind_end):
            if trade_dataset.Pred_Sideways[j] == 1:
                investment = strat2.invest(0)
                fund_evolution.append(strat2.balance)
            elif trade_dataset.Pred_Down[j] == 1 :
                investment = strat2.invest(0)
                fund_evolution.append(strat2.balance)
            elif trade_dataset.Pred_Up[j] == 1:
                investment = strat2.invest(increments)
                shares_bought = (investment/trade_dataset.CLOSE[j])
                profit = (trade_dataset.CLOSE[j+1]-trade_dataset.CLOSE[j])*shares_bought
                strat2.profit(profit+investment)
                fund_evolution.append(strat2.balance)
        stratDF3 = pd.DataFrame({"quote_date": trade_dataset.Date, "Balance": fund_evolution})
        data3 = pd.DataFrame({"Data": [[stratDF3]],"Strategy": ["1 Day, Shorting NOT Allowed"]})
        results = results.append(data3, ignore_index=True)
        
    # STRATEGY 3
    # if int(strats[2]) == 1:
        
    return results;

