#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/3/11 16:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : GOoboAnnotationExtractor.py
#
# Parse the go.OBO file.

import sys
ipath = sys.argv[1]
import re
with open(ipath) as f:
    t = f.read()
ver = re.search("releases/(.*)",t)[1]
ls = t.split("[Term]")
f = open(ver+"_go_term_list.txt","w")
for i in ls:
    if "id: " in i:
        id_ = re.search("id: (.*?)\n",i)[1]
        name = re.search("name: (.*?)\n",i)[1]
        ns = re.search("namespace: (.*?)\n",i)[1]
        alid = re.findall("alt_id: (.*?)\n",i)
        f.write(id_+"\t"+name+"\t"+ns+"\n")
        for i in alid:
            f.write(i+"\t"+name+"\t"+ns+"\n")

f.close()
        
        
