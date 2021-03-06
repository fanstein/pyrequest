# coding=utf-8
from __future__ import division

import getopt

import sys
from bs4 import BeautifulSoup
import csv
import os, errno
import xlsxwriter
from xmlutils.xml2csv import xml2csv
from xmlutils.xml2json import xml2json
from jtl import create_parser
from pandas import Series, DataFrame, ExcelWriter, np
from openpyxl import load_workbook
import numpy as na
import pandas as pd
import time
import re
from datetime import datetime, timedelta

# obj = Series([4, 7, -5, 3])
# print obj.values
# print obj.index
# obj2 = Series([4, 7, -5, 3], index=['a','b','c','d'])
# print obj2.index, obj2['a'], obj2[['a', 'b']]

# print obj2[obj2 > 0]
# print np.exp(obj2)

# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
# 'year': [2000, 2001, 2002, 2001, 2002],
# 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
#      index=['one', 'two', 'three', 'four', 'five'])
# print frame2
# print frame2[frame2['year']>2001]
# print obj
# print obj[obj["threadName"] == '线程组 1-3'].elapsed.head(3)
# print obj[obj["threadName"] == '线程组 1-3'].elapsed.head(3).value_counts()

# obj = pd.read_csv("10-overall-summary.csv")
# # throughout = obj.groupby(obj["threadName"])['elapsed'].count()/(obj.groupby(obj["threadName"])['elapsed'].mean()/1000)
# # throughout = throughout.to_frame()
# ela= obj.groupby(obj["threadName"])['elapsed']
# f = lambda x: x.count()/x.mean()*1000
# print ela.apply(f)
# res = obj.groupby(obj["threadName"])['elapsed'].agg(['min', 'max', 'mean', 'count', ])

# df = DataFrame(res, columns=['min', 'max', 'mean', 'count', 'throughout'])
# print throughout
# df['throughout'] = throughout

# df = pd.merge(res, throughout, left_on='threadName', right_index=True)
# print df



# pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# frame3 = DataFrame(pop)
# print frame3
# frame3.index.name = 'year'
# frame3.columns.name = 'state'
# print frame3.values
# !/usr/bin/python
# coding :utf-8
from string import Template


class MyTemplate(Template):
    """docstring for MyTemplate"""
    delimiter = '#'


def _test():
    s = '#who likes #what'
    t = MyTemplate(s)
    d = {'who': 'jianpx', 'what': 'mac'}
    print t.substitute(d)
    print MyTemplate.delimiter
    print Template.delimiter


def mkdir():
    currpath = os.path.dirname(os.path.realpath(__file__))
    path = 'PerformanceTest'
    folders = ['script','reuslt']
    for each in folders:
        try:
            os.makedirs(os.path.join(currpath, path, each))
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


def test1():
    for each in range(5):
        print "a"
        time.sleep(1)


def test2():
    for each in range(5):
        print "b"
        time.sleep(1)

def multi():
    from multiprocessing import Pool
    for i in range(2):
        p = Pool(2)
        print i
        p.apply_async(test1)
        p.apply_async(test2)
        p.close()
        p.join()



def usage():
    print "usage"

def do():
    opts, args = getopt.getopt(sys.argv[1:], "hi:t:", ["version", "file="])
    input_file = ""
    output_file = ""
    for op, value in opts:
        if op == "-i":
            input_file = value
            for each in value.split(","):
                print each
        elif op == "-t":
            output_file = value
            for each in value.split(","):
                print each
        elif op == "-h":
            usage()
        elif op == "--version":
            print "version 1.0"
            sys.exit()
    print input_file, output_file


def get_jmx():
    jmx_file = []
    script_jmx = ''
    _this_dir = os.path.dirname(os.path.abspath(__file__))
    l = os.listdir(_this_dir)
    for i in l:
        if os.path.splitext(i)[1] == '.jmx':
            jmx_file.append(i)
    print jmx_file
    if len(jmx_file) >1:
        i = input(u"选择文件(1,2,3):")
        script_jmx = jmx_file[i-1]
    print script_jmx
    return script_jmx


def generator_function():
    for i in range(10):
        yield i


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def test():
    return 'hh'

@logit()
def myfunc1():
    pass


# 外汇储备
if __name__ == '__main__':
    l1 = [-1,-2,3,4]
    l = [x+1 for x in l1 if x >2]
    from pprint import pprint

    import urllib2

    response = urllib2.urlopen("http://www.baidu.com")
    print response.read()




