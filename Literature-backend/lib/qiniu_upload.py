from flask import current_app
from qiniu import Auth, put_file, etag



def upload_by_qiniu(image):
    q = Auth(current_app.config["QINIU_AK"], current_app.config["QINIU_SK"])
    #要上传的空间
    bucket_name = 'literature-czl'
    token = q.upload_token(bucket_name)