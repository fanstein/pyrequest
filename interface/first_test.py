# coding=utf8
import unittest
import requests
import os, sys
import mock

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import ddt


@ddt.ddt
class FirstTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(200, 300, 400)
    def test_firstcase(self, param):
        url = "https://612ab671-fe29-43ce-a1da-eaf2befd7ca8.mock.pstmn.io/frt-newshopping-engine-ws/api/recommend/xml/PostPositiveXSearch"
        payload = "11"
        headers = {
            'x-mock-response-code': "200",
            'cache-control': "no-cache",
            'postman_api_key': '5502d55b75c84b3ebb7064c55a4462e4'
        }

        r = requests.request("POST", url, data=payload, headers=headers)
        r = mock.Mock(name="test", return_value="this is mock")
        # print r.text
        # self.result = r.status_code
        # self.assertEqual(self.result, param)
        res = r()
        self.assertEqual(res, 'this is Post')
        # print param


if __name__ == '__main__':
    # test_data.init_data() # 初始化接口测试数据
    unittest.main()
