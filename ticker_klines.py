import pandas as pd
import numpy as np
from binance.client import Client
from binance.exceptions import BinanceAPIException

client = Client('api_key', 'secret_key')
api_key = ''
secret_key = ''

#This pulls out all the symbols(a.k.a tickers) from the market
def tickers(volume=0):
    tickers = pd.DataFrame(client.get_ticker())
    # isolates the symbol and volume
    tickers = tickers.loc[:, ['symbol', 'volume']]
    # floats volume
    tickers['volume'] = tickers.loc[:, ['volume']].astype(float)
    #checks through, and only returns the tickers with a higher amount of volume than listed
    tickers = tickers.loc[tickers['volume'] >= volume, 'symbol']
    return tickers

tickers = tickers(volume=150000)

#This pulls out all the market data for the isolated tickers
def test_iterdf(tickers):
    try:
        print('Running 1m')
        #we are only using the 5 min kline window here, because you can access the necessary data --
        #for all other klines with indexing. 
        #!!!except for volume. volume must be summed for that duration of each time frame
        _5m = [pd.DataFrame(client.get_historical_klines(i, client.KLINE_INTERVAL_1HOUR, "10 September, 2018")) for i in tickers]

    except BinanceAPIException as e:
        print(e.status_code)
        print(e.message)

    return _5m

klines = test_iterdf(tickers)
k_len = len(klines)


#Creating a np bool list to compare tickers to null data 
def tick_check():
    mask = np.ones(len(klines), dtype=bool)

    for i in range(len(klines)):
        if klines[i].empty == True:
            mask[[i]] = False
    return mask
mask = tick_check()


#deleting all data frames that are empty
def clean_data():    

    print('running clean_data')
    try:
        list = []
        for i in range(len(klines)):
            if klines[i].empty == True:
                list.append('1')
                del klines[i]
    except:
        print('working on it')
    for i in list:
        if i == '1':
            clean_data()
    symbol = []
    for i in range(len(tickers)):
        #compares tickers to np mask
        #appends the ticker to the symbol list if the data frame had data
        if mask[i] == True:
            symbol.append(tickers.iloc[i])

    return symbol

clean_data()
#this runs clean_data one more time to make sure it cleaned everything
#it also returns symbol as ticker just to keep continuity 
tickers = clean_data()


#Slicing to the different time frames. 
#all the time frame functions to be broken down into one function, and fill a single list to push into change_klines_to_np()
#volume needs to be summed for each frame
_10m=[]        
_15m=[]        
_30m=[]        
_1h=[]        
_2h=[]        
_4h=[]        
_6h=[]        
_12h=[] #144 steps

def get_time_frames():
    for df in range(len(klines)):
        _10m.append(klines[df].iloc[0::2])
        _15m.append(klines[df].iloc[0::3])
        _30m.append(klines[df].iloc[0::6])
        _1h.append(klines[df].iloc[0::12])
        _2h.append(klines[df].iloc[0::24])
        _4h.append(klines[df].iloc[0::48])
        _6h.append(klines[df].iloc[0::72])
        _12h.append(klines[df].iloc[0::144])
    return print('time frames created')


#klines for 5 min window      
#5m = klines
#10m = 2 steps
#15m = 3 steps
#30m = 6 step
#1h = 12 step
#2h = 24 step
#4h = 48 step
#6h = 72 step
#12h = 144 steps

#klines for 1 min window
#_1m = klines
#_5m=  # 5 step
#_10m=  #10 step
#_15m=  #15 step
#_30m=  #30 step
#_1h=  #60 step
#_2h=  #120 step
#_4h=  #240 step
#_6h=  #360 step
#_12h=  #720 step


#changes all the data Frames to np array
def change_klines_to_np(a=0):
    if a < len(klines):
        for i in range(len(klineschange_klines_to_np[a])):
            klines[a][i] = klines[a][i].values
            klines[a][i] = klines[a][i].astype(np.float64)
    else:
#float 64 because that's what tulipy uses. Going to eventually make it so the times and volume stay int
        return print('klines is numpy')

change_klines_to_np()
