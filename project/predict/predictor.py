# -*- coding: utf-8 -*-

#Created on Wed May 30 19:09:44 2018
#https://www.quantinsti.com/blog/artificial-neural-network-python-using-keras-predicting-stock-price-movement/
#@author: Eier

import numpy as np
import random 
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

def movement_prediction(df_ticker):
    random.seed(42)
    
    # Ask user for ticker input (case-sensitive)
    
    
    X = df_ticker.iloc[:, 3:-2]
    y = df_ticker.iloc[:, -1] #-1
    
    #We then create two data frames storing the input and the output variables. The dataframe ‘X’ stores the input features, the columns starting from the fifth column (or index 4) of the dataset till the second last column. The last column will be stored in the dataframe y, which is the value we want to predict, i.e. the price rise.
    
    split = int(len(df_ticker)*0.8)
    X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]
    
    # Feature Scaling
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    
    classifier = Sequential()
    
    # 2
    
    model = Sequential()
    classifier.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu', input_dim = X.shape[1]))
    classifier.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])
    classifier.fit(X_train, y_train, batch_size = 32, epochs = 100)
    
    y_pred = classifier.predict_classes(X_test)
    #y_pred = (y_pred > 0.5)
    
    df_ticker['y_pred'] = np.NaN
    df_ticker.iloc[(len(df_ticker) - len(y_pred)):,-1:] = y_pred
    trade_dataset = df_ticker.dropna()
    
    classifier.summary()
    
    return trade_dataset