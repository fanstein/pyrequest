# coding=utf8
import time

def ds_asyncore(callback):
    i = 0
    while True:
        callback(i)
        print i
        i = i + 1


if __name__ == "__main__":
    def callback(res):
        time.sleep(10)
        print res


    ds_asyncore(callback)
