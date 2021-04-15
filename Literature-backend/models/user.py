from flask_login import UserMixin
from sqlalchemy.sql import func
from .BaseModel import db, BaseModel
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask import current_app


book_shelf = db.Table(
    'tb_book_shelf',
    db.Column('book_id', db.Integer, db.ForeignKey("tb_book.book_id"), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey("tb_user.id"), primary_key=True)
)


class User(BaseModel, UserMixin, db.Model):
    """ 用户表 """
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    openId = db.Column(db.String(128), unique=True)
    userName = db.Column(db.String(16), unique=True)
    password_hash = db.Column(db.String(256))
    gender = db.Column(db.Integer, server_default='0')  # 1 男  0女
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    avatarUrl = db.Column(db.String(128))

    # 阅读器配置
    preference = db.Column(db.Integer, server_default='0')  # 1 男  0女
    brightness = db.Column(db.Integer, server_default='30')  # 10~100 亮度
    fontSize = db.Column(db.Integer, server_default='14')  # 字号
    background = db.Column(db.String(10), server_default='B1')  # B1 ~ B6 内置背景
    turn = db.Column(db.String(10), server_default='T1')  # T1 仿真 T2 平滑 T3 无 翻页模式

    last_read = db.Column(db.Integer)  # 最后阅读一本书
    last_read_chapter_id = db.Column(db.Integer)  # 最后阅读一本书的章节id

    create_time = db.Column(db.DateTime, server_default=func.now())
    update_time = db.Column(db.DateTime, server_default=func.now())
    is_delete = db.Column(db.Boolean, default=False)

    book_shelf = db.relationship('Book', secondary=book_shelf)

    def __init__(self, data):
        self.updateInfo(data)

    def updateInfo(self, data):
        if hasattr(data, 'openId'):
            self.openId = data['openId']
        self.userName = data['userName']
        self.password = data['password']
        self.gender = data['gender']
        self.province = data['province']
        self.city = data['city']
        self.district = data['district']
        self.avatarUrl = data['avatarUrl']
        if hasattr(data, 'id'):
            self.update_time = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'openId': self.openId,
            'userName': self.userName,
            'gender': self.gender,
            'province': self.province,
            'city': self.city,
            'district': self.district,
            'avatarUrl': self.avatarUrl if self.avatarUrl.startswith('http') else current_app.config['QINIU_URLPREFIX'] + self.avatarUrl,

            'preference': self.preference,
            'brightness': self.brightness,
            'fontSize': self.fontSize,
            'background': self.background,
            'turn': self.turn
        }

    @property
    def password(self):
        raise AttributeError('该参数只能设置,不能读取')
        pass

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

