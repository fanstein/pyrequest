# coding=utf-8

from pandas import Series, DataFrame
import pandas as pd
import csv
import re

# s = Series([100, "python", "soochow", "qiwsir"])
# print s[0]


# sd = {"python":800, "c++":8100, "c#":4000}
# s4 = Series(sd)
# print s4
#
# print pd.isnull(s4)
#
# csv_reader = csv.reader(open("log.csv"))
# for row in csv_reader:
#     print row


# marks = pd.read_csv("log.csv")
# print marks
# print marks.columns
# print marks.index

# data = {"name":["yahoo","google","facebook"],"marks":[200,400,122],"price":[9,3,7]}
# f1 = DataFrame(data)
# f1.to_csv("test.csv", index=False, sep=',')
# print f1

#
# t = '0:00:01.171010'
# x = re.split(':|\.',t)
# time_stamp = (int(x[0])*60*60+int(x[1])*60+int(x[2])+float('0.'+x[3]))*1000
# print time_stamp

