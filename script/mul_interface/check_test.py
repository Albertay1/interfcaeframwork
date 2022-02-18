import os
import unittest

import requests
import csv


class check_test(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://129.211.129.101:9006/user/check_vaild.do"
        path = os.getcwd()
        # 通过os方法获取文件的前两级路径
        p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")
        path1 = p2 + "\\testdatefile\ind_interfile\checktest.csv"
        self.file = open(path1, 'r')
        path2 = p2 + "\\testdatefile\ind_interfile\checkresult.csv"
        self.file1 = open(path2, 'w')

    def test_Check(self):
        checkinfo = {}
        table = csv.reader(self.file)
        for row in table:
            checkinfo["str"] = row[0]
            checkinfo["type"] = row[1]
            s = requests.session()
            response = s.post(self.url, data=checkinfo).text
            print(response)
            msg = response.find(row[2])
            if msg > 0:
                print("测试通过")
                self.file1.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + '测试通过' + '\n')
            else:
                print("不通过")
                self.file1.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + '测试失败' + '\n')
        self.file1.close()


if __name__ == '__main__':
    unittest.main()
