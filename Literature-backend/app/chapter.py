from flask import Blueprint, current_app, request
from models import db, Book, BookChapters, BookChapterContent
from utils.response_code import ResponseData, RET, PageModel

chapter_router = Blueprint('chapter', __name__, url_prefix='/chapter')


@chapter_router.route('/list/<int:book_id>', methods=['GET'])
def chapterList(book_id):
    result = ResponseData(RET.OK)
    page_num = request.args.get('pageNum', type=int)
    if not page_num:
        result.code = RET.NOPARAMS
        return result.to_dict()
    page_size = request.args.get('pageSize', type=int, default=30)
    book = Book.query.get(book_id)
    if not book:
        result.code = RET.NODATA
        return result.to_dict()
    try:
        chapter_query = BookChapters.query.filter(BookChapters.book_id == book_id).order_by(BookChapters.chapter_id.asc())
        chapters_paginate = chapter_query.paginate(page=page_num, per_page=page_size, error_out=False)
        chapters = [dict(chapter) for chapter in chapters_paginate.items]
        page_model = PageModel(page_num=page_num, items=chapters, total_page=chapters_paginate.pages, total_num=chapters_paginate.total)
        result.data = dict(page_model)
        return result.to_dict()
    except Exception as e:
        current_app.logger.error(e)
        result.code = RET.DBERR
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
    print(chapter_content)
    chapter_name = request.form.get('chapter_name')
    if not chapter_id:
        result.code = RET.NODATA
        return result.to_dict()
    try:
        chapter = BookChapters.query.filter(BookChapters.book_id == book_id,BookChapters.chapter_id == chapter_id).first()
        if chapter:
            if chapter.chapter_name != chapter_name:
                chapter.chapter_name = chapter_name
            chapter_detail = BookChapterContent.query.get(chapter.id)
            if not chapter_detail:
                chapter.word_count = len(chapter_content) - chapter_content.count(' ') - chapter_content.count('\n')
                db.session.add(chapter_detail)
            else:
                if len(chapter_detail.content) != len(chapter_content):
                    chapter_detail.content = chapter_content
                    chapter.word_count = len(chapter_content) - chapter_content.count(' ') - chapter_content.count('\n')
        else:
            chapter = BookChapters(book_id=book_id, chapter_id=chapter_id, chapter_name=chapter_name, word_count=len(chapter_content))
            db.session.add(chapter)
            db.session.flush()
            chapter_detail = BookChapterContent(id=chapter.id, content=chapter_content)
            db.session.add(chapter_detail)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
    return result.to_dict()


@chapter_router.route('/update/<int:id>', methods=['POST'])
def chapterUpdate(id):
    result = ResponseData(RET.OK)
    content = request.form.get('content')
    chapter_name = request.form.get('chapter_name')
    chapter_id = request.form.get('chapter_id')
    if not all([id, content, chapter_name, chapter_id]):
        result.code = RET.NOPARAMS
        return result.to_dict()
    chapter = BookChapters.query.get(id)
    if not chapter:
        result.code = RET.NODATA
        return result.to_dict()
    try:
        chapter.chapter_id = chapter_id
        chapter.chapter_name = chapter_name
        chapter.content.content = content
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        result.code = RET.DBERR
        return result.to_dict()
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
    data = dict(chapter)
    data['content'] = chapter.content.content
    result.data = data
    return result.to_dict()