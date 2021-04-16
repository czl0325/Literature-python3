from .BaseModel import BaseModel, db


class SearchKeyWord(BaseModel, db.Model):
    """ 搜索关键词 """
    __tablename__ = 'tb_search_keyword'
    id = db.Column(db.Integer(), primary_key=True)
    keyword = db.Column(db.String(100))
    count = db.Column(db.Integer(), default=0)
    is_hot = db.Column(db.Boolean, default=False)

    def keys(self):
        return 'id', 'keyword', 'count'

    def __getitem__(self, item):
        return getattr(self, item)