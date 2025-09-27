#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/7/20 4:43
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : MitosToGFF.py
#
# Parse the results obtained by Mitos into a GFF file.


import sys

mit = sys.argv[1]
fas = sys.argv[2]

f = open(mit)
ls = f.readlines()
f.close()
ls = [i.strip().split("\t") for i in ls]

with open(fas) as f:
	lt = f.readlines()
seq = ""
for i in lt[1:]:
	seq += i.strip().upper()


def getseq(st,ed,lin):
	s = seq[st-1:ed]
	if lin =="-1":
		t = ""
		for i in s[::-1]:
			if i == "A":
				t += "T"
			elif i == "T":
				t += "A"
			elif i == "C":
				t += "G"
			elif i == "G":
				t += "C"
			else:
				t += i
		s = t
	return s
	
def coplist(lis):
	s = seq[int(lis[4]):int(lis[5])+1]
	if lis[6]=="-1":
		t = ""
		for i in s[::-1]:
			if i == "A":
				t += "T"
			elif i == "T":
				t += "A"
			elif i == "C":
				t += "G"
			elif i == "G":
				t += "C"
			else:
				t += i
		s = t
	tem = [lis[2]+("-"+lis[9]+" "+lis[13] if lis[9] != "-" else ""),getseq(int(lis[4])+1,int(lis[5])+1,lis[6])]
	return tem
	
f = open("result_mitos.fasta","w")

for i in ls:
	tb = coplist(i)
	f.write(">"+tb[0]+"\n"+tb[1]+"\n\n")

f.close()