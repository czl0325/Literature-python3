from flask import Blueprint, request, current_app
from models import db, BookCategory
from utils.response_code import ResponseData, RET

cate_router = Blueprint('category', __name__, url_prefix='/category')


@cate_router.route('/list', methods=['GET'])
def category_list():
    cates = BookCategory.query.all()
    res = ResponseData(RET.OK)
    dicts = [dict(cate) for cate in cates]
    res.data = dicts
    return res.to_dict()


@cate_router.route('/add', methods=['POST'])
def category_add():
    category = BookCategory()
    result = ResponseData(RET.OK)
    category_name = request.args.get('category_name')
    if not category_name:
        result.code = RET.NOPARAMS
        return result.to_dict()
    category.cate_name = category_name
    category_icon = request.files.get('category_icon')
    if not category_icon:
        category.icon = '/static/img/cate_cover.jpeg'
    try:
        db.session.add(category)
        db.session.commit()
    except Exception as e:
        print(current_app.logger.error(e))
        result.code = RET.DBERR
        return result.to_dict()

    result.data = dict(category)
    return result.to_dict()


@cate_router.route('/delete/<int:id>', methods=['GET'])
def category_del(id):
    result = ResponseData(RET.OK)
    if not id:
        result.code = RET.NOPARAMS
        return result.to_dict()
    cate = BookCategory.query.get(id)
    db.session.delete(cate)
    db.session.commit()
    return result.to_dict()
