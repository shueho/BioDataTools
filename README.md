# BioDataTools      
这是一套囊括组学分析与生态遗传分析在内的生物信息学通用数据处理脚本，涵盖了多种数据处理工具，以满足不同研究需求。       

## 1. Metagenome            
宏基因组分析数据处理和绘图脚本。         
   
### 1.01 get_sum.py    
**脚本功能：** 用于整合多样本组装评估数据。           
**参数说明：** 无需任何参数配置，只需将该脚本置于Quast软件所生成的组装评估结果目录下，即可自动获取组装评估信息汇总表。  
**生成文件：** sumary.tsv（表格文件，每一列表示一个样本，每一行对应一个组装数据）。      
      
### 1.02 fasta_rename.py [FASTA_FILE_PATH]   
**脚本功能：** 在宏基因组或转录组项目中，当合并多个样品组装结果前，可使用该脚本将每个FASTA文件内的序列名称统一标准化，例如按照1、2、3等连续编号的方式重命名。这样，在进行基因丰度分析和注释之前，能确保合并后FASTA数据中每个序列的标识符唯一，进而便于后续识别差异基因并追溯到原始序列。
**FASTA_FILE_PATH：** 指定需要重新编号其序列名称的FASTA文件的路径。    
**生成文件：** out_\<your fasta file name>（FASTA文件，将输入文件的序列名称重新命名）。    
         
### 1.03 mergeMpa.py     
**脚本功能：** 此脚本能够将多个MPA文件批量转换为物种丰度矩阵格式。           
**参数说明：** 不需要配置参数。可直接放置于由kraken1、kraken2或bracken软件所生成的MPA文件目录下运行。在执行此脚本之前，请确保您已使用kreport2mpa.py脚本来将相应的报告文件成功转换成了MPA格式。这样，脚本就能自动处理同一目录下的所有MPA文件，并将其整合为物种丰度矩阵。       
**生成文件：** mpaMatrix.txt（表格文件，整合后的丰度表，每一列都表示一个样品）。   

### 1.04 splitFromLevel.py [MPA_MERGE_FILE] [SPLIT_LEVEL]       
**脚本功能：** 该脚本旨在从物种丰度定量分析结果中提取各分类层级的物种丰度数据并构建相应的丰度矩阵。         
**MPA_MERGE_FILE：** 由1.03 mergeMpa.py脚本生成的mpaMatrix.txt文件的路径。         
**SPLIT_LEVEL：** 需要输出物种丰度表的分类阶元，可按照界、门、纲、目、科、属、种的首字母标识，分别用"a"（表示所有类别丰度表都输出）、"k"（Kingdom 只输出界水平丰度表）、"p"（Phylum 只输出门水平丰度表）、"c"（Class 只输出纲水平丰度表）、"o"（Order 只输出目水平丰度表）、"f"（Family 只输出科水平丰度表）、"g"（Genus 只输出属水平丰度表）和"s"（Species 输出每一个物种的丰度表）或其对应的大写字母进行选择。输入字母"a"则表示生成包括所有分类级别的丰度表。       
**生成文件：** taxLevel_\<uppercase letter of level>_output.\<mpaMatrix file name>（一个或多个TABLE 文件）。       
     

## 2. Genetics     
用于基因组和比较基因组学研究中的数据处理，涵盖从NCBI批量获取数据，以及批量提取和批量转化数据信息内容的脚本。           
        
### 2.01 Get_gb_by_gi.py
***需要安装requests库***    
**脚本功能：** 通过GI编号批量下载fasta文件。         
**参数说明：** 不需要配置参数。该脚本自动检测并读取文件夹内所有以“_gi.txt”为扩展名的文本文件。这些“_gi.txt”文件内部存储着待抓取的GI编号列表。          
**场景举例：** 比如在需要批量获取大量gb文件的情况下，您只需创建一个或多个名为“xxx_gi.txt”的文本文件，并将所需GI编号粘贴其中。这种设计允许您按照GI编号所存放的列表文件不同，将下载的fasta文件存放在多个独立的文件夹内，这一做法在群体遗传学中针对单倍型分析的情况尤为常见。请注意，通常情况下会批量提取GB（GenBank）文件然后再转换为FASTA格式，这是因为FASTA格式相较于GB格式简化了许多信息。                       
**生成文件：** gb/\<your gi_list_file name>\_\<GI ACCESSION>.gb（多个GENEBANK文件）。        

### 2.02 Name_gb_by_isolate.py     
**脚本功能：** 该脚本能够读取GB文件内的isolate信息，并依据这些信息为对应的GB文件重新命名，尤其适用于群体遗传学分析中对大批量GB文件进行统一管理和组织。      
**参数说明：** 不需要配置参数。运行应将该脚本直接存放于包含GB文件的目录中，本脚本会自动批量读取目录下所有gb文件。        
**脚本改写：** 如果你想遵循特定的genbank指令来命名你的序列文件，你可以在我的脚本中适当地重写正则表达式。          
**生成文件：** output/\<ISOLATE>.gb（多个GENEBANK文件，重新命名的）。    
     
### 2.03 gb_to_fasta.py   
**脚本功能：** 批量地将GB文件转换为FASTA格式，并且在转换过程中，将原GB文件的文件名插入到FASTA格式序列记录的描述行（“>”后面的部分），以便于追踪源文件信息。这对于高效处理大量的GB文件，在进行诸如群体遗传学分析等工作时尤为重要。       
**参数说明：** 不需要配置参数。运行时，需要将该脚本放置在GB文件所在的目录中（推荐在1.02生成的output文件中）。      
**生成文件：** output/\<FASTA_FILE_NAME>.fas (多个FASTA文件)   。 

> 群体遗传学分析快速下载数据流程：比如要从NCBI下载特定物种的cox1基因，可以先创建一个文件夹，分别列出该物种不同个体的cox1基因的GI编号，并将每个物种的编号保存在独立的xxx_gi.txt文件中；接着运行脚本2.01来下载相应的gb文件；再运行脚本2.02，依据isolate标签对下载的gb文件进行重命名；最后执行脚本2.03，从而生成以isolate为名称的最终fasta格式序列文件。这是快速整合其他研究群体遗传学分析结果的流程。                
       
### 2.04 Merge_dif_seq.py [FASTA_FILE_1] [FASTA_FILE_2]    
***过时代码***     
**脚本功能：** 合并序列的低级版本，后续会提供该脚本的进阶版本。      
**FASTA_FILE_1：** 第一个序列。       
**FASTA_FILE_2：** 第二个序列。    
**场景举例：** 假设你有来自样本A、B和C的16S和COI序列，出于某种目的，你想要结合来自不同样本的16S和COI序列。您可以使用这个脚本。      
**多次调用：** 如果要合并多个序列，可以重复调用此脚本。       
**生成文件：** merge.fas（FASTA文件）。    

### 2.05 S_to_H.py -p [FASTA_FILE_NAME] -l [LIST_NAME]      
**脚本功能：** 将fasta文件多个样品序列根据单倍型归类。     
**参数说明：** 使用前需要获取两个文件，一个是DnaSP导出的单倍型和样品对应的表格（可能需要手工制作）。另一个是包含所有物种序列的fasta文件。     
**场景举例：** 比如，对于包含a、b、c、d、e五个样品的序列数据，其中样品a、b、c的序列完全相同，样品d和e的序列也完全一致，意味着我们拥有两个独特的单倍型。借助这段代码，能够将具有相同序列的样品合并归类为各自的单倍型，有利于后续针对不同单倍型序列进行系统发育分析。参考示例文件和示例代码！！！      
**FASTA_FILE_NAME：** 样品序列文件名（example/sample.fas）。    
**LIST_NAME：** 单倍型对应样品的表格（example/hap.list）。    
```python S_to_H.py -p example/sample.fas -l example/hap.list```      
**生成文件：** out_hap.fasta（FASTA文件，由单倍型组成的fasta文件）。          

### 2.06 ExtractFasta.py [FASTA_FILE] [LIST_FILE] [Regular_expressions (Optional)]      
**脚本功能：** 根据给定列表，可以从包含多个序列的总体fasta文件中筛选出子集fasta文件。列表中的ID项可以是总体fasta文件中序列ID的一部分，默认情况下，系统将匹配">"符号后直至第一个空格前的文本作为对应ID。若实际情况下的ID对应关系并非如此简单，则可通过配置自定义正则表达式来进行精确匹配。                            
**场景举例：** 共线性分析或者同源基因聚类时，从NCBI下载的pep文件常包含冗余内容，可以再NCBI下载只由染色体编码的去冗余蛋白质序列集，使用这个脚本可以根据提供的序列名称从总的pep文件中提取想要的部分，亦可以提取相应蛋白质序列的CDS序列，由于蛋白质序列ID和CDS不是一致的，这时或许你需要配置正则表达式来提取相应的序列，当然你也可以用后续的代码2.09来完成这个操作。    
**FASTA_FILE：** Fasta格式的序列文件，也就是包括所有序列的文件，比如全基因组的pep或者CDS序列。           
**LIST_FILE：** 列表中应包含希望提取的序列编号或名称，这部分信息可以是FASTA_FILE中每条序列“>”符号后紧跟的整个描述字段，也可以只是该描述字段中的一部分内容。       
**Regular_expressions：** 假如你的列表中的名称与FASTA文件序列名称有所不同，你可以指定正则表达式对序列进行提取。如果没有填写，默认为："\_(.*?)".，这意味着你将“>”之后第一个空格前的内容作为ID名称。       
***如果你所需要提取的序列名称是第一个空格前的内容，尤其是针对那些直接从NCBI下载的fasta文件，你可以直接运用：***        
```python ExtractFasta.py example/text.fa example/list1.txt```      
***！！！常用！如果你所需要提取的序列名称是>后的所有内容，你可以直接运用：***        
```python ExtractFasta.py example/text2.fa example/list2.txt "\>(.*)"```      
***如果使用正则表达式提取：***      
```python ExtractFasta.py example/text.fa example/list2.txt "\_(.*?) " ```       
**生成文件：** out_match_seq.fasta（FASTA文件）。                  

### 2.07 ProteinPropertyFromExpasy.py [FASTA_FILE]      
**脚本功能：** 从Expasy（https://web.expasy.org/protparam）中批量获得蛋白质的理化性质。     
**FASTA_FILE：** 提供蛋白质序列的fasta格式可以是多序列的文件。      
```python ProteinPropertyFromExpasy.py example/text.fa ```       
**生成文件：** expasy_output.csv（TABLE file）。        

### 2.08 FeaturesBaseComponents.py [FASTA_FILE] [TABLE]       
**脚本功能：** 细胞器基因组专用，特征提取和碱基组成统计。如果你想基于开始和结束位置截断fasta文件，你也可以使用这个脚本!       
**FASTA_FILE：** 只包含一个序列的fasta文件。    
**TABLE：** 表格包含特征名称、组别和起始位置的表。第一列为基因组，第二列为基因，第三列为基因起始位置，第四列为基因终止位置。基因是名义上的概念，你可以给任何片段分配分组。        
**注意事项：** 如果序列中含有中间终止密码子慎用，并且如果不是+链编码的基因会提取到其反向互补序列。    
```python FeaturesBaseComponents.py example/all.fa example/matrix.txt```         
**生成文件 1：** ex_seq.fasta（FASTA文件，提取到的小片段序列）。           
**生成文件 2：** Base_composition.txt (表格ATGC的碱基占比) 。      

### 2.09 ExAndRename.py [MAP_FILE] [FASTA_FILE]      
**脚本功能：** 从fasta文件中提取部分序列，并对这些序列按照规则修改名称。    
**场景举例：** 适用于从全基因组序列中提取染色体并修改名称。     
**MAP_FILE：** 在提供的信息中，第一列所列出的是欲提取或重命名的序列名，它对应fasta文件中“>”符号之后，首个空格之前的文本内容；若无空格，则为“>”符号之后的完整序列标识符。第二列则是期望修改为目标的新名称。当第一列与第二列内容相同时，这一操作相当于执行代码2.06的功能。            
**FASTA_FILE：** Fasta格式的序列文件，也就是包括所有序列的文件，比如全基因组fa文件、pep或者CDS序列。             
```python ExAndRename.py example/map.txt example/text.fa ```       
**生成文件：** subset_fasta.faa（FASTA文件，如果在map表存在多余的内容会有提示）。              


## 3. Gadget     
一些通用的文本处理和分析工具，以及与富集注释分析相关的代码。         

### 3.01 MergeTable.py       
***图形界面的合并表格工具***   
**脚本功能：** 合并多个表格时，可以根据它们的第一列数据进行对应联接操作。       
**参数说明：** 不需要配置参数。将所有需要依据首列进行合并的表格逐一导入，并通过相应功能一键实现按第一列内容的合并操作。     

### 3.02 VLookup.py [KEY_FILE] [MAP_FILE] [KEY_LOC] [VALUE_LOC] [SEP]     
**脚本功能：** vlookup函数的Python实现。可以自定义键值的位置。   
**场景举例：** 从总注释表中提取一些基因的注释信息。注意这个只能提取一列内容。       
**KEY_FILE：** 一个文件，包含需要检索值的列。   
**MAP_FILE：** 在其中检索的表格，需要至少有两个列，其中一个是key，另外一个是值。        
**KEY_LOC：** 键列在MAP_FILE表格中位于的列号，比如第一列是key填写1。   
**VALUE_LOC：** 值列在MAP_FILE表格中位于的列号，比如第一列是value填写1。    
**SEP：** MAP的制表符，比如制表符分隔填写"\t"，注意引号是英文的。      
**生成文件：** map_\<map file name>（TABLE file）。    

### 3.03 SumByGroup.py [MAP_FILE] [MATRIX_FILE] [KEY_COL_ID] [VALUE_COL_ID]             
**务必确保map表和matrix表均包含标题行以便正确识别列信息。另外，在进行相对丰度计算时，应当使用all.count的总计数值作为计算每个序列丰度的分母。**       
**脚本功能：** 分组求和的进阶版。       
**场景举例：** 在处理数据时，假如你拥有一份map表，该表记录了每个基因与其所属基因家族的关系；同时你还有一份matrix表，其中列出了各基因的丰度数据。此时，你需要通过联合这两份表，来计算出每个基因家族总的丰度值，物种丰度表同理。                 
**MAP_FILE：** 在进行数据处理时，所使用的表格需包含分组列以及该组内所有成员列。分组和成员关系可以是一对一、一对多、多对一或多对多的形式。分组及其成员之间用逗号分隔，例如："A,B" 表示 A 组和 B 组都包含相同的成员 "a"；而 "A a,b" 则表示 A 组内包含成员 "a" 和 "b"。        
**MATRIX_FILE：** 丰度表或类似的矩阵，请确保矩阵文件包含标题行，其中第一列的元素必须与MAP_FILE中的成员值（不是分组）相匹配。举例来说，在基因丰度矩阵中，第一列通常是基因名称，这些基因属于不同的基因家族，并且矩阵中还包含了针对各个样品的丰度数据列。       
**KEY_COL_ID：** 在MAP文件中，指定组名所在的列编号，其中0代表第一列，1代表第二列，以此类推，用于指示每一行记录中的组别信息所在位置。      
**VALUE_COL_ID：** 在MAP文件中，指定成员名所在的列编号，其中0代表第一列，1代表第二列，以此类推，用于指示每一行记录中的成员信息所在位置。         
```python SumByGroup.py example/map.txt example/matrix.txt 1 0```          
**生成文件 1：** out.count（TABLE file, 分组求和表）。      
**生成文件 1：** all.count（TABLE file, 总求和表）。          

### 3.04 CountByGroup.py [-h] [-a MAPA] [-b MAPB] [-k KEA] [-K KEB] [-v VAA] [-V VAB] [-s SEA] [-S SEB] [--seka SEKA] [--sekb SEKB] [--seva SEVA] [--sevb SEVB] [-n HEADA] [-N HEADB]         
**脚本功能：** 针对具有三层映射关系A-B-C的数据结构，任务是在A层中寻找关联到C层的所有元素，并统计这些元素的数量。      
**场景举例：** 比如在生物过程中包括三个GO术语，这三个术语之间存在交集基因，你想统计生物过程下一共的基因数目（去重的）。    
**注意事项：** -a和-b参数是必需的，其他参数都有默认值！**   
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
**生成文件：** count_Map.txt（TABLE file）。       

### 3.05 splitFasta.py [FASTA_FILE_PATH] [Number_of_split_files]       
**脚本功能：** 针对含有大量序列的FASTA文件，可根据序列数量对其进行分割，形成多个较小的FASTA文件。      
**场景举例：** 例如，在进行在线KEGG注释时，KEGG服务可能对一次上传的序列数目有所限制，通过预先分割大的FASTA文件，可以确保符合上传要求并顺利完成注释任务。      
**FASTA_FILE_PATH：** 要分割的FASTA文件的路径。     
**Number_of_split_files：** 分割完成后每个文件包含的序列数。       
***运行下列代码将7个序列的fasta文件分为3个2序列的文件（不够整除最后一个文件只有一个序列）。*** 
```python splitFasta.py example/text.fa 2```          
**生成文件：** \<Split file number>_\<your fasta file name>（多个FASTA文件）。   

### 3.06 read_keg.py [KEG_FILE]   
**脚本功能：** 解析KEG文件。可以解析从KEGG网页下载的.keg注释文件，用于富集分析或基因注释。      
**场景举例：** 有两个场景，一种是手动通过在线KEGG平台对序列进行注释以提取信息可以用到这个脚本；另一种则是自主下载所有KO编号对应的通路信息，随后自行进行注释和富集分析。第二个场景最为常用，比如你还可以下载老鼠的通路文件等。                 
**KEG_FILE：** 从KEGG数据库下载的KEG文件比如通用的：ko00001.keg         
> 你可以点击链接下载：https://www.kegg.jp/kegg-bin/download_htext?htext=ko00001&format=htext&filedir=          

**生成文件 1：** output_\<your keg file name> (TABLE file)   
**生成文件 2：** ko_match_KO.txt (TABLE file)     
**生成文件 3：** KO_map.txt (TABLE file)     

### 3.07 KEGG_pathway_geneNum.py [3.06_生成文件_1] [GENE_KO]    
**脚本功能：** KEGG通路基因数量统计，导出用于KEGG注释富集绘图的数据。    
**3.06_ 生成文件_1：** 脚本3.06的生成文件。            
**GENE_KO：** GENE-KO映射表，第一列是基因ID或名称，第二列为ko编号，多个ko编号可以用逗号隔开，可参考示例文件。    
**生成文件 1：** A.txt (all_gene is the total number of genes, and you can use this number to find the gene ratio. TABLE file)   
**生成文件 2：** A-B.txt (TABLE file)   
**生成文件 3：** A-C.txt (TABLE file)   
**生成文件 4：** D.txt (TABLE file)   
**生成文件 5：** err.txt (There is no matching KO number. TABLE file)      

### 3.08 read_goOBO.py [obo_FILE]      
**脚本功能：** 从obo文件读取并解析GO号对应的描述及分类，生成GO编号\t描述信息\t分类的三列表格。      
**obo_FILE：** GO网站上下载的obo文件路径（打开网址：https://purl.obolibrary.org/obo/go/go-basic.obo 将网页另存为txt文件即可）。       
**生成文件：** go_term_list.txt（TABLE文件，第一列是GO号，第二列是描述信息，第三列是分类）。   
  
### 3.09 read_goOBO.py [go_term_list] [GENE_GO_MAP]                 
**脚本功能：** 给gene-go文件加上GO注释的描述和分类内容。通过运行这个命令生成的文件配合R包clusterProfiler完成富集分析的内容。               
**go_term_list：** 推荐是使用3.08脚本生成的go_term_list.txt文件。     
**GENE_GO_MAP：** 第一列是基因名称，第二列是对应的GO号，注意你需要把注释原始数据格式转换为一一对应的格式。       
**注意事项：** 有时自己注释的表格是某一列是geneID，还有一列是很多GO号。你可以通过代码3.10（推荐）或者下面的代码把一个基因对应多个GO号的文件转换为一一对应的格式！如果是go号之间是逗号隔开，把下边的分号改为分号即可，注意需要是英文的！input_file是你输入的文件名，也就是一个gene对应很多GO编号的表格，output_file是指输出的文件名，注意不要和已有文件相同。                  
```awk -F'\t' '{split($2, arr, ";"); for (j in arr) print $1 "\t" arr[j]}' input_file > output_file```      
**因为完整的GOterm表格很大，下面的示例用简化版的表格，实际使用时需要按照3.08生成表格文件。**         
```python getGOinfo.py example/go_term.txt example/gene_go.txt```      
**生成文件：** gene_GO_info.txt（TABLE文件，第一列是geneid，第二列是GOID，第三列是描述信息，第四列是GO三大类的分类）。   

### 3.10 ConvertGene-GO.py [GENE_GOs_MAP]                 
**脚本功能：** 转换注释表格。  
从表格：    
| Gene | GO Terms |            
| GeneA | GO:000001, GO:000002 |      
| GeneB | GO:000006 |      
改写为：     
| Gene | GO Term |            
| --- | --- |      
| GeneA	 | GO:000001 |      
| GeneA	 | GO:000002 |      
| GeneB	 | GO:000006 |      
其中：原始表格不一定是逗号分隔，也可以是分号分隔或者可以包含多余的描述信息，或者是 GO:000001(描述信息), GO:000002(描述信息)  的格式。          
**GENE_GOs_MAP：** 二列表格，第一列是基因名称，第二列是对应的许多GO号，每一行都是一对多的形式。           
```python ConvertGene-GO.py example/seq_gos.txt```      
**生成文件：** g-go.txt（TABLE文件，第一列是geneid，第二列是GOID）。   

### 3.11 GenoSpider     
**脚本功能：** 基因组数据爬虫，详细说明待补充！       


## 4.Plotscript     
绘图代码工具集。     

### 4.01 geneArrangementMap.py [GENE_LIST] [COLOR_CONFIG] [Vertical_spacing]     
**脚本功能：** 根据不同的颜色来区分基因的线性排列，你可以使用其他更专业的工具绘制。     
**GENE_LIST：** List of gene sequences, TAB delimited. Each row represents a linear order of a genome. Different lines represent different genomes.     
**COLOR_CONFIG：** Color configuration table, TAB delimited. The RGB hexadecimal representation of the colors in the first column and the gene names in the remaining columns.     
**Vertical_spacing：** Spacing of adjacent row genomes, default 50.    
```python geneArrangementMap.py example/gene.txt example/color.txt 50```      
** 生成文件:** out.svg （SVG file）。     





==============      
**Author: Hao Xue**     
**E-mail: studid@163.com**   
**引用：没有文献可以引用，如果对您科研工作有帮助的话，偷偷夸我厉害就行。**            
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