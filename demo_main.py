#!/usr/bin/env python
# -*-coding:utf-8 -*-

'''
 import os
 os.chdir('')  切换到工作目录
 import 模块  as 模块别称 例如 import datetime as dt
'''

def foo():
    str="function"
    print(str)

if __name__=="__main__":
    print("main")
    foo()
    # print("并不调用foo函数")