from flask import current_app
from qiniu import Auth, put_data


def upload_by_qiniu(image_data):
    q = Auth(current_app.config["QINIU_AK"], current_app.config["QINIU_SK"])
    bucket_name = current_app.config["QINIU_BUCKETNAME"]
    token = q.upload_token(bucket_name)
    ret, info = put_data(token, None, image_data)
    if info.status_code == 200:
        return ret.get("key")
    else:
        raise Exception("上传七牛失败!")

