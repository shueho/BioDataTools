#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/1/3 20:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : KEGGPathwayCounter.py
#
# KEGG pathway gene number statistics.


import sys

allKeg = sys.argv[1]
gene_vs_ko = sys.argv[2]

print("1/3: read keg file")
with open(allKeg) as f:
    ls = f.readlines()
    ls = [i.strip().split("\t") for i in ls[1:] if i.strip()]

all_d = dict()

B = dict()
C = dict()
D = dict()

for i in ls:
    all_d[i[0]] = i[1]
    all_d[i[2]] = i[3]
    all_d[i[4]] = i[5]
    
    B[i[2]] = i[0] #B:A       
    C[i[4]] = i[2] #C:B

    #if i[6] not in D: #D:{C}
        #D[i[6]] = set()
    #D[i[6]].update((i[4],))

print("2/3: read match file and count gene number")
err = []
A_cout = dict()
B_cout = dict()
C_cout = dict()
#D_cout = dict()
with open(gene_vs_ko) as f:
    gk = f.readlines()
    gk = [i.strip().split("\t")[1].split(",") for i in gk if i.strip()]
for i in gk:
    #t_set = set()
    #for d in i:
        #if d not in D_cout:
            #D_cout[d] = 0
        #D_cout[d] += 1
        #if d not in D:
            #err.append(d)
        #else:
            #t_set.update(D[d]) #{C}
    #tem = list(t_set)

    t_set = set()
    for c in i:
        if c not in C:
            err.append(c)
            continue
        if c not in C_cout:
            C_cout[c] = 0
        C_cout[c] += 1
        t_set.update((C[c],)) #{B}
    tem = list(t_set)

    t_set = set()
    for b in tem:
        if b not in B_cout:
            B_cout[b] = 0
        B_cout[b] += 1
        t_set.update((B[b],))
    tem = list(t_set)

    t_set = set()
    for a in tem:
        if a not in A_cout:
            A_cout[a] = 0
        A_cout[a] += 1

print("3/3: save date")

with open("A.txt","w") as f:
    f.write("A\tnum\nall_gene\t"+str(len(gk))+"\n")
    for i in A_cout:
        f.write(all_d[i]+"\t"+str(A_cout[i])+"\n")
        
        
with open("A-B.txt","w") as f:
    f.write("A\tB\tnum\n")
    for i in B_cout:
        f.write(all_d[B[i]]+"\t"+all_d[i]+"\t"+str(B_cout[i])+"\n")

with open("A-C.txt","w") as f:
    f.write("A\tB\tC\tnum\n")
    for i in C_cout:
        f.write(all_d[B[C[i]]]+"\t"+all_d[C[i]]+"\t"+all_d[i]+"\t"+str(C_cout[i])+"\n")

#with open("D.txt","w") as f:
    #f.write("D\tnum\n")
    #for i in D_cout:
        #f.write(i+"\t"+str(D_cout[i])+"\n")

with open("err.txt","w") as f:
    f.write("\n".join(err))
    
print("OK!")
    
