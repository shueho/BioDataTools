#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/10/21 13:55
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : BatchModificationSequence.py
#
# Modifies the sequence before the specified sequence.

import sys

fas = sys.argv[1]
fix_seq = sys.argv[2]
start_seq = sys.argv[3]

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

def modSeq(text, fix, new_):
    flag = text.find(fix)
    if flag >= 0:
        return [str(flag+1), str(flag+len(fix)), new_+text[flag:]]
    else:
        return ["-","-","-"]

seqs = readFasta(fas)


with open("modif_seq.tab", "w") as f:
    for i in seqs:
        cont = modSeq(seqs[i],fix_seq,start_seq)
        f.write(i+"\t"+seqs[i]+"\t"+"\t".join(cont)+"\n")

print("ok!")
