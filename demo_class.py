#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Student(object):
    __name=""#私有变量
    __score=0#私有变量
    ''' 定义初始化方法'''
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    '''
      getter setter 方法
    '''

    def getName(self):
        return self.__name
    def getScore(self):
        return self.__score
    def setName(self,name):
        self.__name=name
    def setScore(self,score):
        self.__score=score

if __name__=="__main__":
    obj=Student('david',100)
    obj.setName('david')
    obj.setScore(90)
    print ("NAME===========SCORE=============")
    print ("%s----------%d----------------" %(obj.getName(),obj.getScore()))
