# coding=utf8
import json
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class Base(object):
    def load(self, file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def write_test(file_list):
        global f
        name = parentdir + "/db_fixture/need_test"
        if os.path.exists(name):
            os.remove(name)
        try:
            f = open(name, 'a')
            for each in file_list:
                f.write(each)
                f.write('\n')
        finally:
            if f:
                f.close()

    @staticmethod
    def read_test():
        name = parentdir + "/db_fixture/need_test"
        rs = []
        for ln in file(name, 'rt'):
            rs.extend(ln.strip().split(' '))
        return rs


if __name__ == "__main__":
    print Base.read_test()
