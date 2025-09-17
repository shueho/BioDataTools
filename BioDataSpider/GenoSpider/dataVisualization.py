#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/5 8:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @SupFile : GenoSpider.py
# @File    : dataVisualization.py
#
# Data Processing and visualization.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "Times New Roman"

Rank = ["superkingdom",
        "kingdom",
        "phylum",
		"subphylum", 
        "class",
        "subclass",
		"infraclass",
		"superorder",
        "order",
        "family",
        "genus",
        "species",
        "taxID"
        ]

Sig = ["assembly_info.assembly_level",
       "assembly_info.refseq_category",
       "assembly_info.release_date",
       "assembly_stats.total_number_of_chromosomes",
       "assembly_stats.total_sequence_length",
       "assembly_stats.number_of_contigs",
       "assembly_stats.gc_percent",
       "annotation_info.stats.gene_counts.protein_coding",
       "annotation_info.stats.gene_counts.non_coding",
       "annotation_info.stats.gene_counts.pseudogene"
       ]

Level = ["Complete Genome",
         "Chromosome",
         "Scaffold",
         "Contig"
         ]


def filteringData(path, ref=False, fin=1, MaxR=None):
	#path: The merged table.
	#ref: Filter the reference genome.
	#fin: Simplify the output table.
	#MaxR: Maximum taxonomic rank.
	with open(path,encoding="utf-8") as f:
		ls = f.readlines()
	ls = [i.strip().split("\t") for i in ls if i.strip()]
	data = pd.DataFrame(ls[1:],columns=ls[0])
	if ref:
		data = data[data["assembly_info.refseq_category"]=="representative genome"]
	if fin:
		data = data[Rank+Sig]
	if MaxR:
		data = data[Rank[Rank.index(MaxR):]+Sig]
	return data

def plotAll(path, ref=False, fin=1, MaxR=None, dpi_=300, format_="jpg", w=8, h=10, hsp=0.4): #Width Height HSPace
	d = filteringData(path,ref=ref,fin=fin,MaxR=MaxR)
	plt.figure(figsize=(w,h))

	plt.subplot(311)
	category = list(d[d.columns[0]])
	for i in range(len(category)):
		if category[i] == "-":
			category[i] = "Other"
	g = list(d["assembly_info.assembly_level"])
	uni = list(d["taxID"])
	tid_to_c = dict()   #tid: MaxR
	tid_to_lev = dict()   #tid: Level
	for i in range(len(category)):
		tid_to_c[uni[i]] = category[i]
		if uni[i] not in tid_to_lev:
			tid_to_lev[uni[i]] = g[i]
		elif Level.index(g[i]) < Level.index(tid_to_lev[uni[i]]):
			tid_to_lev[uni[i]] = g[i]
	count_list = []
	category = list(set(category))
	result = pd.DataFrame(0,columns=category,index=Level)        
	for i in tid_to_c:
		result[tid_to_c[i]][tid_to_lev[i]] += 1
	result.to_csv("assemblyLevelCountsFor_{}.txt".format(d.columns[0]),sep="\t")
	ly = [0]*len(result.columns)
	for i in Level:
		plt.barh(result.columns, result.loc[i],label=i,left=ly)
		ly += result.loc[i]
	plt.xlabel("Number")
	plt.title("Statistics of the number of genome assembly levels in different {}.".format(d.columns[0]))
	plt.legend(frameon=False)

	plt.subplot(312)
	gc = list(pd.to_numeric(d['assembly_stats.gc_percent']))
	tem = dict()
	category = list(d[d.columns[0]])
	for i in range(len(category)):
		if category[i] in tem:
			tem[category[i]].append(gc[i])
		else:
			tem[category[i]] = [gc[i]]
	tem = {i: pd.Series(np.array(tem[i])) for i in tem}
	pd.DataFrame(tem).boxplot(vert=False, patch_artist=True)
	plt.xlabel("Proportion/%")
	plt.title("Statistics of the GC content in different {}.".format(d.columns[0]))
	plt.grid(False)

	plt.subplot(313)
	release = list(d["assembly_info.release_date"])
	release = [int(i.split("-")[0]) for i in release]
	coun = dict()
	coun_cu = dict()
	ymin = min(release)
	ymax = max(release)
	for i in range(ymin, ymax+1):
		coun[i] = 0
	for i in release:
		coun[i] += 1
	coun_cu[ymin] = coun[ymin]
	for i in range(ymin+1, ymax+1):
		coun_cu[i] = coun_cu[i-1] + coun[i]
	x = [i for i in range(ymin, ymax+1)]
	y1 = [coun[i] for i in range(ymin, ymax+1)]
	y2 = [coun_cu[i] for i in range(ymin, ymax+1)]
	plt.plot(x, y1, 'r', marker='*', markersize=10)
	plt.plot(x, y2, 'b', marker='*', markersize=10)
	plt.legend(["Annual Increment", "Total"],frameon=False)
	plt.xticks(np.arange(ymin, ymax+1, 2))
	plt.xlabel("Year")
	plt.ylabel("Genome number")
	plt.title("Statistics on the number of NCBI assembly information submissions.")
	plt.subplots_adjust(hspace=hsp)
	plt.savefig("OverviewDiagram_{}dpi.{}".format(dpi_,format_), dpi=dpi_, format=format_, width=w, height=h)
	plt.close()
	print("Image export complete!")

