# -*- coding: utf-8 -*-

#Created on Wed May 30 19:09:44 2018
#https://www.quantinsti.com/blog/artificial-neural-network-python-using-keras-predicting-stock-price-movement/
#@author: Eier

import numpy as np
import random 
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

def movement_prediction(df_ticker):
    random.seed(42)
    
    
    X = df_ticker.iloc[:, 1:-5] #X = df_ticker.iloc[:, 3:-5] to exclude closing dif & std. closing dif
    y = df_ticker.iloc[:, -3:] 
    
    #We then create two data frames storing the input and the output variables. The dataframe ‘X’ stores the input features, the columns starting from the fifth column (or index 4) of the dataset till the second last column. The last column will be stored in the dataframe y, which is the value we want to predict, i.e. the price rise.
    
    split = int(len(df_ticker)*0.8)
    X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]
    
    # Feature Scaling
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    
    model = Sequential()
    
    model.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu', input_dim = X.shape[1]))
    model.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
    model.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
    model.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
    model.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
    model.add(Dense(3, activation = 'softmax'))
    
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    model.fit(X_train, y_train, batch_size = 32, epochs = 200)
    
    y_pred = model.predict_classes(X_test)
    
    df_ticker['pred_up'] = np.NaN
    df_ticker['pred_sideways'] = np.NaN
    df_ticker['pred_down'] = np.NaN

    y_pred_OneHot = np_utils.to_categorical(y_pred, num_classes = 3)
    df_ticker.iloc[(len(df_ticker) - len(y_pred)):,-3:] = y_pred_OneHot
    trade_dataset = df_ticker.dropna()
    
    model.summary()
    
    return trade_dataset