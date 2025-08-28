#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/4/3 23:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : BatchFastaToPam.py
#
# Batch conversion of aligned fasta files to pam files.

import sys
dirpath = sys.argv[1]
import os
p_list = os.listdir(dirpath)

try:
    os.makedirs("pamlfile")
except:
    pass

def cope_one(ipath,opath):
    with open(ipath) as f:
        ls = f.readlines()
    tem = dict()
    for i in ls:
        if ">" in i:
            flag = i.strip("\n>")
            tem[flag] = ""
        else:
            tem[flag] += i.strip()
    s = len(tem)
    l = len(tem[flag])
    with open(opath,"w") as f:
        f.write(str(s)+"\t"+str(l)+"\n")
        for i in tem:
            f.write(i+"  \n"+tem[i]+"\n")
for i in p_list:
    cope_one(dirpath+"/"+i,"pamlfile/"+i+".pam")
