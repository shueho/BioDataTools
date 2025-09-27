#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/9/5 10:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : GFFSimplifier.py
#
# Simplified GFF information to reduce GFF file size.

import sys
import os
path = sys.argv[1]

I = ["ID","Parent"]
if len(sys.argv) > 2:
	item_ = sys.argv[2:]
else:
	item_ = I
item_ = [i.strip() for i in item_ if i.strip()]
if "Parent" not in item_:
	item_ = item_ + ["Parent"]
if "ID" not in item_:
	item_ = ["ID"] + item_

with open(path) as f:
	ls = f.readlines()

tem = list()

def getItem(text):
	t = text.strip().split("\t")
	con = t[-1].split(";")
	d = dict()
	for c in con:
		lef = c.split("=")[0].strip()
		rig = c.split("=")[1].strip()
		d[lef] = rig
	fin = "\t".join(t[:-1])+"\t"

	for i in item_:
		if i in d: 
			fin += i+"="+d[i]+";"
	return fin.rstrip(";")


for i in ls:
	if not i.strip():
		continue
	if i.strip()[0] == "#":
		tem.append(i.strip())
		continue
	tem.append(getItem(i))

with open("simp_"+os.path.basename(path),"w") as f:
	f.write("#Simplified by https://github.com/shueho/BioDataTools.\n"+"\n".join(tem)+"\n")
	