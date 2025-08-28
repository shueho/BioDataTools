#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/12/31 22:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : MergeMultipleFasta.py
#
# Merge multiple FASTA files and remove redundant sequences. 

import sys 
import os

path_list = sys.argv[1:]

def readFasta(path):
	tem = dict()
	with open(path) as f:
		ls = f.readlines()
	for i in ls:
		if ">" in i:
			flag = i.strip(">\n")
			tem[flag] = ""
		else:
			tem[flag] += i.strip().upper()
	d = dict()
	for i in tem:
		if tem[i] not in d:
			d[tem[i]] = i
		else:
			d[tem[i]] += "/" + i
	seqName = [d[i] for i in d] 
	return d

all_ = dict()
for i in path_list:
	print("Read " + i)
	all_[i] = readFasta(i)
print("Merge")
seq = set()
for i in all_:
	seq.update(all_[i].keys())

f = open("merge.fasta","w")
flag = 0
res = dict()
for i in list(seq):
	flag += 1
	Nid = "N_{:0>10} ".format(flag)
	f.write(">"+Nid+"\n"+i+"\n")
	res[Nid] = []
	for j in path_list:
		if i in all_[j]:
			res[Nid].append(all_[j][i])
		else:
			res[Nid].append("-")
f.close()
f = open("GeneIDMatch.table","w")
f.write("Nid"+"\t"+"\t".join(path_list)+"\n")
for i in res:
	f.write(i+"\t"+"\t".join(res[i])+"\n")
f.close()
print("OK")
	


