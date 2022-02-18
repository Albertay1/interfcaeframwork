import os
import unittest

import requests
import csv


class test_register(unittest.TestCase):
    def setUp(self) -> None:
        path = os.getcwd()
        self.p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        path1 = self.p2 + "\\testdatefile\ind_interfile\\register.csv"
        self.file = open(path1, 'r')
        path2 = self.p2 + "\\testdatefile\ind_interfile\\register_restule.csv"
        self.file2 = open(path2, 'w')
        self.url = "http://129.211.129.101:9006/user/register.do"

    def test_case(self):
        table = csv.reader(self.file)
        userinfo = {}
        for ray in table:
            userinfo["username"] = ray[0]
            userinfo["password"] = ray[1]
            userinfo["email"] = ray[2]
            userinfo["phone"] = ray[3]
            userinfo["question"] = ray[4]
            userinfo["answer"] = ray[5]

            respones = requests.post(self.url, data=userinfo).text
            print(respones)
            print(userinfo)
            msg = respones.find(ray[6])
            if msg > 0:
                print("接口测试通过")
                self.file2.write(ray[0] + "," + ray[1] + "," + ray[2] + "," + ray[3] + ','
                                 + ray[4] + ',' + ray[5] + ',' + ray[6] + ',' + "测试通过" + "\n")
            else:
                print("接口测试不通过")
                self.file2.write(ray[0] + "," + ray[1] + "," + ray[2] + "," + ray[3] + ','
                                 + ray[4] + ',' + ray[5] + ',' + ray[6] + ',' + "测试不通过" + "\n")
        self.file2.close()


if __name__ == '__main__':
    unittest.main()
