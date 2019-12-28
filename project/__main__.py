# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:02:50 2018

@author: Eier
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import pyqtSlot, QCoreApplication
import gui
import account
import data
import plotter
import predict
import strat
import sys

# Import homemade functions:

strat1,strat2,strat3 = "1","1","1"
ml_parameters = {'batch_size' : 32, 'epochs' : 200}

# Function runs if "Run Neural Network" button is pressed
def run_algorithm_on_stock(selected_ticker, stratstring):
    # Retrieve data of the index and the selected stock
    df_stock, df_index = data.retriever_stock(selected_ticker)
    
    # Add additional signals based on fundamental parameters of the stock
    data.extender(df_stock) 
    trade_dataset = predict.movement_prediction(df_stock, ml_parameters)

    # Evaluate the performance of the strategy
    trading_results = strat.strategies(trade_dataset,stratstring)
    
    # Plot the results and the timeseries of the stock
    plotter.timeseries(df_stock, selected_ticker)
    plotter.account(trading_results, selected_ticker)
    plotter.cumulativereturns(trade_dataset, trading_results, selected_ticker)

            

if __name__ == '__main__':    
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    # Retrieve the current list of tickers:
    dataframe_tickers = data.retriever_ticker_list()
    ticker_list = dataframe_tickers.to_dict(orient='records')    
    
    ex = gui.gui_constructor.Example(ticker_list)
    sys.exit(app.exec_())