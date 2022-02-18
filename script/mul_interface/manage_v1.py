import unittest

import requests


class workflow_forgetpassword(unittest.TestCase):
    # 用户注册接口
    def test_register(self):
        url = "http://129.211.129.101:9006/user/register.do"
        userinfo = {"username": "ray912",
                    "password": "123456",
                    "email": "12345645374327@qq.com",
                    "phone": "15255554545",
                    "question": "最喜欢的水果",
                    "answer": "苹果"}
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        r = reponse.find("注册成功")
        if r > 0:
            print("用户注册接口测试成功")
        else:
            print("用户注册接口测试失败")

    # 使用已注册的用户登录
    def test_login(self):
        url = "http://129.211.129.101:9006/user/login.do"
        userinfo = {"username": "ray912",
                    "password": "123456"}
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        r = reponse.find("登录成功")
        if r > 0:
            print("用户登录接口测试成功")
        else:
            print("用户登录接口测试失败")

    # 查询用户对于的密保信息
    def test_forgetpassword(self):
        url = "http://129.211.129.101:9006/user/forget_get_question.do"
        userinfo = {"username": "ray912"
                    }
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        r = reponse.find("最喜欢的水果")
        if r > 0:
            print("用户忘记密码提示接口测试成功")
        else:
            print("用户忘记密码提示接口测试失败")

    # 获取已经登录的用户token
    def test_Submitpassword(self):
        url = "http://129.211.129.101:9006/user/forget_check_answer.do"
        userinfo = {"username": "ray912",
                    "question": "最喜欢的水果",
                    "answer": "苹果"
                    }
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        dic = {}
        dic = eval(reponse)
        self.token = dic["data"]
        print(self.token)
        r = reponse.find("data")
        if r > 0:
            print("获取接口token值测试成功")
        else:
            print("获取接口token值测试失败")
        return self.token

    # 用户修改密码接口
    def test_changepassword(self):
        url = "http://129.211.129.101:9006/user/forget_reset_password.do"
        userinfo = {"username": "ray912",
                    "passwordNew": "111111",
                    "forgetToken": self.token}
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        print(self.token)
        r = reponse.find("修改密码成功")
        if r > 0:
            print("用户修改密码接口测试成功")
        else:
            print("用户修改密码接口测试失败")


if __name__ == '__main__':
    unittest.main()
