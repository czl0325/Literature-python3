import requests
import WXBizDataCrypt

AppID = "wx1b2f5daa9d11bf8f"
AppSecret = "7007076baf023fa30cb9a76dfd573ca7"


def get_wx_session_key(code):
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(AppID, AppSecret, code)
    data = requests.get(url).json()
    return data


def get_user_info(encryptedData, iv, session_key):
    pc = WXBizDataCrypt(AppID, session_key)
    return pc.decrypt(encryptedData, iv)
