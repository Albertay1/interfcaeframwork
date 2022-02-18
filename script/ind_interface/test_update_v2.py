import csv
import os
import unittest
import warnings

import requests


class test_updateuser(unittest.TestCase):

    # 先使用登录接口进行登录
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        # 获取文件所在的路径
        path = os.getcwd()
        # 通过os方法获取文件的前两级路径
        p2 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
        print(p2)
        # 将获取的路径和框架文件结构相结合从而获取到想要的文件路径
        self.path1 = p2 + r"\testdatefile\ind_interfile\test_updateuser.csv"
        userinfo = {}
        # 打开已经定义好的类的变量path1，获取文件内的信息
        file = open(self.path1, "r")
        table = csv.reader(file)
        for row in table:
            url = row[0]
            userinfo[row[3]] = row[4]
            userinfo[row[5]] = row[6]
            break
        s = requests.Session()
        print(userinfo)
        response = s.post(url, data=userinfo)
        # 获取用户登录成功后的Jsessionid，并赋予self变更为类本身的属性变量
        self.jsessionid = dict(response.cookies)['JSESSIONID']
        print(self.jsessionid)

    # 登录成功后调用信息更新接口进行信息修改
    def test_update(self):
        # 将类中共用的实例path1文件再次打开以便读取数据
        file1 = open(self.path1, "r")
        talble = csv.reader(file1)
        userinfo = {}
        num = 0
        for row in talble:
            num = num + 1
            # 增加一个mun用于跳过第一行，mun大于几就等于跳过前面几行
            if num > 1:
                url = row[0]
                # print(url)
                expresule = row[1]
                # 定义两个变量获取userinfo内的数据内容，方便进行测试验证
                j = int(row[2])
                for i in range(3, j * 2 + 3, 2):
                    userinfo[row[i]] = row[i + 1]
                print(userinfo)
                # 讲定义好的类属性变量赋值给session，进行JSESSIONID的获取
                session = {"JSESSIONID": self.jsessionid}
                s = requests.Session()
                # 在调用方法时传入所需要的JSESSIONID，进行正常的接口调用
                response = s.post(url, data=userinfo, cookies=session).text
                print(response)
                userinfo = {}
                # 使用判断函数替代if语句进行结果验证
                self.assertIn(expresule, response)
                # 通过find函数对比已编写好的验证信息，判断测试结果
                # msg = response.find(expresule)
                # if msg > 0:
                #     print("测试通过")
                # else:
                #     print("测试失败")


if __name__ == '__main__':
    unittest.main()
