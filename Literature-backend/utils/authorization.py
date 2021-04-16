import functools
from flask import g, request
from lib.jwt_utils import verify_jwt


def LoginRequired(view_func):
    @functools.wraps(view_func)
    def check_auth(*args, **kwargs):
        g.user_id = None
        auth = request.headers.get('token')
        payload = verify_jwt(auth)
        if payload:
            g.user_id = payload.get('user_id')
            return view_func(*args, **kwargs)
        else:
            from utils.response_code import RET, ResponseData
            return ResponseData(RET.TOKENERROR).to_dict()

    return check_auth
