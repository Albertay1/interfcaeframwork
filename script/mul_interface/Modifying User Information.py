import requests


class Modifying_user_update():

    # 用户注册接口
    def test_register(self):
        url = "http://129.211.129.101:9006/user/register.do"
        userinfo = {"username": "ray9112",
                    "password": "123456",
                    "email": "1234564327@163.com",
                    "phone": "15255554511",
                    "question": "最喜欢看的书",
                    "answer": "秦砖"}
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
        userinfo = {"username": "ray9112",
                    "password": "123456"}
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        r = reponse.find("登录成功")
        if r > 0:
            print("用户登录接口测试成功")
        else:
            print("用户登录接口测试失败")

    # 用户登录后获取用户的信息
    def test_get_information(self):
        url = "http://129.211.129.101:9006/user/get_information.do"
        userinfo = {}
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        r = reponse.find("成功获取用户信息")
        if r > 0:
            print("获取用户信息接口测试成功")
        else:
            print("获取用户信息接口测试失败")

    # 获取已经登录的用户token
    def test_update_information(self):
        url = "http://129.211.129.101:9006/user/update_information.do"
        userinfo = {"email": "1234564327@163.com",
                    "phone": "123456432",
                    "answer": "苹果",
                    "question": "最喜欢的水果"
                    }
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        dic = {}
        dic = eval(reponse)
        token = dic["data"]
        print(token)
        r = reponse.find("data")
        if r > 0:
            print("获取接口token值测试成功")
        else:
            print("获取接口token值测试失败")
        return token

    # 用户修改密码接口
    def test_changepassword(self, token):
        url = "http://129.211.129.101:9006/user/forget_reset_password.do"
        userinfo = {"username": "ray912",
                    "passwordNew": "111111",
                    "forgetToken": token}
        s = requests.Session()
        reponse = s.post(url, data=userinfo).text
        print(reponse)
        print(token)
        r = reponse.find("修改密码成功")
        if r > 0:
            print("用户修改密码接口测试成功")
        else:
            print("用户修改密码接口测试失败")


if __name__ == '__main__':
    modifyingobj = Modifying_user_update()
    # modifyingobj.test_register()
    modifyingobj.test_login()
    modifyingobj.test_get_information()
