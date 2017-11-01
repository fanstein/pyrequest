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


def jtl_parse():
    data = {}
    response_time = []
    time_stamp = []
    error_count = 0
    response = ''
    total = 0
    lables = []
    parser = create_parser('re.log')
    for sample in parser.itersamples():
        # response_time.append(t2s(str(sample.elapsed_time)))
        # time_stamp.append(sample.timestamp)
        # error_count = error_count + sample.error_count
        # response = str(sample.timestamp) + ":" + sample.response_data + "\n"
        # total = total+1
        # print len(lables)
        data[sample.label] = {"response_time": response_time}
    # response_time_avg = make_avg(response_time)
    # lables = list(set(lables))
    print data


    # df = pd.DataFrame({"response_time": response_time, "time_stamp": time_stamp},
    #                      columns=["time_stamp", "response_time"])
    # w2e(df, "test.xlsx", u"明细")


def make_avg(l):
    num = len(l)
    sum_l = sum(l)
    avg = sum_l/num
    return round(avg, 2)


def w2e(df, excelFile, sheetName):
    xlsxwriter.Workbook(excelFile)
    # f.to_csv("test.csv", index="false") # 写入csv
    # writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter') # 写入xlsx,但是会覆盖
    writer = pd.ExcelWriter(excelFile, engine='openpyxl') # 这个引擎不会覆盖
    book = load_workbook(excelFile)
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, sheet_name=sheetName)
    writer.save()


def t2s(t):
    x = re.split(':|\.', str(t))
    if len(x) == 4:
        time_stamp = (int(x[0]) * 60 * 60 + int(x[1]) * 60 + int(x[2]) + float('0.' + x[3])) * 1000
    else:
        time_stamp = (int(x[0]) * 60 * 60 + int(x[1]) * 60 + int(x[2])) * 1000
    return time_stamp

if __name__ == '__main__':
    jtl_parse()
    # data = {"sample_1": {"response_time": 12, "time_stamp":111}, "sample_2": {"response_time":13,"time_stamp":112}}
    # df = pd.DataFrame(data, index=["time_stamp", "response_time"], columns=["sample_1", "sample_2"]).T
    # df = pd.DataFrame(data).T
    # print df
    # w2e(df, "test.xlsx", u"明细")