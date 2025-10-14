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

HOME = os.path.dirname(os.path.abspath(__file__))    #os.path.abspath(sys.path[0])
#PWD = os.path.abspath('.')
if len(sys.argv) == 2:
	URL = sys.argv[1]
else:
	URL = "https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz"

def fix_taxdump():
	#import zipfile
	import tarfile
	#zip_file = zipfile.ZipFile(HOME+"/taxdump.zip")
	tar_file = tarfile.open(HOME+"/taxdump.tar.gz", 'r:gz')
	#zip_extract = zip_file.extractall(HOME+"/.taxdump")
	tar_file.extractall(path=HOME+"/.taxdump")
	print("taxdump.tar.gz: Unzip done!")

ON = 0
if not os.path.exists(HOME+"/.taxdump"):
	if os.path.exists(HOME+"/taxdump.tar.gz"):
		print("Find the taxdump.tar.gz you downloaded! Unzip it for you!")
		try:
			fix_taxdump()
			ON = 1
		except:
			print("Error! The compressed download is not complete, please download again! https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.zip")
	else:
		print("Warning! Offline database not found! Switched to online mode for you.")
		print("Please download the species database file https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz to: "+HOME)
		print("It is recommended that you first use a one-click download command such as wget:\n\
	wget https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz -o {}\n\
or use the download function that comes with this script. (Failure is possible!):\n\
	python offlineExtraction.py".format(HOME.replace("\\","/")+"/taxdump.tar.gz"))

def download_taxdump(url="https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz"):
	print("wait! Attention! Since downloading the database is slow, it is recommended that you download it yourself.")
	taxdump_zip = requests.get(url, stream=True)	
	with open(HOME+"/taxdump.tar.gz", "wb") as f:
		FLAG = 0
		for i in taxdump_zip.iter_content(10240):
			FLAG += 10
			f.write(i)
			if FLAG % 1024 == 0:
				print("Current download progress: {:.1f} Mb.".format(FLAG/1024))
	print("Download successful!")
	fix_taxdump()

if __name__=='__main__':
	download_taxdump(url=URL)