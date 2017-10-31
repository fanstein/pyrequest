# coding=utf-8
from bs4 import BeautifulSoup
import csv
import os
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
        print each


def jtl_parse():
    response_time = []
    time_stamp = []
    error_count = 0
    response = ''
    parser = create_parser('log.xml')
    for sample in parser.itersamples():
        response_time.append(t2s(str(sample.elapsed_time)))
        time_stamp.append(sample.timestamp)
        error_count = error_count + sample.error_count
        response = str(sample.timestamp) + ":" + sample.response_data + "\n"
    w2e(response_time,time_stamp)


def w2e(response_time, time_stamp):
    f = pd.DataFrame({"response_time": response_time, "time_stamp": time_stamp},
                     columns=["time_stamp", "response_time"])
    # f.to_csv("test.csv", index="false") #写入csv
    # writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter') #写入xlsx,但是会覆盖
    book =load_workbook("test.xlsx")
    writer = pd.ExcelWriter("test.xlsx", engine='openpyxl') #这个引擎不会覆盖
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    f.to_excel(writer, sheet_name='bc')
    writer.save()


def t2s(t):
    x = re.split(':|\.', str(t))
    time_stamp = (int(x[0]) * 60 * 60 + int(x[1]) * 60 + int(x[2]) + float('0.' + x[3])) * 1000
    return time_stamp

if __name__ == '__main__':
    jtl_parse()
