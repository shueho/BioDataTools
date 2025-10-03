#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/9/29 1:06
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : FeatureStitch.py
#
# Stitch features preserving the original coding direction, reverse complementing those on the negative strand.

import sys
import os
import re 

spath = sys.argv[1]
dirpath = sys.argv[2]
flag = sys.argv[3] if len(sys.argv) == 4 else ""
#p = os.listdir(dirpath)

def readfasta(path):
    with open(path) as f:
        tem = f.readlines()
    sd = dict()
    for i in tem:
        if ">" in i:
            flag = i.strip("\n>")
            sd[flag] = ""
        else:
            sd[flag] += i.strip().upper()
    return sd

def reverse_complement(seq):
	comp = {'A': 'T', 
			'T': 'A', 
			'G': 'C', 
			'C': 'G', 
			'R': 'Y', 
			'Y': 'R', 
			'K': 'M', 
			'M': 'K', 
			'B': 'V', 
			'V': 'B', 
			'D': 'H', 
			'H': 'D',			
			'U': 'A', 
			'S': 'S',			
			'W': 'W', 
			'N': 'N', 
			'-': '-'}
	return ''.join(comp[base] for base in reversed(seq))

std = dict()
with open(spath) as f:
	ls = f.readlines()
ls = [i.strip() for i in ls if i.strip()]
for i in range(len(ls)):
	if ls[i][0] == "-":
		std[i] = (ls[i].strip("-")+flag, 1)
	else:
		std[i] = (ls[i]+flag, 0)
		
def getReg(dic):
	tem = list(dic.keys())[0]
	return len(dic[tem])
		
f_site = open("regions.txt", "w") 
f_site.write("\t".join(["FeatureName","start","end","length","Strand"])+"\n")

seqName = list(readfasta(dirpath+"/"+std[0][0]).keys())
seqDic = {i:"" for i in seqName}

s = 1
for i in range(len(std)):
	seq = readfasta(dirpath+"/"+std[i][0])
	l = getReg(seq)
	f_site.write("\t".join([std[i][0],str(s),str(s+l-1),str(l),"-" if std[i][1] else "+"])+"\n")
	s += l
	for j in seqName:	
		if std[i][1]:
			seqDic[j] += reverse_complement(seq[j])
		else:
			seqDic[j] += seq[j]
f_site.close()

only_atgcn = open("only_atgcn.fas","w")
with open("merge.fas","w") as f:
	for i in seqName:
		f.write(">"+i+"\n"+seqDic[i]+"\n")
		only_atgcn.write(">"+i+"\n")
		for j in seqDic[i]:
			if j not in "ATGCN-":
				only_atgcn.write("N")
			else:
				only_atgcn.write(j)
		only_atgcn.write("\n")
