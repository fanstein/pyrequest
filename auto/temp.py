# coding=utf-8
from __future__ import division
from bs4 import BeautifulSoup
import csv
import os
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


# obj = Series([4, 7, -5, 3])
# print obj.values
# obj2 = Series([4, 7, -5, 3], index=['a','b','c','d'])
# print obj2[obj2 > 0]
# print np.exp(obj2)
obj = pd.read_csv("10-overall-summary.csv")
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
# 'year': [2000, 2001, 2002, 2001, 2002],
# 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
#      index=['one', 'two', 'three', 'four', 'five'])
# print frame2
# print frame2[frame2['year']>2001]
# print obj
print obj[obj["threadName"] == '线程组 1-3'].elapsed.head(3)
print obj[obj["threadName"] == '线程组 1-3'].elapsed.head(3).value_counts()

throughout = obj.groupby(obj["threadName"])['elapsed'].count()/obj.groupby(obj["threadName"])['elapsed'].mean()

re = obj.groupby(obj["threadName"])['elapsed'].agg(['min', 'max','mean','count'])
print "ss:"

print re
print pd.merge(throughout,re)
