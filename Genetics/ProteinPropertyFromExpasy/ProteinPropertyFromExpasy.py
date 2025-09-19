#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2022/3/25 18:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : ProteinPropertyFromExpasy.py
#
# Protein physicochemical properties were obtained from Expasy in batches.

from urllib import request
import urllib.parse
import sys

fasta_path = sys.argv[1]

item_ls = ["Number of amino acids",
           "Molecular weight",
           "Theoretical pI",
           "Instability index",
           "Aliphatic index",
           "Grand average of hydropathicity (GRAVY)"]

try:
    f = open("expasy_output.csv","r")
    f.close()
except:
    f = open("expasy_output.csv","w")
    f.write("id,")
    for i in item_ls:
            f.write(i+",")
    f.write("\n")
    f.close()
    

def askURL(seq):
    url = "https://web.expasy.org/cgi-bin/protparam/protparam"
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Referer":"https://web.expasy.org/protparam/"
            }
    data = {"sequence":seq}
    post_data = urllib.parse.urlencode(data).encode("utf-8")

    respond = request.Request(url=url,headers=head,data=post_data,method="POST")
    html = request.urlopen(respond).read().decode("utf-8")
    return html

def out_info(txt):
    ls = txt.split("\n")
    lt = []
    #for i in ls:
	#if "<B>" in i or "instability index" in i:
            #lt.append(i)
            
    d={}
    for i in ls:
        if "Number of amino acids" in i:
            d["Number of amino acids"]=i.split(">")[-1].strip()
        if "Molecular weight" in i:
            d["Molecular weight"]=i.split(">")[-1].strip()
        if "Theoretical pI" in i:
            d["Theoretical pI"]=i.split(">")[-1].strip()
        if "instability" in i:
            d["Instability index"]=i.split("e")[-1].strip()
        if "Aliphatic index" in i:
            d["Aliphatic index"]=i.split(">")[-1].strip()
        if "Grand average of hydropathicity (GRAVY)" in i:
            d["Grand average of hydropathicity (GRAVY)"]=i.split(">")[-1].strip()
    return d

def fn(seq):
    d = out_info(askURL(seq))
    with open("expasy_output.csv","a") as f:
        for i in item_ls:
            f.write(d[i]+",")
        f.write("\n")

def get_seq(file_name):
    d = {}
    with open(file_name,"r",encoding="utf-8") as f:
        text_lis = f.readlines()
    for i in text_lis:
        if not i.strip():
            continue
        if i.strip()[0] == ">":
            seqId = i.strip().split(" ")[0].strip(">")
            d[seqId] = ""
        else:
            d[seqId] += i.strip()
    return d

def main():
    fi = fasta_path.strip()
    sd = get_seq(fi)
    lensd = len(sd)
    flag = 1
    for item in sd:
        with open("expasy_output.csv","a") as f:
            f.write(item+",")
        print("{}/{}:{}".format(flag,lensd,item))
        try:
            fn(sd[item])
        except:
            try:
                fn(sd[item])
            except:
                with open("expasy_output.csv","a") as f:
                    f.write("error!\n")
                print("{}:error!".format(item))
        flag += 1

main()
    

