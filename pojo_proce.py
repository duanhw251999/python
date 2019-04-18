#!/usr/bin/env python
# -*-coding:utf-8 -*-

class MyProcess(object):
    name="" #进程名
    exe=""         #进程的bin路径
    cwd=""        #进程的工作目录绝对路径
    status=""     #进程状态
    create_time=""  #进程创建时间
    uids=""      #进程uid信息
    gids=""      #进程的gid信息
    cpu_times=""    #进程的cpu时间信息,包括user,system两个cpu信息
    cpu_affinity=""  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
    memory_percent=""  #进程内存利用率
    memory_info=""    #进程内存rss,vms信息
    io_counters=""    #进程的IO信息,包括读写IO数字及参数
    connectios=""    #返回进程列表
    num_threads=""  #进程开启的线程数



    def getName(self):           return self.name
    def getExe(self):            return self.exe
    def getCwd(self):            return self.cwd
    def getStatus(self):         return self.status
    def getCreate_Time(self):    return self.create_time
    def getUids(self):           return self.uids
    def getGids(self):           return self.gids
    def getCpu_Times(self):      return self.cpu_times
    def getCpu_Affinity(self):   return self.cpu_affinity
    def getMemory_Percent(self): return self.memory_percent
    def getMemory_Info(self):    return self.memory_info
    def getIo_Counters(self):    return self.io_counters
    def getConnectios(self):     return self.connectios
    def getNum_Threads(self):    return self.num_threads

    def setName(self,name):           self.name            =name
    def setExe(self,exe):            self.exe             =exe
    def setCwd(self,cwd):            self.cwd             =cwd
    def setStatus(self,status):         self.status          =status
    def setCreate_Time(self,create_time):    self.create_time     =create_time
    def setUids(self,uids):           self.uids            =uids
    def setGids(self,gids):           self.gids            =gids
    def setCpu_Times(self,cpu_times):      self.cpu_times       =cpu_times
    def setCpu_Affinity(self,cpu_affinity):   self.cpu_affinity    =cpu_affinity
    def setMemory_Percent(self,memory_percent): self.memory_percent  =memory_percent
    def setMemory_Info(self,memory_info):    self.memory_info     =memory_info
    def setIo_Counters(self,io_counters):    self.io_counters     =io_counters
    def setConnectios(self,connectios):     self.connectios      =connectios
    def setNum_Threads(self,num_threads):    self.num_threads     =num_threads