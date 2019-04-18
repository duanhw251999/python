#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
ienv=os.environ

for key in ienv:
    print (key+"===>"+ienv[key])

print("=======================================")
for key in ienv.keys():
    print (key+"===>"+ienv[key])
print("=======================================")
for value in ienv.values():
    print(value)
print("=======================================")
for key,value in ienv.items():
    print (key+"===>"+value)
print("=======================================")
for kv in ienv.items():
    print(kv)
