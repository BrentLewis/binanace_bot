import tulipy as ti
import numpy as np
import pandas as pd

# This can be used to propegate the databse, but needs to be rewritten for live trading after that
''' a recursive funciton that computes market indicators and pushes to the appropriate table 
 it perfroms the operation on one symbol at a  time. see symbol = 0 in arguments'''


def indicators(time=_5m):
    Indicators={}
    close={}
    time_={}
    for i in range(len(tickers)):

        ''' 2 = High, 3 = Low, 4 = Close, 5 = Volume
        collects the needed market data into one list to push to the indicators'''
        close[tickers[i]] = np.array([time[i][df][4] for df in range(len(time[i]))])
        close[tickers[i]] = close[tickers[i]].astype(np.float64)
        time_[tickers[i]]= np.array([time[i][df][6] for df in range(len(time[i]))])
        time_[tickers[i]] = time_[tickers[i]].astype(np.float64)
        high = np.array([time[i][df][2] for df in range(len(time[i]))])
        high = high.astype(np.float64)
        low = np.array([time[i][df][3] for df in range(len(time[i]))])
        low = low.astype(np.float64)
        # !!!This needs to be changed. Each volume of the base time must be indexed up to the slice
        volume = np.array([time[i][df][5] for df in range(len(time[i]))])
        volume = volume.astype(np.float64)
        # these are the indicators currently being used, and recored
        Indicators[tickers[i]] = {'stochrsi': ti.stochrsi(close[tickers[i]], 5),
                      'rsi': ti.rsi(close[tickers[i]], 5),
                      # indicators that need to be doublechecked
                      'mfi': ti.mfi(high, low, close[tickers[i]], volume, 5),
                      'sar': ti.psar(high, low, .2, 2),
                      'cci': ti.cci(high, low, close[tickers[i]], 5),
                      'ema': ti.ema(close[tickers[i]], 5)
                      }
        # this one is good
        stoch_k, stoch_d = ti.stoch(high, low, close[tickers[i]], 5, 3, 3)

        # check on this, to see if it functions properly
        bbands_lower, bbands_middle, bbands_upper = ti.bbands(close[tickers[i]], 5, 2)
        macd, macd_signal, macd_histogram = ti.macd(close[tickers[i]], 12, 26, 9)

        Indicators[tickers[i]]['stoch_k'] = stoch_k
        Indicators[tickers[i]]['stoch_d'] = stoch_d

        Indicators[tickers[i]]['macd'] = macd
        Indicators[tickers[i]]['macd_histogram'] = macd_histogram
        Indicators[tickers[i]]['macd_signal'] = macd_signal

        Indicators[tickers[i]]['bbands_upper'] = bbands_upper
        Indicators[tickers[i]]['bbands_middle'] = bbands_middle
        Indicators[tickers[i]]['bbands_lower'] = bbands_lower

        # below changes the length of each array to match the longest one, for a pandas df
        # np.nan for the tail of the shorter ones
        b = []
        for x in Indicators[tickers[i]]:
            b.append(len(Indicators[tickers[i]][x]))
        b = max(b)

        for x in Indicators[tickers[i]]:
            if len(Indicators[tickers[i]][x]) < b:
                a = b - len(Indicators[tickers[i]][x])
                Indicators[tickers[i]][x] = np.append(Indicators[tickers[i]][x], [np.nan] * a)
        Indicators[tickers[i]] = pd.DataFrame(Indicators[tickers[i]])
        
    return Indicators

_5m_ind=indicators(time = _5m)
_10m_ind=indicators(time= _10m)
_15m_ind=indicators(time = _15m)
_30m_ind=indicators(time = _30m)
_1h_ind=indicators(time = _1h)
_2h_ind=indicators(time = _2h)
_4h_ind=indicators(time = _4h)
_6h_ind=indicators(time = _6h)
_12h_ind=indicators(time = _12h)

def ind_tables():
    time_frame=['5m','10m','15m',
                '30m','1h','2h',
                '4h','6h','12h']
    for i in time_frame:
        # make this section a seperate method
        # Below calls the function that pushes all the indicators to the time frames table
        if i == '5m':
            _5m_(_5m_ind)
        elif i == '10m':
            _10m_(_10m_ind)
        elif i == '15m':
            _15m_(_15m_ind)
        elif i == '30m':
            _30m_(_30m_ind)
        elif i == '1h':
            _1h_(_1h_ind)
        elif i == '2h':
            _2h_(_2h_ind)
        elif i == '4h':
            _4h_(_4h_ind)
        elif i == '6h':
            _6h_(_6h_ind)
        elif i == '12h':
            _12h_(_12h_ind)
        else:
            return 'Time Frame not recognized'


