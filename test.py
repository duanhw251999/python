#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Student(object):#括号中的object 是父类 括号就是继承
    # def get_score(self):
    #         return self._score
    #
    # def set_score(self, value):
    #         if not isinstance(value, int):
    #             raise ValueError('score must be an integer!')
    #         if value < 0 or value > 100:
    #             raise ValueError('score must between 0 ~ 100!')
    #         self._score = value

    __score=0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,score):
        print('----------------------------------------')
        if 1>3:
            self.__score=700
        else:
            self.__score=200


######################## 执行
obj=Student()
obj.score=100
print(obj.score)