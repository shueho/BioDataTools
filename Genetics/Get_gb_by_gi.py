#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/7/30 13:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : Get_gb_by_gi.py
#
# Crawl the corresponding genebank file by reading the GI number.

import os
import sys
path = sys.argv[1]
file_list = os.listdir(path)
file_list = [i.replace("_gi.txt","") for i in file_list if "_gi.txt" in i]
try:
    os.makedirs("gb")
except:
    ...

from urllib import request
def askURL(url):#爬虫函数
     headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.10251 SLBChan/15",
                "referer":"https://www.ncbi.nlm.nih.gov/nuccore/MK637058.1"
                }
     respond = request.Request(url,headers=headers)
     html = request.urlopen(respond).read().decode("utf-8")
     
     return html

def getGB(gid):
    url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=genbank&id={}&conwithfeat=on&hide-cdd=on".format(gid)
    return askURL(url)

def downloadGB(filename):
    with open(filename+"_gi.txt") as f:
        gi_list = f.readlines()
        gi_list = [i.strip() for i in gi_list if i]
    for gi in gi_list:
        try:
            with open("gb/"+os.path.basename(filename)+"_"+gi+".gb","w") as f:
                f.write(getGB(gi))
                print(gi+"\tsuccess")
        except:
            print(gi+"\terror")

def main():
    for i in file_list:
        downloadGB(path+"/"+i)

main()