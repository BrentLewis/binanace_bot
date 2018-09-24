import pandas as pd
import numpy as np
from binance.client import Client
from binance.exceptions import BinanceAPIException

client = Client('api_key', 'secret_key')
api_key = ''
secret_key = ''

def tickers():
    tickers = pd.DataFrame(client.get_ticker())
    # isolates the symbol and volume
    tickers = tickers.loc[:, ['symbol', 'volume']]
    # floats volume
    tickers['volume'] = tickers.loc[:, ['volume']].astype(float)
    tickers = tickers.loc[tickers['volume'] >= 150000, 'symbol']
    return tickers

tickers = tickers()

def test_iterdf(tickers):
    try:
        print('Running 1m')
        _5m = [pd.DataFrame(client.get_historical_klines(i, client.KLINE_INTERVAL_1HOUR, "10 September, 2018")) for i in tickers]

    except BinanceAPIException as e:
        print(e.status_code)
        print(e.message)

    return _5m

klines = test_iterdf(tickers)
k_len = len(klines)

def tick_check():
    mask = np.ones(len(klines), dtype=bool)

    for i in range(len(klines)):
        if klines[i].empty == True:
            mask[[i]] = False
    return mask
mask = tick_check()

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
        if mask[i] == True:
            symbol.append(tickers.iloc[i])

    return symbol


clean_data()
tickers = clean_data()


_10m=[]        
def _10m_(df=0):
    if df < len(klines):
        _10m.append(klines[df].iloc[0::2])
        _10m_(df=df+1)
    else:
        print('generated 10min')

_15m=[]        
def _15m_(df=0):
    if df < len(klines):
        _15m.append(klines[df].iloc[0::3])
        _15m_(df=df+1)
    else:
        print('generated 15 min')

_30m=[]        
def _30m_(df=0):
    if df < len(klines):
        _30m.append(klines[df].iloc[0::6])
        _30m_(df=df+1)
    else:
        print('generated 30 min')

_1h=[]        
def _1h_(df=0):
    if df < len(klines):
        _1h.append(klines[df].iloc[0::12])
        _1h_(df=df+1)
    else:
        print('generated 1 hour')
_2h=[]        
def _2h_(df=0):
    if df < len(klines):
        _2h.append(klines[df].iloc[0::24])
        _2h_(df=df+1)
    else:
        print('generated 2 hour')

_4h=[]        
def _4h_(df=0):
    if df < len(klines):
        _4h.append(klines[df].iloc[0::48])
        _4h_(df=df+1)
    else:
        print('generated 4 hour')

_6h=[]        
def _6h_(df=0):
    if df < len(klines):
        _6h.append(klines[df].iloc[0::72])
        _6h_(df=df+1)
    else:
        print('generated 6 hour')

_12h=[] #144 steps
def _12h_(df=0):
    if df < len(klines):
        _12h.append(klines[df].iloc[0::144])
        _12h_(df=df+1)
    else:
        print('generated 12 hour')



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



def change_klines_to_np():
    for i in range(len(klines)):
        klines[i] = klines[i].values
        klines[i] = klines[i].astype(np.float64)

    return print('klines is numpy')

change_klines_to_np()

