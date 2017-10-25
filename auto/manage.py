# coding=utf-8
from bs4 import BeautifulSoup
import csv
import os
import xmlutils

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
    pass

