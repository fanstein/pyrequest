# coding=utf-8
import os
import errno
import subprocess
import time
from string import Template

currpath = os.path.dirname(os.path.realpath(__file__))

JmxTemlFileName = "D:/Users/fanp/Desktop/jp@gc - Dummy Sampler.jmx"

JMETER_Home = "D:/apache-jmeter-3.3/bin/jmeter.bat"

path = u'性能测试项目'

def getDateTime():
    '''
    获取当前日期时间，格式'20150708085159'
    '''
    return time.strftime(r'%Y%m%d%H%M%S', time.localtime(time.time()))


def execcmd(command):
    print "command " + command

    output = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
        universal_newlines=True)

    stderrinfo, stdoutinfo = output.communicate()
    print "stderrinfo " + stderrinfo
    print "stdoutinfo " + stdoutinfo
    print "returncode={0}".format(output.returncode)


def execjmxs(Num_Threads, Loops):
    tmpstr = ''
    mkdir()
    with open(JmxTemlFileName, "r") as file:
        tmpstr = Template(file.read()).safe_substitute(
            num_threads=Num_Threads,
            loops=Loops
        )
    now = getDateTime()
    tmpjmxfile = os.path.join(currpath , path , "/script/T{0}XL{1}{2}.jmx".format(Num_Threads, Loops, now))
    with open(tmpjmxfile, "w+") as file:
        file.writelines(tmpstr)
    csvfilename = currpath +path + "/result/result{0}.csv".format(now)
    htmlreportpath = currpath + path + "/result/htmlreport{0}".format(now)
    if not os.path.exists(htmlreportpath):
        os.makedirs(htmlreportpath)
    execjmxouthtml = "cmd.exe /c {JMETER_Home} -n -t {tmpjmxfile} -l {csvfilename} -e -o {htmlreportpath}"\
    .format(JMETER_Home=JMETER_Home, tmpjmxfile=tmpjmxfile, csvfilename=csvfilename, htmlreportpath=htmlreportpath)
    execcmd(execjmxouthtml)


def mkdir():
    currpath = os.path.dirname(os.path.realpath(__file__))
    path = u'性能测试项目'
    folders = ['script','reuslt']
    for each in folders:
        try:
            os.makedirs(os.path.join(currpath, path, each))
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

jobs = [dict(Num_Threads=x * 10, Loops=10) for x in range(2, 3)]
[execjmxs(x["Num_Threads"], x["Loops"]) for x in jobs]
