#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : S_to_H.py
#
# Convert fasta files of sample sequences to fasta files consisting of haplotypes. Realize the merging of identical sequences!

import argparse

arg = argparse.ArgumentParser()

arg.add_argument("-p","--path") #.fas
arg.add_argument("-l","--lis") #h_list

parser = arg.parse_args()

with open(parser.path) as f:
	all_ = f.read()

ls = all_.strip().lstrip(">").split(">")

lt = [i.strip().split("\n") for i in ls if i.strip()]
del ls


d = dict()
for i in lt:
	if i[1] in d.keys():
		d[i[1]].append(i[0])
	else:
		d[i[1]] = []
		d[i[1]].append(i[0])

#print(len(d))
del lt
with open(parser.lis) as f:
	ls = f.readlines()

ls = [i.split(" ")[-1].strip().strip("]") for i in ls if "[" in i] 

f = open("out_hap.fasta","w")
for i in range(len(ls)):
	for j in d.keys():
		if ls[i] in d[j]:
			f.write(">H%d\n%s\n"%(i+1,j))

f.close()
print("ok!")