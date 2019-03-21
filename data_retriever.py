# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

def data_retriever(ticker):
    ind_date_correspondence = -1
    
    #Unit test:
    if(ticker == "UNSELECTED"):
        print("Error occured in data retriever, ticker is invalid!")
    
    # Retrieving the data from NetFonds
    url = "https://www.netfonds.no/quotes/paperhistory.php?paper=" + ticker + ".OSE&csv_format=csv"
    url_index = "https://www.netfonds.no/quotes/paperhistory.php?paper=OSEBX.OSE&csv_format=csv"
    df = pd.read_csv(url, encoding = "ISO-8859-1")
    df_index = pd.read_csv(url_index, encoding = "ISO-8859-1")
    
    # Reverse the order of the CSV readings
    df = df.reindex(index=df.index[::-1])
    df = df.reset_index(drop=True)
    df_index = df_index.reindex(index=df_index.index[::-1])
    df_index = df_index.reset_index(drop=True)
    
    # Convert date column from int to string
    df['quote_date'] = df['quote_date'].astype(str)
    df_index['quote_date'] = df_index['quote_date'].astype(str)
    
    for i in range(0,len(df_index.quote_date)):
        if (df.quote_date[0] == df_index.quote_date[i]):
            ind_date_correspondence = i
            break
    
    if ind_date_correspondence != -1:
        df_index = df_index.drop(df_index.index[:ind_date_correspondence])
    else: 
        print("Error occured, no date correspondence was found between index and selected stock!")
    
    # Reformat dates to ISO standard
    for i in range(df.index[0],len(df)):
        new_string = str(df.quote_date.iloc[i])[0:4] + "-" + str(df.quote_date.iloc[i])[4:6] + "-" + str(df.quote_date.iloc[i])[6:8]
        df.set_value(i, 'quote_date', new_string)
    for i in range(df_index.index[0],df_index.index[-1]+1):
        new_string2 = str(df_index.quote_date[i])[0:4] + "-" + str(df_index.quote_date[i])[4:6] + "-" + str(df_index.quote_date[i])[6:8]
        df_index.set_value(i, 'quote_date', new_string2)
    
            #What is in DF, but not in DF_index?
    delete = df.quote_date[-df.quote_date.isin(df_index.quote_date)]
        
        #What is in DF_index, but not in DF?
    delete2 = df_index.quote_date[-df_index.quote_date.isin(df.quote_date)]
        
    # Remove entries from DF that are in DF but not in DF_index
    if len(delete) != 0:
        for i in range(0,len(delete)):
            try:
                df = df.drop([delete.index[i]])
                df = df.reset_index(drop=True)    
            except ValueError: 
                print("Delete: Could not find date scheduled for deletion: [date index] ", delete[delete.index[i]], i)

            
    # Remove entries from DF_index that are in DF_index but not in DF
    if len(delete2) != 0:
        for i in range(0,len(delete2)):
            try:
                df_index = df_index.drop([delete2.index[i]])
                df_index = df_index.reset_index(drop=True)
            except ValueError: 
                print("Delete2: Could not find date scheduled for deletion: [date index] ", delete2[delete2.index[i]], i)
            
    # Rearrange indexnumbers
    df = df.reset_index(drop=True)
    df_index = df_index.reset_index(drop=True)
    
    
    return df, df_index

def ticker_list_retriever():
    url = "https://www.netfonds.no/quotes/kurs.php?exchange=OSE&sec_types=&sectors=&ticks=&table=tab&sort=alphabetic"
    dataframe_complete = pd.read_csv(url, encoding = "ISO-8859-1", sep="\t")
    dataframe_tickers = dataframe_complete[['name','paper']]
    return dataframe_tickers
