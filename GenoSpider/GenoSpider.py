#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/1/4 16: 00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : GenoSpider.py
#
# Genome Information Crawler tool.

help_doc = {"getTaxInfoFromName": "Get taxonomic information for Scientific name of species.", 
			"getTaxInfoFromNameList": "Get taxonomic information for all species in a list.", 
			"getTaxInfoFromTid": "Get taxonomic information for Tax ID of species.", 
			"getTaxInfoFromTidList": "Get taxonomic information for Tax ID in a list.", 
			"getAssembleFromName": "Get information about all genomes in a given category. It is not recommended due to the occurrence of species with the same name.", 
			"getAssembleFromTid": "Get information about all genomes in a given Tax ID.", 
			"getAssembleFromTidList": "Get information about all genomes in a given Tax ID in a list.", 
			"getTaxInfoFromAssemble": "The taxonomic information is obtained from the assembly information file. This is equivalent to the getTaxInfoFromTidList being triggered automatically after manually executing the command to get the assembly information.", 
			"mergeAssemble_TaxInfo": "Merge assembly information and species classification information files.", 
			"dataVisualization": "Output visual image.", 
			"com": "Output a list of all functions.", 
			"help": "Get complete help information.", 
			"settingOutputFormat": "View or configure the output format.", 
            "exit": "exit the program."
            }

help_num = {"1": "getTaxInfoFromName", 
			"2": "getTaxInfoFromNameList", 
			"3": "getTaxInfoFromTid", 
			"4": "getTaxInfoFromTidList", 
			"5": "getAssembleFromName", 
			"6": "getAssembleFromTid", 
			"7": "getAssembleFromTidList", 
			"8": "getTaxInfoFromAssemble", 
			"9": "mergeAssemble_TaxInfo", 
			"p": "dataVisualization", 
			"c": "com", 
			"h": "help", 
			"f": "settingOutputFormat", 
			"e": "exit"
			}

com_num = "123456789pchfe"

CONFIG = {"1": ["Simplify assembly information", False], 
          "2": ["Output picture format", "jpg", {"1": "jpg", "2": "png", "3": "svg", "4": "eps"}], 
		  "3": ["Export of image pixels", 300], 
		  "4": ["Only the reference genome is concerned", True],
		  "5": ["Use the Species Database Offline pack", False],
		  "6": ["Picture width", 8],
		  "7": ["Picture height", 10],
		  "8": ["Subgraph gap", 0.4]
		}
stc = "145"
otc = "2"
itc = "3678"

def printConfig(): 
	print("The current configuration information is displayed, and you can change it by entering the sequence number of the corresponding configuration value.")
	n = "1"
	for i in CONFIG: 
		print(i+": \t"+CONFIG[i][0]+"\t"+str(CONFIG[i][1]))
	print("======\n")
	while True: 
		getV = input("Entering an other number will return: ")
		print("======\n")
		if not getV:
			break
		if getV in stc: 
			CONFIG[getV][1] = not CONFIG[getV][1]			
		elif getV in otc: 
			for i in CONFIG[getV][2]: 
				print(i+": "+CONFIG[getV][2][i], end="\t")
			print("\n")
			optV = input("Enter the selection number: ")
			if optV in CONFIG[getV][2]: 
				CONFIG[getV][1] = CONFIG[getV][2][optV]
		elif getV in itc: 
			iptV = input("Enter the value to modify: ")
			try: 
				CONFIG[getV][1] = type(CONFIG[getV][1])(iptV)
			except: 
				print("Unsupported value!")
		else: 
			break
		for i in CONFIG: 
				print(i+": \t"+CONFIG[i][0]+"\t"+str(CONFIG[i][1]))

def printHelp(flag=1): 
	print("Listed below are all the functions of the program and detailed descriptions.\
If you have any questions, or have bugs you want to submit, please contact the author: studid@163.com. Hope to make progress with you.")
	for i in com_num: 
		en = "\t"
		if flag: 
			en += help_doc[help_num[i]]
		print(">> "+i+"\t"+help_num[i], end=en+"\n")

import sys
import os
import argparse
import offlineExtraction as oe
import getTaxClassification as gtc
import getGenomicInformation as ggi
import dataVisualization as dv

HOME = os.path.abspath(sys.path[0])
PWD = os.path.abspath('.')

if oe.ON:
	CONFIG["5"][1] = False

E = 0
def main(): 
	if len(sys.argv) == 1: 
		while True: 
			if E: 
				break
			try: 
				manu()
			except: 
				print("===\nInput format error or unknown error. Please report the process that triggered the error.\n===")
	else: 
		auto()

def manu(): 
	global E
	print("Please type a specific command Or its numerical number to excutive function! If you forget it, you can type 'help' or 'com' to get all command.")
	flag = 0
	fir = 1
	while True:
		if fir and CONFIG["5"][1]:
			import offlineGetTaxinfo as ogt
			fir = 0
		comm = input("You command: >>")
		if comm.lower() in com_num and len(comm) == 1: 
			comm = help_num[comm.lower()]
		if comm == "help": 
			printHelp()
		elif comm == "com": 
			printHelp(0)
		elif comm == "getTaxInfoFromName": 
			q = input("Enter the species name: ").strip()
			if CONFIG["5"][1]:
				ogt.taxonomy_from_name(q)
				#ogt.taxonomy_from_name(q, dict_format=1)
			else:
				r = gtc.post_taxonomy_from_name(q)
				print(r)
		elif comm == "getTaxInfoFromNameList": 
			ogt.taxonomy_from_name_list() if CONFIG["5"][1] else gtc.post_taxonomy_from_name_list() 
		elif comm == "getTaxInfoFromTid": 
			q = input("Enter the species Tax ID: ").strip()
			r = ogt.taxonomy_from_id(q) if CONFIG["5"][1] else gtc.get_taxonomy_from_id(q)
			print(r)
		elif comm == "getTaxInfoFromTidList": 
			ogt.taxonomy_from_tid_list() if CONFIG["5"][1] else gtc.post_taxonomy_from_tid_list()
		elif comm == "getAssembleFromName": 
			q = input("Enter the species name: ").strip()
			r = gtc.post_taxonomy_from_name(q)
			print("The species you might be looking for are: "+str(r))
			t = r["taxID"]
			print("The species ID of this entry is: "+t)
			ggi.get_all_assembly_main(i=t, fin=CONFIG["1"][1])
		elif comm == "getAssembleFromTid": 
			q = input("Enter the species Tax ID: ").strip()
			ggi.get_all_assembly_main(i=q, fin=CONFIG["1"][1])
		elif comm == "getAssembleFromTidList": 
			ggi.get_all_assembly_main(fin=CONFIG["1"][1])
		elif comm == "getTaxInfoFromAssemble": 
			q = input("The default is: all_accession.txt \nEnter the path to the Assemble Info file: ")
			q = q if q else "all_accession.txt"
			ogt.taxonomy_from_assembly(q) if CONFIG["5"][1] else gtc.get_taxonomy_from_assembly(q)
		elif comm == "mergeAssemble_TaxInfo": 
			q1 = input("Enter the path to the Assemble Info file: ")
			q2 = input("Enter the path to the Tax Info file: ")
			gtc.mergeInfoTable(q1, q2)
		elif comm == "dataVisualization": 
			q1 = input("The default is: mergeResult.txt \nEnter the path to the Summary information file: ").strip()
			q1 = q1 if q1 else "mergeResult.txt"
			print("===\nThe items you can choose are: "+", ".join(dv.Rank[:-1])+"\n===")
			q2 = input("Enter the category level of concern: ")
			if q2 not in dv.Rank: 
				q2 = "class"
			dv.plotAll(q1, ref=CONFIG["4"][1], MaxR=q2, dpi_=CONFIG["3"][1], format_=CONFIG["2"][1], w=CONFIG["6"][1], h=CONFIG["7"][1], hsp=CONFIG["8"][1])
		elif comm == "settingOutputFormat": 
			printConfig()
		elif comm == "exit": 
			E = 1
			break
		else: 
			flag += 1
			print(comm+": This is not the correct command!")
			if flag > 5: 
				print("You seem to be having some problems! If you forget it, you can type 'help' or 'com' to get correct command.")
				flag = 0
		continue


def auto():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--simplify", help=CONFIG["1"][0], action="store_true", default=CONFIG["1"][1])
	parser.add_argument("-f", "--format", help=CONFIG["2"][0], choices=["jpg", "png", "svg", "eps"], default=CONFIG["2"][1])
	parser.add_argument("-p", "--pixels", help=CONFIG["3"][0], type=int, default=CONFIG["3"][1])
	parser.add_argument("-r", "--reference", help=CONFIG["4"][0], action="store_true", default=CONFIG["4"][1])
	parser.add_argument("-u", "--offline", help=CONFIG["5"][0], action="store_true", default=CONFIG["5"][1])
	parser.add_argument("-w", "--width", help=CONFIG["6"][0], type=float, default=CONFIG["6"][1])
	parser.add_argument("-H", "--height", help=CONFIG["7"][0], type=float, default=CONFIG["7"][1])
	parser.add_argument("-g", "--gap", help=CONFIG["8"][0], type=float, default=CONFIG["8"][1])
	parser.add_argument("-n", "--name", help="The scientific name to retrieve.", default=None)
	parser.add_argument("-i", "--tid", help="The Taxid to retrieve.", default=None)
	parser.add_argument("-l", "--level", help="The category level of concern.", default="class")
	args = parser.parse_args()
	CONFIG["1"][1] = args.simplify
	CONFIG["2"][1] = args.format
	CONFIG["3"][1] = args.pixels
	CONFIG["4"][1] = args.reference
	CONFIG["5"][1] = args.offline
	CONFIG["6"][1] = args.width
	CONFIG["7"][1] = args.height
	CONFIG["8"][1] = args.gap
	if not args.name and not args.tid:
		exit()
	q = "all_accession.txt"
	q1 = "mergeResult.txt"
	q2 = args.level
	if args.name and not args.tid:
		r = gtc.post_taxonomy_from_name(args.name)
		print("The species you might be looking for are: "+str(r))
		t = r["taxID"]
		print("The species ID of this entry is: "+t)
		ggi.get_all_assembly_main(i=t, fin=CONFIG["1"][1])
	elif not args.name and args.tid:
		ggi.get_all_assembly_main(i=args.tid, fin=CONFIG["1"][1])	
	else:
		exit()
	if CONFIG["5"][1]:
		import offlineGetTaxinfo as ogt
	ogt.taxonomy_from_assembly(q) if CONFIG["5"][1] else gtc.get_taxonomy_from_assembly(q)
	dv.plotAll(q1, ref=CONFIG["4"][1], MaxR=q2, dpi_=CONFIG["3"][1], format_=CONFIG["2"][1], w=CONFIG["6"][1], h=CONFIG["7"][1], hsp=CONFIG["8"][1])

if __name__=='__main__': 
	main()