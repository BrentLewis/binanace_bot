import talib as tab
import pandas as pd

klines_1 = np.append(klines[a][i], np.array([('first', 10, 11)], dtype= float64))
#Are the numbers coming out right?
def indicators():
    for i in range(len(klines)):
        # 2 = High, 3 = Low, 4 = Close, 5 = Volume
        Indicators = {
            'SMA': pd.DataFrame(tab.SMA(klines[i][df][4], timeperiod=30) for df in range(len(klines[i]))),
            'ROC': pd.DataFrame(tab.ROC(klines[i][df][4], timeperiod=10) for df in range(len(klines[i]))),
            'ROCP': pd.DataFrame(tab.ROCP(klines[i][df][4], timeperiod= 10) for df in range(len(klines[i]))),
            'ROCR': pd.DataFrame(tab.ROCR(klines[i][df][4], timeperiod=10) for df in range(len(klines[i]))),
            'RSI': pd.DataFrame(tab.RSI(klines[i][df][4], timeperiod=14) for df in range(len(klines[i]))),
            'BB': pd.DataFrame(tab.BBANDS(klines[i][df][4],timeperiod= 5, nbdevup=2, nbdevdn=2,matype=0) for df in range(len(klines[i]))),
            'EMA': pd.DataFrame(tab.EMA(klines[i][df][4], timeperiod=30) for df in range(len(klines[i]))),
            'MA': pd.DataFrame(tab.MA(klines[i][df][4],timeperiod=30,matype=0) for df in range(len(klines[i]))),
            'WMA': pd.DataFrame(tab.WMA(klines[i][df][4], timeperiod=30) for df in range(len(klines[i]))),
            'KAMA': pd.DataFrame(tab.KAMA(klines[i][df][4],timeperiod=30) for df in range(len(klines[i]))),
            'MACD': pd.DataFrame(tab.MACD(klines[i][df][4], fastperiod=12, slowperiod=26, signalperiod=9) for df in range(len(klines[i]))),
            'STOCHRSI': pd.DataFrame(tab.STOCHRSI(klines[i][df][4], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0) for df in range(len(klines[i]))),
            'SAR': pd.DataFrame(tab.SAR(klines[i][df][2], klines[i][df][3],acceleration=0, maximum=0) for df in range(len(klines[i]))),
            'ATR': pd.DataFrame(tab.ATR(klines[i][df][2], klines[i][df][3], klines[i][df][4], timeperiod=14) for df in range(len(klines[i]))),
            'NATR': pd.DataFrame(tab.NATR(klines[i][df][2], klines[i][df][3],klines[i][df][4],timeperiod=14) for df in range(len(klines[i]))),
            'CCI':pd.DataFrame(tab.CCI(klines[i][df][2], klines[i][df][3], klines[i][df][4], timeperiod=14) for df in range(len(klines[i]))),
            'W%R':pd.DataFrame(tab.WILLR(klines[i][df][2], klines[i][df][3], klines[i][df][4], timeperiod=14) for df in range(len(klines[i]))),
            'MFI':pd.DataFrame(tab.MFI(klines[i][df][2], klines[i][df][3], klines[i][df][4], klines[i][df][5], timeperiod=14) for df in range(len(klines[i]))),
            'AD':pd.DataFrame(tab.AD(klines[i][df][2], klines[i][df][3], klines[i][df][4], klines[i][df][5]) for df in range(len(klines[i]))),
            'DOSC':pd.DataFrame(tab.ADOSC(klines[i][df][2], klines[i][df][3], klines[i][df][4], klines[i][df][5], fastperiod=3, slowperiod=10) for df in range(len(klines[i])))
                         }
    return Indicators
Indicators = indicators(klines)

#Make recursive??
def Indicators(a=0):
    for i in range(len(klines[a])):
        Indicators= {
                'SMA': pd.DataFrame(tab.SMA(df['Close'], timeperiod=30) for df in klines[i]),
                'ROC': pd.DataFrame(tab.ROC(df['Close'], timeperiod=10) for df in klines[i]),
                'ROCP': pd.DataFrame(tab.ROCP(df['Close'], timeperiod= 10) for df in klines[i]),
                'ROCR': pd.DataFrame(tab.ROCR(df['Close'], timeperiod=10) for df in klines[i]),
                'RSI': pd.DataFrame(tab.RSI(df['Close'], timeperiod=14) for df in klines[i]),
                'BB': pd.DataFrame(tab.BBANDS(df['Close'],timeperiod= 5, nbdevup=2, nbdevdn=2,matype=0) for df in klines[i]),
                'EMA': pd.DataFrame(tab.EMA(df['Close'], timeperiod=30) for df in klines[i]),
                'MA': pd.DataFrame(tab.MA(df['Close'],timeperiod=30,matype=0) for df in klines[i]),
                'WMA': pd.DataFrame(tab.WMA(df['Close'], timeperiod=30) for df in klines[i]),
                'KAMA': pd.DataFrame(tab.KAMA(df['Close'],timeperiod=30) for df in klines[i]),
                'MACD': pd.DataFrame(tab.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9) for df in klines[i]),
                'STOCHRSI': pd.DataFrame(tab.STOCHRSI(df['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0) for df in klines[i]),
                'SAR': pd.DataFrame(tab.SAR(df['High'], df['Low'],acceleration=0, maximum=0) for df in klines[i]),
                'ATR': pd.DataFrame(tab.ATR(df['High'], df['Low'], df['Close'], timeperiod=14) for df in klines[i]),
                'NATR': pd.DataFrame(tab.NATR(df['High'], df['Low'],df['Close'],timeperiod=14) for df in klines[i]),
                'CCI':pd.DataFrame(tab.CCI(df['High'], df['Low'], df['Close'], timeperiod=14) for df in klines[i]),
                'W%R':pd.DataFrame(tab.WILLR(df['High'], df['Low'], df['Close'], timeperiod=14) for df in klines[i]),
                'MFI':pd.DataFrame(tab.MFI(df['High'], df['Low'], df['Close'], df['Volume'], timeperiod=14) for df in klines[i]),
                'AD':pd.DataFrame(tab.AD(df['High'], df['Low'], df['Close'], df['Volume']) for df in klines[i]),
                'DOSC':pd.DataFrame(tab.ADOSC(df['High'], df['Low'], df['Close'], df['Volume'], fastperiod=3, slowperiod=10) for df in klines[i])
                         }
    
    a = a + 1
    if a < len(klines):
        t_loop(a=a)
    return print('inserted time')


Indicators(a=0)
