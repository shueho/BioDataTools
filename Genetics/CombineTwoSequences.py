#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : CombineTwoSequences.py
#
# Merge different sequences of the same sample (recommendation is the result of the comparison).

import sys

arg = sys.argv
assert len(arg) == 3
a = arg[1]
b = arg[2]
#a = "16s.fas"
#b = "co1.fas"

def read_fas(path):
    with open(path) as f:
        ls = f.readlines()
    key_ = ""
    d = dict()
    for i in ls :
        if ">" in i:
            key_ = i.strip()
            d[key_] = ""
            continue
        else:
            d[key_] += i.strip()
    return d
            
d1 = read_fas(a)
d2 = read_fas(b)

d = dict()
f = open("merge.fas","w")
for i in d1.keys():
    d[i] = d1[i] + d2[i]
    f.write(i+"\n"+d[i]+"\n")
f.close()
