# BioDataTools      
一套用于生物信息学分析的通用数据处理脚本。包含组学分析、生态遗传分析等数据处理工具。     

## 1. Metagenome            
宏基因组与转录组分析数据处理和绘图脚本。         
   
### 1.01 get_sum.py    
不需要配置参数。将脚本放置在quast软件完成的装配评估结果的上机目录中，获得组装评估信息汇总表。        
** 生成文件:** sumary.tsv (表格文件，每一列表示一个样本，每一行对应一个组装数据)        
      
### 1.02 fasta_rename.py [FASTA_FILE_PATH]   
修改指定FASTA文件的每个序列中的名称，使其标准化和统一，即将序列名称按照1、2...的规则编码，用于宏基因组或者转录组合并多个样品组装结果之后，基因丰度、注释之前，可以保证合并后的fasta数据每个序列的ID是唯一的，并且可以方便后续找到差异基因后回溯序列。         
FASTA_FILE_PATH: 需要重新编号序列的FASTA文件的路径      
** 生成文件:** out_\<your fasta file name> (FASTA文件，每个序列被重新命名)   
     
### 1.03 mergeMpa.py   
这个脚本可以将许多mpa文件转换成物种丰度矩阵。不需要配置参数。将脚本放在kracken1/2或bracken软件生成的mpa文件所在的文件夹中。在此之前您可能需要运行kreport2mpa.py脚本将报告文件转换为mpa文件 。            
** 生成文件:** mpaMatrix.txt (TABLE file)   

### 1.04 splitFromLevel.py [MPA_MERGE_FILE] [SPLIT_LEVEL]     
用于从物种丰度定量结果中提取各个分类的物种丰度矩阵。     
MPA_MERGE_FILE: 由1.3 mergeMpa.py脚本生成的mpaMatrix.txt文件的路径。       
SPLIT_LEVEL: 物种丰度表的分类，以界、门、纲、目、科、属和种的首字母进行选择。Level可以从“a”、“k”、“p”、“c”、“o”、“f”、“g”、“s”或它的大写字母选择。输入“a”表示生成了所有的分类分割表。    
** 生成文件:** taxLevel_\<uppercase letter of level>_output.\<mpaMatrix file name> (一个或多个TABLE 文件)   
     

## 2. Genetics     
基因组/比较基因组分析的数据处理，包括从NCBI下载数据的转换和部分信息的批量获取或批量数据转换。       
        
### 2.01 Get_gb_by_gi.py
***需要安装requests库***    
通过GI编号批量下载fasta文件。    
不需要配置参数，读取脚本自动读取文件夹下以“_gi.txt”结尾的所有文本文件，每个“_gi.txt”文件包含需要抓取的GI编号。      
比如你想获取一些fasta文件，你只需要新建一个xxx_gi.txt的文件，把GI编号粘贴进去即可，之所以如此设置，是为了让你下载的fasta文件分别存放在不同的文件夹中，这在群体遗传学单倍型分析中比较常用。     
** 生成文件:** ./gb/\<your gi_list_file name>\_\<GI ACCESSION>.gb (多个GENEBANK文件)    

### 2.02 Name_gb_by_isolate.py   
读取GB文件中的isolate信息，并以isolate信息为GB文件命名。主要用于批量处理大量GB文件，适用于群体遗传学分析。    
运行时，需要将该脚本放置在GB文件所在的目录中。       
如果你想遵循特定的genbank指令来命名你的序列文件，你可以在我的脚本中适当地重写正则表达式。          
** 生成文件:** ./output/\<ISOLATE>.gb (多个GENEBANK文件)    
     
### 2.03 gb_to_fasta.py   
将GB文件转换为FASTA文件，并将GB文件名作为FASTA文件中“>”后修饰符的内容。主要用于批量处理大量GB文件。      
运行时，需要将该脚本放置在GB文件所在的目录中。      
** 生成文件:** ./output/\<FASTA_FILE_NAME>.fas (多个FASTA文件)    

### 2.04 Merge_dif_seq.py [FASTA_FILE_1] [FASTA_FILE_2]    
***过时代码***   
FASTA_FILE_1: 第一个序列       
FASTA_FILE_2: 第二个序列    
合并序列的低级版本，后续会提供该脚本的进阶版本。      
假设你有来自样本A、B和C的16S和COI序列，出于某种目的，你想要结合来自不同样本的16S和COI序列。您可以使用这个脚本。      
如果要合并多个序列，可以重复调用此脚本。       
** 生成文件:** merge.fas (FASTA文件)    

### 2.05 S_to_H.py -p [FASTA_FILE_NAME] -l [LIST_NAME]      
转换快速文件的样本序列组成的快速文件单倍型。实现相同序列的合并!      
使用前需要获取两个文件，一个是DnaSP导出的单倍型样本控制表格(可能需要手工制作)。另一个是包含所有物种序列的fasta文件。  
FASTA_FILE_NAME: 序列文件名    
LIST_NAME: The column haplotype table.     
** 生成文件:** out_a.fasta (FASTA文件)        

### 2.06 ExtractFasta.py [FASTA_FILE] [LIST_FILE] [Regular_expressions (Optional)]      
根据列表提取总多序列fasta文件中的子集。列表中的ID可以是总文件的ID的子字符串，默认是以>后第一个空格前的序列作为对应。如果不是这样的对应关系，可以配置正则表达式。               
使用场景：共线性分析或者同源基因聚类时从NCBI下载的pep文件中提取需要的序列。    
FASTA_FILE: Fasta格式的序列文件，也就是包括所有序列的文件。           
LIST_FILE: 列表中需要包含要提取的序列编号或名称，可以是FASTA_FILE中“>”之后的所有内容，也可以是其中的一部分。     
Regular_expressions: 加入你的列表中的名称与FASTA文件序列名称有所不同，你可以指定正则表达式对序列进行提取。如果没有填写，默认为："\_(.*?)".，这意味着你将“>”之后第一个空格前的内容作为ID名称。       
***如果你想要提取的序列名称和fasta格式的一致，或者是从NCBI直接下载的文件你可以直接调用：***      
```python ExtractFasta.py example/text.fa example/list1.txt```      
***使用正则表达式提取：***      
```python ExtractFasta.py example/text.fa example/list2.txt "\_(.*?) " ```       
** 生成文件:** out_match_seq.fasta (FASTA文件)         

### 2.07 ProteinPropertyFromExpasy.py [FASTA_FILE]      
从Expasy（https://web.expasy.org/protparam）中批量获得蛋白质的理化性质。     
FASTA_FILE：提供蛋白质序列的fasta格式可以是多序列的文件      
```python ProteinPropertyFromExpasy.py example/text.fa ```       
** 生成文件:** expasy_output.csv (TABLE file)         

### 2.08 FeaturesBaseComponents.py [FASTA_FILE] [TABLE]       
细胞器基因组专用，特征提取和碱基组成统计。如果你想基于开始和结束位置截断fasta文件，你也可以使用这个脚本!       
FASTA_FILE：只包含一个序列的fasta文件    
TABLE：表格包含特征名称、组别和起始位置的表。第一列为基因组，第二列为基因，第三列为基因起始位置，第四列为基因终止位置。基因是名义上的概念，你可以给任何片段分配分组。        
注意：如果序列中含有中间终止密码子慎用，并且如果不是+链编码的基因会提取到其反向互补序列。    
```python FeaturesBaseComponents.py example/all.fa example/matrix.txt```         
** 生成文件 1：** ex_seq.fasta (FASTA文件，提取到的小片段序列)           
** 生成文件 2：** Base_composition.txt (表格ATGC的碱基占比)           


## 3. Gadget     
一些通用的文本处理、分析工具，包括富集分析相关代码。      

### 3.01 MergeTable.py       
***图形界面的合并表格工具***   
导入多表并根据第一列合并表。    
将所有需要按照第一列合并的表格导入，点击合并即可。      

### 3.02 VLookup.py [KEY_FILE] [MAP_FILE] [KEY_LOC] [VALUE_LOC] [SEP]     
vlookup函数的Python实现。并且适当更改，使用场景从总注释表中提取一些基因的注释信息。        
注意这个只能提取一列内容。      
KEY_FILE：一个文件，包含需要检索值的列。   
MAP_FILE：在其中检索的表格，需要至少有两个列，其中一个是key，另外一个是值。        
KEY_LOC：键列在MAP_FILE表格中位于的列号，比如第一列是key填写1。   
VALUE_LOC：值列在MAP_FILE表格中位于的列号，比如第一列是value填写1。    
SEP：MAP的制表符，比如制表符分隔填写"\t"，注意引号是英文的。      
** 生成文件:** map_\<map file name> (TABLE file)     

### 3.03 SumByGroup.py [MAP_FILE] [MATRIX_FILE] [KEY_COL_ID] [VALUE_COL_ID]             
**注意map表和matrix表需要包含标题行！注意相对丰度计算需要用all.count的总数作为分母**       
分组求和的进阶版。使用场景：当你有一个map表，比如每个基因对应基因家族表，还有一个矩阵表，比如基因丰度表，你需要计算每个基因家族的丰度。               
MAP_FILE: 需要包含分组列和组内所有的成员列。可以是组-成员一一对应的样式，也可以多对多，一对多和多对一，无论是组和成员都可以用逗号隔开比如：A,B a表示AB组都包含a；A a,b表示A组包含a和b。           
MATRIX_FILE：矩阵，包括标题行，第一列必须是MAP_FILE中的成员值。例如，在基因丰度表中，第一列是基因名称包含于多个基因家族中，同时还包含每个样品的数据列。       
KEY_COL_ID：组名在MAP文件中的列号，0表示第一列，1表示第二列。          
VALUE_COL_ID：成员名在MAP文件中的列号，0表示第一列，1表示第二列。          
```python SumByGroup.py example/map.txt example/matrix.txt 1 0```          
** 生成文件 1:** out.count (TABLE file, 分组求和表)       
** 生成文件 2:** all.count (TABLE file, 总求和表)          

### 3.04 CountByGroup.py [-h] [-a MAPA] [-b MAPB] [-k KEA] [-K KEB] [-v VAA] [-V VAB] [-s SEA] [-S SEB] [--seka SEKA] [--sekb SEKB] [--seva SEVA] [--sevb SEVB] [-n HEADA] [-N HEADB]         
给定映射A- b -C的三个层次，找出A中的C个元素并计数。        
**Note: -a和-b参数是必需的，其他参数都有默认值!**   
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

### 3.05 splitFasta.py [FASTA_FILE_PATH] [Number_of_split_files]     
根据序列数将FASTA文件分割成更小的FASTA文件，比如在线KEGG注释可能会对上传的序列数有限制。  
FASTA_FILE_PATH：要分割的FASTA文件的路径。     
Number_of_split_files每个文件包含的序列数。       
运行下列代码将7个序列的fasta文件分为3个2序列的文件（不够整除最后一个文件只有一个序列）。 
```python splitFasta.py example/text.fa 2```          
** 生成文件:** \<Split file number>_\<your fasta file name> (FASTA files)   

### 3.06 read_keg.py [KEG_FILE]   
解析KEG文件。可以解析从KEGG网页下载的.keg注释文件，用于富集分析或基因注释。      
KEG_FILE：从KEGG数据库下载的KEG文件比如通用的：ko00001.keg         
你可以点击链接下载：https://www.kegg.jp/kegg-bin/download_htext?htext=ko00001&format=htext&filedir=       
** 生成文件 1:** output_\<your keg file name> (TABLE file)   
** 生成文件 2:** ko_match_KO.txt (TABLE file)     
** 生成文件 3:** KO_map.txt (TABLE file)     

### 3.07 KEGG_pathway_geneNum.py [1.6_ 生成文件_1] [GENE_KO]    
KEGG通路基因数量统计，导出用于KEGG注释富集绘图的数据。    
1.6_ 生成文件_1：脚本1.6的生成文件        
GENE_KO：GENE-KO映射表，第一列是基因ID或名称，第二列为ko编号，多个ko编号可以用逗号隔开，可参考示例文件。    
生成文件包括各种等级的计数。    
** 生成文件 1:** A.txt (all_gene is the total number of genes, and you can use this number to find the gene ratio. TABLE file)   
** 生成文件 2:** A-B.txt (TABLE file)   
** 生成文件 3:** A-C.txt (TABLE file)   
** 生成文件 4:** D.txt (TABLE file)   
** 生成文件 5:** err.txt (There is no matching KO number. TABLE file)      

### 3.08 read_goOBO.py [obo_FILE]      
从obo文件读取并解析GO号对应的描述及分类，生成GO编号\t描述信息\t分类的三列表格。      
obo_FILE：网站上下载的obo文件路径（打开网址：https://purl.obolibrary.org/obo/go/go-basic.obo 将网页另存为txt文件即可）。       
** 生成文件 1:** output_\<your keg file name> (TABLE file)      

### 3.09 GenoSpider     
基因组数据爬虫，详细说明待补充！       


## 4.Plotscript     
绘图代码工具集。     

### 4.1 geneArrangementMap.py [GENE_LIST] [COLOR_CONFIG] [Vertical_spacing]     
根据不同的颜色来区分基因的线性排列，你可以使用其他更专业的工具绘制。     
GENE_LIST: List of gene sequences, TAB delimited. Each row represents a linear order of a genome. Different lines represent different genomes.     
COLOR_CONFIG: Color configuration table, TAB delimited. The RGB hexadecimal representation of the colors in the first column and the gene names in the remaining columns.     
Vertical_spacing: Spacing of adjacent row genomes, default 50.    
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
