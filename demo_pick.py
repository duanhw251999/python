#!/usr/bin/env python
# -*-coding:utf-8 -*-

'''
序列化与反序列化
'''
import pickle as pick

data=dict(name='duanhw', age=20, score=88)

def write2txt(bs):
    wf=open("abc.txt","wb")
    pick.dump(bs,wf)
    wf.close()

def read():
    write2txt(data)

    rf=open("abc.txt","rb")#读取文件
    data2=pick.load(rf)
    rf.close()
    print(data2)

def pickin(data):
    d=pick.dumps(data)
    return d

read()



