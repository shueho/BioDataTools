#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/12 18:50
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : CustomFastaExtractor.py
#
# Extract the fasta sequence in the list.

import sys
import re

fas_path = sys.argv[1]
lis_path = sys.argv[2]

if len(sys.argv) == 4:
    rule = sys.argv[3]
else:
    rule = "\>(.*?) "

with open(lis_path) as f:
    ls = f.readlines()
ls = [i.strip() for i in ls if i.strip()]

with open(fas_path) as f:
    tem = f.readlines()

def idRules(text, rules="\>(.*?) "):     
    return re.search(rules,text)[1]

fas = dict()
for i in tem:
    if ">" in i:
        key = idRules(i, rule)
        fas[key] = ""
    fas[key] += i

with open("out_match_seq.fasta", "w") as f:
    for i in ls:
        f.write(fas[i])

print("ok!")
