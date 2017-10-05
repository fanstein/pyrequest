# coding=utf8
import unittest
from modular import Count
import mock


class TestCount(unittest.TestCase):
    def test_add(self):
        count = Count()
        cnt = mock.Mock(name="add", return_value=9)
        result = cnt(3, 5)
        print result
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
