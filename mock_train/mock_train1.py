# coding=utf8
import unittest
from modular import Count
import mock
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from base import base


class TestCount(unittest.TestCase):
    def setUp(self):
        print "parentdir：" + parentdir

    def tearDown(self):
        pass

    def test_add(self):
        file_name = parentdir + "/interface/test_1.json"
        cnt = mock.Mock(name="add", return_value=9)
        load_file = base.Base()
        temp_json = load_file.load(file_name)
        result = cnt(3, 5)
        print temp_json
        if temp_json["mock"] == {}:
            print "hello"
        print result
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
