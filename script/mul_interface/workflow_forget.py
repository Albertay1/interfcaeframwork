import csv
import os
import unittest

import requests


class WorkFlow_Test_v1(unittest.TestCase):
    def setUp(self) -> None:
        path = os.getcwd()
        self.p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        path1 = self.p2 + "\\testdatefile\ind_interfile\workflow_test.csv"
        self.file = open(path1, "r")

    def test_interface(self):
        table = csv.reader(self.file)
        for row in table:
            self.url = row[1]
            self.expresult = row[3]
            self.interfacename = row[5]
            print(self.url, "+", self.expresult, "+", self.interfacename)
            self.userinfo = {}
            j = int(row[6])
            for i in range(7, j * 2 + 7, 2):
                self.userinfo[row[i]] = row[i + 1]
                print(self.userinfo)
                resultdate = {}
                s = requests.Session()
                response = s.post(self.url, data=self.userinfo).text
                print(response)
                r = response.find(self.expresult)
                if r > 0:
                    print(self.interfacename + "测试通过")
                else:
                    print(self.interfacename + "测试失败")

            # def result_request(self, resultdate, reportfilename):
            #     file = open(reportfilename, "a")


if __name__ == '__main__':
    unittest.main()
