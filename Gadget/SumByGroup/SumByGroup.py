#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/12 14:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : SumByGroup.py
#
# Python implementation of sum by group.

import numpy as np
import sys

map_p = sys.argv[1]

matrix_p = sys.argv[2]

ke = int(sys.argv[3])

va = int(sys.argv[4])


def getMap(path, ke, va, sep = ",", head = 1):
    with open(path) as f:
        ls = f.readlines()
    ls = [i.strip().split("\t") for i in ls]
    tem = dict()
    for i in ls[head:]:
        k_ls = i[ke].split(sep)
        for j in k_ls:
            if j not in tem:
                tem[j] = set()
            tem[j].update(i[va].split(sep))       
    return tem

def readMatrix(path):
    with open(path) as f:
        ls = f.readlines()
    coun = dict()
    for i in ls[1:]:
        tem = i.strip().split("\t")
        coun[tem[0]] = np.array(tem[1:],dtype=float)
    return coun, ls[0].strip().split("\t")


map_ = getMap(map_p,ke,va)
matrix_ = readMatrix(matrix_p)

new_matrix = dict()
for i in map_.keys():
    new_matrix[i] = np.array([0]*(len(matrix_[1])-1),dtype=float)
    for j in list(map_[i]):
        if j in matrix_[0].keys():
            new_matrix[i] += matrix_[0][j]

with open("out.count","w") as f:
    f.write("\t".join(matrix_[1])+"\n")
    for i in new_matrix:
        tem = [str(j) for j in list(new_matrix[i])]
        f.write(i+"\t"+"\t".join(tem)+"\n")

all_c = np.array([0]*(len(matrix_[1])-1),dtype=float)
for i in matrix_[0]:
    all_c += matrix_[0][i]
all_c = [str(j) for j in list(all_c)]
with open("all.count","w") as f:
    f.write("\t".join(matrix_[1])+"\n")
    f.write("all_gene\t"+"\t".join(all_c)+"\n")
print("ok!")
