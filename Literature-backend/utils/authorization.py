import functools
from flask import g, request
from lib.jwt_utils import verify_jwt
from response_code import ResponseData, RET


def Authorization(view_func):
    @functools.wraps(view_func)
    def check_auth(*args, **kwargs):
        g.user_id = None
        auth = request.headers.get('Authorization')
        payload = verify_jwt(auth)
        if payload:
            g.user_id = payload.get('user_id')
            return view_func(args, kwargs)
        else:
            return ResponseData(RET.TOKENERROR).to_dict()

    return check_auth
