from flask_restful import Api, Resource, reqparse
from models import db, Book
from flask import Blueprint, current_app, request
from utils.response_code import ResponseData, RET

book_router = Blueprint('book', __name__, url_prefix='/book')

api = Api(book_router)


@book_router.route('/add', methods=['POST'])
def addBook():
    result = ResponseData(RET.OK)
    book_name = request.form.get('book_name')
    channel_name = request.form.get('channel_name', type=str, default='')
    channel_url = request.form.get('channel_url', type=str, default='')
    author_name = request.form.get('author_name')
    cate_id = request.form.get('cate_id')
    cate_name = request.form.get('cate_name')
    intro = request.form.get('intro', type=str, default='')
    word_count = request.form.get('word_count', type=int, default=0)
    chapter_num = request.form.get('chapter_num', type=int, default=0)
    cover = request.form.get('cover')
    if not book_name or not author_name or not cate_id or not cate_name:
        result.code = RET.NOPARAMS
        return result.to_dict()
    book = Book({ 'book_name': book_name, 'channel_name': channel_name, 'channel_url': channel_url, 'author_name': author_name, 'cate_id': cate_id, 'cate_name': cate_name, 'intro': intro, 'word_count': word_count, 'chapter_num': chapter_num, 'cover': cover })
    try:
        db.session.add(book)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        result.code = RET.DBERR
        return result.to_dict()
    result.data = dict(book)
    return result.to_dict()


@book_router.route('/list', methods=['GET'])
def bookList():
    result = ResponseData(RET.OK)
    cates = request.args.get('cates', type=str, default='')
    books = Book.query.order_by(Book.create_time)
    if cates:
        books = books.filter(Book.cate_id.in_(cates.split(",")))
    books = [dict(book) for book in books]
    result.data = books
    return result.to_dict()


class ChapterListResource(Resource):
    """小说目录列表"""
    def get(self, book_id):
        # 1.获取查询字符串参数，page/pagesize/order
        req = reqparse.RequestParser()
        req.add_argument('page', required=True, type=int, default=1, location='args', help='page必传')
        req.add_argument('size', type=int, default=10, location='args')
        req.add_argument('order', type=int, default=0, location='args')
        args = req.parse_args()
        page = args.get('page')
        size = args.get('size')
        order = args.get('order')

        res_data = ResponseData(code=RET.OK)
        # 2.根据书籍id参数，查询书籍表
        try:
            book = Book.query.get(book_id)
            if not book:
                res_data.code = RET.NODATA
                return res_data.to_dict()
        except Exception as e:
            current_app.logger.error(e)
            res_data.code = RET.NODATA
            return res_data.to_dict()

        return res_data.to_dict()


api.add_resource(ChapterListResource, '/chapters/<int:book_id>')
