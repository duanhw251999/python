#!/usr/bin/env python
# -*-coding:utf-8 -*-

'''
from demo_class  import Student

obj=Student('duanhw',100)
obj.age=33  #临时绑定的属性
print(obj.age)
'''

class Student(object):
    '''正常的属性 gtter setter 方法'''
    name=""
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name

    ''' 利用property 装饰器来改造一个属性 score
        首先设置变量为私有变量
        其次使用 @property 来创建变量的getter方法
        之后，自动创建了@score.setter方法

        完成以上内容后，创建的对象可以直接调用score，
        赋值时调用的其实是37行-42行的代码
        取值时，调用的33-34行代码

    '''
    _score=0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if score<0 or score>100:
            raise ValueError('score must between 0 ~ 100!')
        self._score=score

if __name__ =="__main__":
    obj=Student()
    obj.score=10

    print(obj.score)




