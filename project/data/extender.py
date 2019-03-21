import numpy as np
import pandas as pd
import talib


def extender(df):
    df['H-L'] = df['high'] - df['low']
    df['O-C'] = df['close'] - df['open']
    df['3day MA'] = df['close'].shift(1).rolling(window = 3).mean()
    df['10day MA'] = df['close'].shift(1).rolling(window = 10).mean()
    df['30day MA'] = df['close'].shift(1).rolling(window = 30).mean()
    df['Std_dev_closing']= df['close'].rolling(5).std()
    df['RSI'] = talib.RSI(df['close'].values, timeperiod = 9)
    df['Williams %R'] = talib.WILLR(df['high'].values, df['low'].values, df['close'].values, 7)
    #df['positive_movement'] = np.where(df['close'].shift(-1) > df['close'], 1, 0)
    df['Closing Difference'] = (df['close'].shift(-1)- df['close'])
    df['Std_dev_close_diff']= df['Closing Difference'].rolling(5).std()
    df['Movement'] = "NaN"
    # 1 = UP , 0 = SIDEWAYS , -1 = DOWN
    for i in range(0,len(df)-1):
        if (abs(df['Closing Difference'].iloc[i]) > df['Std_dev_close_diff'].iloc[i]) and (df['Closing Difference'].iloc[i] > 0):
            df.set_value(i, 'Movement', 1)
        elif (abs(df['Closing Difference'].iloc[i]) > df['Std_dev_close_diff'].iloc[i])  and (df['Closing Difference'].iloc[i] < 0):
            df.set_value(i, 'Movement', -1)
        else: 
            df.set_value(i, 'Movement', 0)
    df = df.dropna()

    return df;