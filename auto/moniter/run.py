import time
import os
import errno
import subprocess
import time
from string import Template
import platform


def execcmd(command):
    print "command " + command

    output = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
        universal_newlines=True)

    stderrinfo, stdoutinfo = output.communicate()
    print "stderrinfo " + stderrinfo
    print "stdoutinfo " + stdoutinfo
    print "returncode={0}".format(output.returncode)


if __name__ == '__main__':
    execcmd('fab start')
