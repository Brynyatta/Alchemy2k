# Alchemy2k

A very crude version of a trading aid that predicts stock movement, and lets you simulate using different strategies by backtesting. Still a huge work in progress!

_________________
LIBRARIES NEEDED:
talib, PyQt5, pandas, keras, numpy, sklearn, plotly



_________________________________
Composed of the following packages & modules:

__main__.py - You want to run this file first, which handles the graphical user interface. 

data package: 
_____________
retriever.py - Downloads ticker list and financial data for the selected stock, from Netfonds. Scrubs the data and ensures that the datapoints of the    stock and the index of the exchange have common dates. 

extender.py - Derives useful financial metrics from the raw data extracted by data_retriever using the 'talib' Python library. Produces values for RSI, standard deviation, Williams %R and so forth.  

predict package: 
__________
predictor.py - 3-layer neural network that predicts the next day movement of the stock. Prediction output for stock movement is either -1 (downwards), 0 (sideways) or 1 (upwards). 

account package:
________________
broker.py - Class to keep track of the cash reserve and stock assets of the hypothetical broker account. Also acts as the stock exchange, keeps track of completed trades. 

strats package:
_____________
strategies.py - The behaviour of each trading strategy is written here. Communicates with the account package to conduct trades, and stores the profits/losses in a dataframe. 

plotter package: 
_______________
account.py - Plotly tool for showing the evolution of the hypothetical broker account 

timeseries.py - Plotly tool for showing the evolution of the underlying stock price 
