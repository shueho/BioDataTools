#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : get_sum.py
#
# Place the script in the parent directory of the assembly evaluation results completed by quast software to obtain the assembly evaluation information summary table.

import os
print("Author: XueHao\nE-mail: studid@163.com")
print("begin")
ls = list(os.popen("find -name transposed_report.tsv"))
ls = [i.strip() for i in ls if i.strip()]

fi = open("sumarry.tsv","w")
with open(ls[0]) as f:
    tem = f.readlines()
    fi.write("sample_ID\t"+tem[0])

def get_one(path):
    with open(path) as f:
        tem = f.readlines()
    fi.write(i.split("/")[-2]+"\t"+tem[1])

for i in ls:
    get_one(i)

fi.close()
print("OK!")
