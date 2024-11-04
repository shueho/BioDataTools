#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : GBRenameByX.py
#
# Read a information in the GB file and name the GB file through the information.It is mainly used for batch processing of a large number of GB files.

import os
import re
import sys
path = sys.argv[1]
item_ = sys.argv[2]

try:
    os.mkdir("output",)
except:
    ...
ls = os.listdir(path)
ls = [path+"/"+i for i in ls if ".gb" in i]


def get_sample(file_path):
    with open(file_path) as f:
        text = f.read()
    filename = re.findall('/{}="(.*?)"'.format(item_),text)[0].replace(" ","_")
    with open("./output/{}.gb".format(filename),"w") as f:
        f.write(text)

for i in ls:
    get_sample(i)