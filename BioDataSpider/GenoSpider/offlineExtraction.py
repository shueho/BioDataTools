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

def fix_taxdump(p):
	#import zipfile
	import tarfile
	#zip_file = zipfile.ZipFile(HOME+"/taxdump.zip")
	tar_file = tarfile.open(p, 'r:gz')
	#zip_extract = zip_file.extractall(HOME+"/.taxdump")
	tar_file.extractall(path=HOME+"/.taxdump")
	print("taxdump.tar.gz: Unzip done!")

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
	fix_taxdump(HOME+"/taxdump.tar.gz")
if __name__=='__main__':
	
	print("""
	Default download link: https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz
	If the download speed is slow, you can specify an acceptable mirror source, such as http://xxx.xxx/taxdump.tar.gz. Use the script:
		python offlineExtraction.py http://xxx.xxx/taxdump.tar.gz
	to complete the download.
	If you cannot find a suitable download source, manually download the taxdump.tar.gz file to {} and use this script to extract it. For example:
		wget https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz -o {}
		python offlineExtraction.py taxdump.tar.gz
	If applicable, you can also use the compressed package downloaded on November 16, 2025:
		python offlineExtraction.py example/taxdump.tar.gz
		""".format(HOME.replace("\\","/"),HOME.replace("\\","/")+"/taxdump.tar.gz"))
	if os.path.exists(URL):
		fix_taxdump(URL)
	else:
		download_taxdump(url=URL)