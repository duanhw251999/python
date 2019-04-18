#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('我是进程 %s 进程号 %s ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('我是进程 %s 执行时间为 %0.2f seconds.' % (name, (end - start)))

if __name__=="__main__":
    print('父进程 %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('等待所有子进程执行完毕...')
    p.close()
    p.join()
    print('所有子进程执行完毕.')