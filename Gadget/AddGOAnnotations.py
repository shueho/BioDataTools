#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/3/11 18:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : AddGOAnnotations.py
#
# Merge gene GO annotation table.


import sys
term = sys.argv[1]#"goterm_list"
gg = sys.argv[2]#"go.out"

with open(gg) as f:
    ls = f.readlines()

with open(term) as f:
    lt = f.readlines()

d = dict()
for i in lt:
    t = i.strip().split("\t")
    if t:
        d[t[0]] = "\t".join(t[1:])

f = open("gene_GO_info.txt","w")

f.write("gene_id\tID\tDescription\tONTOLOGY\n")
for i in ls:
    t = i.strip().split("\t")
    f.write(t[0]+"\t"+t[1]+"\t"+d[t[1]]+"\n")

print("ok!")
        
