

import os

mpath = "../pro_matrix.txt"
p = os.listdir("4dtv")

with open(mpath) as f:
    ls = f.readlines()
d = dict()
sam = ls[0].strip().split("\t")[1:]
for i in ls[1:]:
    tem = i.strip().split("\t")
    d[tem[0]] = tem[1:]

def readfasta(path):
    with open(path) as f:
        tem = f.readlines()
    sd = dict()
    for i in tem:
        if ">" in i:
            flag = i.strip("\n>")
            sd[flag] = ""
        else:
            sd[flag] += i.strip()
    return sd

ad = dict()
for i in p:
    ad.update(readfasta("4dtv/"+i))
fia = dict()
for i in sam:
    fia[i] = ""

for i in d:
    for j in range(len(sam)):
        if d[i][j] in ad:
            fia[sam[j]] += ad[d[i][j]]

f = open("4dtv.fasta","w")
for i in fia:
    f.write(">"+i+"\n"+fia[i]+"\n")
f.close()

