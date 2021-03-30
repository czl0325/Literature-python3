# coding:utf-8
from flask import jsonify

class RET:
    OK = "0"
    DBERR = "4001"
    NODATA = "4002"
    DATAEXIST = "4003"
    UNKOWNERR = "4501"


error_map = {
    RET.OK: u"成功",
    RET.DBERR: u"数据库查询错误",
    RET.NODATA: u"无数据",
    RET.DATAEXIST: u"数据已存在",
    RET.UNKOWNERR: u"未知错误",
}


class ResponseData(object):
    code = RET.OK
    msg = error_map[RET.OK]
    data = None

    def __init__(self, code, data=None):
        self.code = code
        self.data = data

    @property
    def code(self):
        return self.code

    @code.setter
    def code(self, value):
        if not error_map[value]:
            self.msg = '未知错误'
        self.msg = error_map[value]

    def to_dict(self):
        return jsonify({'code': self.code, 'msg': self.msg, 'data': self.data})