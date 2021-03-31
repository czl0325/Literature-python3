from .BaseModel import BaseModel, db
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TEXT, MEDIUMTEXT
from datetime import datetime


class BookShelf(BaseModel, db.Model):
    """ 书架 """
    __tablename__ = 'tb_book_shelf'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, index=True)     # 书籍ID
    book_name = db.Column(db.String(100))           # 书籍名称
    cover = db.Column(db.String(300))               # 封面图片（文件名）
    user_id = db.Column(db.Integer)                 # 用户id
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
    channel_book_id = db.Column(db.String(20), unique=True)  # 渠道书籍id 渠道名:书籍id
    book_name = db.Column(db.String(100))  # 书籍名称
    cate_id = db.Column(db.Integer, index=True)  # 书籍二级分类ID
    cate_name = db.Column(db.String(50))  # 书籍二级分类名称
    channel_type = db.Column(db.SmallInteger(), index=True)  # 书籍频道（1：男；2: 女 3: 出版 0: 无此属性默认为0）
    author_name = db.Column(db.String(50))      # 作者
    chapter_num = db.Column(db.Integer)         # 章节数量
    is_publish = db.Column(db.Integer)          # 是否出版（1：是；2：否）
    status = db.Column(db.Integer)              # 连载状态（1：未完结；2：已完结）
    cover = db.Column(db.String(300))           # 封面图片（链接）
    intro = db.Column(TEXT)                     # 简介
    word_count = db.Column(db.Integer)          # 字数
    showed = db.Column(db.Boolean(), default=False)  # 是否上架
    source = db.Column(db.String(50))  # 来源
    ranking = db.Column(db.Integer, server_default='0')  # 排序
    short_des = db.Column(db.String(50), server_default='')  # 短描述

    collect_count = db.Column(db.Integer, server_default='0')  # 被收藏数量
    heat = db.Column(db.Integer, server_default='0')  # 热度

    def __init__(self, data):
        self.channel_book_id = data['channel_book_id']
        self.book_name = data['book_name']
        self.cate_id = int(data['cate_id'])
        self.channel_type = int(data['channel_type'])
        self.author_name = data['author_name']
        self.chapter_num = data['chapter_num']
        self.is_publish = data['is_publish']
        self.status = data['status']
        self.create_time = data['create_time']
        self.cover = data['cover']
        self.intro = data['intro']
        self.word_count = int(data['word_count'])
        self.update_time = data['update_time']
        self.source = data['source']

    def keys(self):
        return 'book_id', 'channel_book_id', 'book_name', 'cate_id', 'cate_name', 'channel_type', 'author_name', 'chapter_num', 'is_publish', 'status', 'cover', 'intro', 'word_count', 'showed', 'source', 'short_des', 'collect_count', 'heat'

    def __getitem__(self, item):
        return getattr(self, item)

# class BookCategoryRelation(BaseModel, db.Model):
#     """
#     分类和一级分类的关系
#     多对多关系
#     """
#     __tablename__ = 'tb_book_category_relation'
#     id = db.Column(db.Integer, primary_key=True)
#     big_cate_id = db.Column(db.Integer, db.ForeignKey('tb_book_big_category.cate_id'))
#     cate_id = db.Column(db.Integer, db.ForeignKey('tb_book_category.cate_id'))


BookCategoryRelation = db.Table('tb_book_category_relation',
    db.Column('big_cate_id', db.Integer, db.ForeignKey('tb_book_big_category.cate_id')),
    db.Column('cate_id', db.Integer, db.ForeignKey('tb_book_category.cate_id'))
)


class BookBigCategory(BaseModel, db.Model):
    """ 书籍一级分类信息 """
    __tablename__ = 'tb_book_big_category'

    cate_id = db.Column(db.Integer, primary_key=True)   # 分类ID
    cate_name = db.Column(db.String(50))                # 分类名称
    channel = db.Column(db.Integer)                     # 频道  1:男生, 2:女生
    showed = db.Column(db.Boolean(), default=True)
    icon = db.Column(db.String(100))

    # second_cates = db.relationship('BookCategory', secondary=BookCategoryRelation.__table__)


class BookCategory(BaseModel, db.Model):
    """ 书籍分类信息 """
    __tablename__ = 'tb_book_category'
    cate_id = db.Column(db.Integer, primary_key=True)  # 分类ID
    cate_name = db.Column(db.String(50))  # 分类名称
    showed = db.Column(db.Boolean(), default=True)
    icon = db.Column(db.String(100))


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
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = db.Column(db.Integer, primary_key=True)  # ID
    book_id = db.Column(db.Integer, index=True)  # 书籍ID
    volume_id = db.Column(db.Integer, index=True)  # 卷ID
    chapter_id = db.Column(db.Integer, index=True)  # 章节ID
    chapter_name = db.Column(db.String(100))  # 章节名称
    word_count = db.Column(db.Integer)  # 字数

    def __init__(self, data):
        self.book_id = int(data['book_id'])
        self.volume_id = int(data['volume_id'])
        self.chapter_id = int(data['chapter_id'])
        self.chapter_name = data['chapter_name']
        self.word_count = int(data['word_count'])
        self.create_time = datetime.now()
        self.update_time = datetime.now()


class BookChapterContent(BaseModel, db.Model):
    """ 书籍章节内容信息 """
    __tablename__ = 'tb_book_chapter_content'
    id = db.Column(db.Integer, primary_key=True)  # ID
    book_id = db.Column(db.Integer)  # 书籍ID
    volume_id = db.Column(db.Integer)  # 卷ID
    chapter_id = db.Column(db.Integer)  # 章节ID
    content = db.Column(MEDIUMTEXT)  # 章节内容

    db.Index('ix_book_id_chapter_id', book_id, chapter_id)

    def __init__(self, data):
        self.book_id = int(data['book_id'])
        self.volume_id = int(data['volume_id'])
        self.chapter_id = int(data['chapter_id'])
        self.content = data['content'].replace('　', '').replace(' ', '')
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def update(self, data):
        self.content = data['content'].replace('　', '').replace(' ', '')
        self.update_time = datetime.now()

