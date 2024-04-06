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
**脚本功能：** 合并序列的低级版本，后续会提供该脚本的进阶版本（脚本2.14）。      
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
**脚本功能：** 从Expasy（ https://web.expasy.org/protparam ）中批量获得蛋白质的理化性质。     
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
       
### 2.10 BatchFastaToPam.py [FASTA_FILE_DIR]         
**脚本功能：** 批量将比对过的fasta文件转换为paml比对文件。     
**FASTA_FILE_DIR：** 文件夹路径名，在该目录下包含需要转换的fasta格式的比对文件。            
**注意事项：** 文件夹中不能包含未比对的序列文件，也不能有其他文件，否则将会报错！                       
```python BatchFastaToPam.py example/ali_fasta```          
**生成文件：** pamlfile (文件夹，其中包含需要转换的fasta文件名+pam后缀) 。      

### 2.11 ReassignSequence.py [IN_FASTA_FILE_DIR] [MATRIX_FILE] [OUT_FASTA_FILE_DIR]        
**脚本功能：** 将fasta文件中的序列按照要求分配到不同的fasta文件中。       
**使用场景：** ①单拷贝同源基因每个基因家族的序列提取过程中，将下载的CDS序列按照基因家族分组将CDS分别归属到新的不同的文件中，用于后续CDS和蛋白质序列的匹配，矩阵文件是Orthogroups/Orthogroups.tsv（MATRIX_FILE，可以参照示例文件example/seq_matrix2.txt），你只需要从NCBI下载每个物种的fna文件（重要：需要使用cut命令分列并保留第一列，使得每个序列的名称只包含ID号！）放置在同一文件夹中（IN_FASTA_FILE_DIR），然后指定输出文件就可以将不同物种的CDS文件分配到已基因家族名称命名的fasta文件中；②提取同一基因家族的基因进行合并分析。       
**IN_FASTA_FILE_DIR：** 文件夹路径名，在该目录下包含需要重新分配的fasta格式序列文件，可以是DNA、CDS、转录本、蛋白质或其他序列。            
**MATRIX_FILE：** 矩阵文件位置，制表符隔开，包含标题行！每一行的第一个项目是新分配后的文件名，其余位置是该文件中包含的序列名称。      
**OUT_FASTA_FILE_DIR：** 文件夹路径名，输出路径。             
**注意事项：** 索引表格一定要包含标题行，可以是标准的同行数同列数的矩阵，但不强制要求。                       
```python ReassignSequence.py example/ali_fasta example/seq_matrix.txt out```          
**生成文件：** \<OUT_FASTA_FILE_DIR\> (文件夹，其中包含重新分配后的序列)       

### 2.12 BatchAlignedProteinToDNA.py [-h] [-c CODON] [-m MAPFILE] [-p PEP] [-C CDS] [-s SUFFIX_P] [-S SUFFIX_C]          
**脚本功能：** 假如你有蛋白质的比对文件，想要得到对应CDS的密码子比对文件可以使用此脚本，简单来说是批量将比对过的蛋白质序列转换为DNA序列，通过本脚本可以过滤掉：①CDS系列长度不为3的倍数的序列；②CDS-蛋白序列不匹配的序列；③含有未知碱基N的序列。      
**场景举例：** 通过OrthoFinder软件对多个物种的同源基因家族进行搜索期间会在WorkingDirectory/Alignments_ids目录生成单拷贝正交基因蛋白序列的比对文件，从其中提取单拷贝正交基因家族（单拷贝基因家族列表在Orthogroups/Orthogroups_SingleCopyOrthologues.txt，可以使用for循环提取）存放到文件夹中（PEP参数），从NCBI等数据库下载CDS序列（CDS序列编号和蛋白序列编号是相同的），使用脚本2.11提取蛋白序列对应的CDS序列（未比对）存放到文件夹中（CDS参数），OrthoFinder结果文件中WorkingDirectory下的SequenceIDs.txt即为蛋白质名称-CDS名称对照表（MAPFILE参数）。      
```options:
  -h, --help            显示帮助信息
  -c CODON, --codon 密码子表文件，第一列为氨基酸单字母缩写，第二列是对应的密码子，示例文件中cod.txt为标准密码子表。
  -m MAPFILE, --mapfile 索引表文件，蛋白质序列名称及其对应的CDS序列名称表。第一列是蛋白质名称，第二列是对应CDS名称。
  -p PEP, --pep 包含所有蛋白质序列的目录，蛋白质系列需要是被比对过的。
  -C CDS, --cds 包含所有CDS序列的目录，推荐使用脚本2.11生成的。
  -s SUFFIX_P, --suffix_p 蛋白质序列的扩展名，即蛋白质序列文件最后的.后的内容，默认是fa。
  -S SUFFIX_C, --suffix_c CDS序列的扩展名，即CDS序列文件最后的.后的内容，默认是fna。
```         
**注意事项：** 由软件自动生成的SequenceIDs.txt需要手动按照冒号和空格分列，删除多余的部分，详细可以查看示例文件            
```python BatchAlignedProteinToDNA.py -c example/cod.txt -m example/SequenceIDs.txt -p example/pep -C example/cds -s "fa" -S "fna"```          
**生成文件 1：** output（文件夹，用于存放比对过的CDS序列，运行上述命令生成的文件参考example/output）。      
**生成文件 2：** err_cds.txt（错误日志文件，显示过滤掉的序列，如果没有错误的序列将不生成）。      
  
### 2.13 Extract4DTv.py [-h] [-c CODON] [-m MAPFILE] [-p PEP] [-C CDS] [-s SUFFIX_P] [-S SUFFIX_C]          
**脚本功能：** 批量提取蛋白质序列比对结果中的4DTv（四倍简并位点）。      
**场景举例：** 同源基因建树。      
**注意事项：** 所有参数均与脚本2.12一致，代码内容其实差不多，只是生成的文件名称不同。            
```python Extract4DTv.py -c example/cod.txt -m example/SequenceIDs.txt -p example/pep -C example/cds -s "fa" -S "fna"```          
**生成文件 1：** 4dtv（文件夹，用于存放提取到的4DTv位点，运行上述命令生成的文件参考example/4dtv）。      
**生成文件 2：** err_4dtv.txt（错误日志文件，显示过滤掉的序列，如果没有错误的序列将不生成）。      
  
### 2.14 MergeSequences.py [MATRIX_FILE] [FASTA_FILE_DIR] [SUFFIX] [ORDER_LIST（可选参数）]      
**脚本功能：** 进阶版合并序列脚本。     
**MATRIX_FILE：** 矩阵文件位置，制表符隔开，包含标题行！每一列是一个样品，每一行的第一个项目是对应的序列名称（fasta文件名,不包含后缀），行和列可以确定每个样品对应序列的序列名称。            
**FASTA_FILE_DIR：** 文件夹路径名，在该目录下包含需要合并的fasta格式的比对文件，文件名没有要求，只要包含MATRIX_FILE中所有序列名即可。            
**ORDER_LIST：** 指定连接顺序，通过指定连接顺序既可以排除某个序列，也可以指定连接顺序，如果不指定则默认按照序列名称的哈希值为序全部连接。            
**注意事项：** 文件夹中不能包含未比对的序列文件，可能会发生连接错误！         
***运行下列代码将不指定顺序全连接。***               
```python MergeSequences.py example/seq_matrix2.txt example/4dtv```          
***若指定连接顺序运行下列代码。***              
```python MergeSequences.py example/seq_matrix2.txt example/4dtv example/order.txt```          
**生成文件 1：** <FASTA_FILE_DIR的名称>.fasta （FASTA文件，每个序列名称为第一行的样品名称）。      
**生成文件 2：** order.true （实际合并顺序）。      

### 2.15 BatchGenerationCodeML_CTL.py [PAML_FILE_DIR] [TREE_FILE]         
**脚本功能：** 批量生成CodeML的配置文件。           
**PAML_FILE_DIR：** PAML格式的比对文件所在目录，在运行本脚本时要求目录中必须含有需要进行选择压力分析的比对文件，并且尽量不使用相对路径，否则将无法读取需要比对文件路径。            
**TREE_FILE：** 树文件路径（相对于CodeML运行时的路径），不要求在本脚本运行时该文件存在，但是务必要保证在运行CodeML程序时程序可以读取到该路径。          
**注意事项：** 本脚本只是生成配置文件，请务必注意脚本导入树文件路径并不是CodeML程序运行时树文件路径！配置文件模板选择的是Branch model模型，如果有其他需求可以直接修改配置文件。                           
```python BatchGenerationCodeML_CTL.py example/paml_file "./out/a.tree"```          
**生成文件 1：** codemlnull (文件夹，基于无效假设的配置文件） 。            
**生成文件 1：** codeml2 (文件夹，基于替代假设的配置文件） 。            

### 2.16 ParsingCodeMLResults.py [MOD0_DIR] [MOD2_DIR]         
**脚本功能：** 批量解析CodeML结果，如果以2.15生成的脚本，结果会生成在m0和m2文件夹中。           
**MOD0_DIR：** 基于无效假设生成的结果。            
**MOD2_DIR：** 基于替代假设生成的结果。            
```python ParsingCodeMLResults.py example/codeml/m0 example/codeml/m2```          
**生成文件：** result.txt (表格，可能需要手动整理） 。            

> 在比较基因组学分析中对同源基因进行扫描后需要进行4DTv或建树分析，提取4DTv位点的过程可以使用2.11、2.13和2.14脚本。除此之外还会使用PAML软件包的CodeML程序对筛选出的单拷贝基因进行选择压力分析，首先需要使用2.10将2.12得到的文件进行格式转化，然后需要配置ctl文件，比较繁琐可以使用脚本2.15批量生成配置文件，然后使用循环批量运行程序，程序运行完成后使用脚本2.16解析结果，将m0和m2的结果对应起来，得到lnL0、lnL2，（lnL2-lnL0）×2的绝对值服从自由度np2-np0自由度的卡方分布，使用excel的CHISQ.DIST.RT函数可以得到显著性。         

### 2.17 SplitAXT.py [AXT_FILE]     
**脚本功能：** 将单个AXT格式文件拆分为多个AXT文件，使得每个文件中只包含一对序列比对。   
**场景举例：** 脚本2.12生成的密码子比对文件后，如果需要进一步进行4dtv分析，需要使用摘抄代码convert_fasta_to_axt.pl（做了适应性修改）将其转换为AXT文件，本脚本可以把上述代码生成的AXT文件按照序列对进行拆分。           
**AXT_FILE：** 需要拆分的AXT文件。            
**注意事项：** 本脚本只支持序列对名称中含有数字的AXT文件。                           
```python SplitAXT.py example/test.axt```          
***有时你也许需要批处理。***               
```for i in `ls *axt`;do python SplitAXT.py $i ;done```          
**生成文件：** \<序列对\>.axt-split (多个axt文件） 。          

> 你可以参考 https://yanzhongsino.github.io/2022/09/07/bioinfo_Ks_batch.calculation.Ks 来计算 Ka、Ks和4dtv值，由于calculate_4DTV_correction.pl脚本只支持一对序列的4dtv计算，因此可以使用脚本2.17对AXT文件进行拆分。                 

### 2.18 BaseSiteInformation.py [GFF_FILE] [Q_FILE]         
**脚本功能：** 根据指定染色体位置及碱基位点信息，抽取相应的基因数据，比如位点在哪一个转录本上的哪一个CDS区间中，以及CDS或转录本的位置信息，方便后续注释分析。           
**场景举例：** 通过随机森林等算法找到不同种群或不同品种的变异位点，需要定位到该位点所在基因。          
**GFF_FILE：** 基因组GFF文件，只需要保留mRNA和CDS特征，并且每个mRNA需要位于其包含CDS特征的上方，可以选择在运行代码前手动将GFF文件排序！                 
**Q_FILE：** 查找的条目表格，需要包括标题行，至少包含两列：第一列必须是染色体编号，第二列是对应于染色体上的位置。            
```python BaseSiteInformation.py example/genome.gene.gff example/base_loc.txt```          
**生成文件：** out_<Q_FILE>.xls (表格，第一、四列为基因名称，第二列是是否为CDS区域CDS/noCDS，第三列为CDS的起始终止位置以及ORF起始位点，第五列是染色体ID，然后是基因起始位置、得分以及基因CDS数目） 。            

### 2.19 MaskSeq.py [FASTA_FILE] [TABLE_FILE] [TARG 可选参数]       
***待优化！***       
**脚本功能：** 对Fasta文件中的某些区间进行屏蔽（替换为TARG）。           
**场景举例：** 基因组分析中对基因组的一些序列（比如重复序列）进行屏蔽（ mask）以节约分析过程的算力。          
**FASTA_FILE：** Fasta文件，里边包含许多序列，对于基因组来说其中包括许多染色体序列，>后边的内容为序列名称。                        
**TABLE_FILE：** 三列表格，不需要包括标题行，第一列是序列名称（注意和fasta文件名称完全一致），第二、三列分别是屏蔽起始和终止位置（从1开始计数，可以从gff文件中直接复制）。            
**TARG：** 默认是将指定位置的碱基替换为N，你也可以指定替换的字符。         
***默认替换为N。***                          
```python MaskSeq.py example/Chr.fa example/masktbl.txt```          
***默认替换为?。***                          
```python MaskSeq.py example/Chr.fa example/masktbl.txt "?"```          
**生成文件：** maskseq_\<FASTA_FILE> (屏蔽部分序列的FASTA文件） 。   
  
  
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
**注意事项：** -a和-b参数是必需的，其他参数都有默认值！    
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
**脚本功能：** 解析KEG文件。可以解析从KEGG网页下载的.keg注释文件，用于富集分析或基因注释时手动构建背景基因集。      
**场景举例：** 通过本脚本你可以得到KEGG数据库每个ko或者每个物种的通路ID的简易化表格，①用于在KEGG在线注释网站得到的KEGG注释的解析；②用于解析KEGG通路数据库中模式生物或通用注释表的解析。                 
**KEG_FILE：** 从KEGG数据库下载的KEG文件比如通用的：ko00001.keg或者人类KEG文件：hsa00001.keg。                
> 你可以点击链接下载通用KEG文件：https://www.kegg.jp/kegg-bin/download_htext?htext=ko00001&format=htext&filedir=          
将上述网址中的htext=ko00001中的ko替换为物种缩写可以下载特定物种的KEG文件，比如替换为hsa https://www.kegg.jp/kegg-bin/download_htext?htext=hsa00001&format=htext&filedir= 即是人类的KEG文件。         
物种缩写你可以参照：  https://www.genome.jp/kegg/catalog/org_list.html   比如老鼠的缩写是mmu。

**注意事项：** 在示例文件中有从KEGG网址下载的人类和通用keg文件，为保证数据库的最新建议手动下载。      
**比如解析通用keg文件：**        
```python read_keg.py example/ko00001.keg```          
**比如解析人类keg文件：**        
```python read_keg.py example/hsa00001.keg```          
**生成文件 1：** output_\<你的keg文件名> (TABLE file)       
**生成文件 2：** \<你的keg前缀（物种缩写）\>_map.txt （表格文件，如果需要进行KEGG富集分析，你可以使用excel的Vlookup函数对完成背景基因文件）    

### 3.07 KEGG_pathway_geneNum.py [3.06_生成文件_1] [GENE_KO]    
**脚本功能：** KEGG通路基因数量统计，导出用于KEGG注释富集绘图的数据。    
**3.06_ 生成文件_1：** 脚本3.06的生成文件。            
**GENE_KO：** GENE-KO映射表，第一列是基因ID或名称，第二列为ko编号（或其他通路编号），多个ko编号可以用逗号隔开，可参考示例文件。    
```python KEGG_pathway_geneNum.py example/output_ko00001.txt example/gene_ko.txt```         
**生成文件 1：** A.txt (all_gene is the total number of genes, and you can use this number to find the gene ratio. TABLE file)   
**生成文件 2：** A-B.txt (TABLE file)   
**生成文件 3：** A-C.txt (TABLE file)   
**生成文件 5：** err.txt (There is no matching KO number. TABLE file)      

### 3.08 read_goOBO.py [obo_FILE]      
**脚本功能：** 从obo文件读取并解析GO号对应的描述及分类，生成GO编号\t描述信息\t分类的三列表格，你可以直接使用示例文件中的go_term_list.txt，要注意这个文件可能不是最新的版本，因此推荐使用该脚本提取最新的GO注释信息。           
**obo_FILE：** GO网站上下载的obo文件路径（打开网址：https://purl.obolibrary.org/obo/go/go-basic.obo 推荐打开网页后，右键，点击另存为，保存为文本文件） 。       
**注意事项：** 由于网页加载可能不全因此不推荐将网页CTRL+A全选CTRL+C复制，新建txt文件并打开CTRL+V粘贴。      
**比如你将网页复制或保存到了abc.txt，你可以运行下方代码：**        
```python read_goOBO.py abc.txt```   
**生成文件：** \<版本号\>_go_term_list.txt（TABLE文件，第一列是GO号，第二列是描述信息，第三列是分类）。   
          
### 3.09 ConvertGene-GO.py [GENE_GOs_MAP]                 
**脚本功能：** 转换GO注释表格：  
将表格：    
| Gene | GO Terms |          
| --- | --- |      
| GeneA | GO:000001, GO:000002 |      
| GeneB | GO:000006 |      

转换为：     
| Gene | GO Term |            
| --- | --- |      
| GeneA	 | GO:000001 |      
| GeneA	 | GO:000002 |      
| GeneB	 | GO:000006 |    
  
其中：原始表格不一定是逗号分隔，也可以是分号分隔或者可以包含多余的描述信息，比如： GO:000001(描述信息), GO:000002(描述信息)  的格式。          
**GENE_GOs_MAP：** 二列表格，第一列是基因名称，第二列是对应的许多GO号，每一行都是一对多的形式。     
```python ConvertGene-GO.py example/seq_gos.txt```       
**生成文件：** g-go.txt（TABLE文件，第一列是geneid，第二列是GOID）。     
      
### 3.10 getGOinfo.py [go_term_list] [GENE_GO_MAP]                 
**脚本功能：** 给gene-go文件加上GO注释的描述和分类内容。通过运行这个命令生成的文件配合R包clusterProfiler完成富集分析的内容。               
**go_term_list：** 推荐是使用3.08脚本生成的go_term_list.txt文件，包含所有GO术语的描述信息。     
**GENE_GO_MAP：** 推荐是3.09生成的文件，第一列是基因名称，第二列是对应的GO号。       
**注意事项：** 有时自己注释的表格是某一列是geneID，还有一列是很多GO号。你可以通过代码3.09（推荐）或者下面的代码把一个基因对应多个GO号的文件转换为一一对应的格式！如果是go号之间是逗号隔开，把下边的分号改为分号即可，注意需要是英文的！input_file是你输入的文件名，也就是一个gene对应很多GO编号的表格，output_file是指输出的文件名，注意不要和已有文件相同。                  
```awk -F'\t' '{split($2, arr, ";"); for (j in arr) print $1 "\t" arr[j]}' input_file > output_file```      
**使用时需要按照3.08生成表格文件xxx-go_term_list.txt，示例中的2024-01-17_go_term_list.txt是版本2024-01-17。建议通过3.08代码获取最新的版本。**             
```python getGOinfo.py example/2024-01-17_go_term_list.txt example/gene_go.txt```      
**生成文件：** gene_GO_info.txt（TABLE文件，第一列是geneid，第二列是GOID，第三列是描述信息，第四列是GO三大类的分类）。   

> **无参GO富集分析流程：** 当你已经得到所有基因/蛋白质的GO注释结果，①如果原始注释表格是gene-GOs一对多的格式，使用3.09转换为gene-GO一对一的格式；②使用3.08下载并解析所有GO术语描述信息表；③使用3.10为每个gene添加GO注释信息；④使用R包clusterProfiler 计算受关注基因（比如差异基因/正选择基因/扩张基因等）的GO术语富集到背景基因（所有注释基因/蛋白质）GO术语的结果。比较常见的富集结果（气泡图的横坐标）有基因比例（gene Ratio）、富集得分（enrichment score，又称fold enrichment富集倍率）和富集因子（rich factor），比如clusterProfiler计算得到的GeneRatio是20/100（表示100个关注基因富集到某术语20个gene），BgRatio是50/150（表示所有的150个基因富集到某术语50个gene）那么，基因比例即为20/100=0.20，富集得分为两个比例的比值即为(20/100)/(50/150)=0.6，富集因子是两个分子的比值即为20/50=0.4。注意如小鼠、人等模式生物，由于自己注释出的背景基因很可能不全面，因此推荐使用专门的富集网站或者富集工具包完成。    
**无参KEGG富集分析流程与GO富集类似。**            

> 富集分析R代码参考的是知乎文章  https://zhuanlan.zhihu.com/p/561522453 中的无参GO富集分析部分，并对部分内容进行修改，使之同时适合KEGG和GO无参富集分析。    

> **文件1 背景基因注释分组文件 gene_ID.txt**    
第一列是gene或蛋白质的名称（可以不唯一）；第二列是GO号或ko号；第三列是描述信息，对于GO富集分析是GO术语的详细解释（level2），对于KEGG分析是levelC的描述信息；第四列是分组信息，对于GO是指GO的三大类，对于KEGG可以选择levelC所属的levelA或levelB的描述信息。      
 
> GO富集分析的文件可以使用脚本3.10生成，但是需要按照下列格式修改：            
             
| gene_id | ID | Description | GROUP |            
| --- | --- | --- | --- |        
| GeneA | GO:000001 | mitochondrion inheritance | biological_process |        
| GeneA | GO:000002 | mitochondrial genome maintenance | biological_process |         
| GeneB | GO:000006 | high-affinity zinc transmembrane transporter activity | molecular_function |        
| ... | ... | ... | ... |        
                
> KEGG富集分析的文件需要按照下列格式修改可以使用代码3.05和EXCEL的vlookup函数生成该文件：           
               
| gene_id | ID | Description | GROUP |            
| --- | --- | --- | --- |        
| GeneA | ko00010 | Glycolysis / Gluconeogenesis | Metabolism |        
| GeneA | ko00020 | Citrate cycle (TCA cycle) | Metabolism |         
| GeneB | ko04016 | MAPK signaling pathway - plant | Environmental Information Processing |        
| ... | ... | ... | ... |        
          
> **文件2 关注的基因（差异基因/特异基因/正选择基因等）列表 gene.txt**      
至少有一列是以gene_id为列名的列，注意该列不得有重复的基因，否则计算将错误。       
   
| gene_id |                   
| --- |           
| GeneA |     
| GeneB |        
| GeneD |         
| ... |           
      
> 准备好上述两个文件，即可使用下列代码计算富集统计数，基于富集统计数即可绘制气泡图。       
   
```    
#富集分析R代码参考的是知乎文章  https://zhuanlan.zhihu.com/p/561522453 中的无参GO富集分析部分。      

library(clusterProfiler)        
#读取手动准备好的背景基因集
gene_ID <- read.delim('gene_ID.txt', stringsAsFactors = FALSE)
#读取基因列表文件中的基因名称
genes <- read.delim('gene.txt', stringsAsFactors = FALSE)$gene_id
#GO/KEGG 富集分析
gene_rich <- enricher(gene = genes,  #待富集的基因列表
    TERM2GENE = gene_ID[c('ID', 'gene_id')],  #背景基因集
    TERM2NAME = gene_ID[c('ID', 'Description')], 
    pAdjustMethod = 'BH',  #指定 p 值校正方法
        pvalueCutoff = 0.05,  #指定 p 值阈值（可指定 1 以输出全部）
    qvalueCutoff = 0.2)  #指定 q 值阈值（可指定 1 以输出全部）
#输出富集结果
write.table(gene_rich, 'gene_rich.txt', sep = '\t', row.names = FALSE, quote = FALSE)
#再把 GO Ontology或KEGG levelA 信息添加在上述富集结果中
tmp <- read.delim('gene_rich.txt')
gene_ID <- gene_ID[!duplicated(gene_GO$ID), ]
tmp <- merge(tmp, gene_GO[c('ID', 'GROUP')], by = 'ID')
tmp <- tmp[c(10, 1:9)]
tmp <- tmp[order(tmp$pvalue), ]
#输出
write.table(tmp, 'gene_rich.add_Ontology.txt', sep = '\t', row.names = FALSE, quote = FALSE)
```       

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
