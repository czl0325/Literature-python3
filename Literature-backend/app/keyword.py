from flask import Blueprint, current_app
from models import SearchKeyWord
from utils.response_code import RET, ResponseData

keyword_router = Blueprint('keyword', __name__, url_prefix='/keyword')


@keyword_router.route('/hot', methods=['GET'])
def getHotKeyword():
    result = ResponseData(RET.OK)
    try:
        keywords = SearchKeyWord.query.filter_by(is_hot=True).order_by(SearchKeyWord.count.desc()).limit(10)
        if keywords:
            result.data = [dict(keyword) for keyword in keywords]
    except Exception as e:
        current_app.logger.error(e)
        result.code = RET.DBERR
    return result.to_dict()