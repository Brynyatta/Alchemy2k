# Alchemy2k

A very crude version of a trading aid that predicts stock movement, and lets you simulate using different strategies by backtesting. Still a huge work in progress!


Composed of the following modules:

main.py - You want to run this file first, which handles the graphical user interface. 

data_retriever.py - Downloads ticker list and financial data for the selected stock, from Netfonds. Scrubs the data and ensures that the datapoints of the stock and the index of the exchange have common dates. 

data_extender.py - Derives useful financial metrics from the raw data extracted by data_retriever using the 'talib' Python library. Produces values for RSI, standard deviation, Williams %R and so forth.  

predictor.py - 3-layer neural network that predicts the next day movement of the stock. Prediction output for stock movement is either -1 (downwards), 0 (sideways) or 1 (upwards). 

account.py - Class to keep track of the cash reserve and stock assets of the hypothetical broker account. 

investment_manager.py - Acts as the stock exchange, keeps track of completed trades. 

account_plotter.py - Plotly tool for showing the evolution of the hypothetical broker account 

timeseries_plotter.py - Plotly tool for showing the evolution of the underlying stock price 
