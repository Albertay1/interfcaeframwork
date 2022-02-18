import unittest

import requests


class register_test(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://129.211.129.101:9006/user/register.do"
        self.userinfo = {"username": "ray0001",
                         "password": "123456",
                         "email": "7981310@qq.com",
                         "phone": "152645124",
                         "question": "最喜欢看的书",
                         "answer": "秦制度两千年"}

    def test_register(self):
        s = requests.session()
        response = s.post(self.url, data=self.userinfo).json()
        print(response)
        self.assertIn("注册成功", str(response))


if __name__ == "__main__":
    unittest.main()
