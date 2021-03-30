from flask_login import UserMixin
from sqlalchemy.sql import func
from .BaseModel import db, BaseModel
from datetime import datetime


class User(BaseModel, UserMixin, db.Model):
    """ 用户表 """
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    openId = db.Column(db.String(128), unique=True)
    nickName = db.Column(db.String(50))
    gender = db.Column(db.Integer, server_default='0')  # 1 男  0女
    city = db.Column(db.String(50))
    province = db.Column(db.String(50))
    country = db.Column(db.String(50))
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

    def __init__(self, data):
        self.openId = data['openId']
        self.updateInfo(data)

    def updateInfo(self, data):
        self.nickName = data['nickName']
        self.gender = data['gender']
        self.city = data['city']
        self.province = data['province']
        self.country = data['country']
        self.avatarUrl = data['avatarUrl']
        self.update_time = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'openId': self.openId,
            'nickName': self.nickName,
            'gender': self.gender,
            'city': self.city,
            'province': self.province,
            'country': self.country,
            'avatarUrl': self.avatarUrl,

            'preference': self.preference,
            'brightness': self.brightness,
            'fontSize': self.fontSize,
            'background': self.background,
            'turn': self.turn
        }
