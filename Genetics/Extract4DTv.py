#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/4/4 19:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : Extract4DTv.py
#
# Batch extraction of 4DTv sites.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--codon", help="Codon Table File.", default=None)
parser.add_argument("-m", "--mapfile", help="Protein Sequence Names and their Corresponding CDS Sequence Names Table.", default=None)
parser.add_argument("-p", "--pep", help="Directory containing Protein Sequences.", default=None)
parser.add_argument("-C", "--cds", help="Directory containing CDS Sequences.", default=None)
parser.add_argument("-s", "--suffix_p", help="Protein sequence file extensions.", default="fa")
parser.add_argument("-S", "--suffix_c", help="CDS sequence file extensions.", default="fna")
args = parser.parse_args()

codpath = args.codon #"cod.txt"
mappath = args.mapfile #"SequenceIDs.txt"   #The first column is the ID of the aligned AA file and the second column is the ID of the CDS.
pepdir = args.pep #"../seq"
cdsdir = args.cds #"../cds"
suffix_p = args.suffix_p #"fa"
suffix_c = args.suffix_c #"fna"

import os
p_list = os.listdir(pepdir)
p_list = [i for i in p_list if "."+suffix_p in i]

try:
    os.makedirs("4dtv")
except:
    pass
#Read the codon table.
with open(codpath) as f:
    tem = f.readlines()
cod_aa = dict()
aa_cod = dict()
for i in tem:
    if i.strip():
        t = i.strip().split("\t")
        cod_aa[t[1]] = t[0]
        if t[0] not in aa_cod:
            aa_cod[t[0]] = []
        aa_cod[t[0]].append(t[1])
fdtv = dict()#4dtv
for i in aa_cod:
    if len(aa_cod[i]) >= 4:
        for j in aa_cod[i]:
            f = None
            if "A"+j[1:] in aa_cod[i] and "T"+j[1:] in aa_cod[i] and "C"+j[1:] in aa_cod[i] and "G"+j[1:] in aa_cod[i]:
                f = 1
            if j[0]+"A"+j[2] in aa_cod[i] and j[0]+"T"+j[2] in aa_cod[i] and j[0]+"C"+j[2] in aa_cod[i] and j[0]+"G"+j[2] in aa_cod[i]:
                f = 2
            if j[:2]+"A" in aa_cod[i] and j[:2]+"T" in aa_cod[i] and j[:2]+"C" in aa_cod[i] and j[:2]+"G" in aa_cod[i]:
                f = 3
            if f:
                fdtv[j] = f
                
#Read the ID mapping table
with open(mappath) as f:
    tem = f.readlines()
name_map = dict()
for i in tem:
    if i.strip():
        t = i.strip().split("\t")
        name_map[t[0]] = t[1]

def readfasta(path):
    with open(path) as f:
        tem = f.readlines()
    s_d = dict()
    for i in tem:
        if ">" in i:
            flag = i.strip("\n>")
            s_d[flag] = ""
        else:
            s_d[flag] += i.strip().replace("\n","").replace(" ","")
    return s_d

def translation(seq):
    seq = seq.upper()
    if len(seq) % 3 != 0:
        return None
    le = len(seq)//3
    cs = ""
    for i in range(le):
        tem = seq[i*3:i*3+3]
        cs += cod_aa[tem]
    return cs

def Reverse_translation(cdsseq,pepseq):
    le = len(cdsseq)//3
    cd = dict()
    outseq = ""
    for i in range(le):
        cd[i] = cdsseq[i*3:i*3+3]
    flag = 0
    for i in pepseq:
        if i != "-":
            outseq += cd[flag]
            flag += 1
        else:
            outseq += "---"
    return outseq

def processing(item):
    pep = readfasta(pepdir+"/"+item)
    cds = readfasta(cdsdir+"/"+item.replace(suffix_p,suffix_c))
    finseq = dict()
    for i in pep:
        tem = pep[i].replace("-","").rstrip("*")
        if "N" in cds[name_map[i]]:
            with open("err_4dtv.txt","a") as f:
                f.write(item + "\tThere is N in the CDS.\n")
            return None
        tem2 = translation(cds[name_map[i]])
        if not tem2:
            with open("err_4dtv.txt","a") as f:
                f.write(item + "\tThe CDS is not a multiple of 3.\n")
            return None
        if "*" == tem2[-1]:
            cds[name_map[i]] = cds[name_map[i]][:-3]
            tem2 = tem2[:-1]
        #assert "*" not in tem2
        if tem2 != tem:
            with open("err_4dtv.txt","a") as f:
                f.write(item + "\tSequence mismatch\n")
            return None
        if "*" in tem2:
            print(item,i)
        finseq[name_map[i]] = Reverse_translation(cds[name_map[i]],pep[i])
    return finseq

def get4dtv(dic):
    nu = set()
    for i in dic:
        tem = dic[i]
        le = len(tem)//3
        for j in range(le):
            if tem[j*3:j*3+3] in fdtv:
                nu.add(j*3+fdtv[tem[j*3:j*3+3]]-1)
    nu = list(nu)
    nu.sort()
    fi = dict()
    for i in nu:
        for j in dic:
            if j not in fi:
                fi[j] = ""
            fi[j] += dic[j][i]
    return fi
        
def main():
    for i in p_list:
        d = processing(i)
        if not d:
            continue
        F = get4dtv(d)
        with open("4dtv/"+i,"w") as f:
            for j in F:
                f.write(">"+j+"\n"+F[j]+"\n")

main()
        
        

        
        
