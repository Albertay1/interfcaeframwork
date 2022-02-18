import os
import unittest

import requests
import csv


class manage_test(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://129.211.129.101:9006/manage/user/login.do"

    def test_Manage(self):
        self.manageinfo = {}
        path = os.getcwd()
        p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        path1 = p2 + "\\testdatefile\ind_interfile\manage2.csv"
        file = open(path1, "r")
        path2 = p2 + "\\testdatefile\ind_interfile\manage2restule.csv"
        file1 = open(path2, "w")
        table = csv.reader(file)
        for row in table:
            self.manageinfo["username"] = row[0]
            self.manageinfo["password"] = row[1]
            s = requests.session()
            response = s.post(self.url, data=self.manageinfo).text
            print(response)
            msg = response.find(row[2])
            if msg > 0:
                print("测试通过")
                file1.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + "测试通过" + '\n')
            else:
                print("测试不通过")
                file1.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + "测试不通过" + '\n')
        file1.close()


if __name__ == '__main__':
    unittest.main()
