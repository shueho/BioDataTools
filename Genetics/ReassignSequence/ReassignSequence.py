#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/4/4 10:45
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : ReassignSequence.py
#
# The sequences in the fasta file were assigned to different fasta files as required.

import sys
in_ = sys.argv[1]
map_ = sys.argv[2]
out_ = sys.argv[3]

import os
p=os.listdir(in_)
#p = [i for i in p if ".fna" in i]

try:
    os.makedirs(out_)
except:
    pass

d = dict()
for i in p:
    with open(in_+"/"+i) as f:
        ls = f.readlines()
    for j in ls:
        if ">" in j:
            flag = j.strip().strip(">").split(" ")[0]
            d[flag] = ""
        else:
            d[flag] += j.strip()
        
with open(map_) as f:
    ls = f.readlines()
for i in ls[1:]:
    tem = i.strip().split("\t")
    with open(out_+"/"+tem[0]+".fna","w") as f:
        for j in tem[1:]:
            f.write(">"+j+"\n"+d[j]+"\n")
