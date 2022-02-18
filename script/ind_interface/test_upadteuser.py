import unittest
import warnings

import requests


class test_updateuser(unittest.TestCase):

    # 先使用登录接口进行登录
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        url = "http://129.211.129.101:9006/user/login.do"
        userinfo = {"username": "ray0001",
                    "password": "123456"}
        s = requests.Session()
        response = s.post(url, data=userinfo)
        # 获取用户登录成功后的Jsessionid，并赋予self变更为类本身的属性变量
        self.jsessionid = dict(response.cookies)['JSESSIONID']
        print(self.jsessionid)

    # 登录成功后调用信息更新接口进行信息修改
    def test_update(self):
        url = "http://129.211.129.101:9006/user/update_information.do"
        userinfo = {"email": "1552222@qq.com",
                    "phone": "1525521",
                    "answer": "秦砖",
                    "question": "最喜欢的书"}
        # 讲定义好的类属性变量赋值给session，进行JSESSIONID的获取
        session = {"JSESSIONID": self.jsessionid}
        s = requests.Session()
        # 在调用方法时传入所需要的JSESSIONID，进行正常的接口调用
        response = s.post(url, data=userinfo, cookies=session).text
        print(response)


if __name__ == '__main__':
    unittest.main()
