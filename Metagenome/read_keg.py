#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : read_keg.py
#
# Parse the KEG file.

import sys
import os

file_path = sys.argv[1]
file_path = os.path.basename(file_path)

print("Author: XueHao\nE-mail: studid@163.com")
with open(file_path) as f:
	ls = f.readlines()

def splitFirstChr(text,ch=" "):
	_index = text.find(ch)
	if _index == -1:
		return None
	left = text[:_index]
	right = text[_index+len(ch):]
	return [left.strip(), right.strip()]

flag_A = ""
flag_B = ""
flag_C = ""
flag_D = ""
f = open("output_"+file_path.replace(".keg",".txt"),"w")
f.write("A-PATH\tLEVEL-A\tB-PATH\tLEVEL-B\tko (C-PATH)\tLEVEL-C\tKO (D-PATH)\tLEVEL-D\tD-detail\n")
for i in ls:
	if i[0] == "A":
		flag_A = i.strip("A")
		flag_A = splitFirstChr(flag_A)
		continue
	if i[0] == "B":
		flag_B = i.strip("B").strip()
		flag_B = splitFirstChr(flag_B)
		continue
	if i[0] == "C":
		flag_C = i.strip("C").strip()
		flag_C = splitFirstChr(flag_C)
		flag_C[0] = "ko" + flag_C[0]
		flag_C[1] = flag_C[1].split(" [")[0]
		continue
	if i[0] == "D":
		flag_D = i.strip("D").strip()
	if flag_D:
		if "\t" not in flag_D: 
			tem = splitFirstChr(flag_D,"  ")
			tem[1] = splitFirstChr(tem[1],";") if splitFirstChr(tem[1],";") else ["-",tem[1]]
			lt = [tem[0]] + tem[1]
		else:
			tem = flag_D.split("\t")
			tem[0] = [tem[0][:tem[0].index(" ")],tem[0][tem[0].index(" ")+1:]]
			tem[1] = [tem[1][:tem[1].index(" ")],tem[1][tem[1].index(" ")+1:]]
			tem[1][1] = [i.strip() for i in tem[1][1].split(";")]
			lt = [tem[1][0]] + tem[1][1] + tem[0]
		all_list = flag_A + flag_B + flag_C + lt
		f.write("\t".join(all_list)+"\n")

f.close()

with open("output_"+file_path.replace(".keg",".txt")) as f:
	ls = f.readlines()
set_all = set()
set_map = set()
for i in ls[1:]:
	tem = i.split("\t")
	set_map.add(tuple([tem[1],tem[3],tem[5],tem[4]]))
	set_all.add(tuple([tem[4],tem[6],tem[7]]))

with open("ko_match_KO.txt","w") as f:
	f.write("ko-id\tKO-id\tD-level\n")
	for i in list(set_all):
		f.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\n")

with open("KO_map.txt","w") as f:
	f.write("Level-A\tLevel-B\tLevel-C\tko\n")
	for i in list(set_map):
		f.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\n")
print("ok!")

