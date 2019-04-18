
#!/usr/bin/env python
# -*-coding:utf-8 -*-

import json

d = dict(name='Bob', age=20, score=88)

wf=open("abc2.txt","w")
json.dump(d,wf)
wf.close()

rf=open("abc2.txt","r")
d2=json.load(rf)
rf.close()

print(d2)