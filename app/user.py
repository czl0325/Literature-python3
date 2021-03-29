from flask import Blueprint

user_router = Blueprint('user_router', __name__, url_prefix='/user')


@user_router.route('/')
def userIndex():
    return 'user info'