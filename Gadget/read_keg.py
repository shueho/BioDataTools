#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.1
# @Time    : 2023/7/30 13:00
# @Update  : 2024/3/26 18:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : read_keg.py
#
# Parse the KEG file.

import sys
import os
import re

file_path = sys.argv[1]

print("Author: XueHao\nE-mail: studid@163.com")
with open(file_path) as f:
	ls = f.readlines()

if "GENES" in ls[0]:
	add_t = "D-GENES\t"
else:
	add_t = ""

for i in ls:
	if i[0] == "C":
		Head = re.search("PATH:([a-zA-Z]+)",i)[1]
		break
def splitFirstChr(text,ch=" "):
	_index = text.find(ch)
	if _index == -1:
		return None
	left = text[:_index]
	right = text[_index+len(ch):]
	return [left.strip(), right.strip()]
file_path = os.path.basename(file_path)
flag_A = ""
flag_B = ""
flag_C = ""
flag_D = ""
f = open("output_"+file_path.replace(".keg",".txt"),"w")
f.write("A-PATH\tLEVEL-A\tB-PATH\tLEVEL-B\tID (C-PATH)\tLEVEL-C\t"+add_t+"D-KO\n")
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
		flag_C[0] = Head + flag_C[0]
		flag_C[1] = flag_C[1].split(" [")[0]
		continue
	if i[0] == "D":
		flag_D = i.strip("D").strip()
	if flag_D:
		all_list = flag_A + flag_B + flag_C + [flag_D]
		f.write("\t".join(all_list)+"\n")

f.close()

with open("output_"+file_path.replace(".keg",".txt")) as f:
	ls = f.readlines()

set_map = set()
for i in ls[1:]:
	tem = i.split("\t")
	set_map.add(tuple([tem[1],tem[3],tem[5],tem[4]]))

with open(Head +"_map.txt","w") as f:
	f.write(Head + "\tLevel-A\tLevel-B\tLevel-C\n")
	for i in list(set_map):
		f.write(i[3]+"\t"+i[0]+"\t"+i[1]+"\t"+i[2]+"\n")
print("ok!")

