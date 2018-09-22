import tulipy as ti
import numpy as np
import pandas as pd

# a recursive funciton that computes market indicators and pushes to the appropriate table 
# it perfroms the operation on one symbol at a  time. see symbol = 0 in arguments
def indicators(symbol=0,time_frame='5m', time = _5m):
    # 2 = High, 3 = Low, 4 = Close, 5 = Volume
    #collects the needed market data into one list to push to the indicators
    close = np.array([time[symbol][df][4] for df in range(len(time[symbol]))])
    close = close.astype(np.float64)
    high = np.array([time[symbol][df][2] for df in range(len(time[symbol]))])
    high = high.astype(np.float64)
    low = np.array([time[symbol][df][3] for df in range(len(time[symbol]))])
    low = low.astype(np.float64)
    #!!!This needs to be changed. Each volume of the base time must be indexed up to the slice
    volume = np.array([time[symbol][df][5] for df in range(len(time[symbol]))])
    volume = volume.astype(np.float64)
    #these are the indicators currently being used, and recored
    Indicators ={'stochrsi' : ti.stochrsi(close, 5),
                 'rsi' : ti.rsi(close, 5),
                 #indicators that need to be doublechecked
                 'mfi' : ti.mfi(high, low, close, volume, 5),
                 'psar' : ti.psar(high, low, .2, 2),
                 'cci' : ti.cci(high, low, close, 5),
                 'ema' : ti.ema(close, 5)
                 }
#this one is good
    stoch_k, stoch_d = ti.stoch(high, low, close, 5, 3, 3)

    # check on this, to see if it functions properly
    bbands_lower, bbands_middle, bbands_upper = ti.bbands(close, 5, 2)
    macd, macd_signal, macd_histogram = ti.macd(close, 12, 26, 9)

    Indicators['stoch_k'] = stoch_k
    Indicators['stoch_d'] = stoch_d

    Indicators['macd'] = macd
    Indicators['macd_histogram']= macd_histogram
    Indicators['macd_signal']= macd_signal

    Indicators['bbands_upper']= bbands_upper
    Indicators['bbands_middle']= bbands_middle
    Indicators['bbands_lower']= bbands_lower
    
    #below changes the length of each array to match the longest one, for a pandas df
    #np.nan for the tail of the shorter ones
    b=[]
    for i in Indicators:
        b.append(len(Indicators[i]))
    b= max(b)

    for i in Indicators:
        if len(Indicators[i]) < b:
            a= b - len(Indicators[i]) 
            Indicators[i] = np.append(Indicators[i], [np.nan]*a)
    
    Indicators = pd.DataFrame(Indicators)

#Below calls the function that pushes all the indicators to the time frames table
    if time_frame == '5m':
        _5m_()
    elif time_frame == '10m':
        _10m_()
    elif time_frame == '15m':
        _15m_()
    elif time_frame == '30m':
        _30m_()
    elif time_frame == '1h':
        _1h_()
    elif time_frame == '2h':
        _2h_()
    elif time_frame == '4h':
        _4h_()
    elif time_frame == '6h':
        _6h_()
    elif time_frame == '12h':
        _12h_()

    symbol = symbol + 1
    if symbol < len(klines):
        indicators(symbol=symbol,time_frame = time_frame, time=time)
    else:
#returns indicators for attatchment to live trading
        return Indicators

