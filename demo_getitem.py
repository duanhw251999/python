#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Fbi(object):
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a

if __name__=="__main__":
    f=Fbi()
    f[0]