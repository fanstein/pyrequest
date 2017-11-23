# coding=utf-8
from __future__ import division
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
from redis import Redis

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


# ! /usr/bin/env python
# -*- coding:utf-8 -*-
# xml 转 json
# xml2json.py
# Version 1.0

from xml.parsers.expat import ParserCreate
import json


class Xml2Json:
    LIST_TAGS = ['COMMANDS']

    def __init__(self, data=None):
        self._parser = ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.CharacterDataHandler = self.data
        self.result = None
        if data:
            self.feed(data)
            self.close()

    def feed(self, data):
        self._stack = []
        self._data = ''
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1)
        del self._parser

    def start(self, tag, attrs):
        assert attrs == {}
        assert self._data.strip() == ''
        self._stack.append([tag])
        self._data = ''

    def end(self, tag):
        last_tag = self._stack.pop()
        assert last_tag[0] == tag
        if len(last_tag) == 1:  # leaf
            data = self._data
        else:
            if tag not in Xml2Json.LIST_TAGS:
                # build a dict, repeating pairs get pushed into lists
                data = {}
                for k, v in last_tag[1:]:
                    if k not in data:
                        data[k] = v
                    else:
                        el = data[k]
                        if type(el) is not list:
                            data[k] = [el, v]
                        else:
                            el.append(v)
            else:  # force into a list
                data = [{k: v} for k, v in last_tag[1:]]
        if self._stack:
            self._stack[-1].append((tag, data))
        else:
            self.result = {tag: data}
        self._data = ''

    def data(self, data):
        self._data = data


if __name__ == '__main__':
    xml = open("D:\\Users\\fanp\\Desktop\\test_script.jmx", 'r').read()
    result = Xml2Json(xml).result
    print result
    # outputfile = open("京东手机列表_1.json", 'w', encoding='UTF-8')
    # outputfile.write(str(result))
    # outputfile.close()

