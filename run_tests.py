# -*- coding: utf-8 -*-
import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data
from base import base,requests_base



# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './model_script'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据
    file_list = ["test_2.json", "test_2.json"]
    base.Base.write_test(file_list)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()