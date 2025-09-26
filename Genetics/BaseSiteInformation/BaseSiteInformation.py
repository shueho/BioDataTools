#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/4/4 21:40
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : BaseSiteInformation.py
#
# According to the specified chromosome position and base site information, the corresponding gene data were extracted.


import re
import sys
import os
gff_path = sys.argv[1]
q = sys.argv[2]


with open(gff_path) as f:
    ls = f.readlines()

class mRNA:
    def __init__(self,Chr,start,end,score,name):
        self.Chr = Chr
        self.start = start
        self.end = end
        self.score = score
        self.name = name
        self.CDS = list()
    def addCDS(self,li):
        self.CDS.append(li)
    def view(self):
        le = len(self.CDS)
        return "\t".join((self.name,self.Chr,self.start,self.end,self.score,str(le)))
    def findCDS(self,pos):
        for i in self.CDS:
            ran = i[0:2]
            if pos >= min(ran) and pos <= max(ran):
                return ("CDS",str(i),self.name,self.Chr,self.start,self.end,self.score,str(len(self.CDS)))
            continue
        return ("noCDS","-",self.name,self.Chr,self.start,self.end,self.score,str(len(self.CDS)))
    
gene = dict()
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
    if tem[2] == "mRNA":
        name = re.search("ID=(.*?);",tem[8])[1]
        gene[name] = mRNA(tem[0],*tem[3:6],name)
        all_[tem[0]][(int(tem[3]),int(tem[4]))] = name
    elif tem[2] == "CDS":
        pname = re.search("Parent=(.*?);",tem[8])[1]
        CDS = (int(tem[3]),int(tem[4]),tem[7])
        gene[pname].addCDS(CDS)

del ls    
def findPos(ch,pos):
    pos = int(pos)
    for i in all_[ch]:
        s = min(i)
        e = max(i)
        if pos >= s and pos <= e:
            name = all_[ch][i]
            cds = gene[name].findCDS(pos)
            return [name,*cds]
    return["-"]*9


with open(q) as f:
    lt = f.readlines()

f = open("out_"+os.path.basename(q)+".xls","w")
tem = ["gene_name","CDS/noCDS","CDS(start,end,codon start pos)","gene","ChrID","gene_start_pos","gene_end_pos","score","CDS_num"] + lt[0].split("\t")
f.write("\t".join(tem))
for i in lt[1:]:
    tem_list = i.split("\t")
    tem = findPos(*tem_list[0:2]) + tem_list
    f.write("\t".join(tem))
f.close()
