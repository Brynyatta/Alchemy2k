# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:07:14 2018

@author: Eier
"""
import plotly


def timeseries(df, ticker):
    
    trace_high = plotly.graph_objs.Scatter(
        x=df.Date,
        y=df['HIGH'],
        name = ticker + " High",
        line = dict(color = '#17BECF'),
        opacity = 0.3)
    
    close = plotly.graph_objs.Scatter(
        x=df.Date,
        y=df['CLOSE'],
        name = ticker + " Closing",
        line = dict(color = '#3300ff'),
        opacity = 0.8)
    
    trace_low = plotly.graph_objs.Scatter(
        x=df.Date,
        y=df['LOW'],
        name = ticker + " Low",
        line = dict(color = '#ff1c63'),
        opacity = 0.3)
    
    data = [trace_high,close,trace_low]
    
    layout = dict(
        title='Time Series of ' + ticker,
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
        "layout": layout
    },filename='timeseries.html')
    return;