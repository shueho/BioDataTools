#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/10/21 11:15
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : ExtractFastaWithGene.py
#
# Extract the full transcripts or protein sequences of the specified gene list.

import sys

fas_path = sys.argv[1]
lis_path = sys.argv[2]

with open(lis_path) as f:
    ls = f.readlines()
ls = [i.strip() for i in ls if i.strip()]

with open(fas_path) as f:
    tem = f.readlines()


fas = dict()
for i in tem:
    if ">" in i:
        key = i.strip(">\n")
        fas[key] = ""
    fas[key] += i

g_s = dict()
for i in fas:
    flag = i.split("_")[0]
    if flag not in g_s.keys():
        g_s[flag] = []
    g_s[flag].append(i)

with open("out_match_seq.fasta", "w") as f:
    for i in ls:
        for j in g_s[i]:
            f.write(fas[j])

print("ok!")
