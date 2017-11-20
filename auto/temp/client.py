# coding=utf8

import socket
import sys
import thread

import time

remote_ip = ['127.0.0.1', '10.33.20.20']
port = 4444



def Client(each_ip, port):
    filename = each_ip + '.csv'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit()

    try:
        s.connect((each_ip, port))
    except socket.gaierror:
        #could not resolve
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
    try:
        message = 'test\ninterval:1\nmetrics:cpu:	memory:	\n'
        s.sendall(message)
    except socket.error:
        #Send failed
        print 'Send failed'
        sys.exit()
    for each in range(1, 10):
        with open(filename, 'a') as f:
            reply = s.recv(1024)
            reply = reply.replace('\t', ',')
            f.write(reply)
            f.flush()
            print reply
    end_mes = 'exit\n'
    s.sendall(end_mes)

for each_ip in remote_ip:
    i = 0
    try:
        thread.start_new_thread(Client(each_ip, port), (i,))
    except:
        print "Error: unable to start thread"
    i = i+1
