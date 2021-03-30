from .BaseModel import BaseModel, db


class BrowseHistory(BaseModel, db.Model):
    """ 浏览记录 """
    __tablename__ = 'tb_browse_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('tb_book.book_id'))
    book = db.relationship('Book', uselist=False)
