# coding=utf8
import sys, os
import unittest
import mock
import ddt
from base import base, requests_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

file_name = base.Base.read_test()


@ddt.ddt
class ModelTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*file_name)
    def test_model(self, filename):
        response = ""
        # print "start"
        fname = parentdir + "/interface/" + filename
        base_ = base.Base()
        temp_json = base_.load(fname)
        assert_string = temp_json["assert"]["string"]
        if temp_json["request"]["method"].lower() == "get":
            url = temp_json["request"]["url"]
            response = requests_base.RequestBase.request_get(url)
            # print response.text
        if temp_json["request"]["method"].lower() == "post":
            url = temp_json["request"]["url"]
            querystring = temp_json["request"]["querystring"]
            headers = temp_json["request"]["headers"]
            response = requests_base.RequestBase. \
                request_post(url=url, querystring=querystring, headers=headers)
        self.assertIn(assert_string, response.text)


if __name__ == "__main__":
    unittest.main()
