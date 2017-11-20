# coding=utf8
from fabric.api import *
import time

env.hosts = ['10.3.6.15']
env.user = 'root'  # 多台主机用户名密码相同可以只写一次
env.password = '123.Ctrip'
env.shell = "/bin/bash -c"
env.warn_only = True


# 打包
@runs_once  # 该装饰器表示只执行一次，没有的话默认每台主机都执行一次
def task_tar():  # 该场景本地文件打包本身就只需要执行一次
    with lcd('/home/python/test'):
        local('tar zcvf test.tar.gz test.py')


# 上传
def task_upload():
    run('mkdir -p /root/Desktop/ff')
    put('ServerAgent-2.2.3.zip', '/root/Desktop/ff/ServerAgent-2.2.3.zip')


# 验证md5
def task_md5():
    # 计算本地的md5
    local_md5 = local('md5sum /home/python/test/test.tar.gz', capture=True).split('  ')[0]
    # 计算远程主机md5
    remote_md5 = run('md5sum /home/python/temp/test.tar.gz').split('  ')[0]
    print(local_md5)
    print(remote_md5)
    if remote_md5 == local_md5:
        print('上传成功')
    else:
        print('上传出错')


# 解包并执行
def task_exc():
    with cd('/root/Desktop/ff'):
        run('unzip ServerAgent-2.2.3.zip')
        run('rm -rf ServerAgent-2.2.3.zip')
        run('(nohup sh /root/Desktop/ff/ServerAgent-2.2.3/startAgent.sh &) && sleep 1')
        time.sleep(3600)
        run('pkill -f CMDRunner.jar')
        # pid = run('pgrep -f CMDRunner.jar')
        # run('kill '+pid)
        run('rm -rf ServerAgent-2.2.3')


# 调度
@task
def start():
    # task_tar()
    task_upload()
    # task_md5()
    task_exc()
