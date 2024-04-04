#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/4/4 21:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : ParsingCodeMLResults.py
#
# Batch parsing of CodeML results.

import os
import re
import sys

m0 = sys.argv[1] #m0
m2 = sys.argv[2] #m2
p0 = os.listdir(m0)
p2 = os.listdir(m2)

def readR(path):
    #print(path)
    with open(path) as f:
        t = f.read()
    try:
        ntime,np,lnL = re.findall("lnL\(ntime: (.*?)  np: (.*?)\):  (.*?) ",t)[0]
        if not lnL:
            ntime,np,lnL = re.findall("lnL\(ntime: (.*?)  np: (.*?)\):   (.*?) ",t)[0]
    except:
        ntime,np,lnL = re.findall("lnL\(ntime: (.*?)  np: (.*?)\): (.*?) ",t)[0]
    o1 = re.findall("omega \(dN/dS\) =  (.*?)\n",t)
    o2 = re.findall("w \(dN/dS\) for branches:  (.*?)\n",t)
    if o1:
        flag = "null"
        omega = o1
    else:
        flag = "m2"
        omega = o2   
    return (path,flag,ntime,np,lnL,omega[0])

f = open("result.txt","w")
f.write("path\tflag\tntime\tnp\tlnL\tomega\n")
for i in p0:
    tem = readR(m0+"/"+i)
    f.write("\t".join(tem)+"\n")
for i in p2:
    tem = readR(m2+"/"+i)
    f.write("\t".join(tem)+"\n")
f.close()
