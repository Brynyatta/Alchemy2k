# -*- coding: utf-8 -*-

import plotly


def cumulativereturns(df, results, ticker):
    strategynames = results.Strategy[:]
    num_strategies = results.shape[0]
    
    # Find the cumulative returns of the stock itself
    df['Cumulative_Return'] = 0.0;
    ind_start = df.index[0]
    ind_end = df.index[-1]
    for i in range(ind_start+1, ind_end+1):
         df.set_value(i, 'Cumulative_Return', ((df.CLOSE[i]-df.CLOSE[ind_start])/df.CLOSE[ind_start]))
    
    Cumulative_Return_Stock = plotly.graph_objs.Scatter(
        x=df.Date,
        y=df['Cumulative_Return'],
        name = ticker + " Cumulative Returns",
        line = dict(color = '#17BECF'),
        opacity = 0.3)

    data = [Cumulative_Return_Stock]

    # Find the cumulative returns of the strategies
    results['Cumulative_Return_Start1'] = 0.0;
    if(num_strategies > 1): 
        results['Cumulative_Return_Start2'] = 0.0;
    if(num_strategies > 2):
        results['Cumulative_Return_Start3'] = 0.0;
    ind_start = results.Data[1][0].Balance.index[0]
    ind_end = results.Data[1][0].Balance.index[-1]
    for i in range(ind_start+1, ind_end+1):
         results.set_value(i, 'Cumulative_Return_Start1', ((results.Data[0][0].Balance[i]-results.Data[0][0].Balance[ind_start])/results.Data[0][0].Balance[ind_start]))
         if(num_strategies > 1): 
             results.set_value(i, 'Cumulative_Return_Start2', ((results.Data[1][0].Balance[i]-results.Data[1][0].Balance[ind_start])/results.Data[1][0].Balance[ind_start]))
         if(num_strategies > 2): 
             results.set_value(i, 'Cumulative_Return_Start3', ((results.Data[2][0].Balance[i]-results.Data[2][0].Balance[ind_start])/results.Data[2][0].Balance[ind_start]))

#    cumret_start1 = plotly.graph_objs.Scatter(
#    x=results.Data[0][0].quote_date,
#    y=results.Cumulative_Return_Start1,
#    name = strategynames[0],
#    line = dict(color = '#17BECF'),
#    opacity = 0.5)
#    data.append(cumret_start1)
    
    if(num_strategies > 1): 
        cumret_start2 = plotly.graph_objs.Scatter(
        x=results.Data[1][0].quote_date,
        y=results.Cumulative_Return_Start2,
        name = strategynames[1],
        line = dict(color = '#3300ff'),
        opacity = 0.5)
        data.append(cumret_start2)
        
    if(num_strategies > 2): 
        cumret_start3 = plotly.graph_objs.Scatter(
        x=results.Data[2][0].quote_date,
        y=results.Cumulative_Return_Start3,
        name = strategynames[2],
        line = dict(color = '#000000'),
        opacity = 0.5)
        data.append(cumret_start3)
    
    
    layout = dict(
        title='Cumlative returns of ' + ticker + ' under different strategies',
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
    },filename='cumulativereturns.html')
    return;