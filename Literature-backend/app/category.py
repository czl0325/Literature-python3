from flask import Blueprint, request, current_app
from models import db, BookCategory
from utils.response_code import ResponseData, RET
from lib.qiniu_upload import upload_by_qiniu

cate_router = Blueprint('category', __name__, url_prefix='/category')


@cate_router.route('/list', methods=['GET'])
def category_list():
    cates = BookCategory.query.all()
    res = ResponseData(RET.OK)
    dicts = [cate.to_dict() for cate in cates]
    res.data = dicts
    return res.to_dict()


@cate_router.route('/add', methods=['POST'])
def category_add():
    category = BookCategory()
    result = ResponseData(RET.OK)
    cate_name = request.form.get('cate_name')
    if not cate_name:
        result.code = RET.NOPARAMS
        return result.to_dict()
    category.cate_name = cate_name
    file = request.files.get('file')
    if not file:
        category.cate_icon = '/static/img/cate_cover.jpeg'
    else:
        try:
            key = upload_by_qiniu(file)
            category.cate_icon = key
        except Exception as e:
            current_app.logger.error(e)
            result.code = RET.THIRDPARTYERROR
            return result.to_dict()
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
