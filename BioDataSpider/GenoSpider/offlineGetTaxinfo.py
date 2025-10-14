#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/7 21:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @SupFile : GenoSpider.py, getTaxClassification.py
# @File    : offlineGetTaxinfo.py
#
# Parsing species database offline package.

import sys
import os
import getTaxClassification as gtc

HOME = os.path.dirname(os.path.abspath(__file__))    #os.path.abspath(sys.path[0])
#PWD = os.path.abspath('.')


def idNameMap(path):   #id: Name
    with open(path) as f:
        ls = f.readlines()
    n_map = dict()
    for i in ls:
        if "|	scientific name	|" in i:
            tem = i.split("|")
            n_map[tem[0].strip()] = tem[1].strip()
    return n_map

def nameIdMap(path):   #Name: [id]
    with open(path) as f:
        ls = f.readlines()
    i_map = dict()
    for i in ls:
        tem = i.split("|")
        if tem[1].strip() in i_map:
            i_map[tem[1].strip()].append(tem[0].strip())
        else:
            i_map[tem[1].strip()] = [tem[0].strip()]
    return i_map

def readNodes(path): #id: [sup, lev]
    with open(path) as f:
        ls = f.readlines()
    dic = dict()
    for i in ls:
        tem = i.split("|")
        item = tem[0].strip()
        sup = tem[1].strip()
        lev = tem[2].strip()
        if sup == item:
            sup = None
        dic[item] = [sup, lev]
    return dic
    
print("Load the offline package!")
print("1/3 Read the name-tid map.")
n_iMap = nameIdMap(HOME+"/.taxdump/names.dmp")
print("2/3 Read the tid-name map.")
i_nMap = idNameMap(HOME+"/.taxdump/names.dmp")
print("3/3 Read the tid-nodes map.")
nodes = readNodes(HOME+"/.taxdump/nodes.dmp")
print("Loaded successfully!")

def tracingPedigree(item, fir=1):   #test
    if fir:
        print("Query: "+item)
    if item == None:
        return 
    print(item, i_nMap[item], nodes[item][1])
    tracingPedigree(nodes[item][0], fir=0)
               
def taxonomy_from_id(tid):   # == gtc:post_taxonomy_from_name(query)
    ls = []
    def getPedigree(item, fir=1):
        nonlocal ls
        if fir:
            ls += [("query", i_nMap[item]), ("flag", "Offline fetching"), ("taxID", item)]
        if item == None:
            return
        ls.append((nodes[item][1], i_nMap[item]))
        getPedigree(nodes[item][0], fir=0)
    getPedigree(tid)
    all_d = dict()
    for i in ls:
        if i[0] in all_d:
            all_d[i[0]] += "&"+i[1]
        else:
            all_d[i[0]] = i[1]
    for i in gtc.TAX_RANK:
        if i not in all_d:
            all_d[i] = "-"
    return all_d

def taxonomy_from_name(n, dict_format=0):
    try:
        tids = n_iMap[n]
    except:
        tids = []
    print("{}: {} were retrieved for the offline package.".format(n, len(tids)))
    if not dict_format:
        for i in tids:
            tracingPedigree(i)
    else:
        if len(tids) != 1 :
            print("Too many target.")
            with open("MultipleMatching_tid.list", "a", encoding="utf-8") as f:
                f.write("\n".join(tids)+"\n")
            all_d = dict()
            for i in gtc.TAX_RANK:
                all_d[i] = "-"
            all_d["query"] = n
            if len(tids) > 1:
                all_d["flag"] = "Too many target."+"/".join(tids)
            else:
                all_d["flag"] = "Not retrieved"
            return all_d
        else:
            return taxonomy_from_id(tids[0])

def taxonomy_from_name_list():
    ipath = input("Enter the path to the species name list file：")
    with open("MultipleMatching_tid.list", "w", encoding="utf-8") as f:
        ...
    with open(ipath, encoding="utf-8") as f:
        ls = f.readlines()
    ls = [i.strip() for i in ls if i.strip()]
    gtc.writeInfoDict(path="NameListToTaxinfo_{}.txt".format(gtc.baseName(ipath)), cover=1)
    co = 0
    for i in ls:
        co += 1
        d = taxonomy_from_name(i, dict_format=1)
        gtc.writeInfoDict(path="NameListToTaxinfo_{}.txt".format(gtc.baseName(ipath)), d=d)
        print("{}/{} {}".format(co, len(ls), i))
    print("FROM TID")
    with open("MultipleMatching_tid.list", encoding="utf-8") as f:
        ls = f.readlines()
        ls = [i.strip() for i in ls if i.strip()]
        gtc.writeInfoDict(path="MultipleMatching_NameListToTaxinfo_{}.txt".format(gtc.baseName(ipath)), cover=1)
        co = 0
        for i in ls:
            co += 1
            d = taxonomy_from_id(i)
            gtc.writeInfoDict(path="MultipleMatching_NameListToTaxinfo_{}.txt".format(gtc.baseName(ipath)), d=d)
            print("{}/{} {}".format(co, len(ls), i))

def taxonomy_from_tid_list(in_=None):
    if not in_:
        ipath = input("Enter the path to the species Tax ID list file：")
        with open(ipath, encoding="utf-8") as f:
            ls = f.readlines()
        ls = [i.strip() for i in ls if i.strip()]
    else:
        ls = in_
        ipath = "autoInput.txt"
    co = 0
    gtc.writeInfoDict(path="TidListToTaxinfo_{}.txt".format(gtc.baseName(ipath)), cover=1)
    for i in ls:
        co += 1
        try:
            d = taxonomy_from_id(i)
        except:
            d = gtc.get_taxonomy_from_id(i)
        gtc.writeInfoDict(path="TidListToTaxinfo_{}.txt".format(gtc.baseName(ipath)), d=d)
        print("{}/{} {}".format(co, len(ls), i))

def taxonomy_from_assembly(path):
    with open(path, encoding="utf-8") as f:
        ls = f.readlines()
    ls = [i.strip().split("\t") for i in ls if i.strip()]
    tid_index = ls[0].index("organism.tax_id")
    tid_list = [i[tid_index] for i in ls[1:]]
    tid_list = list(set(tid_list))
    taxonomy_from_tid_list(in_=tid_list)
    gtc.mergeInfoTable(path,"TidListToTaxinfo_autoInput.txt")
    
