#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/4/8 16:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : BaseCompositionCalculation.py
#
# Base composition calculations.

import sys
cds = sys.argv[1]
if len(sys.argv) > 2:
	del_cod = sys.argv[2] #TAG,TAA,TGA
else:
	del_cod = "TAG,TAA,TGA"
del_cod = del_cod.split(",")

def readfasta(path):
    with open(path) as f:
        tem = f.readlines()
    s_d = dict()
    for i in tem:
        if ">" in i:
            flag = i.strip("\n>")
            s_d[flag] = ""
        else:
            s_d[flag] += i.strip().replace("\n","").replace(" ","").upper()
    return s_d

def check_seq(seq): #将序列打断为密码子，支持提前终止，-1为找不到三位
	flag = 0
	ls = []
	tem = ""
	for i in seq:
		flag += 1
		tem += i
		if flag == 3:
			if tem not in del_cod:
				ls.append(tem)
			else:
				flag = 0
				break
			tem = ""
			flag = 0
	if flag != 0:
		return -1
	else:
		return ls

head = ["name","A1","T1","G1","C1","A2","T2","G2","C2","A3","T3","G3","C3","all"]
f = open("BaseComposition.txt","w")
f.write("\t".join(head)+"\n")
def calculate(Name, lis):
	d = dict()
	if lis == -1:
		f.write(Name + "\t-"*(len(head)-1) + "\n")
		return
	for i in lis:
		for j in range(3):
			if i[j]+str(j+1) not in d:
				d[i[j]+str(j+1)] = 0
			d[i[j]+str(j+1)] += 1
	d["all"] = 3*len(lis)
	d["name"] = Name
	for i in head:
		if i not in d:
			d[i] = 0
		f.write(str(d[i])+"\t")
	f.write("\n")
all_ = readfasta(cds)
for i in all_:
	lt = check_seq(all_[i])
	calculate(i, lt)
f.close()


	