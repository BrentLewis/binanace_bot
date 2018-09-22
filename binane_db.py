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

###These are all a repeat of the same finction
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
