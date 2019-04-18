#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os,os.path

def getOsName():
    osname=os.name
    if osname=='posix':
        print("系统是Linux、Unix或Mac OS X")
    elif osname=="nt":
        print("系统是windows")

def getEnv():
    tenv=os.environ
    for key in tenv:
        print(key+"==>"+tenv[key])

def getabsPath():
    print(os.path.abspath("."))

def op_dir():
    #拼接目录地址
    print(os.path.join("D:/personal/DUANHW/perl","20190330"))
    #拆分目录
    print(os.path.split("D:/personal/DUANHW/perl/20190330"))
    #获取文件扩展名
    print(os.path.splitext("D:/personal/DUANHW/perl/clear.pl"))
    #创建目录2
    os.mkdir("D:/personal/DUANHW/perl/20190330")
    #删除目录
    os.rmdir("D:/personal/DUANHW/perl/new")

def os_file():
    dir="D:/personal/DUANHW/perl/"
    #重命名文件
    os.rename(os.path.join(dir,'新建文本文档 - 副本 - 副本 - 副本 - 副本 - 副本.txt'),os.path.join(dir,'001.txt'))
    # 删掉文件
    os.remove(os.path.join(dir,"新建文本文档 - 副本.txt"))
    #拷贝文件
    #读取目录，且只显示目录中的子目录
    subDir=[x for x in os.listdir(dir) if os.path.isdir(os.path.join(dir,x))]
    #读取目录，且只显示扩展名为.txt的文件
    dirs=[x for x in os.listdir(dir) if os.path.splitext(os.path.join(dir,x))[1]==".txt"]
    #读取目录，既是文件又是python文件
    [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


# 中文目录，需要编码
def ZNdir():
    cPath = os.getcwd()
    # 如果目录名字为中文 需要转码处理
    uPath = unicode(cPath,'utf-8')
    for fileName in os.listdir(uPath) :
            print (fileName)

def test():

    dir='D:/personal/DUANHW/perl/'
    #重命名文件
    #dirs=[d for d in os.listdir(dir) if os.path.isdir(d)]
    dirs=[x for x in os.listdir(dir) if os.path.splitext(os.path.join(dir,x))[1]==".txt"]

    print(dirs)

test()