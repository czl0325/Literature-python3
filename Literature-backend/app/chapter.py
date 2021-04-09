from flask import Blueprint, current_app, request
from models import db, Book, BookChapters, BookChapterContent
from utils.response_code import ResponseData, RET

chapter_router = Blueprint('chapter', __name__, url_prefix='/chapter')


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
    chapter_name = request.form.get('chapter_name')
    if not chapter_id:
        result.code = RET.NODATA
        return result.to_dict()
    try:
        chapter = BookChapters.query.filter(BookChapters.book_id == book_id,BookChapters.chapter_id == chapter_id).first()
        if chapter:
            if chapter.chapter_name != chapter_name:
                chapter.chapter_name = chapter_name
            chapter_detail = BookChapterContent.query.filter(BookChapterContent.book_id == book_id, BookChapterContent.chapter_id == chapter_id).first()
            if chapter_detail and len(chapter_detail.content) != len(chapter_content):
                chapter_detail.content = chapter_content
        else:
            chapter = BookChapters(book_id=book_id, chapter_id=chapter_id, chapter_name=chapter_name, word_count=len(chapter_content))
            chapter.content = chapter_content
            db.session.add(chapter)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
    return result.to_dict()


@chapter_router.route('/<int:id>', methods=['GET'])
def chapterDetail(id):
    result = ResponseData(RET.OK)
    if not id:
        result.code = RET.NOPARAMS
        return result.to_dict()
    chapter = BookChapters.query.get(id)
    if not chapter:
        result.code = RET.NODATA
        return result.to_dict()

    return result.to_dict()