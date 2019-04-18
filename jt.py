#!/usr/bin/env python
# -*-coding:utf-8 -*-
import json

path="conf.json"

def getDAPX(key):
     with open(path,"r") as f:
         jsonObj=json.load(f)
         return jsonObj[key]

if __name__ == '__main__':
    day=getDAPX("day")
    for d in day:
        print(d)