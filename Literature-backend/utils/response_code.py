# coding:utf-8
from flask import jsonify

class RET:
    OK = "0"
    DBERR = "4001"
    NODATA = "4002"
    DATAEXIST = "4003"
    NOPARAMS = "4004"
    PARAMERROR = "4005"
    TOKENERROR = "4100"
    THIRDPARTYERROR = "4200"
    UNKOWNERR = "4501"


error_map = {
    RET.OK: u"成功",
    RET.DBERR: u"数据库查询错误",
    RET.NODATA: u"无数据",
    RET.DATAEXIST: u"数据已存在",
    RET.NOPARAMS: u"缺少必要参数",
    RET.PARAMERROR: u"参数有误",
    RET.TOKENERROR: u"token过期",
    RET.THIRDPARTYERROR: u"第三方库报错",
    RET.UNKOWNERR: u"未知错误",
}


class ResponseData(object):
    def __init__(self, code, data=None):
        self.code = code
        self.data = data

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = int(value)
        if not error_map[value]:
            self.message = '未知错误'
        self.message = error_map[value]

    def to_dict(self):
        return jsonify({'code': self._code, 'message': self.message, 'data': self.data})