#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Student(object):#括号中的object 是父类 括号就是继承
    __name=""#私有变量
    __score=0#私有变量

    __slots__=('__name','__score')# 限制学生类 只能有姓名和成绩两个属性

    def getName(self):
        return self.__name
    def getScore(self):
        return self.__score
    def setName(self,name):
        self.__name=name
    def setScore(self,score):
        self.__score=score
