import jwt
from flask import current_app


# payload表示存储的用户信息, expire表示jwt的过期时间,secret_key表示密钥
def generate_jwt(payload, expire, secret_key=None):
    _payload = {'exp': expire}
    _payload.update(payload)
    if secret_key is None:
        secret_key = current_app.config["SECRET_KEY"]
    token = jwt.encode(_payload, secret_key, algorithm='HS256')
    return token


def verify_jwt(token, secret_key=None):
    if not secret_key:
        secret_key = current_app.config["SECRET_KEY"]
    try:
        payload = jwt.decode(token, secret_key, algorithms='HS256')
    except jwt.PyJWTError:
        payload = None
    return payload