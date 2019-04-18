#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Chain(object):

    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path,"abc"))
    def __str__(self):
        return self._path

    __repr__=__str__

    if __name__=="__main__":
        print(Chain().status.user.timeline.list)
