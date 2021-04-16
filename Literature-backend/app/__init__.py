from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from config import config_dict

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


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config_dict[config])
    from .user import user_router
    app.register_blueprint(user_router)
    from .book import book_router
    app.register_blueprint(book_router)
    from .category import cate_router
    app.register_blueprint(cate_router)
    from .chapter import chapter_router
    app.register_blueprint(chapter_router)
    return app
