from flask_restful import Api, Resource, reqparse
from models import db, Book, BookChapters
from flask import Blueprint, current_app, request
from utils.response_code import ResponseData, RET, PageModel

book_router = Blueprint('book', __name__, url_prefix='/book')

api = Api(book_router)


@book_router.route('/add', methods=['POST'])
def addBook():
    result = ResponseData(RET.OK)
    book_name = request.form.get('book_name')
    channel_name = request.form.get('channel_name')
    channel_url = request.form.get('channel_url')
    author_name = request.form.get('author_name')
    cate_id = request.form.get('cate_id')
    cate_name = request.form.get('cate_name')
    intro = request.form.get('intro')
    word_count = request.form.get('word_count')
    chapter_num = request.form.get('chapter_num')
    cover = request.form.get('cover')
    book_id = request.form.get('book_id')
    if not book_id:
        if not book_name or not author_name or not cate_id or not cate_name:
            result.code = RET.NOPARAMS
            return result.to_dict()
    if book_name:
        book = Book.query.filter_by(book_name=book_name).first()
        if book:
            result.data = dict(book)
            return result.to_dict()
    data = { 'book_name': book_name, 'channel_name': channel_name, 'channel_url': channel_url, 'author_name': author_name, 'cate_id': cate_id, 'cate_name': cate_name, 'intro': intro, 'word_count': word_count, 'chapter_num': chapter_num, 'cover': cover }
    book = Book(data)
    if book_id:
        book.book_id = int(book_id)
    try:
        if book_id:
            old_book = Book.query.get(book_id)
            for key in book.keys():
                if book[key] is not None and key != 'book_id':
                    if hasattr(old_book, key):
                        setattr(old_book, key, book[key])
            result.data = dict(old_book)
        else:
            db.session.add(book)
            db.session.flush()
            result.data = dict(book)
        db.session.commit()
        return result.to_dict()
    except Exception as e:
        current_app.logger.error(e)
        result.code = RET.DBERR
        return result.to_dict()


@book_router.route('/list', methods=['GET'])
def bookList():
    result = ResponseData(RET.OK)
    cates = request.args.get('cates', type=str, default='')
    page_num = request.args.get('pageNum', type=int, default=1)
    page_size = request.args.get('pageSize', type=int, default=20)
    books_query = Book.query.order_by(Book.create_time)
    if cates:
        books_query.filter(Book.cate_id.in_(cates.split(",")))
    books_paginate = books_query.paginate(page=page_num, per_page=page_size, error_out=False)
    books = [dict(book) for book in books_paginate.items]
    page_model = PageModel(page_num=page_num, items=books, total_page=books_paginate.pages, total_num=books_paginate.total)
    result.data = dict(page_model)
    return result.to_dict()


@book_router.route('/detail/<int:book_id>', methods=['GET'])
def bookDetail(book_id):
    result = ResponseData(RET.OK)
    if not book_id:
        result.code = RET.NOPARAMS
        return result.to_dict()
    book = Book.query.get(book_id)
    if not book:
        result.code = RET.NODATA
        return result.to_dict()
    result.data = dict(book)
    return result.to_dict()


@book_router.route('/getbookuser', methods=['GET'])
def getBookUser():
    result = ResponseData(RET.OK)
    book_id = request.args.get('book_id')
    if not book_id:
        result.code = RET.NOPARAMS
        return result.to_dict()
    book = Book.query.get(book_id)
    users = [user.to_dict() for user in book.users]
    result.data = users
    return result.to_dict()



