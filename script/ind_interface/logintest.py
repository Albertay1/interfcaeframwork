import os
import unittest

import requests
import csv


class login_test(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://129.211.129.101:9006/user/login.do"
        path = os.getcwd()
        self.p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        print(self.p2)
        path1 = self.p2 + str("\\testdatefile\ind_interfile\login.csv")
        self.file = open(path1, "r")
        path2 = self.p2 + str("\\testdatefile\ind_interfile\\testresult.csv")
        print(path2)
        self.file2 = open(path2, "w")

    def test_case1(self):

        table = csv.reader(self.file)

        # 脚本要实现的功能：
        # 1.调用接口

        for row in table:
            self.userinfo = {"username": row[0],
                             "password": row[1]}
            self.restule = row[2]
            self.user = row[0]
            self.password = row[1]
            print(self.user, self.user, self.password, self.restule)

            respones = requests.post(self.url, data=self.userinfo).text
            print(respones)
            print(self.userinfo)
            # 2.传入接口参数
            # 3.获取响应结果
            # 4.进行比对，得出测试结论
            msg = respones.find(self.restule)
            if msg > 0:
                print("登录成功，测试通过")
                self.file2.write(self.user + ',' + self.password + ',' + self.restule + ',' + "测试通过" + "\n")
            else:
                print("登录成功，测试不通过")
                self.file2.write(self.user + ',' + self.password + ',' + self.restule + ',' + "测试不通过" + "\n")
        self.file2.close()


if __name__ == '__main__':
    unittest.main()
