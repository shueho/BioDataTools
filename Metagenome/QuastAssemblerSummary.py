#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : QuastAssemblerSummary.py
#
# Place the script in the parent directory of the assembly evaluation results completed by quast software to obtain the assembly evaluation information summary table.

import os
import sys
root = sys.argv[1]

print("Author: XueHao\nE-mail: studid@163.com")
print("begin")
ls = os.listdir(root)
ls = [root+ "/" + i + "/transposed_report.tsv" for i in ls if os.path.exists(root+ "/" + i + "/transposed_report.tsv")]

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
