

class symbol(db.Model):

    id = db.Column('symbol_id', db.Integer, primary_key=True)
    symbol_col = db.Column('symbol_col', db.VARCHAR(45))

    _time = db.relationship('time', backref='Symbol', lazy=True)
    _open_close = db.relationship('open_close', backref='Symbol', lazy=True)
    _h_l_v = db.relationship('h_l_v', backref='Symbol', lazy=True)
    _i_5m = db.relationship('i_5m', backref='Symbol', lazy=True)
    _i_10m = db.relationship('i_10m', backref='Symbol', lazy=True)
    _i_15m = db.relationship('i_15m', backref='Symbol', lazy=True)
    _i_30m = db.relationship('i_30m', backref='Symbol', lazy=True)
    _i_1h = db.relationship('i_1h', backref='Symbol', lazy=True)
    _i_2h = db.relationship('i_2h', backref='Symbol', lazy=True)
    _i_4h = db.relationship('i_4h', backref='Symbol', lazy=True)
    _i_6h = db.relationship('i_6h', backref='Symbol', lazy=True)
    _i_12h = db.relationship('i_12h', backref='Symbol', lazy=True)


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
#I want to come back ot here and put in *kwargs in the __init__ and make a class generator to cut out 200-300 lines
################################################################################################################################
class i_5m(db.Model):
    id = db.Column('i_5m_id', db.Integer, primary_key = True)
    _5m_RSI = db.Column('RSI', db.VARCHAR(45))
    _5m_MFI = db.Column('MFI', db.VARCHAR(45))
    _5m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _5m_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _5m_RSI, _5m_MFI, _5m_BBANDS_LOWER, _5m_BBANDS_MIDDLE, _5m_BBANDS_UPPER,
               vEMA, _5m_MA, _5m_MACD, _5m_MACD_SIGNAL, _5m_MACD_HISTOGRAM, _5m_STOCHRSI, 
               _5m_SAR,_5m_STOCH_K,_5m_STOCH_D, _5m_CCI): #indicators __int__
        
        self._5m_RSI = _5m_RSI
        self._5m_MFI = _5m_MFI
        self._5m_BBANDS_LOWER = _5m_BBANDS_LOWER
        self._5m_BBANDS_MIDDLE = _5m_BBANDS_MIDDLE
        self._5m_BBANDS_UPPER = _5m_BBANDS_UPPER
        self._5m_EMA = _5m_EMA
        self._5m_MA =_5m_MA
        self._5m_MACD = _5m_MACD
        self._5m_MACD_SIGNAL = _5m_MACD_SIGNAL
        self._5m_MACD_HISTOGRAM = _5m_MACD_HISTOGRAM
        self._5m_STOCHRSI = _5m_STOCHRSI
        self._5m_SAR = _5m_SAR
        self._5m_STOCH_K = _5m_STOCH_K
        self._5m_STOCH_D = _5m_STOCH_D
        self._5m_CCI = _5m_CCI

       
    def __repr__(self):
        return '<i_5m %r>' % self.id


class i_10m(db.Model):
    id = db.Column('i_10m_id', db.Integer, primary_key = True)
    _10m_RSI = db.Column('RSI', db.VARCHAR(45))
    _10m_MFI = db.Column('MFI', db.VARCHAR(45))
    _10m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _10m_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _10m_RSI, _10m_MFI, _10m_BBANDS_LOWER, _10m_BBANDS_MIDDLE, _10m_BBANDS_UPPER,
               _10m_EMA, _10m_MA, _10m_MACD, _10m_MACD_SIGNAL, _10m_MACD_HISTOGRAM, _10m_STOCHRSI, 
               _10m_SAR,_10m_STOCH_K,_10m_STOCH_D, _10m_CCI): #indicators __int__
        
        self._10m_RSI = _10m_RSI
        self._10m_MFI = _10m_MFI
        self._10m_BBANDS_LOWER = _10m_BBANDS_LOWER
        self._10m_BBANDS_MIDDLE = _10m_BBANDS_MIDDLE
        self._10m_BBANDS_UPPER = _10m_BBANDS_UPPER
        self._10m_EMA = _10m_EMA
        self._10m_MA =_10m_MA
        self._10m_MACD = _10m_MACD
        self._10m_MACD_SIGNAL = _10m_MACD_SIGNAL
        self._10m_MACD_HISTOGRAM = _10m_MACD_HISTOGRAM
        self._10m_STOCHRSI = _10m_STOCHRSI
        self._10m_SAR = _10m_SAR
        self._10m_STOCH_K = _10m_STOCH_K
        self._10m_STOCH_D = _10m_STOCH_D
        self._10m_CCI = _10m_CCI

    def __repr__(self):
        return '<i_10m %r>' % self.id

class i_15m(db.Model):
    id = db.Column('i_15m_id', db.Integer, primary_key = True)
    _15m_RSI = db.Column('RSI', db.VARCHAR(45))
    _15m_MFI = db.Column('MFI', db.VARCHAR(45))
    _15m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _15m_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _15m_RSI, _15m_MFI, _15m_BBANDS_LOWER, _15m_BBANDS_MIDDLE, _15m_BBANDS_UPPER,
               _15m_EMA, _15m_MA, _15m_MACD, _15m_MACD_SIGNAL, _15m_MACD_HISTOGRAM, _15m_STOCHRSI, 
               _15m_SAR,_15m_STOCH_K,_15m_STOCH_D, _15m_CCI): #indicators __int__
        
        self._15m_RSI = _15m_RSI
        self._15m_MFI = _15m_MFI
        self._15m_BBANDS_LOWER = _15m_BBANDS_LOWER
        self._15m_BBANDS_MIDDLE = _15m_BBANDS_MIDDLE
        self._15m_BBANDS_UPPER = _15m_BBANDS_UPPER
        self._15m_EMA = _15m_EMA
        self._15m_MA =_15m_MA
        self._15m_MACD = _15m_MACD
        self._15m_MACD_SIGNAL = _15m_MACD_SIGNAL
        self._15m_MACD_HISTOGRAM = _15m_MACD_HISTOGRAM
        self._15m_STOCHRSI = _15m_STOCHRSI
        self._15m_SAR = _15m_SAR
        self._15m_STOCH_K = _15m_STOCH_K
        self._15m_STOCH_D = _15m_STOCH_D
        self._15m_CCI = _15m_CCI

    def __repr__(self):
        return '<i_15m %r>' % self.id

class i_30m(db.Model):
    id = db.Column('i_30m_id', db.Integer, primary_key = True)
    _30m_RSI = db.Column('RSI', db.VARCHAR(45))
    _30m_MFI = db.Column('MFI', db.VARCHAR(45))
    _30m_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _30m_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _30m_RSI, _30m_MFI, _30m_BBANDS_LOWER, _30m_BBANDS_MIDDLE, _30m_BBANDS_UPPER,
               _30m_EMA, _30m_MA, _30m_MACD, _30m_MACD_SIGNAL, _30m_MACD_HISTOGRAM, _30m_STOCHRSI, 
               _30m_SAR,_30m_STOCH_K,_30m_STOCH_D, _30m_CCI): #indicators __int__
        
        self._30m_RSI = _30m_RSI
        self._30m_MFI = _30m_MFI
        self._30m_BBANDS_LOWER = _30m_BBANDS_LOWER
        self._30m_BBANDS_MIDDLE = _30m_BBANDS_MIDDLE
        self._30m_BBANDS_UPPER = _30m_BBANDS_UPPER
        self._30m_EMA = _30m_EMA
        self._30m_MA =_30m_MA
        self._30m_MACD = _30m_MACD
        self._30m_MACD_SIGNAL = _30m_MACD_SIGNAL
        self._30m_MACD_HISTOGRAM = _30m_MACD_HISTOGRAM
        self._30m_STOCHRSI = _30m_STOCHRSI
        self._30m_SAR = _30m_SAR
        self._30m_STOCH_K = _30m_STOCH_K
        self._30m_STOCH_D = _30m_STOCH_D
        self._30m_CCI = _30m_CCI


    def __repr__(self):
        return '<I_30m %r>' % self.id

class i_1h(db.Model):
    id = db.Column('i_1h_id', db.Integer, primary_key = True)
    id = db.Column('i_1h_id', db.Integer, primary_key = True)
    _1h_RSI = db.Column('RSI', db.VARCHAR(45))
    _1h_MFI = db.Column('MFI', db.VARCHAR(45))
    _1h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _1h_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _1h_RSI, _1h_MFI, _1h_BBANDS_LOWER, _1h_BBANDS_MIDDLE, _1h_BBANDS_UPPER,
               _1h_EMA, _1h_MA, _1h_MACD, _1h_MACD_SIGNAL, _1h_MACD_HISTOGRAM, _1h_STOCHRSI, 
               _1h_SAR,_1h_STOCH_K,_1h_STOCH_D, _1h_CCI): #indicators __int__
        
        self._1h_RSI = _1h_RSI
        self._1h_MFI = _1h_MFI
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
    id = db.Column('i_2h_id', db.Integer, primary_key = True)
    id = db.Column('i_1h_id', db.Integer, primary_key = True)
    _2h_RSI = db.Column('RSI', db.VARCHAR(45))
    _2h_MFI = db.Column('MFI', db.VARCHAR(45))
    _2h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _2h_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _2h_RSI, _2h_MFI, _2h_BBANDS_LOWER, _2h_BBANDS_MIDDLE, _2h_BBANDS_UPPER,
               _2h_EMA, _2h_MA, _2h_MACD, _2h_MACD_SIGNAL, _2h_MACD_HISTOGRAM, _2h_STOCHRSI, 
               _2h_SAR,_2h_STOCH_K,_2h_STOCH_D, _2h_CCI): #indicators __int__
        
        self._2h_RSI = _2h_RSI
        self._2h_MFI = _2h_MFI
        self._2h_BBANDS_LOWER = _2h_BBANDS_LOWER
        self._2h_BBANDS_MIDDLE = _2h_BBANDS_MIDDLE
        self._2h_BBANDS_UPPER = _2h_BBANDS_UPPER
        self._2h_EMA = _2h_EMA
        self._2h_MA =_2h_MA
        self._2h_MACD = _2h_MACD
        self._2h_MACD_SIGNAL = _2h_MACD_SIGNAL
        self._2h_MACD_HISTOGRAM = _2h_MACD_HISTOGRAM
        self._2h_STOCHRSI = _2h_STOCHRSI
        self._2h_SAR = _2h_SAR
        self._2h_STOCH_K = _2h_STOCH_K
        self._2h_STOCH_D = _2h_STOCH_D
        self._2h_CCI = _2h_CCI

       
    def __repr__(self):
        return '<i_2h %r>' % self.id

class i_4h(db.Model):
    id = db.Column('i_4h_id', db.Integer, primary_key = True)
    _4h_RSI = db.Column('RSI', db.VARCHAR(45))
    _4h_MFI = db.Column('MFI', db.VARCHAR(45))
    _4h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _4h_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _4h_RSI, _4h_MFI, _4h_BBANDS_LOWER, _4h_BBANDS_MIDDLE, _4h_BBANDS_UPPER,
               _4h_EMA, _4h_MA, _4h_MACD, _4h_MACD_SIGNAL, _4h_MACD_HISTOGRAM, _4h_STOCHRSI, 
               _4h_SAR,_4h_STOCH_K,_4h_STOCH_D, _4h_CCI): #indicators __int__
        
        self._4h_RSI = _4h_RSI
        self._4h_MFI = _4h_MFI
        self._4h_BBANDS_LOWER = _4h_BBANDS_LOWER
        self._4h_BBANDS_MIDDLE = _4h_BBANDS_MIDDLE
        self._4h_BBANDS_UPPER = _4h_BBANDS_UPPER
        self._4h_EMA = _4h_EMA
        self._4h_MA =_4h_MA
        self._4h_MACD = _4h_MACD
        self._4h_MACD_SIGNAL = _4h_MACD_SIGNAL
        self._4h_MACD_HISTOGRAM = _4h_MACD_HISTOGRAM
        self._4h_STOCHRSI = _4h_STOCHRSI
        self._4h_SAR = _4h_SAR
        self._4h_STOCH_K = _4h_STOCH_K
        self._4h_STOCH_D = _4h_STOCH_D
        self._4h_CCI = _4h_CCI

       
    def __repr__(self):
        return '<i_4h %r>' % self.id

class i_6h(db.Model):
    id = db.Column('i_6h_id', db.Integer, primary_key = True)
    _6h_RSI = db.Column('RSI', db.VARCHAR(45))
    _6h_MFI = db.Column('MFI', db.VARCHAR(45))
    _6h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _6h_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _6h_RSI, _6h_MFI, _6h_BBANDS_LOWER, _6h_BBANDS_MIDDLE, _6h_BBANDS_UPPER,
               _6h_EMA, _6h_MA, _6h_MACD, _6h_MACD_SIGNAL, _6h_MACD_HISTOGRAM, _6h_STOCHRSI, 
               _6h_SAR,_6h_STOCH_K,_6h_STOCH_D, _6h_CCI): #indicators __int__
        
        self._6h_RSI = _6h_RSI
        self._6h_MFI = _6h_MFI
        self._6h_BBANDS_LOWER = _6h_BBANDS_LOWER
        self._6h_BBANDS_MIDDLE = _6h_BBANDS_MIDDLE
        self._6h_BBANDS_UPPER = _6h_BBANDS_UPPER
        self._6h_EMA = _6h_EMA
        self._6h_MA =_6h_MA
        self._6h_MACD = _6h_MACD
        self._6h_MACD_SIGNAL = _6h_MACD_SIGNAL
        self._6h_MACD_HISTOGRAM = _6h_MACD_HISTOGRAM
        self._6h_STOCHRSI = _6h_STOCHRSI
        self._6h_SAR = _6h_SAR
        self._6h_STOCH_K = _6h_STOCH_K
        self._6h_STOCH_D = _6h_STOCH_D
        self._6h_CCI = _6h_CCI

       
    def __repr__(self):
        return '<i_6h %r>' % self.id

class i_12h(db.Model):
    id = db.Column('i_12h_id', db.Integer, primary_key = True)
    _12h_RSI = db.Column('RSI', db.VARCHAR(45))
    _12h_MFI = db.Column('MFI', db.VARCHAR(45))
    _12h_BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    _12h_BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
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

    def __int__(self, _12h_RSI, _12h_MFI, _12h_BBANDS_LOWER, _12h_BBANDS_MIDDLE, _12h_BBANDS_UPPER,
               _12h_EMA, _12h_MA, _12h_MACD, _12h_MACD_SIGNAL, _12h_MACD_HISTOGRAM, _12h_STOCHRSI, 
               _12h_SAR,_12h_STOCH_K,_12h_STOCH_D, _12h_CCI): #indicators __int__
        
        self._12h_RSI = _12h_RSI
        self._1h_MFI = _12h_MFI
        self._12h_BBANDS_LOWER = _12h_BBANDS_LOWER
        self._12h_BBANDS_MIDDLE = _12h_BBANDS_MIDDLE
        self._12h_BBANDS_UPPER = _12h_BBANDS_UPPER
        self._12h_EMA = _12h_EMA
        self._12h_MA =_12h_MA
        self._12h_MACD = _12h_MACD
        self._12h_MACD_SIGNAL = _12h_MACD_SIGNAL
        self._12h_MACD_HISTOGRAM = _12h_MACD_HISTOGRAM
        self._12h_STOCHRSI = _12h_STOCHRSI
        self._12h_SAR = _12h_SAR
        self._12h_STOCH_K = _12h_STOCH_K
        self._12h_STOCH_D = _12h_STOCH_D
        self._12h_CCI = _12h_CCI

       
    def __repr__(self):
        return '<i_12h %r>' % self.id
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
        with db.session.no_autoflush:
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
#these are all meant to be called inside the indicators() function
def _5m_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _5minute = i_5m(_5m_STOCH_K=Indicators['stoch_k'][a],
                      _5m_STOCH_D=Indicators['stoch_d'][a],
                     _5m_STOCHRSI=Indicators['stochrsi'][a],
                      _5m_RSI=Indicators['rsi'][a],
                      _5m_CCI=Indicators['cci'][a],
                     _5m_EMA=Indicators['ema'][a],
                     _5m_MFI=Indicators['mfi'][a],
                     _5m_SAR=Indicators['sar'][a],
                     _5m_BBANDS_UPPER=Indicators['bbands_upper'][a],
                     _5m_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                     _5m_BBANDS_LOWER=Indicators['bbands_lower'][a],
                     _5m_MACD=Indicators['macd'][a],
                     _5m_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                     _5m_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_5m.append(_5minute)
            db.session.add(s)
            db.session.add(_5minute)
    return print('5m table inserted into')


def _10m_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _10minute = i_10m(_10m_STOCH_K=Indicators['stoch_k'][a],
                      _10m_STOCH_D=Indicators['stoch_d'][a],
                     _10m_STOCHRSI=Indicators['stochrsi'][a],
                    _10m_RSI=Indicators['rsi'][a],
                     _10m_CCI=Indicators['cci'][a],
                     _10m_EMA=Indicators['ema'][a],
                    _10m_MFI=Indicators['mfi'][a],
                    _10m_SAR=Indicators['sar'][a],
                    _10m_BBANDS_UPPER=Indicators['bbands_upper'][a],
                    _10m_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                     _10m_BBANDS_LOWER=Indicators['bbands_lower'][a],
                     _10m_MACD=Indicators['macd'][a],
                     _10m_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                     _10m_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_10m.append(_10minute)
            db.session.add(s)
            db.session.add(_10minute)
    return print('10m table inserted into')


def _15m_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _15minute = i_15m(_15m_STOCH_K=Indicators['stoch_k'][a],
                      _15m_STOCH_D=Indicators['stoch_d'][a],
                      _15m_STOCHRSI=Indicators['stochrsi'][a],
                      _15m_RSI=Indicators['rsi'][a],
                     _15m_CCI=Indicators['cci'][a],
                     _15m_EMA=Indicators['ema'][a],
                     _15m_MFI=Indicators['mfi'][a],
                     _15m_SAR=Indicators['sar'][a],
                     _15m_BBANDS_UPPER=Indicators['bbands_upper'][a],
                     _15m_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                     _15m_BBANDS_LOWER=Indicators['bbands_lower'][a],
                     _15m_MACD=Indicators['macd'][a],
                     _15m_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                     _15m_MACD_SIGNAL=Indicators['macd_signal'][a])
            

            s._i_15m.append(_15minute)
            db.session.add(s)
            db.session.add(_15minute)
    return print('15m table inserted into')


def _30m_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _30minute = i_30m(_30m_STOCH_K=Indicators['stoch_k'][a],
                      _30m_STOCH_D=Indicators['stoch_d'][a],
                      _30m_STOCHRSI=Indicators['stochrsi'][a],
                      _30m_RSI=Indicators['rsi'][a],
                     _30m_CCI=Indicators['cci'][a],
                     _30m_EMA=Indicators['ema'][a],
                      _30m_MFI=Indicators['mfi'][a],
                     _30m_SAR=Indicators['sar'][a],
                     _30m_BBANDS_UPPER=Indicators['bbands_upper'][a],
                     _30m_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                     _30m_BBANDS_LOWER=Indicators['bbands_lower'][a],
                     _30m_MACD=Indicators['macd'][a],
                     _30m_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                     _30m_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_30m.append(_30minute)
            db.session.add(s)
            db.session.add(_30minute)
    return print('30m table inserted into')


def _1h_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _1hour = i_1h(_1h_STOCH_K=Indicators['stoch_k'][a],
                      _1h_STOCH_D=Indicators['stoch_d'][a],
                      _1h_STOCHRSI=Indicators['stochrsi'][a],
                      _1h_RSI=Indicators['rsi'][a],
                      _1h_CCI=Indicators['cci'][a],
                      _1h_EMA=Indicators['ema'][a],
                      _1h_MFI=Indicators['mfi'][a],
                      _1h_SAR=Indicators['sar'][a],
                      _1h_BBANDS_UPPER=Indicators['bbands_upper'][a],
                      _1h_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                      _1h_BBANDS_LOWER=Indicators['bbands_lower'][a],
                      _1h_MACD=Indicators['macd'][a],
                      _1h_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                      _1h_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_1h.append(_1hour)
            db.session.add(s)
            db.session.add(_1hour)
    return print('1h table inserted into')


def _2h_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _2hour = i_2h(_2h_STOCH_K=Indicators['stoch_k'][a],
                      _2h_STOCH_D=Indicators['stoch_d'][a],
                      _2h_STOCHRSI=Indicators['stochrsi'][a],
                      _2h_RSI=Indicators['rsi'][a],
                      _2h_CCI=Indicators['cci'][a],
                      _2h_EMA=Indicators['ema'][a],
                      _2h_MFI=Indicators['mfi'][a],
                      _2h_SAR=Indicators['sar'][a],
                      _2h_BBANDS_UPPER=Indicators['bbands_upper'][a],
                      _2h_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                      _2h_BBANDS_LOWER=Indicators['bbands_lower'][a],
                      _2h_MACD=Indicators['macd'][a],
                      _2h_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                      _2h_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_2h.append(_2hour)
            db.session.add(s)
            db.session.add(_2hour)
    return print('2h table inserted into')


def _4h_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _4hour = i_4h(_4h_STOCH_K=Indicators['stoch_k'][a],
                      _4h_STOCH_D=Indicators['stoch_d'][a],
                      _4h_STOCHRSI=Indicators['stochrsi'][a],
                      _4h_RSI=Indicators['rsi'][a],
                      _4h_CCI=Indicators['cci'][a],
                      _4h_EMA=Indicators['ema'][a],
                      _4h_MFI=Indicators['mfi'][a],
                      _4h_SAR=Indicators['sar'][a],
                      _4h_BBANDS_UPPER=Indicators['bbands_upper'][a],
                      _4h_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                      _4h_BBANDS_LOWER=Indicators['bbands_lower'][a],
                      _4h_MACD=Indicators['macd'][a],
                      _4h_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                      _4h_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_4h.append(_4hour)
            db.session.add(s)
            db.session.add(_4hour)
    return print('1h table inserted into')


def _6h_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _6hour = i_6h(_6h_STOCH_K=Indicators['stoch_k'][a],
                      _6h_STOCH_D=Indicators['stoch_d'][a],
                      _6h_STOCHRSI=Indicators['stochrsi'][a],
                      _6h_RSI=Indicators['rsi'][a],
                      _6h_CCI=Indicators['cci'][a],
                      _6h_EMA=Indicators['ema'][a],
                      _6h_MFI=Indicators['mfi'][a],
                      _6h_SAR=Indicators['sar'][a],
                      _6h_BBANDS_UPPER=Indicators['bbands_upper'][a],
                      _6h_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                      _6h_BBANDS_LOWER=Indicators['bbands_lower'][a],
                      _6h_MACD=Indicators['macd'][a],
                      _6h_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                      _6h_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_6h.append(_6hour)
            db.session.add(s)
            db.session.add(_6hour)
    return print('1h table inserted into')


def _12h_(Indicators,_symbol_):
    for a in range(len(Indicators['rsi'])):
        with db.session.no_autoflush:
            s = symbol(symbol_col=tickers[_symbol_])

            _12hour = i_12h(_12h_STOCH_K=Indicators['stoch_k'][a],
                      _12h_STOCH_D=Indicators['stoch_d'][a],
                      _12h_STOCHRSI=Indicators['stochrsi'][a],
                      _12h_RSI=Indicators['rsi'][a],
                      _12h_CCI=Indicators['cci'][a],
                      _12h_EMA=Indicators['ema'][a],
                     _12h_MFI=Indicators['mfi'][a],
                     _12h_SAR=Indicators['sar'][a],
                     _12h_BBANDS_UPPER=Indicators['bbands_upper'][a],
                     _12h_BBANDS_MIDDLE=Indicators['bbands_middle'][a],
                     _12h_BBANDS_LOWER=Indicators['bbands_lower'][a],
                     _12h_MACD=Indicators['macd'][a],
                    _12h_MACD_HISTOGRAM=Indicators['macd_histogram'][a],
                    _12h_MACD_SIGNAL=Indicators['macd_signal'][a])

            s._i_12h.append(_12hour)
            db.session.add(s)
            db.session.add(_12hour)
    return print('1h table inserted into')

