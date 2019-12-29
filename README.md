# Alchemy2k

A very crude version of a trading aid that predicts stock movement, and lets you simulate using different strategies by backtesting. Still a huge work in progress!

_________________
LIBRARIES NEEDED:
PyQt5, pandas, keras, tensorflow, numpy, sklearn, plotly...
and TA-lib, which is a bitch to find online, and thus included in the dependencies :)
```
pip install Dependencies/TA_Lib-0.4.17-cp37-cp37m-win_amd64.whl
pip install plotly
pip install keras
pip install tensorflow
pip install sklearn
pip install pandas
pip install numpy
pip install PyQt5
```
_________________________________
Composed of the following packages & modules:

__main__.py - You want to run this file first, which contains the backend logic before and after GUI instructions. 
_____________
gui package:
_____________
gui_constructor: The QtPy implementation which handles the graphical user interface. 
_____________
data package: 
_____________
retriever.py - Downloads ticker list and financial data for the selected stock, from Oslo Børs. Scrubs the data and ensures that the datapoints of the stock and the index of the exchange have common dates. 

extender.py - Derives useful financial metrics from the raw data extracted by data_retriever using the 'talib' Python library. Produces values for RSI, standard deviation, Williams %R and so forth.  
_____________
predict package: 
__________
predictor.py - 3-layer neural network that predicts the next day movement of the stock. Prediction output for stock movement for the next day is One-Hot Encoded to three columns: Upwards, Sideways and Downwards. 
_____________
account package:
________________
broker.py - Class to keep track of the cash reserve and stock assets of the hypothetical broker account. Also acts as the stock exchange, keeps track of completed trades. 
_____________
strats package:
_____________
strategies.py - The behaviour of each trading strategy is written here. Communicates with the account package to conduct trades, and stores the profits/losses in a dataframe. 
_____________
plotter package: 
_______________
account.py - Plotly tool for showing the evolution of the hypothetical broker account 

timeseries.py - Plotly tool for showing the evolution of the underlying stock price 


cumulativereturns.py - Plotly tool for cumulative returns for different strategies and the stock itself
