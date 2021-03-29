from flask import Flask
import logging
from config import config_dict

logging.basicConfig(level=logging.DEBUG)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config_dict[config])
    from .user import user_router
    app.register_blueprint(user_router)
    return app
