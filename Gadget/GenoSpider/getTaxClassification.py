#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/4 16:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @SupFile : GenoSpider.py
# @File    : getTaxClassification.py
#
# Get information about species taxonomy.

import requests
import os
import re
import time

#Classification level.
TAX_RANK = ["query", 
            "flag", 
            "taxID", 
            "no_rank", 
            "clade", 
            "superkingdom", 
            "kingdom", 
            "subkingdom", 
            "superphylum", 
            "phylum", 
            "subphylum", 
            "superclass", 
            "class", 
            "subclass", 
            "infraclass", 
            "cohort", 
            "subcohort", 
            "superorder", 
            "order", 
            "suborder", 
            "infraorder", 
            "parvorder", 
            "superfamily", 
            "family", 
            "subfamily", 
            "tribe", 
            "subtribe", 
            "genus", 
            "subgenus", 
            "species_group", 
            "species_subgroup", 
            "species", 
            "forma_specialis", 
            "subspecies", 
            "varietas"
            ]

def baseName(path):   #Extract filenames with postfixes removed.
	return ".".join(os.path.basename(path).split(".")[:-1])

def writeInfoDict(path, d=None, cover=0):
	cover = "w" if cover else "a"
	if not d:
		with open(path, cover, encoding="utf-8") as f:
			f.write("\t".join(TAX_RANK)+"\n")
		return
	tem = [d[j] for j in TAX_RANK]
	with open(path, cover, encoding="utf-8") as f:
		f.write("\t".join(tem)+"\n")

def post_taxonomy_from_name(query):   #Species name --> taxID and classification
    headers = {
        #"cookie" : "?", 
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36", 
     }
    all_d = dict()
    for i in TAX_RANK:
        all_d[i] = "-"    
    all_d["query"] = query.strip()
    url = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi"
    post_data = {"mode":"Undef", 
            "name":query.strip(), 
            "lvl": "0"}
    try:
        all_text = requests.post(url, data=post_data, headers=headers).text
    except:
        all_d["flag"] = "non-knowerror."
        return all_d
    if "No result found in the Taxonomy database for complete name" in all_text:
        all_d["flag"] = "Miss taxonomy ID."
        return all_d
    try:
        all_d["taxID"] = re.search(r'Taxonomy ID: (.+?)\<', all_text).group(1)
    except:
        all_d["flag"] = "Too many target."
        tid_list = re.findall("amp;id=(.*?)&amp", all_text)
        all_d["flag"] += "/".join(tid_list)
        with open("MultipleMatching_tid.list", "a", encoding="utf-8") as f:
            f.write("\n".join(tid_list)+"\n")
        return all_d
    try:        
        cla = re.findall('TITLE=\"(.*?)\"\>(.*?)\<', all_text)
        for i in cla:
            if all_d[i[0].replace(" ", "_")] == "-":
                all_d[i[0].replace(" ", "_")] = i[1]
            else:
                all_d[i[0].replace(" ", "_")] += "&"+i[1]
        RAN = re.search('Rank: \<strong\>(.*?)\<', all_text).group(1).replace(" ", "_")
        all_d[RAN] = query.strip()
        all_d["flag"] = "finish!"
    except:
        all_d["flag"] = "Error."
    return all_d

def post_taxonomy_from_name_list():   #Species name list --> taxID and classification
	ipath = input("Enter the path to the species name list file：")
	with open("MultipleMatching_tid.list", "w", encoding="utf-8") as f:
		...
	with open(ipath, encoding="utf-8") as f:
		ls = f.readlines()
	ls = [i.strip() for i in ls if i.strip()]
	writeInfoDict(path="NameListToTaxinfo_{}.txt".format(baseName(ipath)), cover=1)
	co = 0
	for i in ls:
		co += 1
		d = post_taxonomy_from_name(i)
		writeInfoDict(path="NameListToTaxinfo_{}.txt".format(baseName(ipath)), d=d)
		print("{}/{} {}".format(co, len(ls), i))
		time.sleep(0.1)
	print("FROM TID")
	with open("MultipleMatching_tid.list", encoding="utf-8") as f:
		ls = f.readlines()
	ls = [i.strip() for i in ls if i.strip()]
	writeInfoDict(path="MultipleMatching_NameListToTaxinfo_{}.txt".format(baseName(ipath)), cover=1)
	co = 0
	for i in ls:
		co += 1
		d = get_taxonomy_from_id(i)
		writeInfoDict(path="MultipleMatching_NameListToTaxinfo_{}.txt".format(baseName(ipath)), d=d)
		print("{}/{} {}".format(co, len(ls), i))
		time.sleep(0.1)

def get_taxonomy_from_id(tid):    #taxID --> classification
    headers = {
        #"cookie" : "?", 
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36", 
     }
    all_d = dict()
    for i in TAX_RANK:
        all_d[i] = "-"        
    url = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&id={}&lvl=0&srchmode=1&keep=1&unlock".format(tid)
    all_text = requests.get(url, headers=headers).text
    all_d["taxID"] = str(tid)
    try:        
        cla = re.findall('TITLE=\"(.*?)\"\>(.*?)\<', all_text)
        for i in cla:
            if all_d[i[0].replace(" ", "_")] == "-":
                all_d[i[0].replace(" ", "_")] = i[1]
            else:
                all_d[i[0].replace(" ", "_")] += "&"+i[1]
        RAN = re.search('Rank: \<strong\>(.*?)\<', all_text).group(1).replace(" ", "_")
        all_d[RAN] = re.search(' \<title\>Taxonomy browser \((.*?)\)', all_text).group(1)
        all_d["flag"] = "finish!"
    except:
        all_d["flag"] = "Error."
    return all_d

def post_taxonomy_from_tid_list(in_=None):   #taxID list --> classification
	if not in_:
		ipath = input("Enter the path to the species Tax ID list file：")    
		with open(ipath, encoding="utf-8") as f:
			ls = f.readlines()
		ls = [i.strip() for i in ls if i.strip()]
	else:
		ls = in_
		ipath = "autoInput.txt"
	co = 0
	writeInfoDict(path="TidListToTaxinfo_{}.txt".format(baseName(ipath)), cover=1)
	for i in ls:
		co += 1
		d = get_taxonomy_from_id(i)
		writeInfoDict(path="TidListToTaxinfo_{}.txt".format(baseName(ipath)), d=d)
		print("{}/{} {}".format(co, len(ls), i))
		time.sleep(0.1)
        
def mergeInfoTable(acc_path,tax_path):
	flag = 0
	with open(acc_path,encoding="utf-8") as f:
		ls = f.readlines()
	ls = [i.strip().split("\t") for i in ls if i.strip()]
	otid_index = ls[0].index("organism.tax_id")
	with open(tax_path,encoding="utf-8") as f:
		taxInfo = f.readlines()
	taxInfo = [i.strip().split("\t") for i in taxInfo if i.strip()]
	tid_index = taxInfo[0].index("taxID")
	tax_dict = dict()
	for i in taxInfo[1:]:
		tax_dict[i[tid_index]] = i
	ls[0] = taxInfo[0] + ls[0]
	for tem in range(1,len(ls)):
		try:
			ls[tem] = tax_dict[ls[tem][otid_index]] + ls[tem]
		except:
			flag = 1
			print(ls[tem][otid_index]+": Classification information was not retrieved.")		
			with open("UnretrievedSpeciesNumber.txt","a",encoding="utf-8") as f:
				f.write(ls[tem][otid_index]+"\n")
			ls[tem] = ["-"] * len(taxInfo[0]) + ls[tem]
	ls = ["\t".join(i) for i in ls]
	with open("mergeResult.txt","w",encoding="utf-8") as f:
		f.write("\n".join(ls))
	if flag:
		print("Unretrieved species numbers are exported to: UnretrievedSpeciesNumber.txt")
	print("ok!")

def get_taxonomy_from_assembly(path):
	print("wait!")
	with open(path, encoding="utf-8") as f:
		ls = f.readlines()
	ls = [i.strip().split("\t") for i in ls if i.strip()]
	tid_index = ls[0].index("organism.tax_id")
	tid_list = [i[tid_index] for i in ls[1:]]
	tid_list = list(set(tid_list))
	post_taxonomy_from_tid_list(in_=tid_list)
	mergeInfoTable(path,"TidListToTaxinfo_autoInput.txt")

#Offline retrieval of species classification


	





