# BioDataTools      
一套用于生物信息学分析的通用数据处理脚本。包含组学分析、生态遗传分析等数据处理工具。     

## 1. Metagenome            
宏基因组与转录组分析数据处理和绘图脚本。         
   
### 1.1 get_sum.py    
不需要配置参数。将脚本放置在quast软件完成的装配评估结果的上机目录中，获得组装评估信息汇总表。        
** 生成文件:** sumary.tsv (表格文件，每一列表示一个样本，每一行对应一个组装数据)        
      
### 1.2 fasta_rename.py [FASTA_FILE_PATH]   
修改指定FASTA文件的每个序列中的名称，使其标准化和统一，即将序列名称按照1、2...的规则编码，用于宏基因组或者转录组合并多个样品组装结果之后，基因丰度、注释之前，可以保证合并后的fasta数据每个序列的ID是唯一的，并且可以方便后续找到差异基因后回溯序列。         
FASTA_FILE_PATH: 需要重新编号序列的FASTA文件的路径      
** 生成文件:** out_\<your fasta file name> (FASTA文件，每个序列被重新命名)   
     
### 1.3 mergeMpa.py   
这个脚本可以将许多mpa文件转换成物种丰度矩阵。不需要配置参数。将脚本放在kracken1/2或bracken软件生成的mpa文件所在的文件夹中。在此之前您可能需要运行kreport2mpa.py脚本将报告文件转换为mpa文件 。            
** 生成文件:** mpaMatrix.txt (TABLE file)   

### 1.4 splitFromLevel.py [MPA_MERGE_FILE] [SPLIT_LEVEL]     
用于从物种丰度定量结果中提取各个分类的物种丰度矩阵。     
MPA_MERGE_FILE: 由1.3 mergeMpa.py脚本生成的mpaMatrix.txt文件的路径。       
SPLIT_LEVEL: 物种丰度表的分类，以界、门、纲、目、科、属和种的首字母进行选择。Level可以从“a”、“k”、“p”、“c”、“o”、“f”、“g”、“s”或它的大写字母选择。输入“a”表示生成了所有的分类分割表。    
** 生成文件:** taxLevel_\<uppercase letter of level>_output.\<mpaMatrix file name> (一个或多个TABLE 文件)   
     
### 1.5 splitFasta.py [FASTA_FILE_PATH] [Number_of_split_files]   
***Supports all versions of python3.***   
FASTA_FILE_PATH: The FASTA file path you want to split. （要分割的FASTA文件的路径）  
Number_of_split_files: The number of split FASTA files. （分割后的文件数目）      
根据序列数将FASTA文件分割成更小的FASTA文件，比如在线KEGG注释可能会对上传的序列数有限制。   
Split FASTA files into smaller FASTA files according to the number of sequences.   
** 生成文件:** \<Split file number>_\<your fasta file name> (FASTA files)   

### 1.6 read_keg.py [KEG_FILE]   
***Supports all versions of python3.***   
KEG_FILE: KEG files downloaded from the KEGG database, such as the common ko00001.keg (Click to download: https://www.kegg.jp/kegg-bin/download_htext?htext=ko00001&format=htext&filedir=).       
解析KEG文件。可以解析从KEGG网页下载的.keg文件。  
Parse the KEG file.   
** 生成文件 1:** output_\<your keg file name> (TABLE file)   
** 生成文件 2:** ko_match_KO.txt (TABLE file)   
** 生成文件 3:** KO_map.txt (TABLE file)     

### 1.7 KEGG_pathway_geneNum.py [1.6_ 生成文件_1] [GENE_KO]    
***Supports all versions of python3.***   
1.6_ 生成文件_1: 1.6 Generated file 1 or a similar file containing the KEGG annotation results. （脚本1.6的生成文件）    
GENE_KO: The first column is the gene name and the second column is the ko number. The ko numbers are separated by commas. The example file is gk.txt. （GENE-KO映射表，第一列是基因ID或名称，第二列为ko编号，多个ko编号可以用逗号隔开，可参考示例文件）      
KEGG通路基因数量统计，导出用于KEGG注释富集绘图的数据。   
KEGG pathway gene number statistics.     
** 生成文件 1:** A.txt (all_gene is the total number of genes, and you can use this number to find the gene ratio. TABLE file)   
** 生成文件 2:** A-B.txt (TABLE file)   
** 生成文件 3:** A-C.txt (TABLE file)   
** 生成文件 4:** D.txt (TABLE file)   
** 生成文件 5:** err.txt (There is no matching KO number. TABLE file)      

### 1.8 read_goOBO.py [obo_FILE]   
***Supports all versions of python3.***   
obo_FILE: 从网站上下载的obo文件路径（打开网址：https://purl.obolibrary.org/obo/go/go-basic.obo将网页另存为txt文件即可）       
从obo文件读取并解析GO号对应的描述及分类，生成GO编号\t描述信息\t分类的三列表格。      
** 生成文件 1:** output_\<your keg file name> (TABLE file)   


## 2. Genetics     
基因组分析的数据处理，包括从NCBI下载数据的转换和部分信息的批量获取。       
        
### 2.1 Get_gb_by_gi.py
***需要安装requests库***    
通过GI编号批量下载fasta文件。    
不需要配置参数，读取脚本自动读取文件夹下以“_gi.txt”结尾的所有文本文件，每个“_gi.txt”文件包含需要抓取的GI编号。      
比如你想获取一些fasta文件，你只需要新建一个xxx_gi.txt的文件，把GI编号粘贴进去即可，之所以如此设置，是为了让你下载的fasta文件分别存放在不同的文件夹中，这在群体遗传学单倍型分析中比较常用。     
** 生成文件:** ./gb/\<your gi_list_file name>\_\<GI ACCESSION>.gb (多个GENEBANK文件)    

### 2.2 Name_gb_by_isolate.py   
读取GB文件中的isolate信息，并以isolate信息为GB文件命名。主要用于批量处理大量GB文件，适用于群体遗传学分析。    
运行时，需要将该脚本放置在GB文件所在的目录中。       
如果你想遵循特定的genbank指令来命名你的序列文件，你可以在我的脚本中适当地重写正则表达式。          
** 生成文件:** ./output/\<ISOLATE>.gb (多个GENEBANK文件)    
     
### 2.3 gb_to_fasta.py   
将GB文件转换为FASTA文件，并将GB文件名作为FASTA文件中“>”后修饰符的内容。主要用于批量处理大量GB文件。      
运行时，需要将该脚本放置在GB文件所在的目录中。      
** 生成文件:** ./output/\<FASTA_FILE_NAME>.fas (多个FASTA文件)    

### 2.4 Merge_dif_seq.py [FASTA_FILE_1] [FASTA_FILE_2]    
***Supports all versions of python3.***   
FASTA_FILE_1: The preceding sequence.   
FASTA_FILE_2: The following sequence.    
合并序列的低级版本，后续会提供该脚本的进阶版本。      
Merge different sequences of the same sample (recommendation is the result of the comparison).     
Say you have 16S and COI sequences from samples A, B, and C, and for some purpose you want to combine 16S and COI sequences from different samples. You can use this script.
You can call this script repeatedly if you want to merge multiple sequences.    
** 生成文件:** merge.fas (FASTA file)    

### 2.5 S_to_H.py -p [FASTA_FILE_NAME] -l [LIST_NAME]    
***Supports all versions of python3.***     
FASTA_FILE_NAME: Sample sequence.     
LIST_NAME: The column haplotype table.     
转换快速文件的样本序列组成的快速文件单倍型。实现相同序列的合并!      
使用前需要获取两个文件，一个是DnaSP导出的单倍型样本控制表格(可能需要手工制作)。另一个是包含所有物种序列的fasta文件。  
Convert fasta files of sample sequences to fasta files consisting of haplotypes. Realize the merging of identical sequences!    
Two files need to be obtained before use, one is a haplotype sample control form exported by DnaSP (may need to be made by hand). The other is a fasta file containing the sequences of all species.    
** 生成文件:** out_a.fasta (FASTA file)        

### 2.6 ExtractFasta.py [FASTA_FILE] [LIST_FILE] [Regular_expressions (Optional)]      
***Supports all versions of python3.***        
FASTA_FILE: Fasta format sequence file, including all want to extract sequence.            
LIST_FILE: The list includes all the sample numbers you want to extract, which can be all or part of the sample numbers after the ">" in FASTA_FILE.        
Regular_expressions: If not filled in the default is "\_(.*?)". Regular expressions that specify the rule that the number of LIST_FILE is in FASTA_FILE. For example, if the sequence before the first space after ">" is the list number, the regex would be "\_(.*?). "        
根据列表提取总多序列fasta文件中的子集。列表中的ID可以是总文件的ID的子字符串，默认是以>后第一个空格前的序列作为对应。如果不是这样的对应关系，可以配置正则表达式。               
使用场景：共线性分析或者同源基因聚类时从NCBI下载的pep文件中提取需要的序列。    
Extract the fasta sequence in the list.       
***The text before the first space is a number:***      
```python ExtractFasta.py example/text.fa example/list1.txt```      
***Specify the regular expression position as a number:***      
```python ExtractFasta.py example/text.fa example/list2.txt "_(.*?) " ```       
** 生成文件:** out_match_seq.fasta (FASTA file)         

### 2.7 ProteinPropertyFromExpasy.py [FASTA_FILE]      
***Supports all versions of python3.***        
FASTA_FILE: Fasta format sequence file, It needs to be a protein sequence.（提供蛋白质序列的fasta格式可以是多序列的文件）                  
从Expasy (https://web.expasy.org/protparam/)中批量获得蛋白质的理化性质。     
Protein physicochemical properties were obtained from Expasy (https://web.expasy.org/protparam/) in batches.          
```python ProteinPropertyFromExpasy.py example/text.fa ```       
** 生成文件:** expasy_output.csv (TABLE file)         

### 2.8 FeaturesBaseComponents.py [FASTA_FILE] [TABLE]       
***Supports all versions of python3.***        
FASTA_FILE: Fasta format sequence file, Only one complete sequence!                
TABLE: A table containing feature names, groups, and starting positions. The first column is the gene group, the second column is the gene, the third column is the gene start position, and the fourth column is the gene stop position. Genes are nominal concepts, and you can assign groups to any segment.                
表格包含特征名称、组别和起始位置的表。第一列为基因组，第二列为基因，第三列为基因起始位置，第四列为基因终止位置。基因是名义上的概念，你可以给任何片段分配分组。     
特征提取和碱基组成统计。如果你想基于开始和结束位置截断fasta文件，你也可以使用这个脚本!       
注意：如果序列中含有中间终止密码子慎用。    
Feature extraction and base composition statistics. You can also use this script if you want to truncate the fasta file based on the start and end positions!             
```python FeaturesBaseComponents.py example/all.fa example/matrix.txt```         
** 生成文件 1:** ex_seq.fasta (FASTA file)           
** 生成文件 2:** Base_composition.txt (TABLE file, The number of the four bases containing ATCG.)           


## 3. Gadget     
一些通用的文本处理工具。      
Some general text processing tools.    

### 3.1 MergeTable.py       
***Supports all versions of python3.***   
***Only graphical systems are supported.***    
导入多表并根据第一列合并表。    
Import the table and merge the table according to the first column.     

### 3.2 VLookup.py [KEY_FILE] [MAP_FILE] [KEY_LOC] [VALUE_LOC] [SEP]   
***Supports all versions of python3.***   
KEY_FILE: A file with a line listing the contents to retrieve (the so-called key). Fill in the file path here.   
MAP_FILE: A table should have at least two columns: key and value. Fill in the file path here.   
KEY_LOC: The key is located in the column number of MAP_FILE, and fill in the number.   
VALUE_LOC: The value is located in the column number of MAP_FILE, and fill in the number.   
SEP: The file-delimiter symbol for MAP_FILE.The default is a TAB character.     
vlookup函数的Python实现。并且适当更改，使用场景提取一些基因的注释信息从总注释表中。        
Python implementation of the vlookup function. Column numbers start at 1, so the first column number is 1.      
** 生成文件:** map_\<map file name> (TABLE file)     

### 3.3 SumByGroup.py [MAP_FILE] [MATRIX_FILE] [KEY_COL_ID] [VALUE_COL_ID]             
***Supports all versions of python3.***     
**Note: Both map and matrix tables must include header rows!**       
MAP_FILE: A table includes group name columns and individual name columns. Need to include the title line! For example, the group name column is gene family (if the same gene is included in multiple gene families, multiple gene families can be separated by commas); Individuals are genes, and likewise multiple gene families including the same gene can also be separated by commas.      
MATRIX_FILE: Matrix, including a title row and an individual name column (the first column, value in MAP_FILE). For example, in the gene abundance table, the first column is the gene name.         
KEY_COL_ID: Column number of the group name column in MAP_FILE (0 starts counting).           
VALUE_COL_ID: Column number of the individual name column in MAP_FILE (0 starts counting).           
```python SumByGroup.py example/map.txt example/matrix.txt 1 0```          
使用场景：当你有一个map表，比如每个基因对应基因家族表，还有一个矩阵表，比如基因丰度表，你需要计算每个基因家族的丰度。    
**Use cases:** When you have a map table, such as a gene family table for each gene; There is also a matrix table, such as an abundance table, where you need to calculate the abundance of each gene family.        
** 生成文件 1:** out.count (TABLE file, Group sum table)       
** 生成文件 2:** all.count (TABLE file, All sum tables)          

### 3.4 CountByGroup.py [-h] [-a MAPA] [-b MAPB] [-k KEA] [-K KEB] [-v VAA] [-V VAB] [-s SEA] [-S SEB] [--seka SEKA] [--sekb SEKB] [--seva SEVA] [--sevb SEVB] [-n HEADA] [-N HEADB]         
***Supports all versions of python3.***        
给定映射A- b -C的三个层次，找出A中的C个元素并计数。        
**Note: The -a and -b parameters are required, and all other parameters have default values!**
```options:
  -h, --help            show this help message and exit
  -a MAPA, --mapa MAPA  The path of the large group map. 
  -b MAPB, --mapb MAPB  The path of the small group map.
  -k KEA, --kea KEA     The column number of the large group key. default=0 (0 starts counting).
  -K KEB, --keb KEB     The column number of the small group key. default=0 (0 starts counting).
  -v VAA, --vaa VAA     The column number of the large group value. default=1 (0 starts counting).
  -V VAB, --vab VAB     The column number of the small group value. default=1 (0 starts counting).
  -s SEA, --sea SEA     The key-value separator of the large group value. default="\t"
  -S SEB, --seb SEB     The key-value separator of the small group value. default="\t"
  --seka SEKA           The key separator of the large group value. default=","
  --sekb SEKB           The key separator of the small group value. default=","
  --seva SEVA           The value separator of the large group value. default=","
  --sevb SEVB           The value separator of the small group value. default=","
  -n HEADA, --heada HEADA
                        The Number of excluded rows of the large group value. default=0 (0 starts counting).
  -N HEADB, --headb HEADB
                        The Number of excluded rows of the small group value. default=0 (0 starts counting).        
```                  
Given the three levels of map A-B-C, find the C elements in A and count them.         
```python CountByGroup.py -a example/map.txt -b example/map2.txt -n 1 -k 1 -v 0```          
** 生成文件:** count_Map.txt (TABLE file)       

## 4.Plotscript     
绘图代码工具集。     
A collection of drawing codes.     

### 4.1 geneArrangementMap.py [GENE_LIST] [COLOR_CONFIG] [Vertical_spacing]     
***Supports all versions of python3.***   
***Sample files exist.***    
GENE_LIST: List of gene sequences, TAB delimited. Each row represents a linear order of a genome. Different lines represent different genomes.     
COLOR_CONFIG: Color configuration table, TAB delimited. The RGB hexadecimal representation of the colors in the first column and the gene names in the remaining columns.     
Vertical_spacing: Spacing of adjacent row genomes, default 50.    
根据不同的颜色来区分基因的线性排列。     
The linear arrangement of genes is distinguished according to different colors.       
```python geneArrangementMap.py gene.txt color.txt 50```      
** 生成文件:** out.svg (SVG file)    



==============      
**Author: Hao Xue**     
**E-mail: studid@163.com**  
    <a
    id="cy-effective-orcid-url"
    class="underline"
     href="https://orcid.org/0000-0001-9708-3575"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: top">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
      https://orcid.org/0000-0001-9708-3575
    </a>     
