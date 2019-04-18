#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process as pro
import os

#子进程的方法
def run_sub_process(name):
    print("我是子进程:%s 进程号 %s " % (name,os.getpid()))

if __name__=="__main__":
    print('父进程是 %s.' % os.getpid())
    p=pro(target=run_sub_process,args=('子进程0',))
    p2=pro(target=run_sub_process,args=('子进程1',))
    p2.start()
    p2.join()
    p.start()
    p.join()

    print('Child process end.')