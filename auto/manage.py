# coding=utf-8
from __future__ import division
from bs4 import BeautifulSoup
import csv
import os
import xlsxwriter
from xmlutils.xml2csv import xml2csv
from xmlutils.xml2json import xml2json
from jtl import create_parser
from pandas import Series, DataFrame, ExcelWriter
from openpyxl import load_workbook
import numpy as np
import pandas as pd
import time
import re

_this_dir = os.path.dirname(os.path.abspath(__file__))


def get_request():
    fo = open("test.jmx", "r")
    script = fo.read().decode("utf8").encode("GB2312")
    soup = BeautifulSoup(script, "xml")
    ip = soup.HTTPSamplerProxy.find("stringProp", attrs={"name": "HTTPSampler.domain"}).text
    request_text = soup.HTTPSamplerProxy.find("stringProp", attrs={"name": "Argument.value"}).text
    print u"接口ip:" + ip
    print u"报文:" + request_text


def analysis_result():
    converter = xml2csv("log.xml", "log.csv", encoding="utf-8")
    converter.convert(tag="WHATEVER_GOES_HERE_RENDERS_EMPTY_CSV")


def convert_json():
    converter = xml2json("log.xml", encoding="utf-8")
    print converter.get_json()


def self_convert():
    fo = open("log.xml", "r")
    result = fo.read().decode("utf8").encode("GB2312")
    soup = BeautifulSoup(result, "xml")
    for each in soup.find_all("sample"):
        print each["lb"]


def csv_parse():
    obj = pd.read_csv("10-overall-summary.csv")
    obj['start_time'] = obj['timeStamp'] - obj['elapsed']
    temp = obj.groupby(obj["label"])
    test_time = (temp['timeStamp'].max() - temp['start_time'].min())/1000
    throughout = temp['timeStamp'].count()/test_time
    result = temp['elapsed'].agg(['min', 'max', 'mean', 'count'])
    result = DataFrame(result, columns=['min', 'max', 'mean', 'count', 'throughout'])
    result['throughout'] = throughout
    w2e(result, 'result.xlsx', 'temp')


def jtl_parse():
    response_time = []
    time_stamp = []
    start_times = []
    error_count = 0
    response = ''
    threads = []
    lables = []
    parser = create_parser('10-overall-summary.csv')
    for sample in parser.itersamples():
        response_time.append(t2s(str(sample.elapsed_time)))
        time_stamp.append(sample.timestamp)
        lables.append(sample.label)
        threads.append(sample.group_threads)
        start_times.append(sample.timestamp - sample.elapsed_time)
    data = {"response_time": response_time, "time_stamp": time_stamp, "lables": lables, "start_time": start_times}
    obj = pd.DataFrame(data)
    temp = obj.groupby("lables")
    test_time = temp['time_stamp'].max() - temp['start_time'].min()
    throughout = temp['time_stamp'].count()/test_time.astype('timedelta64[ms]')*1000
    result = temp['response_time'].agg(['min', 'max', 'mean', 'count'])
    result = DataFrame(result, columns=['min', 'max', 'mean', 'count', 'throughout'])
    result['throughout'] = throughout
    print result


def w2e(df, excelFile, sheetName):
    xlsxwriter.Workbook(excelFile)
    # f.to_csv("test.csv", index="false") # 写入csv
    # writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter') # 写入xlsx,但是会覆盖
    writer = pd.ExcelWriter(excelFile, engine='openpyxl')  # 这个引擎不会覆盖
    book = load_workbook(excelFile)
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, sheet_name=sheetName)
    writer.save()


def parse_time(dt):
    # 转换成时间数组
    try :
        dt.split('.')[1]
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
    except:
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp


def t2s(t):
    x = re.split(':|\.', str(t))
    if len(x) == 4:
        time_stamp = (int(x[0]) * 60 * 60 + int(x[1]) * 60 + int(x[2]) + float('0.' + x[3])) * 1000
    else:
        time_stamp = (int(x[0]) * 60 * 60 + int(x[1]) * 60 + int(x[2])) * 1000
    return time_stamp


if __name__ == '__main__':
    # jtl_parse()
    # jtl_summary()
    # csv_parse()
    analysis_result()
