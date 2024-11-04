#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/11/4 11:25
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : TableToMultipleFasta.py
#
# Convert the table into a Fasta file by row, with multiple sequences in each row placed in the same file.


import sys
import os

path = sys.argv[1]

out_ = "out_fastas"
os.makedirs(out_)
with open(path) as f:
	ls = f.readlines()

for i in ls:
	if i.strip():
		tem = i.strip().split("\t")
		with open(out_+"/"+tem[0]+".fa","w") as f:
			flag = 1
			for j in tem[1:]:
				f.write(">"+tem[0]+"_"+str(flag)+"\n"+j+"\n")
				flag += 1
