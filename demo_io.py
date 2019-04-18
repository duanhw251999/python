#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
  以下为标准写法
'''
def standard():
    try:
        c=open("D:\personal\DUANHW\待办.txt","r")
        print(c.read()) #使用此方法，如果文件超过10G 会填满内存造成内存严重不足，内存溢出等问题
    except FileNotFoundError as e:
        print (e)
    finally:
        if c:
            c.close()

'''
  进阶写法
'''

def upgrad():
    try:
        with open("D:\personal\DUANHW\待办.txt","r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(e)

def loop():
        try:
            with open("D:\personal\DUANHW\待办.txt","r") as f:
                line=f.readline()
                while line:
                    print(line)
                    line=f.readline()
        except FileNotFoundError as e:
            print(e)
def loop2():
        try:
            with open("D:\personal\DUANHW\待办.txt","r") as f:
                line=f.readlines()
                for l in line:
                    print(l.rstrip('\n'))#rstrip('\n') 剔除本方法自动为每行读取的内容添加的换行符

        except FileNotFoundError as e:
            print(e)

def readBiny():
        try:
            with open("D:\personal\DUANHW\医院系统\QQ截图20181214093252.png","rb") as f:
                for l in f.readlines():
                    print(l.strip())

        except FileNotFoundError as e:
            print(e)

def read_CharCoding():
        try:
            with open("D:\personal\DUANHW\待办.txt","r",encoding="gbk") as f:
                for l in f.readlines():
                    print(l.strip())

        except FileNotFoundError as e:
            print(e)


def demo_StringIO():
        from io import StringIO  # 妈的这种写法很骚

        f=StringIO()
        f.write("hello")
        f.write(" duanhw")
        print (f.getvalue())  #getvalue()方法用于获得写入后的str。

def demo_StringIO2():
    from io import StringIO  # 妈的这种写法很骚

    f=StringIO("Hello,\nlook one's best")
    while 1==1:
        s=f.readline()
        if s=='':
            break
        print (s.strip())

def demo_BytesIO():
        from io import BytesIO  # 妈的这种写法很骚
        f=BytesIO()
        f.write("中文".encode("utf-8"))
        print (f.getvalue())

        print(BytesIO(b'\xe4\xb8\xad\xe6\x96\x87').read())

demo_BytesIO()