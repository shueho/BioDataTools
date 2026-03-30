#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2026/3/30 22:44
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : GBtoInformationTable.py
#
# Extract feature information tables from GenBank files.

import re
import sys
gbpath = sys.argv[1]

with open(gbpath, 'r', encoding='utf-8') as f:
	lines = f.read()

pattern = re.compile(r'/(\w+)=')
info = ["feature_type", "location", "start", "end", "strand", "gene", "product"]

all_keys = []
all_keys = pattern.findall(lines)
tem = list(set(all_keys))
if "translation" in tem:
	tem.remove("translation")
for i in info:
	if i in tem:
		tem.remove(i)
info = info+tem

def get_info(text,tra=False):
	tr = []
	if tra:
		tr = ["translation"]
	#print(text+"\n\n")
	info_dict = {}
	info_list = text.strip().split("\n")
	info_dict["feature_type"], info_dict["location"] = info_list[0].strip().split(" ")[0], info_list[0].strip().split(" ")[-1]
	for i in info_list[1:]:
		match = re.match(r'/(\w+)="([^"]+)"', i.strip())
		if match:
			key = match.group(1)
			value = match.group(2)
		else:
			continue
		info_dict[key] = value
	if info_dict["location"]:
		numbers = re.findall(r'\d+', info_dict["location"])
		numbers = [int(i) for i in numbers]
		if "complement" in info_dict["location"] and "join" not in info_dict["location"]:
			info_dict["strand"] = "-"
		elif "complement" in info_dict["location"] and "join" in info_dict["location"]:
			info_dict["strand"] = "?"
		else:
			if int(numbers[0]) < int(numbers[-1]):
				info_dict["strand"] = "+"
			else:
				info_dict["strand"] = "-"
		info_dict["start"] = str(min(numbers))
		info_dict["end"] = str(max(numbers))
	result = []
	for i in info+tr:
		if i in info_dict:
			result.append(info_dict[i])
		else:
			result.append("NA")
	return(result)

flag = 0
flag2 = 0
lines = lines.split("\n")

for i in lines:
	if "ORIGIN" == i[0:6]:
		features.append(tem)
		break

	if "FEATURES" == i[0:8]:
		flag = 1
		features = []
		tem = ""
		continue
	if flag:
		if flag2:
			tem += " "+i.strip()
			if '"' == i.strip()[-1]:
				flag2 = 0
				tem += "\n"
			continue
		
		if i.strip()[0] != "/":
			if tem:
				features.append(tem)
			tem = i + "\n"
		else:
			flag2 = 0
			if '"' != i.strip()[-1]:
				flag2 = 1
				tem += i
				continue
			tem += i + "\n"


f = open("result.txt", "w")
f.write("\t".join(info)+"\n")
for i in features:
	f.write("\t".join(get_info(i))+"\n")
f.close()

f = open("result_add_translation.txt", "w")
f.write("\t".join(info)+"\ttranslation"+"\n")
for i in features:
	f.write("\t".join(get_info(i,True))+"\n")
f.close()


			
	







