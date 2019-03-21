# -*- coding: utf-8 -*-

#Created on Wed May 30 19:09:44 2018
#https://www.quantinsti.com/blog/artificial-neural-network-python-using-keras-predicting-stock-price-movement/
#@author: Eier

import numpy as np
import random 
from strategies import strategies
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from data_retriever import data_retriever
from data_extender import data_extender
from timeseries_plotter import timeseries_plotter
from account_plotter import account_plotter



def predict(ticker, strats):
    random.seed(42)
    
    # Ask user for ticker input (case-sensitive)
    
    df, df_index = data_retriever(ticker)
    df = data_extender(df)
    
    X = df.iloc[:, 3:-2]
    y = df.iloc[:, -1] #-1
    
    #We then create two data frames storing the input and the output variables. The dataframe ‘X’ stores the input features, the columns starting from the fifth column (or index 4) of the dataset till the second last column. The last column will be stored in the dataframe y, which is the value we want to predict, i.e. the price rise.
    
    split = int(len(df)*0.8)
    X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]
    
    # Feature Scaling
    
    succ = StandardScaler()
    X_train = succ.fit_transform(X_train)
    X_test = succ.transform(X_test)
    
    
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
    
    df['y_pred'] = np.NaN
    df.iloc[(len(df) - len(y_pred)):,-1:] = y_pred
    trade_dataset = df.dropna()
    
    classifier.summary()
    
    
    ## Evaluate the performance of the strategy
    results = strategies(trade_dataset,strats)
    timeseries_plotter(df)
    account_plotter(results)
    return 0;