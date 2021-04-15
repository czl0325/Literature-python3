from flask import Blueprint, current_app, request
from flask_restful import Api, Resource, reqparse
from datetime import datetime, timedelta
from lib.jwt_utils import generate_jwt
from models import db, Book, User
import random
from utils.response_code import RET, ResponseData, PageModel
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
    # book_shelf = BookShelf.query.filter_by(user_id=user_id, book_id=book_id).first()
    # if book_shelf:
    #     result.code = RET.DUPLICATEDATA
    #     return result.to_dict()
    # else:
    #     book = Book.query.get(book_id)
    #     if not book:
    #         result.code = RET.NODATA
    #         return result.to_dict()
    #     try:
    #         book_shelf = BookShelf(book_id=book.book_id, book_name=book.book_name, cover=book.cover, user_id=user_id)
    #         db.session.add(book_shelf)
    #         db.session.commit()
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         result.code = RET.DBERR
    #         return result.to_dict()
    return result.to_dict()


@user_router.route('/mybook', methods=['GET'])
def getMyBookShelf():
    result = ResponseData(RET.OK)
    user_id = request.args.get('user_id')
    keyword = request.args.get('keyword')
    page_num = request.args.get('pageNum', type=int, default=1)
    page_size = request.args.get('pageSize', type=int, default=10)
    # try:
    #     book_query = BookShelf.query.filter_by(user_id=user_id)
    #     if keyword:
    #         book_query.filter(BookShelf.book_name.contains(keyword))
    #     books_paginate = book_query.paginate(page=page_num, per_page=page_size, error_out=False)
    #     books = [dict(book) for book in books_paginate.items]
    #     page_model = PageModel(page_num=page_num, items=books, total_page=books_paginate.pages, total_num=books_paginate.total)
    #     result.data = dict(page_model)
    # except Exception as e:
    #     current_app.logger.error(e)
    #     result.code = RET.DBERR
    return result.to_dict()

