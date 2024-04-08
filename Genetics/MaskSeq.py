#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/4/7 2:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : MaskSeq.py
#
# Mask sequences at specified positions.

import sys
import os
genome = sys.argv[1]
masktbl = sys.argv[2]
targ = "N"
if len(sys.argv) > 3:
	targ = sys.argv[3]
assert len(targ) == 1
def readfasta(path):
    with open(path) as f:
        tem = f.readlines()
    s_d = dict()
    for i in tem:
        if ">" in i:
            flag = i.strip("\n>")
            s_d[flag] = ""
        else:
            s_d[flag] += i.strip().replace("\n","").replace(" ","")
    return s_d

def copetext(text,lis,targ):
	return text[:int(lis[1])-1] + targ*(int(lis[2])-int(lis[1])+1) + text[int(lis[2]):]

with open(masktbl) as f:
	ls = f.readlines()
ls = [i.strip().split("\t") for i in ls if i.strip()]

chr_ = readfasta(genome)
flag = 0
for i in ls:
	if i[0] in chr_:
		chr_[i[0]] = copetext(chr_[i[0]],i,targ)
	flag += 1
	print("{}/{}".format(flag,len(ls)))

f = open("maskseq_"+os.path.basename(genome),"w")
for i in chr_:
	f.write(">"+i+"\n"+chr_[i]+"\n")

print("ok!")