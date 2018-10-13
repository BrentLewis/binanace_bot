
class user_info(db.Model):

    id = db.Column('user_id', db.Integer, primary_key=True)
    user = db.Column('user', db.VARCHAR(45))
    password = db.Column('password', db.VARCHAR(45))
    email = db.Column('email', db.VARCHAR(45))

    _trade_ind = db.relationship('trade_ind', backref='Symbol', lazy=True)
    _test_ind = db.relationship('test_ind', backref='Symbol', lazy=True)

    def __init__(self, user, password, email):
        self.user = user
        self.password = password
        self.email = email

    def __repr__(self):
        return '<symbol %r>' % self.id

'''both indicator tables will have nan 
value fill when there is no variable for that indicator'''


#table to hold indicator pairs they want to trade off of
class trade_ind(db.Model):
    id = db.Column('trade_ind_id', db.Integer, primary_key=True)
    RSI = db.Column('RSI', db.VARCHAR(45))
    BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
    BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    EMA = db.Column('EMA', db.VARCHAR(45))
    MA = db.Column('MA', db.VARCHAR(45))
    MACD = db.Column('MACD', db.VARCHAR(45))
    MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    SAR = db.Column('SAR', db.VARCHAR(45))
    STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    CCI = db.Column('cci', db.VARCHAR(45))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'))
#is the below line needed?
    users = db.relationship('user_info')

    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE,
               BBANDS_UPPER, EMA, MA, MACD, MACD_SIGNAL,
              MACD_HISTOGRAM, STOCHRSI, SAR, STOCH_K, STOCH_D):
        self.RSI = RSI
        self.BBANDS_LOWER = BBANDS_LOWER
        self.BBANDS_MIDDLE = BBANDS_MIDDLE
        self.BBANDS_UPPER = BBANDS_UPPER
        self.EMA = EMA
        self.MA = MA
        self.MACD = MACD
        self.MACD_SIGNAL = MACD_SIGNAL
        self.MACD_HISTOGRAM = MACD_HISTOGRAM
        self.STOCHRSI = STOCHRSI
        self.SAR = SAR
        self.STOCH_K = STOCH_K
        self.STOCH_D = STOCH_D


    def __repr__(self):
        return '<trade_ind %r>' % self.id

#table to hold indicator pairs that are still being tested, but that they want to save
class test_ind(db.Model):
    id = db.Column('test_ind_id', db.Integer, primary_key=True)
    RSI = db.Column('RSI', db.VARCHAR(45))
    BBANDS_LOWER = db.Column('BBANDS_LOWER', db.VARCHAR(45))
    BBANDS_MIDDLE = db.Column('BBANDS_MIDDLE', db.VARCHAR(45))
    BBANDS_UPPER = db.Column('BBANDS_UPPER', db.VARCHAR(45))
    EMA = db.Column('EMA', db.VARCHAR(45))
    MA = db.Column('MA', db.VARCHAR(45))
    MACD = db.Column('MACD', db.VARCHAR(45))
    MACD_SIGNAL = db.Column('MACD_SIGNAL', db.VARCHAR(45))
    MACD_HISTOGRAM = db.Column('MACD_HISTOGRAM', db.VARCHAR(45))
    STOCHRSI = db.Column('STOCHRSI', db.VARCHAR(45))
    SAR = db.Column('SAR', db.VARCHAR(45))
    STOCH_K = db.Column('stoch_k', db.VARCHAR(45))
    STOCH_D = db.Column('stoch_d', db.VARCHAR(45))
    CCI = db.Column('cci', db.VARCHAR(45))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'))
    users = db.relationship('user_info')
    
    def __int__(self, RSI, BBANDS_LOWER, BBANDS_MIDDLE,
               BBANDS_UPPER, EMA, MA, MACD, MACD_SIGNAL,
              MACD_HISTOGRAM, STOCHRSI, SAR, STOCH_K, STOCH_D):
        self.RSI = RSI
        self.BBANDS_LOWER = BBANDS_LOWER
        self.BBANDS_MIDDLE = BBANDS_MIDDLE
        self.BBANDS_UPPER = BBANDS_UPPER
        self.EMA = EMA
        self.MA = MA
        self.MACD = MACD
        self.MACD_SIGNAL = MACD_SIGNAL
        self.MACD_HISTOGRAM = MACD_HISTOGRAM
        self.STOCHRSI = STOCHRSI
        self.SAR = SAR
        self.STOCH_K = STOCH_K
        self.STOCH_D = STOCH_D

    def __repr__(self):
        return '<test_ind %r>' % self.id

    