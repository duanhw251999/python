#!/usr/bin/env python
# -*-coding:utf-8 -*-

import re
import os,shutil
from class_jt import Fileinfo
import jt


'''
hs_day  华盛日目录
ods_day ods日目录
jt_day 集团日目录
hs_month 华盛月目录
ods_month ods月目录
bonc_month 东方国信月目录
kdgc_month 科大月目录
jt_month 集团月目录
'''
paths={"hs_day":r'D:\personal\DUANHW\test\A\\',"ods_day":r'D:\personal\DUANHW\test\B\\',"jt_day":r'D:\personal\DUANHW\test\C\\'
    ,"hs_month":'',"ods_month":'',"bonc_month":'',"kdgc_month":'',"jt_month":''}


'''
集团数据校验过程：
1.读取目录中的文件，如果有文件，分别查看CHECK VAL gz文件
    读出CHECK文件中的内容 校验文件名称
        通过拼接出的名称去当前目录查找文件，
            VAL文件存在 文件大小不为0 通过
                读取VAL文件,得到dat.gz文件名称，大小，行数，账期 时间戳
                   如果大小为0 行数为0 报异常
                   否则，查看dat.gz文件是否存在，且账期是否与VAL文件中的账期是否一致，如果一致 通过
                    通过即可对该数据进行上传，并对上传过程做好日志：
                        |*日文件共 19 个 当前已上传 2 个
                        |---DAPD_DIM_MAPPING_PD 已上传 共3个文件 CHECK 1 VAL 1 DAT 1
                        |------DAPD_DIM_MAPPING_PD.20190318.20190317.00.000.000.862.CHECK
                        |------DAPD_DIM_MAPPING_PD.20190318.20190317.00.001.001.862.VAL
                        |------DAPD_DIM_MAPPING_PD.20190318.20190317.00.001.001.862.DAT.gz
            VAL文件不存在 不做任何操作
2.如果目录中没有文件 不做任何操作
'''
def getFiles(path):

    isQaul=True #是否通过
    msg=""
    files=os.listdir(path)
    if len(files)!=0:
        print("=====扫描到 %s 个文件" %(len(files)))
        for f in files:
            if re.match('^.*?\.(CHECK|VAL|gz)$',f) is not None:
               if os.path.splitext(f)[1]==".CHECK" :
                   vals=readCheck(path+f)
                   for v in vals:
                       if isExist(path+v)==False:
                            isQaul=False
                            break
                       else:
                            obj=Fileinfo()#创建一个新对象
                            obj=readVal(path+v)#通过方法返回对象并赋值给新对象
                            datPath=path+obj.getDatName()+".gz" #gz文件名称拼接

                            if isExist(datPath)==True:
                                if obj.getDatName().split(".")[2]==obj.getDatDate():
                                    print("%s可以上传" % obj.getDatName())
                            else:
                                break

                    #move(path+f,paths['jt_day'])
    else:
        print("=====扫描到 %s 个文件" %(len(files)))

'''
读取CHECK文件内容
'''
def readCheck(file):
    vals=[]  #通过CHECK文件的读取，得出VAL文件的数量和名称
    #datas=[] #通过CHECK文件的读取，得出data文件的数量和名称 注意，是压缩文件

    #如果读取的文件是CHECK文件
    if os.path.splitext(file)[1]==".CHECK" :
        with open(file,"r") as f:
            line=f.readline()
            while line:
                l=line.rstrip('\n')

                vals.append(l.replace("DAT","VAL"))
                #datas.append(l+".gz")
                line=f.readline()
    return vals

'''
 读取VAL文件
'''
def readVal(file):
    #如果读取的文件是VAL文件
    obj=Fileinfo()
    if os.path.splitext(file)[1]==".VAL":
        with open(file,"r") as f:
            line=f.readline()
            obj.setDatName(line.split("")[0])
            obj.setSize(line.split("")[1])
            obj.setRow(line.split("")[2])
            obj.setDatDate(line.split("")[3])
            obj.setTime(line.split("")[4])

        if obj.getRow()=="0" or obj.getSize()=="0":
            print("文件有误不能上传--记录数为0或文件大小为0")

    return obj

'''
   查找文件是否存在
'''
def isExist(path):
    boolean=True
    [dirname,filename]=os.path.split(path)
    if os.path.exists(path)==True:
        print("%s文件存在" % (filename))
    else:
        print("%s文件不存在" % (filename))
        boolean=False

    return boolean

'''
@file 文件名称 带路径
@toPath 将要移动的目录
'''
def move(file,toPath):
    if not os.path.isfile(file):
        print("%s 不是一个文件" %(file))
    else:
        if not os.path.exists(toPath):
            os.mkdir(toPath)
        print("%s-->%s" %(file,shutil.move(file,toPath)))







# 字节数
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    print(round(fsize,3))
    return round(fsize,3)


# 获取文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
        print( formatSize(size))
    except Exception as err:
        print(err)

# 字节bytes转化kb\m\g
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)



if __name__ == '__main__':
    try:
        for (k,v) in paths.items():
            if(k=="hs_day"):
                getFiles(r"D:\personal\DUANHW\test\A\\")
    except Exception as e:
        print(e)



