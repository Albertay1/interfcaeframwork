import unittest


class test_case3(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp初始化")

    def test_case1(self):
        print("登录接口")

    def test_case2(self):
        print("注册接口")

    def tearDown(self) -> None:
        print("tearDown资源回收")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(test_case3("test_case1"))
    # suite.addTest(test_case3("test_case2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
