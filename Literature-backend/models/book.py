from .BaseModel import BaseModel, db
from sqlalchemy.dialects.mysql import TEXT, MEDIUMTEXT
from datetime import datetime
from flask import current_app


class BookShelf(BaseModel, db.Model):
    """ 书架 """
    __tablename__ = 'tb_book_shelf'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, index=True)  # 书籍ID
    book_name = db.Column(db.String(100))  # 书籍名称
    cover = db.Column(db.String(300))  # 封面图片（文件名）
    user_id = db.Column(db.Integer)  # 用户id
    db.Index('ix_book_id_user_id', book_id, user_id, unique=True)


class ReadRate(BaseModel, db.Model):
    """ 阅读进度 """
    __tablename__ = 'tb_read_rate'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    chapter_id = db.Column(db.Integer)  # 章节id
    chapter_name = db.Column(db.String(100))  # 章节名称
    rate = db.Column(db.Integer, default=0)  # 阅读进度(百分率分子)


class Book(BaseModel, db.Model):
    """ 书籍基本信息 """
    __tablename__ = 'tb_book'
    book_id = db.Column(db.Integer, primary_key=True)  # 书籍ID
    book_name = db.Column(db.String(100))  # 书籍名称
    cate_id = db.Column(db.Integer, index=True)  # 书籍二级分类ID
    cate_name = db.Column(db.String(50))  # 书籍二级分类名称
    channel_type = db.Column(db.SmallInteger(), index=True)  # 书籍频道（1：男；2: 女 3: 出版 0: 无此属性默认为0）
    author_name = db.Column(db.String(50))  # 作者
    chapter_num = db.Column(db.Integer)  # 章节数量
    is_publish = db.Column(db.Integer, default=1)  # 是否出版（1：是；2：否）
    status = db.Column(db.Integer, default=1)  # 连载状态（1：未完结；2：已完结）
    cover = db.Column(db.String(256))  # 封面图片（链接）
    intro = db.Column(TEXT, default='暂无简介')  # 简介
    word_count = db.Column(db.Integer, default=0)  # 字数
    showed = db.Column(db.Boolean(), default=True)  # 是否上架
    channel_name = db.Column(db.String(20))  # 渠道书籍id 渠道名:书籍id
    channel_url = db.Column(db.String(256))  # 爬取的网址
    ranking = db.Column(db.Integer, server_default='0')  # 排序
    short_des = db.Column(db.String(50), server_default='')  # 短描述

    collect_count = db.Column(db.Integer, server_default='0')  # 被收藏数量
    heat = db.Column(db.Integer, server_default='0')  # 热度

    def __init__(self, data):
        if 'book_id' in data.keys() and data['book_id']:
            self.book_id = data["book_id"]
        if 'book_name' in data.keys() and data['book_name']:
            self.book_name = data["book_name"]
        if 'channel_name' in data.keys() and data['channel_name']:
            self.channel_name = data['channel_name']
        if 'channel_url' in data.keys() and data['channel_url']:
            self.channel_url = data['channel_url']
        if 'author_name' in data.keys() and data['author_name']:
            self.author_name = data['author_name']
        if 'cate_id' in data.keys() and data['cate_id']:
            self.cate_id = int(data['cate_id'])
        if 'cate_name' in data.keys() and data['cate_name']:
            self.cate_name = data['cate_name']
        if 'intro' in data.keys() and data['intro']:
            self.intro = data['intro']
        if 'word_count' in data.keys() and data['word_count']:
            self.word_count = int(data['word_count'])
        if 'chapter_num' in data.keys() and data['chapter_num']:
            self.chapter_num = int(data['chapter_num'])
        if 'cover' in data.keys() and data['cover']:
            self.cover = data['cover']

    def keys(self):
        return 'book_id', 'channel_name', 'book_name', 'cate_id', 'cate_name', 'channel_type', 'author_name', 'chapter_num', 'is_publish', 'status', 'cover', 'intro', 'word_count', 'showed', 'channel_url', 'short_des', 'collect_count', 'heat'

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        if value is not None:
            self.key = value


class BookCategory(BaseModel, db.Model):
    """ 书籍分类信息 """
    __tablename__ = 'tb_book_category'
    cate_id = db.Column(db.Integer, primary_key=True)  # 分类ID
    cate_name = db.Column(db.String(50))  # 分类名称
    cate_icon = db.Column(db.String(256))

    def to_dict(self):
        cate_icon = "http://127.0.0.1:5000" + self.cate_icon if self.cate_icon.startswith("/static") else self.cate_icon
        if not cate_icon.startswith('http'):
            cate_icon = current_app.config["QINIU_URLPREFIX"] + self.cate_icon
        return {'cate_id': self.cate_id, 'cate_name': self.cate_name, 'cate_icon': cate_icon }


class BookVolume(BaseModel, db.Model):
    """ 书籍卷节信息 """
    __tablename__ = 'tb_book_volume'
    id = db.Column(db.Integer, primary_key=True)  # ID
    book_id = db.Column(db.Integer, index=True)  # 书籍ID
    volume_id = db.Column(db.Integer, index=True)  # 卷ID
    volume_name = db.Column(db.String(100))  # 卷名
    chapter_count = db.Column(db.Integer, default=0)  # 卷字数


class BookChapters(BaseModel, db.Model):
    """ 书籍章节信息 """
    __tablename__ = 'tb_book_chapter'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True)  # ID
    book_id = db.Column(db.Integer, index=True)  # 书籍ID
    volume_id = db.Column(db.Integer, nullable=True)  # 卷ID
    chapter_id = db.Column(db.Integer, index=True)  # 章节ID
    chapter_name = db.Column(db.String(100))  # 章节名称
    word_count = db.Column(db.Integer)  # 字数
    content = db.relationship("BookChapterContent", backref="chapter", uselist=False)

    def keys(self):
        return 'book_id', 'chapter_id', 'chapter_name', 'word_count'

    def __getitem__(self, item):
        return getattr(self, item)


class BookChapterContent(BaseModel, db.Model):
    """ 书籍章节内容信息 """
    __tablename__ = 'tb_book_chapter_content'
    id = db.Column(db.Integer, db.ForeignKey('tb_book_chapter.id'), primary_key=True)
    content = db.Column(MEDIUMTEXT)  # 章节内容