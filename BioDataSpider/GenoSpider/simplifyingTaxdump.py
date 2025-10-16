#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/10/16 20:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : simplifyingTaxdump.py
#
# Simplifying Taxdump File.

import sys
import os

DIR = sys.argv[1]

namePath = DIR+"/names.dmp"

with open(namePath) as f:
	ls = f.readlines()
#n_map = dict()
nam = open("new_names.dmp","w")
for i in ls:
	if "|	scientific name	|" in i:
		nam.write(i)
nam.close()

nodePath = DIR+"/nodes.dmp"
with open(nodePath) as f:
	ls = f.readlines()
nod = open("new_nodes.dmp","w")
for i in ls:
	tem = i.split("|")
	nod.write("|".join([j.strip() for j in tem[:3]])+"\n")
nod.close()
