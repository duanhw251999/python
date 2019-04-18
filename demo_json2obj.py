#!/usr/bin/env python
# -*-coding:utf-8 -*-

import json

class Student(object):

    name=""
    age=0
    score=0

    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

if __name__=="__main__":
    obj=Student("duanhw",30,100)
    abc=json.dumps(obj,default=lambda obj:obj.__dict__)
    print (abc)


