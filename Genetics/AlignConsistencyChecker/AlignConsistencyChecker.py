#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/11/4 13:22
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : AlignConsistencyChecker.py
#
# Compare the resulting Fasta file, match each site, and compare if there are exactly the same sites.


import sys
import os

path = sys.argv[1]

files= os.listdir(path)

def compareF(lis):
	flag = lis[0]
	res = ""
	for i in range(len(flag)):
		fg = 1
		for j in lis[1:]:
			if j[i] != flag[i]:
				fg = 0
				break
		if fg:
			res += "*"
		else:
			res += "_"
	return res

def readFasta(p):
	with open(p) as faf:
		tem = faf.readlines()
	res = dict()
	for i in tem:
		if ">" in i:
			flag = i.strip(">\n")
			res[flag] = ""
		else:
			res[flag] += i.strip()
	seqs = [res[i] for i in res]
	return res, compareF(seqs)

f = open("aln_res.txt","w")
for i in files:
	tem1, tem2 = readFasta(path+"/"+i)
	f.write(i+"\n")
	for j in tem1:
		f.write(j+"\t"+tem1[j]+"\n")
	f.write("**ALN**\t"+tem2)
	f.write("\n\n")
f.close()