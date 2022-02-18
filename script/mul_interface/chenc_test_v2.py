import csv
import unittest

import requests


class check_test_v2(unittest.TestCase):
    def setUp(self) -> None:
        # 初始化部分需要的参数，用来进行后续的代码执行
        self.url = "http://129.211.129.101:9006/user/check_vaild.do"
        self.file = open("../../testdatefile/ind_interfile/checktest.csv", 'r')
        self.file1 = open("../../testdatefile/ind_interfile/checkresult.csv", 'w')

    def test_check_v2(self):
        checkinfo = {}
        table = csv.reader(self.file)
        for row in table:
            checkinfo["str"] = row[0]
            checkinfo["type"] = row[1]
            s = requests.session()
            response = s.post(self.url, data=checkinfo).text
            print(response)
            # 通过assertIn函数进行测试结果的判断
            self.assertIn(row[2], str(response))

    def tearDown(self) -> None:
        # 继承类中的文件方法，用来关闭打开的两个文件
        self.file.close()
        self.file1.close()


if __name__ == '__main__':
    """
    以main函数的方式直接调用
    """
    # unittest.main()
    """
    以测试套的方式调用
    """
    # suite = unittest.TestSuite()
    # suite.addTest(check_test_v2("test_case3"))
    # # 声明运行对象
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    """
    以文件的方式来进行框架设计
    """
    testdir = "./"
    discover = unittest.defaultTestLoader.discover(testdir, pattern="test_case3.py")
    # 声明运行对象进行测试
    runner = unittest.TextTestRunner()
    runner.run(discover)
