# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:07:14 2018

@author: Eier
"""
import plotly


def account(results, ticker):
    
    strategynames = results.Strategy[:]
    num_strategies = results.shape[0]
    
    funds1 = plotly.graph_objs.Scatter(
        x=results.Data[0][0].quote_date,
        y=results.Data[0][0].Balance,
        name = strategynames[0],
        line = dict(color = '#17BECF'),
        opacity = 0.5)
    data = [funds1]
    
    if(num_strategies > 1): 
        funds2 = plotly.graph_objs.Scatter(
            x=results.Data[1][0].quote_date,
            y=results.Data[1][0].Balance,
            name = strategynames[1],
            line = dict(color = '#3300ff'),
            opacity = 0.5)
        data.append(funds2)
        
    if(num_strategies > 2): 
        funds3 = plotly.graph_objs.Scatter(
        x=results.Data[2][0].quote_date,
        y=results.Data[2][0].Balance,
        name = strategynames[2],
        line = dict(color = '#000000'),
        opacity = 0.5)
        data.append(funds3)
    
    layout = dict(
        title={"text":'Evolution of different strategies for ' + ticker,
        'y':0.995,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},               
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(),
            type='date'
        )
    )
    
    plotly.offline.plot({
    "data": data,
        "layout": layout,
    },filename='strats.html')
    return;