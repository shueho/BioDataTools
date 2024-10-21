#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/10/21 12:21
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : CorrespondingNucleotideProteinFasta.py
#
# The corresponding nucleotide protein fasta removes items that do not match.

import sys

fas_n = sys.argv[1]
fas_p = sys.argv[2]

def readFasta(path): 
    with open(path) as f:
        ls = f.readlines()
    seqs = dict()
    for i in ls:
        if ">" in i:
            flag = i.strip(">\n")
            seqs[flag] = ""
        else:
            seqs[flag] += i.strip()
    return seqs

nuc = readFasta(fas_n)
pro = readFasta(fas_p)

n_p = set()
for i in nuc.keys():
	n_p.add(i.replace("_T","_X"))
for i in pro.keys():
	n_p.add(i.replace("_P","_X"))

n_p = list(n_p)
nps = dict()
for i in n_p:
    nps[i] = []
    flag_n = i.replace("_X","_T")
    if flag_n not in nuc:
        nps[i].append("-")
    else:
        nps[i].append(nuc[flag_n])
    flag_p = i.replace("_X","_P")
    if flag_p not in pro:
        nps[i].append("-")
    else:
        nps[i].append(pro[flag_p])

with open("out_match_seq.tab", "w") as f:
    for i in nps:
        f.write(i.split("_")[0]+"\t"+i+"\t"+"\t".join(nps[i])+"\n")

print("ok!")
