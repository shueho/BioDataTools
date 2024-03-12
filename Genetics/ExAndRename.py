#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/3/12 10:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : ExAndRename.py
#
# The sequence was extracted and renamed.

import sys
import re

map_path = sys.argv[1]
fasta_path = sys.argv[2]

with open(fasta_path) as f:
	ls = f.readlines()

d = dict()
for i in ls:
	if ">" in i:
		flag = i.strip(">\n ").split(" ")[0]
		d[flag] = []
	else:
		d[flag].append(i)

with open(map_path) as f:
	ls = f.readlines()

f = open("subset_fasta.faa","w")
for i in ls:
	if not i.strip():
		continue
	tem = i.strip().split("\t")
	if tem[0] in d:
		f.write(">"+tem[1]+"\n"+"".join(d[tem[0]])+"\n")
	else:
		print(tem[0] + ": not in fasta file!")
f.close()
print("ok!")

