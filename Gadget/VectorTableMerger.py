#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/9/4 16:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : VectorTableMerger.py
#
# Connect the A-Bs and B-Cs forms to form an A-Cs form.

import re
import sys

A_B = sys.argv[1]
B_C = sys.argv[2]

if len(sys.argv) == 3:
	s1 = ";"
	s2 = ";"
else:
	s1 = sys.argv[3]
	s2 = sys.argv[4]

with open(A_B) as f:
    ls = f.readlines()
ls = [i.strip().split("\t") for i in ls if i.strip()]

dab = dict()
for i in ls:
	if len(i) == 2:
		tem = i[1].split(s1)
		tem = [j.strip() for j in tem if j.strip()]
		if i[0] not in dab:
			dab[i[0]] = tem
		else:
			dab[i[0]] += tem
	if len(i) == 1:
		dab[i[0]] = []
print("read A-Bs: ok!")

with open(B_C) as f:
    lt = f.readlines()
lt = [i.strip().split("\t") for i in lt if i.strip()]

dbc = dict()
for i in lt:
	if len(i) == 2:
		tem = i[1].split(s2)
		tem = [j.strip() for j in tem if j.strip()]
		if i[0] not in dbc:
			dbc[i[0]] = tem
		else:
			dbc[i[0]] += tem
print("read B-Cs: ok!")
f = open("A-Cs_err.txt","w")

d = dict()
for i in dab:
	tem = dab[i]
	tem2 = set()
	for j in tem:
		if j in dbc:
			for k in dbc[j]:
				tem2.add(k)
			else:
				f.write(i+"\t"+j+": not found!\n")
	d[i] = list(tem2)
f.close()
#print(d)

f = open("A-Cs.table","w")
for i in d:
	f.write(i+"\t"+s2.join(d[i])+"\n")
f.close()
print("ok!")
    
