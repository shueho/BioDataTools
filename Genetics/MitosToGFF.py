#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2025/7/20 4:43
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : MitosToGFF.py
#
# Parse the results obtained by Mitos into a GFF file.


import sys

mit = sys.argv[1]

f = open(mit)
ls = f.readlines()
f.close()
ls = [i.strip().split("\t") for i in ls]


def coplist(lis):
	tem = [lis[0],lis[3],lis[1],str(int(lis[4])+1),str(int(lis[5])+1),".","+" if lis[6]=="1" else "-",".","ID="+lis[2]+("-"+lis[9] if lis[9] != "-" else "")]
	return tem
	
f = open("result_mitos.gff","w")

for i in ls:
	f.write("\t".join(coplist(i))+"\n")

f.close()