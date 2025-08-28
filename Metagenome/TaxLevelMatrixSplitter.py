#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : TaxLevelMatrixSplitter.py
#
# The species abundance matrix was extracted.

import sys
import os
print("Author: XueHao\nE-mail: studid@163.com\nplease wait!")
#level in ["a", "k", "p", "c", "o", "f", "g", "s"] a is all!

mpaMatrix = sys.argv[1]
level = sys.argv[2].lower()
SL = ["k", "p", "c", "o", "f", "g", "s"]

def getLevel(path, lev):
	with open(path) as f:
		ls = f.readlines()
	fo = open("taxLevel_"+lev.upper()+"_output."+os.path.basename(path),"w")
	fo.write("\t".join(SL[:SL.index(lev)+1])+"\t"+"\t".join(ls[0].split("\t")[1:]))
	for i in ls[1:]:
		tem_all = i.split("\t")
		tax = tem_all[0].split("|")
		td = dict()
		if lev == tax[-1][0]:
			for j in tax:
				td[j[0]] = j[3:]
			for j in SL[:SL.index(lev)+1]:
				if j in td:
					fo.write(td[j]+"\t")
				else:
					fo.write("-"+"\t")
			fo.write("\t".join(tem_all[1:]))
		#print(tem)
	fo.close()

if level == "a":
	for i in SL:
		getLevel(mpaMatrix,i)
else:
	getLevel(mpaMatrix,level)

print("ok!")
