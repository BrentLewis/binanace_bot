from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc
import pymysql

pymysql.install_as_MySQLdb()

app = fl(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password0@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DEBUG = True
db = sa(app)


class symbol(db.Model):

    id = db.Column('symbol_id', db.Integer, primary_key=True)
    symbol_col = db.Column('symbol_col', db.VARCHAR(45))

    _time = db.relationship('time', backref='Symbol', lazy=True)
    _open_close = db.relationship('open_close', backref='Symbol', lazy=True)
    _h_l_v = db.relationship('h_l_v', backref='Symbol', lazy=True)


    def __init__(self, symbol_col):
        self.symbol_col = symbol_col

    def __repr__(self):
        return '<symbol %r>' % self.id


class h_l_v(db.Model):
    id = db.Column('h_l_v_id', db.Integer, primary_key=True)
    high = db.Column('high', db.VARCHAR(45))
    low = db.Column('low', db.VARCHAR(45))
    volume = db.Column('volume', db.VARCHAR(45))
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, high, low, volume):
        self.high = high
        self.low = low
        self.volume = volume

    def __repr__(self):
        return '<h_l_v %r>' % self.id


class time(db.Model):
    id = db.Column('time_id', db.Integer, primary_key=True)
    open_time = db.Column(db.VARCHAR(45))
    close_time = db.Column(db.VARCHAR(45))
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, open_time, close_time, symbols):
        self.open_time = open_time
        self.close_time = close_time
        self.symbols = symbols

    def __repr__(self):
        return '<time %r>' % self.id

class open_close(db.Model):
    id = db.Column('open_close_id', db.Integer, primary_key=True)
    open = db.Column('open', db.VARCHAR(45))
    close = db.Column('close', db.VARCHAR(45))
    n_o_t = db.Column('n_o_t', db.VARCHAR(45))
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, open, close, n_o_t):
        self.open = open
        self.close = close
        self.n_o_t = n_o_t

    def __repr__(self):
        return '<open_close %r>' % self.id
#Between this comment line and the next all the functions are the same, they just call different time frames
#I want to come back ot here and put in *args in the __init__ and make a class generator to cut out 200-300 lines
################################################################################################################################
class i_5m(db.Model):
    id = db.Column('I_5m_id', db.Integer, primary_key = True)
    _5m_RSI = db.Column('RSI', db.VARCHAR(45))
    _5m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _5m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _5m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _5m_EMA = db.Column('EMA', db.VARCHAR(45))
    _5m_MA = db.Column('MA', db.VARCHAR(45))
    _5m_MACD = db.Column('MACD', db.VARCHAR(45))
    _5m_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _5m_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _5m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _5m_SAR = db.Column('SAR', db.VARCHAR(45))
    _5m_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _5m_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _5m_CCI = db.Column('cci', db.VARCHAR(45))
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._5m_RSI = _1h_RSI
        self._5m_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._5m_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._5m_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._5m_EMA = _1h_EMA
        self._5m_MA =_1h_MA
        self._5m_MACD = _1h_MACD
        self._5m_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._5m_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._5m_STOCHRSI = _1h_STOCHRSI
        self._5m_SAR = _1h_SAR
        self._5m_STOCH_K = _1h_STOCH_K
        self._5m_STOCH_D = _1h_STOCH_D
        self._5m_CCI = _1h_CCI

       
    def __repr__(self):
        return '<I_5m %r>' % self.id


class i_10m(db.Model):
    id = db.Column('I_10m_id', db.Integer, primary_key = True)
    _10m_RSI = db.Column('RSI', db.VARCHAR(45))
    _10m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _10m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _10m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _10m_EMA = db.Column('EMA', db.VARCHAR(45))
    _10m_MA = db.Column('MA', db.VARCHAR(45))
    _10m_MACD = db.Column('MACD', db.VARCHAR(45))
    _10m_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _10m_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _10m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _10m_SAR = db.Column('SAR', db.VARCHAR(45))
    _10m_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _10m_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _10m_CCI = db.Column('cci', db.VARCHAR(45))
    
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._10m_RSI = _1h_RSI
        self._10m_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._10m_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._10m_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._10m_EMA = _1h_EMA
        self._10m_MA =_1h_MA
        self._10m_MACD = _1h_MACD
        self._10m_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._10m_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._10m_STOCHRSI = _1h_STOCHRSI
        self._10m_SAR = _1h_SAR
        self._10m_STOCH_K = _1h_STOCH_K
        self._10m_STOCH_D = _1h_STOCH_D
        self._10m_CCI = _1h_CCI

    def __repr__(self):
        return '<I_10m %r>' % self.id

class i_15m(db.Model):
    id = db.Column('I_15m_id', db.Integer, primary_key = True)
    _15m_RSI = db.Column('RSI', db.VARCHAR(45))
    _15m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _15m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _15m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _15m_EMA = db.Column('EMA', db.VARCHAR(45))
    _15m_MA = db.Column('MA', db.VARCHAR(45))
    _15m_MACD = db.Column('MACD', db.VARCHAR(45))
    _15m_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _15m_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _15m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _15m_SAR = db.Column('SAR', db.VARCHAR(45))
    _15m_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _15m_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _15m_CCI = db.Column('cci', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._15m_RSI = _1h_RSI
        self._15m_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._15m_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._15m_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._15m_EMA = _1h_EMA
        self._15m_MA =_1h_MA
        self._15m_MACD = _1h_MACD
        self._15m_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._15m_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._15m_STOCHRSI = _1h_STOCHRSI
        self._15m_SAR = _1h_SAR
        self._15m_STOCH_K = _1h_STOCH_K
        self._15m_STOCH_D = _1h_STOCH_D
        self._15m_CCI = _1h_CCI

    def __repr__(self):
        return '<I_15m %r>' % self.id

class i_30m(db.Model):
    id = db.Column('I_30m_id', db.Integer, primary_key = True)
    _30m_RSI = db.Column('RSI', db.VARCHAR(45))
    _30m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _30m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _30m_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _30m_EMA = db.Column('EMA', db.VARCHAR(45))
    _30m_MA = db.Column('MA', db.VARCHAR(45))
    _30m_MACD = db.Column('MACD', db.VARCHAR(45))
    _30m_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _30m_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _30m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _30m_SAR = db.Column('SAR', db.VARCHAR(45))
    _30m_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _30m_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _30m_CCI = db.Column('cci', db.VARCHAR(45))
    
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._30m_RSI = _1h_RSI
        self._30m_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._30m_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._30m_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._30m_EMA = _1h_EMA
        self._30m_MA =_1h_MA
        self._30m_MACD = _1h_MACD
        self._30m_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._30m_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._30m_STOCHRSI = _1h_STOCHRSI
        self._30m_SAR = _1h_SAR
        self._30m_STOCH_K = _1h_STOCH_K
        self._30m_STOCH_D = _1h_STOCH_D
        self._30m_CCI = _1h_CCI


    def __repr__(self):
        return '<I_30m %r>' % self.id

class i_1h(db.Model):
    id = db.Column('I_1h_id', db.Integer, primary_key = True)
    id = db.Column('I_1h_id', db.Integer, primary_key = True)
    _1h_RSI = db.Column('RSI', db.VARCHAR(45))
    _1h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _1h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _1h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _1h_EMA = db.Column('EMA', db.VARCHAR(45))
    _1h_MA = db.Column('MA', db.VARCHAR(45))
    _1h_MACD = db.Column('MACD', db.VARCHAR(45))
    _1h_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _1h_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _1h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _1h_SAR = db.Column('SAR', db.VARCHAR(45))
    _1h_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _1h_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _1h_CCI = db.Column('cci', db.VARCHAR(45))
    
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._1h_RSI = _1h_RSI
        self._1h_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._1h_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._1h_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._1h_EMA = _1h_EMA
        self._1h_MA =_1h_MA
        self._1h_MACD = _1h_MACD
        self._1h_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._1h_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._1h_STOCHRSI = _1h_STOCHRSI
        self._1h_SAR = _1h_SAR
        self._1h_STOCH_K = _1h_STOCH_K
        self._1h_STOCH_D = _1h_STOCH_D
        self._1h_CCI = _1h_CCI

       
    def __repr__(self):
        return '<I_1h %r>' % self.id

class i_2h(db.Model):
    id = db.Column('I_2h_id', db.Integer, primary_key = True)
    id = db.Column('I_1h_id', db.Integer, primary_key = True)
    _2h_RSI = db.Column('RSI', db.VARCHAR(45))
    _2h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _2h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _2h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _2h_EMA = db.Column('EMA', db.VARCHAR(45))
    _2h_MA = db.Column('MA', db.VARCHAR(45))
    _2h_MACD = db.Column('MACD', db.VARCHAR(45))
    _2h_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _2h_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _2h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _2h_SAR = db.Column('SAR', db.VARCHAR(45))
    _2h_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _2h_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _2h_CCI = db.Column('cci', db.VARCHAR(45))
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._2h_RSI = _1h_RSI
        self._2h_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._2h_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._2h_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._2h_EMA = _1h_EMA
        self._2h_MA =_1h_MA
        self._2h_MACD = _1h_MACD
        self._2h_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._2h_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._2h_STOCHRSI = _1h_STOCHRSI
        self._2h_SAR = _1h_SAR
        self._2h_STOCH_K = _1h_STOCH_K
        self._2h_STOCH_D = _1h_STOCH_D
        self._2h_CCI = _1h_CCI

       
    def __repr__(self):
        return '<I_2h %r>' % self.id

class i_4h(db.Model):
    id = db.Column('I_4h_id', db.Integer, primary_key = True)
    _4h_RSI = db.Column('RSI', db.VARCHAR(45))
    _4h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _4h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _4h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _4h_EMA = db.Column('EMA', db.VARCHAR(45))
    _4h_MA = db.Column('MA', db.VARCHAR(45))
    _4h_MACD = db.Column('MACD', db.VARCHAR(45))
    _4h_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _4h_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _4h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _4h_SAR = db.Column('SAR', db.VARCHAR(45))
    _4h_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _4h_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _4h_CCI = db.Column('cci', db.VARCHAR(45))
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._4h_RSI = _1h_RSI
        self._4h_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._4h_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._4h_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._4h_EMA = _1h_EMA
        self._4h_MA =_1h_MA
        self._4h_MACD = _1h_MACD
        self._4h_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._4h_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._4h_STOCHRSI = _1h_STOCHRSI
        self._4h_SAR = _1h_SAR
        self._4h_STOCH_K = _1h_STOCH_K
        self._4h_STOCH_D = _1h_STOCH_D
        self._4h_CCI = _1h_CCI

       
    def __repr__(self):
        return '<I_4h %r>' % self.id

class i_6h(db.Model):
    id = db.Column('I_6h_id', db.Integer, primary_key = True)
    _6h_RSI = db.Column('RSI', db.VARCHAR(45))
    _6h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _6h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _6h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _6h_EMA = db.Column('EMA', db.VARCHAR(45))
    _6h_MA = db.Column('MA', db.VARCHAR(45))
    _6h_MACD = db.Column('MACD', db.VARCHAR(45))
    _6h_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _6h_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _6h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _6h_SAR = db.Column('SAR', db.VARCHAR(45))
    _6h_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _6h_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _6h_CCI = db.Column('cci', db.VARCHAR(45))
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._6h_RSI = _1h_RSI
        self._6h_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._6h_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._6h_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._6h_EMA = _1h_EMA
        self._6h_MA =_1h_MA
        self._6h_MACD = _1h_MACD
        self._6h_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._6h_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._6h_STOCHRSI = _1h_STOCHRSI
        self._6h_SAR = _1h_SAR
        self._6h_STOCH_K = _1h_STOCH_K
        self._6h_STOCH_D = _1h_STOCH_D
        self._6h_CCI = _1h_CCI

       
    def __repr__(self):
        return '<I_6h %r>' % self.id

class i_12h(db.Model):
    id = db.Column('I_12h_id', db.Integer, primary_key = True)
    _12h_RSI = db.Column('RSI', db.VARCHAR(45))
    _12h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _12h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _12h_BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    _12h_EMA = db.Column('EMA', db.VARCHAR(45))
    _12h_MA = db.Column('MA', db.VARCHAR(45))
    _12h_MACD = db.Column('MACD', db.VARCHAR(45))
    _12h_MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    _12h_MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    _12h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _12h_SAR = db.Column('SAR', db.VARCHAR(45))
    _12h_STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    _12h_STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    _12h_CCI = db.Column('cci', db.VARCHAR(45))
    
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE, BBANDS_UPPER,
               EMA, MA, MACD, MACD_SIGNAL, MACD_HISTOGRAM, STOCHRSI, 
               SAR,STOCH_K,STOCH_D, CCI): #indicators __int__
        
        self._12h_RSI = _1h_RSI
        self._12h_BBANDS_LOWER = _1h_BBANDS_LOWER
        self._12h_BBANDS_MIDDLE = _1h_BBANDS_MIDDLE
        self._12h_BBANDS_UPPER = _1h_BBANDS_UPPER
        self._12h_EMA = _1h_EMA
        self._12h_MA =_1h_MA
        self._12h_MACD = _1h_MACD
        self._12h_MACD_SIGNAL = _1h_MACD_SIGNAL
        self._12h_MACD_HISTOGRAM = _1h_MACD_HISTOGRAM
        self._12h_STOCHRSI = _1h_STOCHRSI
        self._12h_SAR = _1h_SAR
        self._12h_STOCH_K = _1h_STOCH_K
        self._12h_STOCH_D = _1h_STOCH_D
        self._12h_CCI = _1h_CCI

       
    def __repr__(self):
        return '<I_12h %r>' % self.id
#####################################################################################################################################    

def _symbol():
    for i in range(len(tickers)):
        data = tickers[i]
        id = i + 1
        db.session.add(symbol(data))
    db.create_all()
    return print('inserted in symbol')


_symbol()


def t_loop(a=0):
    for i in range(len(klines[a])):
        try:
            s = symbol(symbol_col=tickers[a])
            t = time(open_time=klines[a][i][0], close_time=klines[a][i][6])
            s._time.append(t)
            db.session.add(s)
            db.session.add(t)

        except exc.IntegrityError as e:
            db.session.rollback()
    
    a = a + 1
    if a < len(klines):
        t_loop(a=a)
    return print('inserted time')


t_loop(a=0)

def O_C_loop(a = 0):
    for i in range(len(klines[a])):
        with db.session.no_autoflush:
            try:
                s = symbol(symbol_col=tickers[a])
                o_c = open_close(open = klines[a][i][1] , close = klines[a][i][4], n_o_t = klines[a][i][8])
                s._open_close.append(o_c)
                db.session.add(s)
                db.session.add(o_c)

            except exc.IntegrityError as e:
                db.session.rollback()
            
    a = a + 1
    if a < len(klines):
        O_C_loop(a = a)
    return print('inserted open_close')
O_C_loop(a=0)

def h_l_v_loop(a = 0):
    for i in range(len(klines[a])):
        with db.session.no_autoflush:
            try:
                s = symbol(symbol_col=tickers[a])
                hlv = h_l_v(high = klines[a][i][2] , low = klines[a][i][3] , volume = klines[a][i][5] )
                s._h_l_v.append(hlv)
                db.session.add(s)
                db.session.add(hlv)

            except exc.IntegrityError as e:
                db.session.rollback()
            
    a = a + 1
    if a < len(klines):
        h_l_v_loop(a = a)
    return print('inserted h_l_v')
h_l_v_loop(a = 0)

###These are all a repeat of the same finction as well.
#I'll build a decorator, or class not sure which is best yet, later for now it functions
#These are all meant to be called inside the indicators() function
def _5m_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
            
            _5m = _5m(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._5m.append(_5m)
            db.session.add(s)
            db.session.add(_5m)
    return print('5m table inserted into')


def _10m_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
                        
            _10m = _10m(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._10m.append(_10m)
            db.session.add(s)
            db.session.add(_10m)
    return print('10m table inserted into')


def _15m_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
                       
            _15m = _15m(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._15m.append(_15m)
            db.session.add(s)
            db.session.add(_15m)
    return print('15m table inserted into')


def _30m_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
                         
            _30m = _30m(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._30m.append(_30m)
            db.session.add(s)
            db.session.add(_30m)
    return print('30m table inserted into')
      
def _1h_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
                
            _1h = _1h(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._1h.append(_1h)
            db.session.add(s)
            db.session.add(_1h)
    return print('1h table inserted into')

def _2h_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
                         
            _2h = _2h(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._2h.append(_2h)
            db.session.add(s)
            db.session.add(_2h)
    return print('2h table inserted into')

def _4h_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
                  
            _4h = _4h(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._4h.append(_4h)
            db.session.add(s)
            db.session.add(_4h)
    return print('1h table inserted into')

def _6h_():

    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
             
            _6h = _6h(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._6h.append(_6h)
            db.session.add(s)
            db.session.add(_6h)
    return print('1h table inserted into')

def _12h_():
    
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[symbol])
                     
            _12h = _12h(stoch_k = Indicators['stoch_k'][a],
                stoch_d= Indicators['stoch_d'][a],
                stochrsi= Indicators['stochrsi'][a],
                rsi=Indicators['rsi'][a],
                cci= Indicators['cci'][a],
                ema= Indicators['ema'][a],
                mfi= Indicators['mfi'][a],
                psar= Indicators['psar'][a],
                bbands_upper= Indicators['bbands_upper'][a],
                bbands_middle= Indicators['bbands_middle'][a],
                bbands_lower= Indicators['bbands_lower'][a],
                macd= Indicators['macd'][a],
                macd_histogram= Indicators['macd_histogram'][a],
                macd_signal= Indicators['macd_signal'][a])

            s._12h.append(_12h)
            db.session.add(s)
            db.session.add(_12h)
    return print('1h table inserted into')


db.create_all()
db.session.commit()
if __name__ == '__main__':
    app.run()
