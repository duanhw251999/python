#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Animal(object):
    def run(self):
        print("Runing......")

class dog(Animal):
    def  eat(self):
        print('骨头')

class cat(Animal):
    def eat(self):
        print('鱼')

class duck(Animal):
    def run(self):
        print('摇摇摆摆，两条腿')

class Other(Animal):
    __name=""
    __runstuts=""
    __food=""

    def __init__(self,name,runstuts,food):
        self.__name=name
        self.__runstuts=runstuts
        self.__food=food

    def run(self):
        return self.__runstuts

    def eat(self):
        return self.__food

    def getName(self):
        return self.__name

if __name__=="__main__":
    wang=dog()
    wang.run();#此方法继承自Animal父类
    wang.eat();

    miao=cat()
    miao.run()
    miao.eat()

    ga=duck()
    ga.run()

    ele=Other("大象","跑起来很笨重","吃的很多，喜欢吃香江")
    bird=Other('画眉','不会跑，只会飞','喜欢吃虫子')

    print("%s,%s,%s" %(ele.getName(),ele.run(),ele.eat()))
    print("%s,%s,%s" %(bird.getName(),bird.run(),bird.eat()))




