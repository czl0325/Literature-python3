from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now())
    is_delete = db.Column(db.Boolean, default=False)
