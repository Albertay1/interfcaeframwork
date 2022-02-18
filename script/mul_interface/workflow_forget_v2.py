import csv
import os
import unittest

import requests


class WorkFlow_Test_v2(unittest.TestCase):
    def setUp(self) -> None:
        path = os.getcwd()
        p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        path1 = p2 + "\\testdatefile\ind_interfile\workflow_test.csv"
        self.file = open(path1, "r")
        path2 = p2 + "\\testdatefile\ind_interfile\work_test.csv"
        self.filename = open(path2, "r")

    def test_interface_test_v2(self):
        table = csv.reader(self.file)
        for row in table:
            # print(row)
            url = row[1]
            expresult = row[3]
            self.interfacename = row[5]
            userinfo = {}
            self.resultdate = {}
            # print(self.resultdate)
            j = int(row[6])
            for i in range(7, j * 2 + 7, 2):
                # print(1)
                userinfo[row[i]] = row[i + 1]
                print(userinfo)
                self.resultdate = {}
                # print(self.resultdate)
                s = requests.Session()
                response = s.post(url, data=userinfo).text
                print(response)
                self.resultdate["接口测试数据"] = response
            # print(self.resultdate)
                r = response.find(expresult)
                if r > 0:
                    print(self.interfacename + "测试通过")
                    self.resultdate["测试结果"] = "测试通过"
                else:
                    print(self.interfacename + "测试失败")
                    self.resultdate["测试结果"] = "测试失败"
            return self.resultdate

    def test_result_test(self):
        for key, value in self.resultdate.items():
            self.filename.write(str(self.interfacename) + "," + key + "," + value + ",")
        self.filename.write("\n")
        self.filename.close()


if __name__ == '__main__':
    unittest.main()


