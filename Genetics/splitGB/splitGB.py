#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/9/27 11:50
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : SplitGB.py
#
# Split multi-sequence GenBank files.

import sys
import os
import re 

folder_name = "gb_output"
os.makedirs(folder_name, exist_ok=True) 
gbpath = sys.argv[1]
with open(gbpath) as f:
	gb = f.read()

ls = gb.split("//")
ls = [i.strip()+"\n//\n" for i in ls if i.strip()]

def getName(text):
	acc_match = re.search(r'ACCESSION\s+(\S+)', text)
	acc = acc_match.group(1) if acc_match else "None"
	org_match = re.search(r'ORGANISM\s+(.*)', text)
	latin_name = org_match.group(1) if org_match else "None"
	return (latin_name+"_"+acc).replace(" ","_").replace("-","_").replace(".","_").replace(";","")

for i in ls:
	with open(folder_name+"/"+getName(i)+".gb","w") as f:
		f.write(i)
