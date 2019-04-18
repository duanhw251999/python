#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Student:

	name=""
	score=0

	def  setName(self,name):
			self.name=name
	def setScore(self,score):
			self.score=score

	def getName(self):
			return self.name

	def getScore(self):
			return self.score

	def main(self):
		duanhw=Student()
		duanhw.setScore('10')
		print(duanhw.getScore())
