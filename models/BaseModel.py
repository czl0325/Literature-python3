from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

pymysql.install_as_MySQLdb()
db = SQLAlchemy()

# 配置日志信息
# 设置日志的记录等级
logging.basicConfig(level=logging.ERROR)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("./logs/error.log", maxBytes=1024 * 1024 * 100, backupCount=10)
# 创建日志记录的格式   日志等级    输入日志信息的文件名    行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)


class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now())
    is_delete = db.Column(db.Boolean, default=False)
