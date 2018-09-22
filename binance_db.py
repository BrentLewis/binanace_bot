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
    _5m_SMA = db.Column('SMA', db.VARCHAR(45))
    _5m_ROC = db.Column('ROC', db.VARCHAR(45))
    _5m_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _5m_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _5m_RSI = db.Column('RSI', db.VARCHAR(45))
    _5m_BB = db.Column('BB', db.VARCHAR(45))
    _5m_EMA = db.Column('EMA', db.VARCHAR(45))
    _5m_MA = db.Column('MA', db.VARCHAR(45))
    _5m_WMA = db.Column('WMA', db.VARCHAR(45))
    _5m_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _5m_MACD = db.Column('MACD', db.VARCHAR(45))
    _5m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _5m_SAR = db.Column('SAR', db.VARCHAR(45))
    _5m_ATR = db.Column('ATR', db.VARCHAR(45))
    _5m_NATR = db.Column('NATR', db.VARCHAR(45))
    _5m_WR = db.Column('WR', db.VARCHAR(45))
    _5m_CADL = db.Column('CADL', db.VARCHAR(45))
    _5m_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._5m_SMA = _5m_SMA
        self._5m_ROC = _5m_ROC
        self._5m_ROCP = _5m_ROCP
        self._5m_ROCR = _5m_ROCR
        self._5m_RSI = _5m_RSI
        self._5m_BB = _5m_BB
        self._5m_EMA = _5m_EMA
        self._5m_MA =_5m_MA
        self._5m_WMA = _5m_WMA
        self._5m_KAMA = _5m_KAMA
        self._5m_MACD = _5m_MACO
        self._5m_STOCHRSI = _5m_STOCHRSI
        self._5m_SAR = _5m_SAR
        self._5m_ATR = _5m_ATR
        self._m_NATR = _5m_NATR
        self._5m_WR = _5m_WR
        self._5m_CADL = _5m_CADL
        self._5m_CADO = _5m_CADO

    def __repr__(self):
        return '<I_5m %r>' % self.id


class i_10m(db.Model):
    id = db.Column('I_10m_id', db.Integer, primary_key = True)
    _10m_SMA = db.Column('SMA', db.VARCHAR(45))
    _10m_ROC = db.Column('ROC', db.VARCHAR(45))
    _10m_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _10m_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _10m_RSI = db.Column('RSI', db.VARCHAR(45))
    _10m_BB = db.Column('BB', db.VARCHAR(45))
    _10m_EMA = db.Column('EMA', db.VARCHAR(45))
    _10m_MA = db.Column('MA', db.VARCHAR(45))
    _10m_WMA = db.Column('WMA', db.VARCHAR(45))
    _10m_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _10m_MACD = db.Column('MACD', db.VARCHAR(45))
    _10m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _10m_SAR = db.Column('SAR', db.VARCHAR(45))
    _10m_ATR = db.Column('ATR', db.VARCHAR(45))
    _10m_NATR = db.Column('NATR', db.VARCHAR(45))
    _10m_WR = db.Column('WR', db.VARCHAR(45))
    _10m_CADL = db.Column('CADL', db.VARCHAR(45))
    _10m_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._10m_SMA = _10m_SMA
        self._10m_ROC = _10m_ROC
        self._10m_ROCP = _10m_ROCP
        self._10m_ROCR = _10m_ROCR
        self._10m_RSI = _10m_RSI
        self._10m_BB = _10m_BB
        self._10m_EMA = _10m_EMA
        self._10m_MA =_10m_MA
        self._10m_WMA = _10m_WMA
        self._10m_KAMA = _10m_KAMA
        self._10m_MACD = _10m_MACO
        self._10m_STOCHRSI = _10m_STOCHRSI
        self._10m_SAR = _10m_SAR
        self._10m_ATR = _10m_ATR
        self._10m_NATR = _10m_NATR
        self._10m_WR = _10m_WR
        self._10m_CADL = _10m_CADL
        self._10m_CADO = _10m_CADO

    def __repr__(self):
        return '<I_10m %r>' % self.id

class i_15m(db.Model):
    id = db.Column('I_15m_id', db.Integer, primary_key = True)
    _15m_SMA = db.Column('SMA', db.VARCHAR(45))
    _15m_ROC = db.Column('ROC', db.VARCHAR(45))
    _15m_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _15m_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _15m_RSI = db.Column('RSI', db.VARCHAR(45))
    _15m_BB = db.Column('BB', db.VARCHAR(45))
    _15m_EMA = db.Column('EMA', db.VARCHAR(45))
    _15m_MA = db.Column('MA', db.VARCHAR(45))
    _15m_WMA = db.Column('WMA', db.VARCHAR(45))
    _15m_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _15m_MACD = db.Column('MACD', db.VARCHAR(45))
    _15m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _15m_SAR = db.Column('SAR', db.VARCHAR(45))
    _15m_ATR = db.Column('ATR', db.VARCHAR(45))
    _15m_NATR = db.Column('NATR', db.VARCHAR(45))
    _15m_WR = db.Column('WR', db.VARCHAR(45))
    _15m_CADL = db.Column('CADL', db.VARCHAR(45))
    _15m_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._15m_SMA = _15m_SMA
        self._15m_ROC = _15m_ROC
        self._15m_ROCP = _15m_ROCP
        self._15m_ROCR = _15m_ROCR
        self._15m_RSI = _15m_RSI
        self._15m_BB = _15m_BB
        self._15m_EMA = _15m_EMA
        self._15m_MA =_15m_MA
        self._15m_WMA = _15m_WMA
        self._15m_KAMA = _15m_KAMA
        self._15m_MACD = _15m_MACO
        self._15m_STOCHRSI = _15m_STOCHRSI
        self._15m_SAR = _15m_SAR
        self._15m_ATR = _15m_ATR
        self._15m_NATR = _15m_NATR
        self._15m_WR = _15m_WR
        self._15m_CADL = _15m_CADL
        self._15m_CADO = _15m_CADO

    def __repr__(self):
        return '<I_15m %r>' % self.id

class i_30m(db.Model):
    id = db.Column('I_30m_id', db.Integer, primary_key = True)
    _30m_SMA = db.Column('SMA', db.VARCHAR(45))
    _30m_ROC = db.Column('ROC', db.VARCHAR(45))
    _30m_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _30m_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _30m_RSI = db.Column('RSI', db.VARCHAR(45))
    _30m_BB = db.Column('BB', db.VARCHAR(45))
    _30m_EMA = db.Column('EMA', db.VARCHAR(45))
    _30m_MA = db.Column('MA', db.VARCHAR(45))
    _30m_WMA = db.Column('WMA', db.VARCHAR(45))
    _30m_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _30m_MACD = db.Column('MACD', db.VARCHAR(45))
    _30m_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _30m_SAR = db.Column('SAR', db.VARCHAR(45))
    _30m_ATR = db.Column('ATR', db.VARCHAR(45))
    _30m_NATR = db.Column('NATR', db.VARCHAR(45))
    _30m_WR = db.Column('WR', db.VARCHAR(45))
    _30m_CADL = db.Column('CADL', db.VARCHAR(45))
    _30m_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._30m_SMA = _30m_SMA
        self._30m_ROC = _30m_ROC
        self._30m_ROCP = _30m_ROCP
        self._30m_ROCR = _30m_ROCR
        self._30m_RSI = _30m_RSI
        self._30m_BB = _30m_BB
        self._30m_EMA = _30m_EMA
        self._30m_MA =_30m_MA
        self._30m_WMA = _30m_WMA
        self._30m_KAMA = _30m_KAMA
        self._30m_MACD = _30m_MACO
        self._30m_STOCHRSI = _30m_STOCHRSI
        self._30m_SAR = _30m_SAR
        self._30m_ATR = _30m_ATR
        self._30m_NATR = _30m_NATR
        self._30m_WR = _30m_WR
        self._30m_CADL = _30m_CADL
        self._30m_CADO = _30m_CADO

    def __repr__(self):
        return '<I_30m %r>' % self.id

class i_1h(db.Model):
    id = db.Column('I_1h_id', db.Integer, primary_key = True)
    _1h_SMA = db.Column('SMA', db.VARCHAR(45))
    _1h_ROC = db.Column('ROC', db.VARCHAR(45))
    _1h_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _1h_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _1h_RSI = db.Column('RSI', db.VARCHAR(45))
    _1h_BB = db.Column('BB', db.VARCHAR(45))
    _1h_EMA = db.Column('EMA', db.VARCHAR(45))
    _1h_MA = db.Column('MA', db.VARCHAR(45))
    _1h_WMA = db.Column('WMA', db.VARCHAR(45))
    _1h_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _1h_MACD = db.Column('MACD', db.VARCHAR(45))
    _1h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _1h_SAR = db.Column('SAR', db.VARCHAR(45))
    _1h_ATR = db.Column('ATR', db.VARCHAR(45))
    _1h_NATR = db.Column('NATR', db.VARCHAR(45))
    _1h_WR = db.Column('WR', db.VARCHAR(45))
    _1h_CADL = db.Column('CADL', db.VARCHAR(45))
    _1h_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._1h_SMA = _1h_SMA
        self._1h_ROC = _1h_ROC
        self._1h_ROCP = _1h_ROCP
        self._1h_ROCR = _1h_ROCR
        self._1h_RSI = _1h_RSI
        self._1h_BB = _1h_BB
        self._1h_EMA = _1h_EMA
        self._1h_MA =_1h_MA
        self._1h_WMA = _1h_WMA
        self._1h_KAMA = _1h_KAMA
        self._1h_MACD = _1h_MACO
        self._1h_STOCHRSI = _1h_STOCHRSI
        self._1h_SAR = _1h_SAR
        self._1h_ATR = _1h_ATR
        self._1h_NATR = _1h_NATR
        self._1h_WR = _1h_WR
        self._1h_CADL = _1h_CADL
        self._1h_CADO = _1h_CADO

    def __repr__(self):
        return '<I_1h %r>' % self.id

class i_2h(db.Model):
    id = db.Column('I_2h_id', db.Integer, primary_key = True)
    _2h_SMA = db.Column('SMA', db.VARCHAR(45))
    _2h_ROC = db.Column('ROC', db.VARCHAR(45))
    _2h_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _2h_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _2h_RSI = db.Column('RSI', db.VARCHAR(45))
    _2h_BB = db.Column('BB', db.VARCHAR(45))
    _2h_EMA = db.Column('EMA', db.VARCHAR(45))
    _2h_MA = db.Column('MA', db.VARCHAR(45))
    _2h_WMA = db.Column('WMA', db.VARCHAR(45))
    _2h_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _2h_MACD = db.Column('MACD', db.VARCHAR(45))
    _2h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _2h_SAR = db.Column('SAR', db.VARCHAR(45))
    _2h_ATR = db.Column('ATR', db.VARCHAR(45))
    _2h_NATR = db.Column('NATR', db.VARCHAR(45))
    _2h_WR = db.Column('WR', db.VARCHAR(45))
    _2h_CADL = db.Column('CADL', db.VARCHAR(45))
    _2h_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._2h_SMA = _2h_SMA
        self._2h_ROC = _2h_ROC
        self._2h_ROCP = _2h_ROCP
        self._2h_ROCR = _2h_ROCR
        self._2h_RSI = _2h_RSI
        self._2h_BB = _2h_BB
        self._2h_EMA = _2h_EMA
        self._2h_MA =_2h_MA
        self._2h_WMA = _2h_WMA
        self._2h_KAMA = _2h_KAMA
        self._2h_MACD = _2h_MACO
        self._2h_STOCHRSI = _2h_STOCHRSI
        self._2h_SAR = _2h_SAR
        self._2h_ATR = _2h_ATR
        self._2h_NATR = _2h_NATR
        self._2h_WR = _2h_WR
        self._2h_CADL = _2h_CADL
        self._2h_CADO = _2h_CADO

    def __repr__(self):
        return '<I_2h %r>' % self.id

class i_4h(db.Model):
    id = db.Column('I_4h_id', db.Integer, primary_key = True)
    _4h_SMA = db.Column('SMA', db.VARCHAR(45))
    _4h_ROC = db.Column('ROC', db.VARCHAR(45))
    _4h_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _4h_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _4h_RSI = db.Column('RSI', db.VARCHAR(45))
    _4h_BB = db.Column('BB', db.VARCHAR(45))
    _4h_EMA = db.Column('EMA', db.VARCHAR(45))
    _4h_MA = db.Column('MA', db.VARCHAR(45))
    _4h_WMA = db.Column('WMA', db.VARCHAR(45))
    _4h_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _4h_MACD = db.Column('MACD', db.VARCHAR(45))
    _4h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _4h_SAR = db.Column('SAR', db.VARCHAR(45))
    _4h_ATR = db.Column('ATR', db.VARCHAR(45))
    _4h_NATR = db.Column('NATR', db.VARCHAR(45))
    _4h_WR = db.Column('WR', db.VARCHAR(45))
    _4h_CADL = db.Column('CADL', db.VARCHAR(45))
    _4h_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._4h_SMA = _4h_SMA
        self._4h_ROC = _4h_ROC
        self._4h_ROCP = _4h_ROCP
        self._4h_ROCR = _4h_ROCR
        self._4h_RSI = _4h_RSI
        self._4h_BB = _4h_BB
        self._4h_EMA = _4h_EMA
        self._4h_MA =_4h_MA
        self._4h_WMA = _4h_WMA
        self._4h_KAMA = _4h_KAMA
        self._4h_MACD = _4h_MACO
        self._4h_STOCHRSI = _4h_STOCHRSI
        self._4h_SAR = _4h_SAR
        self._4h_ATR = _4_ATR
        self._4h_NATR = _4h_NATR
        self._4h_WR = _4h_WR
        self._4h_CADL = _4h_CADL
        self._4h_CADO = _4h_CADO

    def __repr__(self):
        return '<I_4h %r>' % self.id

class i_6h(db.Model):
    id = db.Column('I_6h_id', db.Integer, primary_key = True)
    _6h_SMA = db.Column('SMA', db.VARCHAR(45))
    _6h_ROC = db.Column('ROC', db.VARCHAR(45))
    _6h_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _6h_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _6h_RSI = db.Column('RSI', db.VARCHAR(45))
    _6h_BB = db.Column('BB', db.VARCHAR(45))
    _6h_EMA = db.Column('EMA', db.VARCHAR(45))
    _6h_MA = db.Column('MA', db.VARCHAR(45))
    _6h_WMA = db.Column('WMA', db.VARCHAR(45))
    _6h_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _6h_MACD = db.Column('MACD', db.VARCHAR(45))
    _6h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _6h_SAR = db.Column('SAR', db.VARCHAR(45))
    _6h_ATR = db.Column('ATR', db.VARCHAR(45))
    _6h_NATR = db.Column('NATR', db.VARCHAR(45))
    _6h_WR = db.Column('WR', db.VARCHAR(45))
    _6h_CADL = db.Column('CADL', db.VARCHAR(45))
    _6h_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._6h_SMA = _6h_SMA
        self._6h_ROC = _6h_ROC
        self._6h_ROCP = _6h_ROCP
        self._6h_ROCR = _6h_ROCR
        self._6h_RSI = _6h_RSI
        self._6h_BB = _6h_BB
        self._6h_EMA = _6h_EMA
        self._6h_MA =_6h_MA
        self._6h_WMA = _6h_WMA
        self._6h_KAMA = _6h_KAMA
        self._6h_MACD = _6h_MACO
        self._6h_STOCHRSI = _6h_STOCHRSI
        self._6h_SAR = _6h_SAR
        self._6h_ATR = _6h_ATR
        self._6h_NATR = _6h_NATR
        self._6h_WR = _6h_WR
        self._6h_CADL = _6h_CADL
        self._6h_CADO = _6h_CADO

    def __repr__(self):
        return '<I_6h %r>' % self.id

class i_12h(db.Model):
    id = db.Column('I_12h_id', db.Integer, primary_key = True)
    _12h_SMA = db.Column('SMA', db.VARCHAR(45))
    _12h_ROC = db.Column('ROC', db.VARCHAR(45))
    _12h_ROCP = db.Column('ROCP', db.VARCHAR(45))
    _12h_ROCR = db.Column('ROCR', db.VARCHAR(45))
    _12h_RSI = db.Column('RSI', db.VARCHAR(45))
    _12h_BB = db.Column('BB', db.VARCHAR(45))
    _12h_EMA = db.Column('EMA', db.VARCHAR(45))
    _12h_MA = db.Column('MA', db.VARCHAR(45))
    _12h_WMA = db.Column('WMA', db.VARCHAR(45))
    _12h_KAMA = db.Column('KAMA', db.VARCHAR(45))
    _12h_MACD = db.Column('MACD', db.VARCHAR(45))
    _12h_STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    _12h_SAR = db.Column('SAR', db.VARCHAR(45))
    _12h_ATR = db.Column('ATR', db.VARCHAR(45))
    _12h_NATR = db.Column('NATR', db.VARCHAR(45))
    _12h_WR = db.Column('WR', db.VARCHAR(45))
    _12h_CADL = db.Column('CADL', db.VARCHAR(45))
    _12h_CADO = db.Column('CADO', db.VARCHAR(45))

    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.symbol_id'))
    symbols = db.relationship('symbol')

    def __int__(self, SMA, ROC, ROCP,
               ROCR, RSI, BB, EMA, MA, WMA,
               KAMA, MACD, STOCHRSI, SAR,
               ATR, NATR, WR, CADL, CADO ): #indicators __int__
        self._12h_SMA = _12h_SMA
        self._12h_ROC = _12h_ROC
        self._12h_ROCP = _12h_ROCP
        self._12h_ROCR = _12h_ROCR
        self._12h_RSI = _12h_RSI
        self._12h_BB = _12h_BB
        self._12h_EMA = _12h_EMA
        self._12h_MA =_12h_MA
        self._12h_WMA = _12h_WMA
        self._12h_KAMA = _12h_KAMA
        self._12h_MACD = _12h_MACO
        self._12h_STOCHRSI = _12h_STOCHRSI
        self._12h_SAR = _12h_SAR
        self._12h_ATR = _12h_ATR
        self._12h_NATR = _12h_NATR
        self._12h_WR = _12h_WR
        self._12h_CADL = _12h_CADL
        self._12h_CADO = _12h_CADO

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
