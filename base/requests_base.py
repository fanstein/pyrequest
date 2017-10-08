# coding=utf8

import requests


class RequestBase(object):

    @staticmethod
    def request_get(url):
        response = requests.request("GET", url)
        return response

    @staticmethod
    def request_post(url, querystring, headers):
        response = requests.request("POST", url, headers=headers, params=querystring)
        return response




