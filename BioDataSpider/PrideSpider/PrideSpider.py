#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/9/17 23:40
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : PrideSpider.py
#
# A web crawler for retrieving information from the PRIDE database.

import os
import sys
import requests

#spFile = "sp.txt"
spFile = sys.argv[1]

URL = "https://www.ebi.ac.uk/pride/ws/archive/v3/search/projects?keyword={}&page={}&pageSize=100"

os.makedirs('json_result', exist_ok=True)

def getContent(q, page=0): # page from 0
    url = URL.format(q.strip().replace(" ", "+"), str(page))
    response = requests.get(url)
    total_records = int(response.headers.get('total_records'))
    with open("json_result/"+q.strip().replace(" ", "_")+"-"+str(page+1),"w", encoding = "utf-8") as f:
        f.write(response.text)
    print("{} : {} / {}".format(q, page+1, int(total_records/100)+1))
    flag = (page+1)*100
    if flag < total_records:
        getContent(q, page+1)
    return [q, str(total_records)]

def getAll():
    print("STEP-1: Get json result.")
    flag = 0
    with open(spFile) as f:
        ls = f.readlines()
    ls = [i.strip() for i in ls if i.strip()]  
    log_ = open("log.txt","w")
    log_.close()
    for i in ls:
        flag += 1
        print("[{} / {}]".format(flag, len(ls)))
        tem = getContent(i)
        with open("log.txt","a") as log_:
            log_.write("\t".join(tem)+"\n")
    
def readJson(path):
    pass

getAll()
