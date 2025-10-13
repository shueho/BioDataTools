#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/7 18:30
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @SupFile : GenoSpider.py
# @File    : offlineExtraction.py
#
# Use offline packages.

import sys
import os
import requests

HOME = os.path.abspath(sys.path[0])
PWD = os.path.abspath('.')
if len(sys.argv) == 2:
	URL = sys.argv[1]
else:
	URL = "https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip"

def fix_taxdmp():
	import zipfile
	zip_file = zipfile.ZipFile(HOME+"/taxdmp.zip")
	zip_extract = zip_file.extractall(HOME+"/.taxdmp")
	print("taxdmp.zip: Unzip done!")

ON = 0
if not os.path.exists(HOME+"/.taxdmp"):
	if os.path.exists(HOME+"/taxdmp.zip"):
		print("Find the taxdmp.zip you downloaded! Unzip it for you!")
		try:
			fix_taxdmp()
			ON = 1
		except:
			print("Error! The compressed download is not complete, please download again! https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip")
	else:
		print("Warning! Offline database not found! Switched to online mode for you.")
		print("Please download the species database file https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip to: "+HOME)
		print("It is recommended that you first use a one-click download command such as wget:\n\
	wget https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip -o {}\n\
or use the download function that comes with this script. (Failure is possible!):\n\
	python offlineExtraction.py".format(HOME.replace("\\","/")+"/taxdmp.zip"))

def download_taxdmp(url="https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip"):
	print("wait! Attention! Since downloading the database is slow, it is recommended that you download it yourself.")
	taxdmp_zip = requests.get(url, stream=True)	
	with open(HOME+"/taxdmp.zip", "wb") as f:
		FLAG = 0
		for i in taxdmp_zip.iter_content(10240):
			FLAG += 10
			f.write(i)
			if FLAG % 1024 == 0:
				print("Current download progress: {:.1f} Mb.".format(FLAG/1024))
	print("Download successful!")
	fix_taxdmp()

if __name__=='__main__':
	download_taxdmp(url=URL)