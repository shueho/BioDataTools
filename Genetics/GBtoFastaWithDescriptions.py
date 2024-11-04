#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : GBtoFastaWithDescriptions.py
#
# Convert the GB file into a FASTA file, and take the GB file name as the content of the modifier after ">" in the FASTA file.It is mainly used for batch processing of a large number of GB files.

import os
import sys
path = sys.argv[1]

try:
	os.mkdir("output")
except:
	...

def gb_to_fas(gb_file):
	with open(gb_file) as f:
		ls = f.readlines()

	text = ""
	flag = 0
	for i in ls:
		if flag:
			for j in i:
				if j in "atcg":
					text += j
		if "ORIGIN" in i:
			flag = 1
	with open("./output/{}.fas".format(os.path.basename(gb_file).replace(".gb","")),"w") as f:
		f.write(">"+os.path.basename(gb_file).replace(".gb","")+"\n")
		f.write(text)

ls = os.listdir(path)
ls = [path+"/"+i for i in ls if ".gb" in i]

for i in ls:
	gb_to_fas(i)