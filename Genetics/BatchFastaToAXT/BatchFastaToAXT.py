#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/10/24 23:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : BatchFastaToAXT.py
#
# Batch conversion of aligned fasta files to AXT files.

import sys
dirpath = sys.argv[1]
import os
p_list = os.listdir(dirpath)

try:
	os.makedirs("AXTfile")
except:
	pass

f = open("merge.axt","w")
def readFasta(path):
	with open(path) as f:
		ls = f.readlines()
		dic = dict()
	for i in ls:
		if ">" in i:
			flag = i.strip("\n>")
			dic[flag] = ""
		else:
			dic[flag] += i.strip()
	return dic
	
def dicToAXT(d,name=""):
	ls = list(d.keys())
	tem = open("AXTfile/"+name+".axt","w")
	for i in range(len(ls)):
		for j in range(i+1,len(ls)):
			f.write(ls[i]+"&"+ls[j]+"|"+name+"\n"+d[ls[i]]+"\n"+d[ls[j]]+"\n\n")
			tem.write(ls[i]+"&"+ls[j]+"\n"+d[ls[i]]+"\n"+d[ls[j]]+"\n\n")
	tem.close()

for i in p_list:
	n = os.path.basename(i).split(".")[0]
	d = readFasta(dirpath+"/"+i)
	dicToAXT(d,n)
f.close()