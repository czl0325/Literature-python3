from flask_restful import Api, Resource, reqparse
from models import db, Book
from flask import Blueprint, current_app
from utils.response_code import ResponseData, RET

book_router = Blueprint('book', __name__, url_prefix='/book')

api = Api(book_router)

"""小说目录列表"""
class ChapterListResource(Resource):
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
