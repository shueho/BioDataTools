#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/3 22:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : VLookup.py
#
# Python implementation of the vlookup function.

import sys
import os

file1 = sys.argv[1]
file2 = sys.argv[2]
key_loc = int(sys.argv[3])-1
value_loc = int(sys.argv[4])-1
try:
	sep = sys.argv[5]
except:
	sep = "\t"

print("wait! sep is "+sep+".")
with open(file1) as f:
	key_ls = f.readlines()
	key_ls = [i.strip() for i in key_ls if i.strip()]

d = dict()
with open(file2) as f:
	map_ls = f.readlines()
	map_ls = [i.strip().split(sep) for i in map_ls if i.strip()]

for tem in map_ls:
	d[tem[key_loc]] = tem[value_loc]

with open("map_"+os.path.basename(file1),"w") as f:
	for i in key_ls:
		if i in d:
			f.write(i+sep+d[i]+"\n")
		else:
			f.write(i+sep+"-"+"\n")

print("ok!")