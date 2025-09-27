#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/11/4 12:38
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : MultipleFastaToTable.py
#
# Convert multiple Fasta files into a single table, with the sequence of the same file in the same row.


import sys
import os

path = sys.argv[1]

files= os.listdir(path)

def readFasta(p):
	with open(p) as faf:
		tem = faf.readlines()
	res = []
	st = ""
	for i in tem:
		if ">" in i:
			if st:
				res.append(st)
			st = i.strip(">\n")+"~"
		else:
			st += i.strip()
	res.append(st)
	return res

f = open("merge.tab","w")
for i in files:
	tem = readFasta(path+"/"+i)
	f.write(i+"\t"+"\t".join(tem)+"\n")
f.close()