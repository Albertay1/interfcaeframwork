import os
import unittest

import requests
import csv


class manage_test(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://129.211.129.101:9006/manage/user/login.do"

    def test_case(self):
        path = os.getcwd()
        p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        path1 = p2 + "\\testdatefile\ind_interfile\manage_text.csv"
        file = open(path1, "r")
        path2 = p2 + "\\testdatefile\ind_interfile\manage_restule.csv"
        file1 = open(path2, "w")
        # file = open("../date_test/manage_text.csv", "r")
        # file1 = open("manage_restule.csv", "w")
        adminuser = {}
        table = csv.reader(file)
        for row in table:
            adminuser["username"] = row[0]
            adminuser["password"] = row[1]
            respones = requests.post(self.url, data=adminuser).text
            print(respones)
            msg = respones.find(row[2])
            if msg > 0:
                file1.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + '测试通过' + "\n")
                print("测试通过")
            else:
                file1.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + '不通过' + "\n")
                print("不通过")
        file1.close()


if __name__ == '__main__':
    unittest.main()
