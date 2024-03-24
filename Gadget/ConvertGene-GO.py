#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/3/24 14:20
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : ConvertGene-GO.py
#
# The comparison tables of gene and multiple GO were converted to Gene-GO one-to-one format.

import re
import sys

path=sys.argv[1]

with open(path) as f:
    ls = f.readlines()

f = open("g-go.txt","w")
for i in ls:
    tem = i.split("\t")
    if len(tem) != 2:
        continue
    gene = tem[0]
    go = re.findall("(GO:\d+)",tem[1])
    for j in go:
        f.write(gene+"\t"+j+"\n")
f.close()

print("ok!")
    
