#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import psutil
import json

from pojo_proce import MyProcess



def forLinux():
    print(os.getpid())

    pid=os.fork()

    if pid==0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
         print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

def forWindows():

    try:
        pids = psutil.pids()
        for pid in pids:
            p=psutil.Process(pid)
            pp=MyProcess()
            pp.setName(p.name())
            pp.setCreate_Time(p.create_time())
            print(json.dumps(pp,default=lambda  pp:pp.__dict__))
    except ProcessLookupError as e:
            print(e)


def win_net():
    netinfo=psutil.net_io_counters()
    print(json.dumps(netinfo))


forWindows()