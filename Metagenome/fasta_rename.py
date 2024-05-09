#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : fasta_rename.py
#
# Modify the name in each sequence of the specified FASTA file to make it standardized and uniform. 

import sys 
import os
print("Author: XueHao\nE-mail: studid@163.com\nplease wait!")
path = sys.argv[1]
with open(path) as f:
	ls = f.readlines()

flag = 0
d = dict()
for i in ls:
	if ">" in i:
		flag += 1
		key_ = ">N_{:0>10} ".format(flag) + " ".join(i.strip().split(" ")[1:])
		d[key_] = ""
	else:
		d[key_] += i.strip()
f = open("out_"+os.path.basename(path),"w")
for i in d:
	f.write(i+"\n"+d[i]+"\n")

f.close()
print("ok!")
