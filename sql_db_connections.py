#azure cloud sql connection
import os
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc

app = fl(__name__)

params = urllib.parse.quote_plus("Driver={ODBC Driver 13 for SQL Server};Server=tcp:tyche-db.database.windows.net,1433;Database=Tyche_db;Uid=Puhtooie@tyche-db;Pwd={P3tr@,J0rd@n};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)


db.create_all()
db.session.commit()
if __name__ == '__main__':
    app.run()

#AWS Mysql connection
from flask import Flask as fl
from flask_sqlalchemy import SQLAlchemy as sa
app = fl(__name__)


application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{puhtooie}:{Al3x2ndr!a}@{tyche-test-instance.ckyjs7xvlpis.ap-northeast-1.rds.amazonaws.com}/{tyche_test_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)


db.create_all()
db.session.commit()
if __name__ == '__main__':
    application.run()


#local sql connection
import os
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc

app = fl(__name__)

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=X1TOUCH-2014;DATABASE=tempdb;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)

db.create_all()
db.session.commit()
if __name__ == '__main__':
    app.run()

#azure cloud sql connection
import os
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy as sa
from flask import Flask as fl
from sqlalchemy import exc

#local mysql connection
import pymysql

pymysql.install_as_MySQLdb()

app = fl(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Password@localhost/data_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = sa(app)


db.create_all()
db.session.commit()
if __name__ == '__main__':
    app.run()


