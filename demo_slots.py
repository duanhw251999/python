#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Employeex(object):
    __name=''
    __age=0
    __sale=0.0

    __slots__=('weight') #此处规定允许绑定的变量

    def __init__(self,name,age,sale):
        self.__name=name
        self.__age=age
        self.__sale=sale

    if __name__=="__main__":
        print(__name__)

if __name__=="__main__":
        print(__name__)
'''
   本程序汇总有两条if __name__=="__main__":
   这两条语句都被执行了,以后对此处深入了解一下
'''