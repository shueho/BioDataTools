#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2026/3/30 23:26
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : FastaAlignPos.py
#
# Corresponds to the positions of each base in the FASTA files before and after alignment.

import sys
faspath = sys.argv[1]
pospath = sys.argv[2]

with open(faspath, 'r', encoding='utf-8') as f:
	lines = f.readlines()
flag = 0
seq = ""
for i in lines:
	if i[0] == ">":
		flag += 1
		continue
	if flag == 1:
		seq += i.strip().replace(" ","")
	if flag == 2:
		break
pos_d = dict()
key = 0
value = 0
for i in seq:
	value += 1
	if i != "-":
		key += 1
	pos_d[str(key)] = str(value)
	
with open(pospath, 'r', encoding='utf-8') as f:
	lines = f.readlines()
	
f = open("result.txt", "w")
f.write(lines[0].strip()+"\tpos_1\tpos_2\n")
for i in lines[1:]:
	if not i.strip():
		continue
	a, b = i.strip().split("\t")  
	c = pos_d[a]
	d = pos_d[b]
	f.write("\t".join([a,b,c,d])+"\n")



			
	







