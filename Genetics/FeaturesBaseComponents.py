#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/1/20 3:20
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : FeaturesBaseComponents.py
#
# Feature extraction and base composition statistics.

import sys


fpath = sys.argv[1]
mpath = sys.argv[2]

with open(fpath) as f:
    tem = f.readlines()    
fasta = ""
for i in tem:
    if ">" in i:
        pass
    else:
        fasta += i.strip()
def getSeq(st, en=None):
    if st <= 0:
        return None
    if en != None:
        return(fasta[st-1:en])
    else:
        return(fasta[st-1])


with open(mpath) as f:
    tem = f.readlines()

gro = dict()   #group:{sample}
sam = dict()   #sample:(st,en)
g_loc = dict() #group:{loc_g}
for i in tem:
    t = i.strip().split("\t")
    g_t = t[0].split(";")
    for j in g_t:
        if j not in gro:
            gro[j] = set()
        gro[j].add(t[1])
    sam[t[1]] = (int(t[2]),int(t[3]))

for i in gro:
    g_loc[i] = set()
    for j in gro[i]:
        g_loc[i].update(range(sam[j][0],sam[j][1]+1))
remain = set(range(1,len(fasta)+1))
for i in g_loc:
    remain -= g_loc[i]

with open("ex_seq.fasta","w") as f:
    for i in sam:
        f.write(">"+i+"\n"+getSeq(*sam[i])+"\n")
    for i in g_loc:
        f.write("\n>GR%"+i+"\n")
        for j in list(g_loc[i]):
            f.write(getSeq(j))
    f.write("\n>$all\n"+fasta+"\n>$other\n")
    for i in list(remain):
        f.write(getSeq(i))


with open("ex_seq.fasta") as f:
    ls =f.readlines()
seqs = dict()
for i in ls:
    if ">" in i:
        flag = i.strip(">\n")
        seqs[flag] = ""
    else:
        seqs[flag] += i.strip()

def ATGC(seq):
    tem = dict()
    for i in "ATGC":
        tem[i] = 0
    for i in seq:
        tem[i] += 1
    text = ""
    for i in "ATGC":
        text += (str(tem[i])+"\t")
    return text

with open("Base_composition.txt","w") as f:
    f.write("SEQ\tA\tT\tG\tC\n")
    for i in seqs:
        f.write(i+"\t"+ATGC(seqs[i])+"\n")
        
print("ok")