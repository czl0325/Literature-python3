from flask import Blueprint, current_app, request
from flask_restful import Api, Resource, reqparse
from datetime import datetime, timedelta
from lib.jwt_utils import generate_jwt
from models import db, Book, BookShelf, User
import random
from utils.response_code import RET, ResponseData
from lib.qiniu_upload import upload_by_qiniu
from werkzeug.security import check_password_hash

user_router = Blueprint('user_router', __name__, url_prefix='/user')

api = Api(user_router)


@user_router.route('/register', methods=['POST'])
def register():
    image_data = request.files.get("file")
    result = ResponseData(RET.OK)
    if not image_data:
        result.code = RET.NOPARAMS
        return result.to_dict()
    location = request.form.get('location')
    if not location:
        location = '北京市/北京市/东城区'
    ls = location.split('/')
    if len(ls) != 3:
        result.code = RET.PARAMERROR
        return result.to_dict()
    token = upload_by_qiniu(image_data)
    if not token:
        result.code = RET.THIRDPARTYERROR
        return result.to_dict()
    try:
        user = User({
            'userName': request.form.get('userName'),
            'password': request.form.get('password'),
            'gender': request.form.get('gender'),
            'province': ls[0],
            'city': ls[1],
            'district': ls[2],
            'avatarUrl': token
        })
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        result.code = RET.DBERR
        return result.to_dict()
    result.data = user.to_dict()
    return result.to_dict()


@user_router.route('/login', methods=['POST'])
def login():
    result = ResponseData(RET.OK)
    userName = request.form.get('userName')
    password = request.form.get('password')
    if not all([userName, password]):
        result.code = RET.NOPARAMS
        return result.to_dict()
    try:
        user = User.query.filter_by(userName=userName).first()
        if not user:
            result.code = RET.NODATA
            return result.to_dict()
        if not check_password_hash(user.password_hash, password):
            result.code = RET.NODATA
            return result.to_dict()
        result.data = user.to_dict()
    except Exception as e:
        current_app.logger.error(e)
        result.code = RET.NODATA
        return result.to_dict()
    return result.to_dict()


@user_router.route('/addMyBook', methods=['POST'])
def addMyBook():
    result = ResponseData(RET.OK)
    book_id = request.form.get('book_id')
    user_id = request.form.get('user_id')
    if not all([book_id, user_id]):
        result.code = RET.NOPARAMS
        return result.to_dict()
    book_shelf = BookShelf.query.filter_by(user_id=user_id, book_id=book_id).first()
    if book_shelf:
        result.code = RET.DUPLICATEDATA
        return result.to_dict()
    else:
        book = Book.query.get(book_id)
        if not book:
            result.code = RET.NODATA
            return result.to_dict()
        try:
            book_shelf = BookShelf(book_id=book.book_id, book_name=book.book_name, cover=book.cover, user_id=user_id)
            db.session.add(book_shelf)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            result.code = RET.DBERR
            return result.to_dict()
    return result.to_dict()


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
        print(res_data)

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


api.add_resource(AddTestUser, '/addtestuser')
api.add_resource(LoginByTestUser, '/logintestuser')
