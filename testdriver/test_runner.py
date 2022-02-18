import unittest

if __name__ == '__main__':
    testdir = "F:\interfcaeframwork\script\ind_interface"
    descover = unittest.defaultTestLoader.discover(testdir, pattern="test_update_v3.py")
    runner = unittest.TextTestRunner()
    runner.run(descover)
