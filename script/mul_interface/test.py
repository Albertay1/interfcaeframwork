"""
以文件的方式来进行框架设计
"""
import unittest

if __name__ == '__main__':
    testdir = "./"
    discover = unittest.defaultTestLoader.discover(testdir, pattern="test_case3.py")
    # 声明运行对象进行测试
    runner = unittest.TextTestRunner()
    runner.run(discover)
