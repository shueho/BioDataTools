#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/2/4 0:50
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : CountByGroup.py
#
# Given the three levels of map A-B-C, find the C elements in A and count them.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--mapa", help="The path of the large group map.", default=None)
parser.add_argument("-b", "--mapb", help="The path of the small group map.", default=None)
parser.add_argument("-k", "--kea", help="The column number of the large group key.", default=0, type=int)
parser.add_argument("-K", "--keb", help="The column number of the small group key.", default=0, type=int)
parser.add_argument("-v", "--vaa", help="The column number of the large group value.", default=1, type=int)
parser.add_argument("-V", "--vab", help="The column number of the small group value.", default=1, type=int)
parser.add_argument("-s", "--sea", help="The key-value separator of the large group value.", default="\t")
parser.add_argument("-S", "--seb", help="The key-value separator of the small group value.", default="\t")
parser.add_argument("--seka", help="The key separator of the large group value.", default=",")
parser.add_argument("--sekb", help="The key separator of the small group value.", default=",")
parser.add_argument("--seva", help="The value separator of the large group value.", default=",")
parser.add_argument("--sevb", help="The value separator of the small group value.", default=",")
parser.add_argument("-n", "--heada", help="The Number of excluded rows of the large group value.", default=0, type=int)
parser.add_argument("-N", "--headb", help="The Number of excluded rows of the small group value.", default=0, type=int)
args = parser.parse_args()

def readMap(path, ke=0, va=1, sep="\t", sep_key=",", sep_value=",", head=0, form_=set):
	with open(path) as f:
		ls = f.readlines()
	tem = dict()
	for i in ls[head:]:
		t = i.strip().split(sep)
		k_ls = t[ke].split(sep_key)
		if not k_ls:
			continue
		for j in k_ls:
			if j not in tem:
				tem[j] = set()
			tem[j].update(t[va].split(sep_value)) 
	if form_ != set:
		for i in tem:
			tem[i] = form_(tem[i])
	return tem

def countSet(pA, pB, 
	keA=0, vaA=1, sepA="\t", sep_keyA=",", sep_valueA=",", headA=0, 
	keB=0, vaB=1, sepB="\t", sep_keyB=",", sep_valueB=",", headB=0):
	da = readMap(pA, ke=keA, va=vaA, sep=sepA, sep_key=sep_keyA, sep_value=sep_valueA, head=headA, form_=list)
	db = db = readMap(pB, ke=keB, va=vaB, sep=sepB, sep_key=sep_keyB, sep_value=sep_valueB, head=headB)
	dc = dict()
	for i in da:
		dc[i] = set()
		for j in da[i]:
			if j not in db:
				continue
			dc[i].update(db[j])
	return dc

a=countSet(args.mapa, args.mapb, 
	keA=args.kea, vaA=args.vaa, sepA=args.sea, sep_keyA=args.seka, sep_valueA=args.seva, headA=args.heada, 
	keB=args.keb, vaB=args.vab, sepB=args.seb, sep_keyB=args.sekb, sep_valueB=args.sevb, headB=args.headb)

with open("count_Map.txt","w") as f:
	for i in a:
		tem = list(a[i])
		f.write(i+"\t"+str(len(tem))+"\t"+";".join(tem)+"\n")