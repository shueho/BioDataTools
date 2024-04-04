#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/4/3 23:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : MergeSequences.py
#
# Merge sequences.

import sys

import os

mpath = sys.argv[1]#"../pro_matrix.txt"
dirpath = sys.argv[2]
p = os.listdir(dirpath)

with open(mpath) as f:
    ls = f.readlines()
d = dict()
sam = ls[0].strip().split("\t")[1:]
for i in ls[1:]:
    tem = i.strip().split("\t")
    d[tem[0]] = tem[1:]

def readfasta(path):
    with open(path) as f:
        tem = f.readlines()
    sd = dict()
    for i in tem:
        if ">" in i:
            flag = i.strip("\n>")
            sd[flag] = ""
        else:
            sd[flag] += i.strip()
    return sd

ad = dict()
for i in p:
    ad.update(readfasta(dirpath+"/"+i))
fia = dict()
for i in sam:
    fia[i] = ""
if len(sys.argv) > 3:
	with open(sys.argv[3]) as f:
		order = f.readlines()
	order = [i.strip() for i in order if i.strip()]
else:
	order = list(d.keys())
f = open("order.true","w")
for i in order:
    f.write(i+"\n")
    for j in range(len(sam)):
        if d[i][j] in ad:
            fia[sam[j]] += ad[d[i][j]]
f.close()
f = open(os.path.basename(dirpath)+".fasta","w")
for i in fia:
    f.write(">"+i+"\n"+fia[i]+"\n")
f.close()
print("ok!")

