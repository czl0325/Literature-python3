from flask import Blueprint, current_app, request
from models import db, Book, BookChapters, BookChapterContent
from utils.response_code import ResponseData, RET

chapter_router = Blueprint('chapter', __name__, url_prefix='chapter')


@chapter_router.route('/list/<int:book_id>', methods=['GET'])
def chapterList(book_id):
    result = ResponseData(RET.OK)
    book = Book.query.get(book_id)
    if not book:
        result.code = RET.NODATA
        return result.to_dict()
    chapters = BookChapters.query.filter(BookChapters.book_id == book_id).order_by(BookChapters.chapter_id.asc()).all()
    chapters = [dict(chapter) for chapter in chapters]
    result.data = chapters
    return result.to_dict()


@chapter_router.route('/add/<int:book_id>', methods=['POST'])
def chapterAdd(book_id):
    result = ResponseData(RET.OK)
    book = Book.query.get(book_id)
    if not book:
        result.code = RET.NODATA
        return result.to_dict()
    chapter_id = request.form.get('chapter_id')
    chapter_content = request.form.get('chapter_content')
    if not chapter_id:
        result.code = RET.NODATA
        return result.to_dict()
    chapter = BookChapters.query.filter(BookChapters.book_id == book_id, BookChapters.chapter_id == chapter_id).first()
    try:
        if chapter:
            pass
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
    return result.to_dict()