from flask import Blueprint, current_app
from flask_restful import Api, Resource, reqparse
from datetime import datetime, timedelta
from lib.jwt_utils import generate_jwt
from models import db, Book, BookShelf, User
import random
from utils.response_code import RET, ResponseData

user_router = Blueprint('user_router', __name__)

api = Api(user_router)


class UserLoginResource(Resource):
    @staticmethod
    def _generate_jwt_token(user_id):
        # 参数：user_id表示生成token的载荷中存储用户信息
        # 1、生成当前时间
        now = datetime.utcnow()
        # 2、根据时间差，指定token的过期时间,
        expire = now + timedelta(hours=current_app.config["JWT_EXPIRE_TIME"])
        # 3、调用jwt工具，传入过期时间
        token = generate_jwt({"user_id": user_id}, expire=expire)
        return token

    """书架增加默认书籍"""

    def add_book_shelf(self, user_id):
        books = Book.query.filter(Book.showed == True).all()
        select_books = random.sample(books, 5)
        for book in select_books:
            db.session.add(BookShelf(book_id=book.book_id, user_id=user_id, book_name=book.book_name, cover=book.cover))
        try:
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)


class AddTestUser(Resource):
    def get(self):
        # 默认添加用户，用来测试数据
        # 构造用户数据
        user = User(dict(
            openId='1' * 32,
            nickName='测试用户001',
            gender=1,
            city='厦门市',
            province='福建省',
            country='中国',
            avatarUrl='http://mrw.so/5OGIYO'
        ))
        res_data = ResponseData(code=RET.OK)
        try:
            db.session.add(user)
            db.session.commit()
            token = UserLoginResource._generate_jwt_token(user.id)
            res_data.data = {'token': token, 'user': user.to_dict()}
            return res_data.to_dict()
        except Exception as e:
            current_app.logger.error(e)
            res_data.code = RET.DBERR
            return res_data.to_dict()


class LoginByTestUser(Resource):
    def post(self):
        res_data = ResponseData(code=RET.OK)

        try:
            openId = '1' * 32
            user = User.query.filter_by(openId=openId).first()
            if not User:
                res_data.code = RET.NODATA
                return res_data.to_dict()
            token = UserLoginResource._generate_jwt_token(user.id)
            res_data.data = {'token': token, 'user': user.to_dict()}
            return res_data.to_dict()
        except Exception as e:
            current_app.logger.error(e)
            res_data.code = RET.DBERR
            return res_data.to_dict()


api.add_resource(AddTestUser, '/user/addtestuser')
api.add_resource(LoginByTestUser, '/user/logintestuser')
