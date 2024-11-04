#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/9/26 13:04
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : IntervalFeatureFinder.py
#
# According to the specified chromosome position information, the corresponding feature data were extracted.


import re
import sys
import os
gff_path = sys.argv[1]
q = sys.argv[2]
#distance = sys.argv[3]
if len(sys.argv) == 4:
    fe = sys.argv[3] #gene/mRNA/CDS/exon/...
else:
    fe = "gene"

with open(gff_path) as f:
    ls = f.readlines()

all_ = dict()
for i in ls:
    tem  = i.strip().split("\t")
    if len(tem) != 9:
        continue
    if tem[0] not in all_:
        all_[tem[0]] = dict()
    #assert int(tem[3]) < int(tem[4])
    if tem[8][-1] != ";":
        tem[8]+=";"
    if tem[2] == fe:
        try:
            name = re.search("ID=(.*?);",tem[8])[1]
        except:
            name = re.search("Parent=(.*?);",tem[8])[1]
        all_[tem[0]][(int(tem[3]),int(tem[4]))] = name


del ls    
def findGene(sname,ch,pos1,pos2):
    #pos = int(pos)
    star = int(pos1)
    end = int(pos2)
    tem = []
    for i in all_[ch]:
        s = min(i)
        e = max(i)
        if not (e < star or s > end):
            if s >= star and s <= end and e > end:
                st = "Right"
            elif e <= end and s >= star:
                st = "Be_include"
            elif e >= star and e <= end and s < star:
                st = "Left"
            else:
                st = "To_include"
            name = all_[ch][i]
            tem.append([sname,name,s,e,st])

    return tem

with open(q) as f:
    lt = f.readlines() #gene/chr/pos

f = open("Inter"+"_"+fe+"_"+os.path.basename(q),"w")
tem = ["site_name","site_chr","site_s","site_e","gene_name",fe+"_s",fe+"_e","position"]
f.write("\t".join(tem)+"\n")
for i in lt:
    tem_list = i.strip().split("\t")
    tem = findGene(*tem_list[0:4])
    if not tem:
        f.write("\t".join(tem_list)+"\t,-\t-\t-\t-\n")
    for j in tem:
        t2 = [str(k) for k in j] 
        f.write("\t".join(tem_list)+"\t"+"\t".join(t2[1:])+"\n")
f.close()
