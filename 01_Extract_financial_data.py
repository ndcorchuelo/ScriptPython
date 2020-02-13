# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 09:26:06 2020

@author: NicolasCorchuelo
"""

import sys
import datetime as dt
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
from pandas import DataFrame
import pyodbc
 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-PVRMLM1\BI;'
                      'Database=Signal_Inversion;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('TRUNCATE TABLE stock.actions_detail ') # Se genera el cursor con el criterio

stocks = ['CIB']

while stocks:
    
    value_stocks = stocks.pop()
    
    print(value_stocks)
    my_share = share.Share(value_stocks)
    symbol_data = None
    
    try:
        symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                              5,
                                              share.FREQUENCY_TYPE_MINUTE,
                                              15)
    except YahooFinanceError as e:
        print(e.message)
        sys.exit(1)
    
    
    df = DataFrame(symbol_data)
        
    df['value_stocks'] = value_stocks
    
    df['timestamp_datetime'] = df.apply(lambda row: dt.datetime.fromtimestamp(row.timestamp / 1e3), axis=1)
        
    cursor = conn.cursor()
    cursor.fast_executemany = True
    for index, row in df.iterrows():
       cursor.execute("INSERT INTO stock.actions_detail ([timestamp],[open],[high],[low],[close],[volume],[value_stocks],[timestamp_datetime]) \
                      values(?,?,?,?,?,?,?,?)", 
                      row['timestamp'], row['open'], row['high'], row['low'], row['close'], row['volume'], row['value_stocks'], row['timestamp_datetime'])
       

conn.commit()
cursor.close()
conn.close()

