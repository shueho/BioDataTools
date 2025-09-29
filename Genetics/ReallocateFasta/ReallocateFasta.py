#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/9/30 0:25
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : ReallocateFasta.py
#
# Reallocate sequences from multiple FASTA files into different FASTA files.

import sys
import os
import re 

mpath = sys.argv[1]
dirpath = sys.argv[2]
flag = sys.argv[3] if len(sys.argv)==4 else "normal"
print("mode: "+flag)
p = os.listdir(dirpath)
folder_name = "fas_output"
os.makedirs(folder_name, exist_ok=True)

std = dict()
def readfasta(path):
    with open(path) as f:
        tem = f.readlines()
    sd = dict()
    for i in tem:
        if ">" in i:
            flag = i.strip("\n>")
            sd[flag] = ""
        else:
            sd[flag] += i.strip()
    return sd
for i in p:
	std[i.split(".")[0]] = readfasta(dirpath+"/"+i)

with open(mpath) as f:
	ls = f.readlines()
ls = [i.strip().split("\t") for i in ls if i.strip()]

if flag == "tRNA":
	for i in range(len(ls)):
		for j in range(len(ls[0])):
			if ls[i][j] in "ABCDEFGHIJKLMNOPQRSTUVWXYZL1L2S1S2" :
				ls[i][j] = "trn"+ls[i][j]
seqid = [i[0] for i in ls]
		
for i in range(1,len(ls[0])):
	f = open(folder_name+"/"+ls[0][i]+".fas","w")
	for j in range(1,len(seqid)):
		f.write(">"+seqid[j]+"\n"+std[ls[j][i].replace("(","_").replace(")","_")][seqid[j]]+"\n")
	f.close()
	