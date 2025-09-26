#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/4/5 22:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : SplitAXT.py
#
# Split the axt file.

import sys
import re

axtpath = sys.argv[1]

with open(axtpath) as f:
	ls = f.readlines()

for i in ls:
	if re.search(r"\d+",i):
		flag = i.strip()
	with open(flag+".axt-split","a") as f:
		f.write(i)

print(axtpath+": ok!")