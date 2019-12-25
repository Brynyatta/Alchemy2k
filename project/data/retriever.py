# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
pd.options.mode.chained_assignment = None # Avoid SettingWithCopyWarning warnings
from requests import request
import datetime

PARAMETER_ROSTER = "CLOSE,OPEN,HIGH,LOW,ASK,BID,TURNOVER_TOTAL,TRADES_COUNT,TRADES_COUNT_TOTAL,VWAP"

def retriever_stock(ticker, parameters = PARAMETER_ROSTER, years_of_data = 30):
    ind_date_correspondence = -1
    
    #Unit test:
    if(ticker == "UNSELECTED"):
        print("Error occured in data retriever, ticker is invalid!")
    
    
    # Retrieving the data from Oslo Stock Exchange
    url = "https://www.oslobors.no/ob/servlets/components/graphdata/(" + parameters + ")/DAY/" + ticker + ".OSE?points=9999&stop=2019-12-23&period=" + str(years_of_data) + "years"
    response=request(url=url, method='get')
    content = response.json()
    array_chosen_stock = content['rows'][0]['values']['series']['c1']['data']
    start_of_array = first_full_datapoint(array_chosen_stock, parameters)
    print("The data from " + ticker + " had all variables intact first at index " + str(start_of_array['index']) + " where the following variable(s) became available: ")
    print(*start_of_array['parameters'])
    df_stock = pd.DataFrame(data=array_chosen_stock, columns=['Date'] + parameters.split(','));
    POSIX_to_ISO_datetime(df_stock)
    
    
    url_index = 'https://www.oslobors.no/ob/servlets/components/graphdata/(CLOSE)/DAY/OSEBX.OSE?points=9999&stop=2019-12-23&period=30years'
    response=request(url=url_index, method='get')
    content_index = response.json()    
    array_index = content_index['rows'][0]['values']['series']['c1']['data']
    df_index = pd.DataFrame(data=array_index, columns=['Date','CLOSE']);
    POSIX_to_ISO_datetime(df_index)

    
    
    for i in range(0,len(df_index.Date)):
        if (df_stock.Date[0] == df_index.Date[i]):
            ind_date_correspondence = i
            break
    
    if ind_date_correspondence != -1:
        df_index = df_index.drop(df_index.index[:ind_date_correspondence])
    else: 
        print("Error occured, no date correspondence was found between index and selected stock!")
    
    #What is in DF, but not in DF_index?
    delete = df_stock.Date[-df_stock.Date.isin(df_index.Date)]
        
    #What is in DF_index, but not in DF?
    delete2 = df_index.Date[-df_index.Date.isin(df_stock.Date)]
        
    # Remove entries from DF that are in DF but not in DF_index
    if len(delete) != 0:
        for i in range(0,len(delete)):
            try:
                df_stock = df_stock.drop([delete.index[i]])   
            except ValueError: 
                print("Delete: Could not find date scheduled for deletion: [date index] ", delete[delete.index[i]], i)

    print('h')
    # Remove entries from DF_index that are in DF_index but not in DF
    if len(delete2) != 0:
        for i in range(0,len(delete2)):
            try:
                df_index = df_index.drop([delete2.index[i]])
            except KeyError or ValueError: 
                print("Delete2: Could not find date scheduled for deletion: [date index] ", delete2[delete2.index[i]], i)
            
    # Rearrange indexnumbers
    df_stock = df_stock.reset_index(drop=True)
    df_index = df_index.reset_index(drop=True)
    
    
    return df_stock, df_index

def retriever_ticker_list():
    name = []; paper_ticker = []
    url = 'https://www.oslobors.no/ob/servlets/components?type=table&generators%5B0%5D%5Bsource%5D=feed.ob.quotes.EQUITIES%2BPCC&generators%5B1%5D%5Bsource%5D=feed.merk.quotes.EQUITIES%2BPCC&filter=&view=DELAYED&columns=PERIOD%2C+INSTRUMENT_TYPE%2C+TRADE_TIME%2C+ITEM_SECTOR%2C+ITEM%2C+LONG_NAME%2C+BID%2C+ASK%2C+LASTNZ_DIV%2C+CLOSE_LAST_TRADED%2C+CHANGE_PCT_SLACK%2C+TURNOVER_TOTAL%2C+TRADES_COUNT_TOTAL%2C+MARKET_CAP%2C+HAS_LIQUIDITY_PROVIDER%2C+PERIOD%2C+MIC%2C+GICS_CODE_LEVEL_1%2C+TIME%2C+VOLUME_TOTAL'
    response=request(url=url, method='get')
    
    for ticker in response.json()['rows']:
        name.append(ticker['values']['LONG_NAME'])
        paper_ticker.append(ticker['values']['ITEM'])
    dataframe_tickers = pd.DataFrame(data=[name,paper_ticker]).T
    dataframe_tickers.rename(columns={0: "name", 1: "paper"},inplace=True)
    return dataframe_tickers

# Modifies the date column from POSIX timestamps to ISO standard dates, call by reference
def POSIX_to_ISO_datetime(df):
    for i in range(0, len(df)):
        POSIX_timestamp = str(df['Date'][i])
        df['Date'][i] = datetime.datetime.fromtimestamp(int(POSIX_timestamp[0:-3])).strftime('%Y-%m-%d')

# Returns the first datapoint in the array that is full, i.e. contains valid data
def first_full_datapoint(array, parameters):
    full_datapoint = {}
    parameters = parameters.split(',')
    
    for i in range(0,len(array)):
        if None in array[i]:
            continue
        else:
            full_datapoint['index'] = i
            full_datapoint['parameters'] = []
            for j in range(0,len(array[i-1])): # What parameters were recently filled / ended being empty?
                if array[i-1][j] == None:
                    full_datapoint['parameters'].append(parameters[j-1])
            return full_datapoint