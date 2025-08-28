#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2024/1/4 16:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @SupFile : GenoSpider.py
# @File    : getGenomicInformation.py
#
# Get information about genome.

import requests

all_trait = ['accession', 
             'current_accession', 
             'paired_accession', 
             'source_database', 
             'organism.tax_id', 
             'organism.organism_name', 
             'organism.common_name', 
             'assembly_info.assembly_level', 
             'assembly_info.assembly_status', 
             'assembly_info.paired_assembly.accession', 
             'assembly_info.paired_assembly.status', 
             'assembly_info.assembly_name', 
             'assembly_info.assembly_type', 
             'assembly_info.bioproject_lineage', 
             'assembly_info.bioproject_accession', 
             'assembly_info.release_date', 
             'assembly_info.submitter', 
             'assembly_info.refseq_category', 
             'assembly_info.sequencing_tech', 
             'assembly_info.assembly_method', 
             'assembly_info.biosample.accession', 
             'assembly_info.biosample.last_updated', 
             'assembly_info.biosample.publication_date', 
             'assembly_info.biosample.submission_date', 
             'assembly_info.biosample.sample_ids', 
             'assembly_info.biosample.description.title', 
             'assembly_info.biosample.description.organism.tax_id', 
             'assembly_info.biosample.description.organism.organism_name', 
             'assembly_info.biosample.owner.name', 
             'assembly_info.biosample.models', 
             'assembly_info.biosample.package', 
             'assembly_info.biosample.attributes', 
             'assembly_info.biosample.status.status', 
             'assembly_info.biosample.status.when', 
             'assembly_info.blast_url', 
             #'assembly_info.comments', 
             'assembly_stats.total_number_of_chromosomes', 
             'assembly_stats.total_sequence_length', 
             'assembly_stats.total_ungapped_length', 
             'assembly_stats.number_of_contigs', 
             'assembly_stats.contig_n50', 
             'assembly_stats.contig_l50', 
             'assembly_stats.number_of_scaffolds', 
             'assembly_stats.scaffold_n50', 
             'assembly_stats.scaffold_l50', 
             'assembly_stats.number_of_component_sequences', 
             'assembly_stats.gc_count', 
             'assembly_stats.gc_percent', 
             'assembly_stats.genome_coverage', 
             'annotation_info.name', 
             'annotation_info.provider', 
             'annotation_info.release_date', 
             'annotation_info.report_url', 
             'annotation_info.stats.gene_counts.total', 
             'annotation_info.stats.gene_counts.protein_coding', 
             'annotation_info.stats.gene_counts.non_coding', 
             'annotation_info.stats.gene_counts.pseudogene', 
             'annotation_info.busco.busco_lineage', 
             'annotation_info.busco.busco_ver', 
             'annotation_info.busco.complete', 
             'annotation_info.busco.single_copy', 
             'annotation_info.busco.duplicated', 
             'annotation_info.busco.fragmented', 
             'annotation_info.busco.missing', 
             'annotation_info.busco.total_count', 
             'annotation_info.method', 
             'annotation_info.pipeline', 
             'annotation_info.software_version', 
             'annotation_info.status', 
             'wgs_info.wgs_project_accession', 
             'wgs_info.master_wgs_url', 
             'wgs_info.wgs_contigs_url']
#=====
fin_trait = ['accession', 
             'organism.tax_id', 
             'organism.organism_name', 
             'organism.common_name', 
             'assembly_info.assembly_level', 
             'assembly_info.assembly_status', 
			 'assembly_info.release_date',
             'assembly_info.refseq_category', 
             'assembly_info.biosample.accession', 
             'assembly_stats.total_number_of_chromosomes', 
             'assembly_stats.total_sequence_length', 
             'assembly_stats.total_ungapped_length', 
             'assembly_stats.number_of_contigs', 
             'assembly_stats.contig_n50', 
             'assembly_stats.contig_l50', 
             'assembly_stats.number_of_scaffolds', 
             'assembly_stats.scaffold_n50', 
             'assembly_stats.scaffold_l50', 
             'assembly_stats.number_of_component_sequences', 
             'assembly_stats.gc_count', 
             'assembly_stats.gc_percent', 
             'assembly_stats.genome_coverage', 
             'annotation_info.stats.gene_counts.total', 
             'annotation_info.stats.gene_counts.protein_coding', 
             'annotation_info.stats.gene_counts.non_coding', 
             'annotation_info.stats.gene_counts.pseudogene', 
             ]
#==

def prefix_dict(di_, prefix_s=''):
    return {prefix_s + k: v for k, v in di_.items()}

def spear_dict(di_, con_s='.'):
    ret_di = {}
    for k, v in di_.items():
        if type(v) is dict:
            v = spear_dict(v)
            ret_di.update(prefix_dict(v, prefix_s=k + con_s))
        else:
            ret_di.update({k: v})
    return ret_di
#=====  #Here we can expand the dictionary

def get_assembly(t_id, page_token=None):   #Implementing page turning
    headers = {
        #"cookie" : "?", 
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36", 
     }
    url = "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/dataset_report"
    j_p = {"filters":{"exclude_paired_reports":True, "assembly_version":"current"}, "page_size":1000, "page_token":page_token, "returned_content":"COMPLETE", "taxons":[str(t_id)]}
    all_js = requests.post(url, headers=headers, json=j_p).json()
    ls_accession = []
    if all_js:
        ls_accession = all_js["reports"]
        if "next_page_token" in all_js:
            pt = all_js["next_page_token"]
        else:
            pt = None
    return pt, ls_accession

def get_all_assembly(t_id):    #taxID --> information about genome
    all_ls_accession = []
    tem = get_assembly(t_id)
    all_ls_accession += tem[1]
    flag = 1
    print("page {}".format(flag))
    while tem[0]:
        flag += 1
        tem = get_assembly(t_id, page_token=tem[0])
        all_ls_accession += tem[1]
        print("page {}".format(flag))
    return all_ls_accession

def get_all_assembly_main(i=None, fin=0):
	if fin:
		trait = fin_trait
	else:
		trait = all_trait
	if not i:
		ipath = input("Enter the path to the species Tax ID list file：")
		with open(ipath, encoding="utf-8") as f:
			ls = f.readlines()
	else:
		ls = [i]
	ls = [i.strip() for i in ls if i.strip()]
	with open("all_accession.txt", "w", encoding="utf-8") as f:
		f.write("\t".join(trait)+"\n")
	co = 0
	for tid in ls:
		co += 1
		print("{}/{} {}".format(co, len(ls), tid))
		tem = get_all_assembly(tid)
		for i in tem:
			td = spear_dict(i)
			for k in trait:
				if k not in td:
					td[k] = "-"
				else:
					td[k] = str(td[k]).replace("\t", "<tab>").replace("\n", "<line>")
			tls = [td[item] for item in trait]
			with open("all_accession.txt", "a", encoding="utf-8") as f:
				f.write("\t".join(tls)+"\n")
    
