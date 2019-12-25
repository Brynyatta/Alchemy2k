import numpy as np
import pandas as pd
import talib


def extender(df):
    df['Non_pubic_trades'] =  df['TRADES_COUNT_TOTAL'] - df['TRADES_COUNT']
    df['H-L'] = df['HIGH'] - df['LOW']
    df['O-C'] = df['CLOSE'] - df['OPEN']
    df['3day MA'] = df['CLOSE'].shift(1).rolling(window = 3).mean()
    df['10day MA'] = df['CLOSE'].shift(1).rolling(window = 10).mean()
    df['30day MA'] = df['CLOSE'].shift(1).rolling(window = 30).mean()
    df['Std_dev_closing']= df['CLOSE'].rolling(5).std()
    df['RSI'] = talib.RSI(df['CLOSE'].values, timeperiod = 9)
    df['Williams %R'] = talib.WILLR(df['HIGH'].values, df['LOW'].values, df['CLOSE'].values, 7)
    #df['positive_movement'] = np.where(df['close'].shift(-1) > df['close'], 1, 0)
    df['Closing Difference'] = (df['CLOSE'].shift(-1)- df['CLOSE'])
    df['Std_dev_close_diff']= df['Closing Difference'].rolling(5).std()

    df['Up'] = "NaN"
    df['Sideways'] = "NaN"
    df['Down'] = "NaN"


    for i in range(0,len(df)-1):
        if (abs(df['Closing Difference'].iloc[i]) > df['Std_dev_close_diff'].iloc[i]) and (df['Closing Difference'].iloc[i] > 0):
            df.set_value(i, 'Up', 1)
            df.set_value(i, 'Sideways', 0)
            df.set_value(i, 'Down', 0)
        elif (abs(df['Closing Difference'].iloc[i]) > df['Std_dev_close_diff'].iloc[i])  and (df['Closing Difference'].iloc[i] < 0):
            df.set_value(i, 'Up', 0)
            df.set_value(i, 'Sideways', 0)
            df.set_value(i, 'Down', 1)
        else: 
            df.set_value(i, 'Up', 0)
            df.set_value(i, 'Sideways', 1)
            df.set_value(i, 'Down', 0)
    
    df = df.dropna()