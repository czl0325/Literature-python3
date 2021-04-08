class BaseConfig(object):
    DEBUG = None
    # jwt的密钥
    SECRET_KEY = "czl"
    JWT_EXPIRE_TIME = 24
    # 数据库的连接信息
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:111@localhost/Literature'
    # 动态追踪修改，如果未配置，只会提示警告信息，不影响代码的业务逻辑
    # 如果True，会跟踪数据库信号的变化，对计算机的性能有一定的影响，如果False，不会跟踪数据库信号变化。
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    QINIU_AK = "_k1OYVrwNoF0ALCVhmlVv89pDSbIJD5GzPlXXzej"
    QINIU_SK = "UysGleEpeyUrIdgYAifuxKyZj9qhlzqNOgWGAdeY"
    QINIU_BUCKETNAME = "literature-czl"
    QINIU_URLPREFIX = "http://qqvpxfcfz.hn-bkt.clouddn.com/"


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(BaseConfig):
    pass


config_dict = {
    'base_config':  BaseConfig,
    'dev_config':   DevConfig,
    'prod_config':  ProdConfig
}