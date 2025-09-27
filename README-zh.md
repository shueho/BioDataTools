[中文](README-zh.md) | [英文](README.md)              

# BioDataTools

这是一套生物信息学脚本，结合了组学和生态遗传分析，支持多种数据处理工具，适应广泛的研究需求。   

## 脚本工具目录

这个README文档提供了每个模块下的脚本文件及其简短的功能描述，以及某些分析工作流的简明概述。本文档有中英文两种版本，您可以根据自己的喜好进行切换。  

<table border="0" cellspacing="0" cellpadding="5">
  <tr>
    <th>脚本编号</th>
    <th>脚本名称</th>
    <th>功能简述</th>
  </tr>
  <tr><th colspan="3" style="text-align:center; font-weight:bold;">Metagenome：宏基因组分析模块</th></tr>
  <tr><td>1.01</td><td>QuastAssemblerSummary</td><td>Quast软件评估结果汇总</td></tr>
  <tr><td>1.02</td><td>FastaSeqsRenamerUniqueContinuous</td><td>为Fasta格式的每条序列重新编号</td></tr>
  <tr><td>1.03</td><td>MPAtoMatrix</td><td>合并kraken1/2或bracken生成的MPA文件</td></tr>
  <tr><td>1.04</td><td>TaxLevelMatrixSplitter</td><td>按照阶元等级分割物种丰度表</td></tr>
  <tr><th colspan="3" style="text-align:center; font-weight:bold;">Genetics：基因组分析模块</th></tr>
  <tr><td>2.01</td><td>GIGenBankDownloader</td><td>按GI号批量下载Fasta文件</td></tr>
  <tr><td>2.02</td><td>GBRenameByX</td><td>根据具体信息批量重命名GB文件</td></tr>
  <tr><td>2.03</td><td>GBtoFastaWithDescriptions</td><td>批量转换GB文件到Fasta文件</td></tr>
  <tr><td>2.04</td><td>CombineTwoSequences</td><td>合并两个序列（低阶）</td></tr>
  <tr><td>2.05</td><td>FastaToHaplotypes</td><td>将样本序列转换为单倍型序列</td></tr>
  <tr><td>2.06</td><td>CustomFastaExtractor</td><td>使用正则表达式从Fasta文件中提取序列子集</td></tr>
  <tr><td>2.07</td><td>ProteinPropertyFromExpasy</td><td>批量获取蛋白质理化性质</td></tr>
  <tr><td>2.08</td><td>FeaturesBaseComponents</td><td>细胞器基因组特征数据统计</td></tr>
  <tr><td>2.09</td><td>ExAndRename</td><td>从Fasta文件提取子序列并重命名</td></tr>
  <tr><td>2.10</td><td>BatchFastaToPam</td><td>批量转换Fasta文件到PAML格式的文件</td></tr>
  <tr><td>2.11</td><td>ReassignSequence</td><td>重新分配序列所在的Fasta文件</td></tr>
  <tr><td>2.12</td><td>BatchAlignedProteinToDNA</td><td>将蛋白质比对文件转换为密码子比对文件</td></tr>
  <tr><td>2.13</td><td>Extract4DTv</td><td>四倍简并位点提取</td></tr>
  <tr><td>2.14</td><td>MergeSequences</td><td>合并序列（高阶）</td></tr>
  <tr><td>2.15</td><td>BatchGenerationCodeML_CTL</td><td>批量生成CodeML的配置文件</td></tr>
  <tr><td>2.16</td><td>ParsingCodeMLResults</td><td>批量解析CodeML结果</td></tr>
  <tr><td>2.17</td><td>SplitAXT</td><td>拆分AXT文件</td></tr>
  <tr><td>2.18</td><td>BaseSiteInformation</td><td>获得核苷酸在基因组上的位置信息</td></tr>
  <tr><td>2.19</td><td>MaskSeq</td><td>序列屏蔽（基因组mask）</td></tr>
  <tr><td>2.20</td><td>BaseCompositionCalculation</td><td>分密码子位碱基数目统计</td></tr>
  <tr><td>2.21</td><td>GFFSimplifier</td><td>简化GFF文件</td></tr>
  <tr><td>2.22</td><td>BaseSiteFeatureFinder</td><td>检索一个位点附近的特征（在指定距离内筛选候选基因）</td></tr>
  <tr><td>2.23</td><td>IntervalFeatureFinder</td><td>检索指定区域内的特征（在指定间隔内筛选候选基因）</td></tr>
  <tr><td>2.24</td><td>ExtractFastaWithGene</td><td>提取一个基因对应的所有转录本/蛋白/cDNA等</td></tr>
  <tr><td>2.25</td><td>CorrespondingNucleotideProteinFasta</td><td>将转录序列与蛋白质序列关联</td></tr>
  <tr><td>2.26</td><td>BatchModificationSequence</td><td>批量将固定序列前的序列替换为指定序列</td></tr>
  <tr><td>2.27</td><td>TableToMultipleFasta</td><td>按照表格的行拆分Fasta文件</td></tr>
  <tr><td>2.28</td><td>MultipleFastaToTable</td><td>将多个Fasta文件合并到一个表中</td></tr>
  <tr><td>2.29</td><td>AlignConsistencyChecker</td><td>简易版可视化序列比对结果</td></tr>
  <tr><td>2.30</td><td>MergeMultipleFasta</td><td>合并多个Fasta文件并删除冗余序列</td></tr>
  <tr><td>2.31</td><td>MitosToGFF</td><td>将Mitos注释结果转换为GFF文件</td></tr>
  <tr><td>2.32</td><td>MitosToFasta</td><td>将Mitos注释结果转换为Fasta文件</td></tr> 
  <tr><td>2.33</td><td>SsToFold</td><td>将tRNAscan-SE产生的二级结构文件（.ss）转换为RNAplot程序支持的格式</td></tr> 
  <tr><td>2.34</td><td>RSCUPlot</td><td>得到蛋白编码基因的密码子偏好性，绘制RSCU柱形图</td></tr> 
  <tr><td>2.35</td><td>splitGB</td><td>拆分多序列的GenBank文件</td></tr>   
  <tr><th colspan="3" style="text-align:center; font-weight:bold;">Gadget：通用工具模块</th></tr>
  <tr><td>3.01</td><td>MergeTable</td><td>超大表格合并</td></tr>
  <tr><td>3.02</td><td>VLookup</td><td>Vlookup函数（高阶）</td></tr>
  <tr><td>3.03</td><td>SumByGroup</td><td>分组求和（高阶）</td></tr>
  <tr><td>3.04</td><td>CountByGroup</td><td>分组计数（高阶）</td></tr>
  <tr><td>3.05</td><td>FastaSplitter</td><td>按指定序列数拆分Fasta文件</td></tr>
  <tr><td>3.06</td><td>KeggAnnotationParser</td><td>解析KEGG注释文件</td></tr>
  <tr><td>3.07</td><td>KEGGPathwayCounter</td><td>KEGG通路数目统计</td></tr>
  <tr><td>3.08</td><td>GOoboAnnotationExtractor</td><td>解析GO注释obo文件</td></tr>
  <tr><td>3.09</td><td>GOTableConverter</td><td>转换GO注释表格</td></tr>
  <tr><td>3.10</td><td>AddGOAnnotations</td><td>添加GO注释的描述和分类内容</td></tr>
  <tr><td>3.11</td><td>VectorTableMerger</td><td>将A-Bs和B-Cs表格连接成A-Cs</td></tr>
  <tr><th colspan="3" style="text-align:center; font-weight:bold;">Plotscript：绘图工具模块</th></tr>
  <tr><td>4.01</td><td>GeneArrangementMap</td><td>绘制基因组特征排布图</td></tr>
  <tr><td>4.02</td><td>TrnaStructureBeautifier</td><td>tRNA二级结构图美化</td></tr>
  <tr><th colspan="3" style="text-align:center; font-weight:bold;">BioDataSpider：生物学数据库爬虫工具模块</th></tr>
  <tr><td>5.01</td><td>GenoSpider</td><td>基因组信息爬虫</td></tr>
  <tr><td>5.02</td><td>PrideSpider</td><td>PRIDE数据库信息爬虫</td></tr>
  <tr><th colspan="3" style="text-align:center; font-weight:bold;">分析流程</th></tr>
  <tr><td colspan="2">宏基因组物种定量分析流程</td><td>位于1.04脚本之后</td></tr>
  <tr><td colspan="2">群体遗传学分析快速下载数据流程</td><td>位于2.03脚本之后</td></tr>
  <tr><td colspan="2">比较基因组学-同源基因建树和选择压力分析流程（一）</td><td>位于2.16脚本之后</td></tr>
  <tr><td colspan="2">比较基因组学-同源基因建树和选择压力分析流程（二）</td><td>位于2.17脚本之后</td></tr>
  <tr><td colspan="2">无参GO/KEGG富集分析流程</td><td>位于3.10脚本之后</td></tr>
</table>


## 1. Metagenome：宏基因组分析相关脚本
   
### 1.01 `QuastAssemblerSummary.py [DIR_PATH]`

**功能描述：** 整合由Quast软件输出的多个样本组装评估结果，生成一个组装信息表矩阵。

- **DIR_PATH：** Quast结果文件夹路径，内含各个样本的 `transposed_report.tsv` 文件。

**生成文件：**

- `sumary.tsv`（表格文件，每一列表示一个样本，每一行对应一个组装数据）。      

**示例：**

如 `example/quast` 文件中包含由Quast软件得到的各样品组装评估结果，其文件结构如下：
```
example/
└── quast/
    ├── sp1/
    │   └── transposed_report.tsv
    ├── sp2/
    │   └── transposed_report.tsv
    └── sp3/
        └── transposed_report.tsv
```
执行命令：
```bash
python QuastAssemblerSummary.py example/quast
```
输出结果文件 `summary.tsv`，内容示例：
```
Sample    N50    Total Length    # Contigs    Largest Contig    GC (%)    ...
sp1       10000   5000000         100           25000       42.3      ...
sp2       12000   5500000         85            30000       41.7      ...
sp3       15000   6000000         70            40000       43.1      ...
```

### 1.02 `FastaSeqsRenamerUniqueContinuous.py [FASTA_FILE_PATH]` 

**功能描述：** 对FASTA格式序列文件中各个序列标头进行统一命名规范，确保每个序列标识唯一且编号连续。

- **FASTA_FILE_PATH：** 原FASTA文件路径。

**使用场景：** 在宏基因组等组学分析项目中，该脚本通过统一重命名各FASTA文件中的序列ID为连续数字（1, 2, 3...），确保合并样品组装数据时标识唯一性，为后续基因丰度分析及注释规范序列名称，便于差异基因追踪及原始序列比对。

**注意事项：** 本代码只适用于后续不再讨论原始序列标识的场景，切勿在定量、注释等下游分析后使用该脚本！不要和2.30搞混，本脚本是将序列重新编号（无论序列是否一致都会赋予不同的ID）；而2.30是将重复序列赋予统一ID，如果原本文件中有相同的ID（无论是否是相同序列）都只保留最后一个。  

**生成文件：** 
- `out_<原始FASTA文件名称>`（FASTA文件，各个序列被重新编码）。    

**示例：**

比如 `example/origin_seq.fa` 文件中包含重复标识的序列：  
```
>aaa
ATCGGCATATATCTTATTATATTTCCCCAAA
>abc
ATCGGCATATATCTTATTATATTTCCCCAAA
TTCCATCA
>aaa
ATCGGCATATATCTTATTATATTTCCCCAAA
>ac
ATCGGCATATATCTTATTATATTTCCCCAAA
>at
ATCGGCATATATCTTATTATATTTCCCCAAA
TTCCATCA
>aa
ATCGGCATATATCTTATTATATTTCCCCAAA
```
执行命令：
```bash
python FastaSeqsRenamerUniqueContinuous.py example/origin_seq.fa
``` 
输出结果文件 `out_origin_seq.fa` ，即为序列标识唯一的FASTA文件： 
```
>N_0000000001 
ATCGGCATATATCTTATTATATTTCCCCAAA
>N_0000000002 
ATCGGCATATATCTTATTATATTTCCCCAAATTCCATCA
>N_0000000003 
ATCGGCATATATCTTATTATATTTCCCCAAA
>N_0000000004 
ATCGGCATATATCTTATTATATTTCCCCAAA
>N_0000000005 
ATCGGCATATATCTTATTATATTTCCCCAAATTCCATCA
>N_0000000006 
ATCGGCATATATCTTATTATATTTCCCCAAA
```  

### 1.03 `MPAtoMatrix.py  [MPA_PATH]` 

**功能描述：** 将Kraken1/2或Bracken软件生成的mpa文件转换为物种丰度矩阵。

- **MPA_PATH：** 存放所有样本的MPA文件的路径。

**注意事项：** 本脚本支持处理由Kraken 1、Kraken 2或Bracken输出的MPA文件目录。运行前，请先利用kreport2mpa.py脚本将结果转换为MPA格式。重要的是，所有MPA文件必须基于相同的核酸数据库生成，因为物种丰度的排列顺序取决于所选数据库，确保数据一致性。

**生成文件：** 
- `mpaMatrix.txt`（表格文件，物种丰度表，每一列都表示一个样品）。   

**示例：**

比如 `example/mpa` 文件中包含多个样本的MPA文件：
```
example/
└── mpa/
    ├── sp1.mpa   
    ├── sp2.mpa   
    ├── sp3.mpa 
    └── sp4.mpa
```
执行命令：
```bash
python MPAtoMatrix.py example/mpa
``` 
输出结果文件 `mpaMatrix.txt` 即为物种丰度矩阵，第一列是注释到的物种分类学信息，其余每一列是各个样品注释到的物种丰度：
```
#Classification	sp1	sp2	sp3	sp4
k__Eukaryota	13682	9638	9039	14460
k__Eukaryota|k__Fungi	13682	9638	9039	14460
k__Eukaryota|k__Fungi|p__Ascomycota	12398	8678	8176	12898
k__Eukaryota|k__Fungi|p__Ascomycota|c__Sordariomycetes	8893	5998	5014	8723
k__Eukaryota|k__Fungi|p__Ascomycota|c__Sordariomycetes|o__Hypocreales	4102	2580	2178	3841
k__Eukaryota|k__Fungi|p__Ascomycota|c__Sordariomycetes|o__Hypocreales|f__Ophiocordycipitaceae	1937	1338	1155	1969
...
k__Eukaryota|k__Fungi|p__Microsporidia	11	5	7	14
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae	11	5	7	14
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon	11	5	7	14
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_intestinalis	5	1	3	3
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_romaleae	2	2	0	5
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_hellem	2	1	3	4
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_cuniculi	1	1	0	2
```  

### 1.04 `TaxLevelMatrixSplitter.py [MPA_MERGE_FILE] [SPLIT_LEVEL]` 

**功能描述：** 该脚本物种丰度表中提取各分类阶元的物种丰度数据并构建相应的丰度矩阵。

- **MPA_MERGE_FILE：** 由 `1.03 MPAtoMatrix.py` 脚本生成的 `mpaMatrix.txt` 文件路径，也可以将您的丰度表修改为示例文件的样式。
- **SPLIT_LEVEL：** 要指定输出的物种丰度表格的分类级别，可使用以下单个字母标识：'a'（全级别）、'K'（界）、'P'（门）、'C'（纲）、'O'（目）、'F'（科）、'G'（属）、'S'（种），其中'a'表示输出所有分类阶元的丰度表。大写或小写字母均可。

**生成文件：** 
- `taxLevel_<指定的阶元等级（大写）>_output.<丰度矩阵文件名>`（一个或多个表格文件，物种丰度表）。

**示例：**

比如 `example/mpaMatrix.txt` 文件中包含物种丰度信息：
```
#Classification	sp1	sp2	sp3	sp4
k__Eukaryota	13682	9638	9039	14460
k__Eukaryota|k__Fungi	13682	9638	9039	14460
k__Eukaryota|k__Fungi|p__Ascomycota	12398	8678	8176	12898
k__Eukaryota|k__Fungi|p__Ascomycota|c__Sordariomycetes	8893	5998	5014	8723
k__Eukaryota|k__Fungi|p__Ascomycota|c__Sordariomycetes|o__Hypocreales	4102	2580	2178	3841
k__Eukaryota|k__Fungi|p__Ascomycota|c__Sordariomycetes|o__Hypocreales|f__Ophiocordycipitaceae	1937	1338	1155	1969
...
k__Eukaryota|k__Fungi|p__Microsporidia	11	5	7	14
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae	11	5	7	14
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon	11	5	7	14
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_intestinalis	5	1	3	3
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_romaleae	2	2	0	5
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_hellem	2	1	3	4
k__Eukaryota|k__Fungi|p__Microsporidia|f__Unikaryonidae|g__Encephalitozoon|s__Encephalitozoon_cuniculi	1	1	0	2
```  
执行命令：
```bash
# 生成所有阶元等级的丰度数据运行：
python TaxLevelMatrixSplitter.py example/mpaMatrix.txt a
# 输出7个阶元的结果文件：taxLevel_K/P/C/O/F/G/S_output.mpaMatrix.txt。

# 只生成科阶元的丰度数据运行：
python TaxLevelMatrixSplitter.py example/mpaMatrix.txt f
# 只输出一个结果文件：taxLevel_F_output.mpaMatrix.txt。
```
即可输出对应的1个或7个结果：
```
#taxLevel_K_output.mpaMatrix.txt
k	sp1	sp2	sp3	sp4
Eukaryota	13682	9638	9039	14460
Fungi	13682	9638	9039	14460

#taxLevel_P_output.mpaMatrix.txt
k	p	sp1	sp2	sp3	sp4
Fungi	Ascomycota	12398	8678	8176	12898
Fungi	Basidiomycota	1273	954	856	1548
Fungi	Microsporidia	11	5	7	14

#taxLevel_C_output.mpaMatrix.txt
k	p	c	sp1	sp2	sp3	sp4
Fungi	Ascomycota	Sordariomycetes	8893	5998	5014	8723
Fungi	Ascomycota	Leotiomycetes	36	20	25	49
Fungi	Ascomycota	Eurotiomycetes	1016	811	1542	1224
Fungi	Ascomycota	Dothideomycetes	530	410	370	616
Fungi	Ascomycota	Saccharomycetes	1409	1010	847	1650
Fungi	Ascomycota	Schizosaccharomycetes	511	427	374	635
Fungi	Basidiomycota	Ustilaginomycetes	658	436	430	679
Fungi	Basidiomycota	Malasseziomycetes	196	167	126	263
Fungi	Basidiomycota	Agaricomycetes	153	124	110	171
Fungi	Basidiomycota	Tremellomycetes	100	91	59	145
Fungi	Basidiomycota	Pucciniomycetes	164	134	130	287

...
#taxLevel_S_output.mpaMatrix.txt
k	p	c	o	f	g	s	sp1	sp2	sp3	sp4
Fungi	Ascomycota	Sordariomycetes	Hypocreales	Ophiocordycipitaceae	Purpureocillium	Purpureocillium_takamizusanense	998	692	605	1019
Fungi	Ascomycota	Sordariomycetes	Hypocreales	Ophiocordycipitaceae	Drechmeria	Drechmeria_coniospora	939	646	549	949
Fungi	Ascomycota	Sordariomycetes	Hypocreales	Nectriaceae	Fusarium	Fusarium_falciforme	390	181	140	284
...
Fungi	Microsporidia	-	-	Unikaryonidae	Encephalitozoon	Encephalitozoon_romaleae	2	2	0	5
Fungi	Microsporidia	-	-	Unikaryonidae	Encephalitozoon	Encephalitozoon_hellem	2	1	3	4
Fungi	Microsporidia	-	-	Unikaryonidae	Encephalitozoon	Encephalitozoon_cuniculi	1	1	0	2
```

> ## 宏基因组物种定量分析流程     
> 宏基因组分析中的物种注释分析可以使用kraken2和bracken分析软件，`database_PATH` 表示关注物种群体的核酸数据库路径，`sp1` 表示样品名称，首先使用kraken2指定数据库得到report文件，其中 `sp1*` 是表示双端测序结果的路径。       
> ```
> kraken2 --db database_PATH --paired sp1*  --threads 128 --use-names --report-zero-counts --report sp1.report --output sp1.output
> ```
> 随后使用bracken将report文件转换为bracken文件。
> ```
> bracken -d database_PATH -i sp1.report -r 150 -l S -t 0 -o sp1.bracken -w sp1.bracken.report
> ```
> 使用kreport2mpa.py得到mpa文件。
> ```
> kreport2mpa.py -r sp1.bracken.report --display-header -o sp1.bracken.mpa
> ``` 
> 上述流程只是对sp1样品进行了分析，实际分析中需要编写循环语句批量对各个样品结果进行输出。得到的mpa文件使用1.03脚本可以获取物种丰度矩阵，使用1.04脚本得到各个阶元水平的丰度矩阵，随后可以进行α/β物种多样性分析、LEfSe分析等与物种丰度相关的分析。 
             

## 2. Genetics：用于基因组和比较基因组学研究中的数据处理，涵盖从NCBI批量获取数据，以及批量提取和批量转化数据信息内容的脚本。           
 
### 2.01 `GIGenBankDownloader.py [GI_LIST_DIR]`

**功能描述：** 通过GI编号批量下载GenBank文件。

- **GI_LIST_DIR：** 存放GI编号的目录路径，脚本自动检测并读取文件夹内所有以 `_gi.txt` 为扩展名的文本文件。这些 `_gi.txt` 文件包含待下载序列的GI编号。

**使用场景：** 为批量下载大量GenBank（gb）文件，您仅需简便地创建若干个“xxx_gi.txt”文件，每文件内粘贴相应的GI编号列表。此设计灵活性高，根据不同的GI编号列表文件，以列表文件名对结果文件进行区分。方便后续将不同分组文件分类归档，极大便利了群体遗传学中常见的单倍型分析任务。

**注意事项：** 需要安装requests库！如果需要下载的序列较多不推荐使用本脚本，推荐使用https://www.ncbi.nlm.nih.gov/sites/batchentrez?批量下载序列。  

**生成文件：** 
- `gb/<列表名称>_<GI编号>.gb`（在 `gb` 文件夹下生成多个GENEBANK文件）。

**示例：**

比如 `example/gi` 文件中存放有需要下载序列的GI编号：
```
#example/gi/Kinaisemen_gi.txt
1820426935
1820426934

#example/gi/Nomomachi_gi.txt
1820426946
1820426945
1820426944
```
执行命令：
```bash
python GIGenBankDownloader.py example/gi
``` 
输出文件夹 `gb` ，其中包括以列表名称为前缀的多个gb文件。
```
gb/
├── Kinaisemen_1820426934.gb   
├── Kinaisemen_1820426935.gb   
├── Nomomachi_1820426944.gb 
├── Nomomachi_1820426945.gb 
└── Nomomachi_1820426946.gb
```

### 2.02 `GBRenameByX.py [GB_DIR] [INFO_NAME]`

**功能描述：** 读取GB文件内的某一样品信息（如isolate信息），并依据这一信息为对应的GB文件重新命名，适用于群体遗传学分析中对大批量GB文件进行统一管理和组织。

- **GB_DIR：** 存放GB文件的目录路径。
- **INFO_NAME：** 需要对GB文件名称修改的参考信息，务必保证不同GB文件中该样品信息是唯一的。

**注意事项：** 务必使用可以区分所有GB文件的信息！每次运行最好手动将上次运行产生的文件删除或重命名。

**生成文件：** 
- `output/<样品信息对应的值（空格以下划线替换）>.gb`（`output` 文件夹下的多个GENEBANK文件）。

**示例：**

比如 `example/gb_isolate` 文件：
```
example/
└── gb_isolate/
    ├── Kinaisemen_1820426934.gb   
    ├── Kinaisemen_1820426935.gb   
    ├── Nomomachi_1820426944.gb 
    ├── Nomomachi_1820426945.gb 
    └── Nomomachi_1820426946.gb
```
和 `example/gb_orgnism` 文件：
```
example/
└── gb_organism/
    ├── Ansan_1820426827.gb   
    ├── Buan_1820426866.gb   
    └── Kinaisemen_1820426929.gb
```
中分别包含以 `isolate` 和 `orgnism` 信息区分的多个样品GB文件，可以执行：
```bash
# 以isolate信息命名运行：
python GBRenameByX.py example/gb_isolate isolate

# 以orgnism信息命名运行：
python GBRenameByX.py example/gb_organism organism
```
即可输出对应的结果于文件夹 `output` 中： 
```
#isolate
output/
├── Kinaisemen_06.gb   
├── Kinaisemen_07.gb   
├── Nomomachi_01.gb 
├── Nomomachi_02.gb 
└── Nomomachi_03.gb

#organism
output/
├── A_a.gb   
├── A_b.gb   
└── A_k.gb
```
     
### 2.03 `GBtoFastaWithDescriptions.py [GB_DIR]`
`
**功能描述：** 批量地将GB文件转换为FASTA格式，并且在转换过程中，将原GB文件的文件名插入到FASTA格式序列记录的描述行（“>”后面的部分），以便于追踪源文件信息。这对于高效处理大量的GB文件，在进行诸如群体遗传学分析等工作时尤为重要。

- **GB_DIR：** 存放GB文件的目录路径。

**生成文件：** 
- `output/<原GB文件名>.fas`（多个FASTA文件）。 

**示例：**

比如需要将 `example/gb_isolate` 文件夹中GB文件转换为FASTA文件：
```
example/
└── gb_isolate/
    ├── Kinaisemen_1820426934.gb   
    ├── Kinaisemen_1820426935.gb   
    ├── Nomomachi_1820426944.gb 
    ├── Nomomachi_1820426945.gb 
    └── Nomomachi_1820426946.gb
```
执行命令：
```bash
python GBtoFastaWithDescriptions.py example/gb_isolate
``` 
即可输出对应的结果于文件夹 `output` 中：
```
output/
├── Kinaisemen_1820426934.fas   
├── Kinaisemen_1820426935.fas   
├── Nomomachi_1820426944.fas 
├── Nomomachi_1820426945.fas 
└── Nomomachi_1820426946.fas
```

> ## 群体遗传学分析快速下载数据流程          
> 比如要从NCBI下载特定多个群体的 `cox1` 基因，可以先创建一个文件夹，分别列出该群体不同个体的 `cox1` 基因的GI编号（可以在NCBI直接导出），并将每个群体的编号保存在独立的xxx_gi.txt文件中；接着运行脚本2.01来下载相应的GB文件；再运行脚本2.02，依据isolate或其他标签对下载的GB文件进行重命名；最后执行脚本2.03，从而生成以标签值为名称的最终FASTA格式序列文件。

### 2.04 `CombineTwoSequences.py [FASTA_FILE_1] [FASTA_FILE_2]`

**功能描述：** 合并序列的低级版本，后续会提供该脚本的进阶版本（脚本2.14）。

- **FASTA_FILE_1：** 第一个序列。
- **FASTA_FILE_2：** 第二个序列。

**使用场景：** 假设你有来自样本A、B和C的16S和COI序列，出于某种目的，你想要结合来自不同样本的16S和COI序列。您可以使用这个脚本。

**多次调用：** 如果要合并多个序列，可以重复调用此脚本。

**注意事项：** 务必在比对后的序列文件中使用该脚本！

**生成文件：** 
- `merge.fas`（合并后的FASTA文件）。

**示例：**

比如 `example/fasta_merge` 目录中包含需要合并的序列 `16s.fasta` 和 `co1.fasta`：
```
#example/fasta_merge/16s.fasta
>AN012
-------------CGCTCTTTGAAATACAAATATAGAGAGTCGTGCCTGCCCAGTGATTT...
>AN015
-------------CGCTCTTTGAAATACAAATATAGAGAGTCGTGCCTGCCCAGTGATTT...

#example/fasta_merge/co1.fasta
>AN012
--TACTTTATATATTTTGTTTGGGATTTGGTCTGGATTGGTTGGAACAGCTTTAAGACTA...
>AN015
--TACTTTATATATTTTGTTTGGGATTTGGTCTGGATTGGTTGGAACAGCTTTAAGACTA...
```
执行命令：
```bash
python CombineTwoSequences.py example/fasta_merge/16s.fasta example/fasta_merge/co1.fasta
``` 
输出结果文件 `merge.fas` ，即为16s+co1合并序列：
```
>AN012
-------------CGCTCTTTGAAATACAAATATAGAGAGTCGTGCCTGCCCAGTGATTT...
--TACTTTATATATTTTGTTTGGGATTTGGTCTGGATTGGTTGGAACAGCTTTAAGACTA...
>AN015
-------------CGCTCTTTGAAATACAAATATAGAGAGTCGTGCCTGCCCAGTGATTT...
--TACTTTATATATTTTGTTTGGGATTTGGTCTGGATTGGTTGGAACAGCTTTAAGACTA...
```

### 2.05 `FastaToHaplotypes.py -p [FASTA_FILE_NAME] -l [LIST_NAME]`

**功能描述：** 将FASTA文件中多个样品序列根据单倍型归类。

- **FASTA_FILE_NAME：** 样品序列文件名（参照example/sample.fas）。
- **LIST_NAME：** 单倍型对应样品的表格（参照example/hap.list）。

**参数说明：** 使用前需要获取两个文件，一个是DnaSP导出的单倍型和样品对应的表格（可能需要手工制作）。另一个是包含所有物种序列的fasta文件。

**使用场景：** 比如，对于包含a、b、c、d、e五个样品的序列数据，其中样品a、b、c的序列完全相同，样品d和e的序列也完全一致，意味着我们拥有两个独特的单倍型。借助这段代码，能够将具有相同序列的样品合并归类为各自的单倍型，有利于后续针对不同单倍型序列进行系统发育分析。参考示例文件和示例代码！！！      

**生成文件：** 
- `out_hap.fasta`（由单倍型组成的FASTA文件）。

**示例：**

比如 `example/sample.fas` 文件是各个样品的序列文件：
```
>a001
ATCGGCTA
>a002
ATCGGCTA
>b001
AT-GCCTA
>b002
AT-GCCTA
>b003
AT-GCCTA
>c001
--CGGCTA
```
`example/hap.list` 文件是单倍型对应样品的表格：
```
[Hap_1:  2    a001 a002]
[Hap_2:  3    b001 b002 b003]
[Hap_3:  1    c001]
```
执行命令：
```bash
python FastaToHaplotypes.py -p example/sample.fas -l example/hap.list
``` 
输出结果文件 `out_hap.fasta` ，即为单倍型序列文件：
```
>H1
ATCGGCTA
>H2
AT-GCCTA
>H3
--CGGCTA
```

### 2.06 `CustomFastaExtractor.py [FASTA_FILE] [LIST_FILE] [Regular_expressions (Optional)]`

**功能描述：** 依据提供的ID列表，该脚本能从一个整合多序列的FASTA文件中抽取出相应序列，生成子FASTA文件。默认配置下，系统识别">"符号后至首个空格前的文本为ID，与列表中的条目匹配。针对复杂情况，支持自定义正则表达式以实现ID的精准匹配，确保灵活高效地筛选目标序列。

- **FASTA_FILE：** Fasta格式的序列文件，也就是包括所有序列的文件，比如全基因组的pep或者CDS序列。
- **LIST_FILE：** 列表中应包含希望提取的序列编号或名称，这部分信息可以是FASTA_FILE中每条序列“>”符号后紧跟的整个描述字段，也可以只是该描述字段中的一部分内容。
- **Regular_expressions：** 可选参数，假如你的列表中的名称与FASTA文件序列名称有所不同，你可以指定正则表达式对序列进行提取。如果没有填写，默认为："\_(.*?)".，这意味着你将“>”之后第一个空格前的内容作为ID名称。

**使用场景：** 在进行共线性分析或同源基因分群时，频繁遇到从NCBI获取的pep文件含有大量冗余数据。为优化此过程，可选择性下载仅涵盖染色体编码的非冗余蛋白质序列数据库。此脚本特地设计用来根据用户提供的序列名称，从庞大的pep文件中抽取出所需片段。此外，它还支持抽取对应的编码序列（CDS），考虑到蛋白质序列ID与CDS ID间可能存在的差异，引入正则表达式自定义匹配规则显得尤为重要。如需进一步简化流程，推荐采用升级版代码2.09，该版本同样能有效执行此类抽取任务。

**注意事项：** 不可用于提取某一基因多个转录本！本代码不支持提取同名基因不同转录本/蛋白质序列！只能提取唯一基因名称的序列！如果你有该需求，可以关注脚本2.24！     

**生成文件：** 
- `out_match_seq.fasta`（FASTA文件）。

**示例：**

比如 `example/text1.fa` 与`example/text2.fa`是完整的FASTA文件：
```
#example/text1.fa
>KAF7112153.1 hypothetical protein RHSIM_RhsimUnG0257300 [Rhododendron simsii]
MASVKNRVRNKLFKCFRPAAIDDDPIKPDATDGPGNSVFTSISGKGKSGKISNLLSGEKGKVYSEGGDAGGDRSNKERSH...
>KAF7112159.1 hypothetical protein RHSIM_RhsimUnG0256100 [Rhododendron simsii]
MASNTQSSFEDFLPIMAHKLGGEALIGELCNGFRLLMDGDKGVITFDSLKKNAAVLGLQELTDGDLRSMLREGDFDGDGA...
...
>KAF7152831.1 hypothetical protein RHSIM_Rhsim01G0241100 [Rhododendron simsii]
MASTHITPQTNFSSFSKAQFMASSATSFTDLLAGDYPSSSAVSRGLSDRIAERTGSGVPKFKSIPPPSIPTSPHAVSPSF...

#example/text2.fa
>Rhsim01G0033600
ATCGGTAC
>Rhsim01G0241100
ATACCCCCVHHHHH
>abc
ADFAAFAFAF
>def
DAFAFAFAGFAG
```
列表`example/list1.txt` 与`example/list1.txt`中是需要提取的序列名称：
```
#example/list1.txt
KAF7112159.1
KAF7153261.1

#example/list2.txt
Rhsim01G0033600
Rhsim01G0241100
```

执行命令：
```bash
# 如果你所需要提取的序列名称是第一个空格前的内容，尤其是针对那些直接从NCBI下载的fasta文件，你可以直接运行：
python CustomFastaExtractor.py example/text1.fa example/list1.txt

# 常用！如果你所需要提取的序列名称是>后的所有内容，你可以直接运行：
python CustomFastaExtractor.py example/text2.fa example/list2.txt "\>(.*)"

# 如果使用正则表达式提取：
python CustomFastaExtractor.py example/text1.fa example/list2.txt "\_(.*?) "
```
即可输出对应的子序列文件：
```
#python CustomFastaExtractor.py example/text1.fa example/list1.txt
>KAF7112159.1 hypothetical protein RHSIM_RhsimUnG0256100 [Rhododendron simsii]
MASNTQSSFEDFLPIMAHKLGGEALIGELCNGFRLLMDGDKGVITFDSLKKNAAVLGLQELTDGDLRSMLREGDFDGDGA...
>KAF7153261.1 hypothetical protein RHSIM_Rhsim01G0033600 [Rhododendron simsii]
MDQVGKSHQQALVSVITEAAQSQLKNEVTESPQCPTSSSELSPTSVTQSISSGPTNKKLSLVANTNSACMPEVVRQNSSN

#python CustomFastaExtractor.py example/text2.fa example/list2.txt "\>(.*)"
>Rhsim01G0033600
ATCGGTAC
>Rhsim01G0241100
ATACCCCCVHHHHH

#python CustomFastaExtractor.py example/text1.fa example/list2.txt "\_(.*?) "
>KAF7153261.1 hypothetical protein RHSIM_Rhsim01G0033600 [Rhododendron simsii]
MDQVGKSHQQALVSVITEAAQSQLKNEVTESPQCPTSSSELSPTSVTQSISSGPTNKKLSLVANTNSACMPEVVRQNSSN...
>KAF7152831.1 hypothetical protein RHSIM_Rhsim01G0241100 [Rhododendron simsii]
MASTHITPQTNFSSFSKAQFMASSATSFTDLLAGDYPSSSAVSRGLSDRIAERTGSGVPKFKSIPPPSIPTSPHAVSPSF...
```

### 2.07 `ProteinPropertyFromExpasy.py [FASTA_FILE]`

**功能描述：** 从Expasy（ https://web.expasy.org/protparam ）中批量获得蛋白质的理化性质。

- **FASTA_FILE：** 提供蛋白质序列的FASTA格式，可以是包含多个序列的文件。

**生成文件：** 
- `expasy_output.csv`（表格文件，包含部分蛋白质序列的理化性质）。

**示例：**

比如 `example/text.fa` 是蛋白序列的FASTA文件：
```
>KAF7112153.1 hypothetical protein RHSIM_RhsimUnG0257300 [Rhododendron simsii]
MASVKNRVRNKLFKCFRPAAIDDDPIKPDATDGPGNSVFTSISGKGKSGKISNLLSGEKGKVYSEGGDAGGDRSNKERSH...
>KAF7112159.1 hypothetical protein RHSIM_RhsimUnG0256100 [Rhododendron simsii]
MASNTQSSFEDFLPIMAHKLGGEALIGELCNGFRLLMDGDKGVITFDSLKKNAAVLGLQELTDGDLRSMLREGDFDGDGA...
...
>KAF7152831.1 hypothetical protein RHSIM_Rhsim01G0241100 [Rhododendron simsii]
MASTHITPQTNFSSFSKAQFMASSATSFTDLLAGDYPSSSAVSRGLSDRIAERTGSGVPKFKSIPPPSIPTSPHAVSPSF...
```
执行命令：
```bash
python ProteinPropertyFromExpasy.py example/text.fa
``` 
即可输出对应结果：
```
id	Number of amino acids	Molecular weight	Theoretical pI	Instability index	Aliphatic index	Grand average of hydropathicity (GRAVY)
KAF7112153.1	242	26387.53	9.6	46.09	65.33	-0.683
KAF7112159.1	215	23735.82	4.91	46.08	73.02	-0.329
KAF7154833.1	86	9692.81	9.84	59.07	40.81	-0.852
KAF7153261.1	397	43507.84	9.07	56.96	61.64	-0.763
KAF7152831.1	548	60491.94	8.44	57.65	43.27	-0.965
```

### 2.08 `FeaturesBaseComponents.py [FASTA_FILE] [TABLE]`

**功能描述：** 细胞器基因组专用，特征提取和碱基组成统计。如果你想基于开始和结束位置截断fasta文件，你也可以使用这个脚本!  

- **FASTA_FILE：** 只包含一个序列的fasta文件。
- **TABLE：** 表格包含特征名称、组别和起始位置的表。第一列为基因组，第二列为基因，第三列为基因起始位置，第四列为基因终止位置。基因是名义上的概念，你可以给任何片段分配分组。

**使用场景：** 如果fasta文件是线粒体基因组，表格文件第一列是特征（比如tRNA、CDS等）、第二类是特征名称（比如基因名称、D-Loop等），可以得到各个区域的碱基使用情况表格。

**注意事项：** 如果序列中含有中间终止密码子慎用，并且如果不是+链编码的基因会提取到其反向互补序列。

**生成文件：** 
- `ex_seq.fasta`（FASTA文件，提取到的小片段序列）。
- `Base_composition.txt` （表格ATGC的碱基占比）。

**示例：**

比如 `example/all.fa` 是小片段序列的FASTA文件：
```
>test dna [LEN=30]
GATTTAGCAG
TAAGATGAGA
TCATCCCCAG
```
`example/matrix.txt` 是特征位置矩阵：
```
A;B	ab	9	11
A	a1	16	21
A	a2	6	10
b	b	14	23
```
执行命令：
```bash
python FeaturesBaseComponents.py example/all.fa example/matrix.txt
``` 
即可输出对应结果：
```
#ex_seq.fasta
>ab
AGT
>a1
TGAGAT
>a2
AGCAG
>b
GATGAGATCA

>GR%A
AGCAGTTGAGAT
>GR%B
AGT
>GR%b
GATGAGATCA
>$all
GATTTAGCAGTAAGATGAGATCATCCCCAG
>$other
GATTTAATCCCCAG

#Base_composition.txt
SEQ	A	T	G	C
ab	1	1	1	0	
a1	2	2	2	0	
a2	2	0	2	1	
b	4	2	3	1	
GR%A	4	3	4	1	
GR%B	1	1	1	0	
GR%b	4	2	3	1	
$all	10	7	7	6	
$other	4	4	2	4	
```

### 2.09 `ExAndRename.py [MAP_FILE] [FASTA_FILE]`

**功能描述：** 从FASTA文件中提取部分序列，并对这些序列按照规则修改名称。

- **MAP_FILE：** 在提供的信息中，第一列所列出的是欲提取或重命名的序列名，它对应fasta文件中“>”符号之后，首个空格之前的文本内容；若无空格，则为“>”符号之后的完整序列标识符。第二列则是期望修改为目标的新名称。当第一列与第二列内容相同时，这一操作相当于执行代码2.06的功能。
- **FASTA_FILE：** Fasta格式的序列文件，也就是包括所有序列的文件，比如全基因组fa文件、pep或者CDS序列。

**使用场景：** 适用于从全基因组序列中提取染色体并修改名称。

**生成文件：** 
- `subset_fasta.faa`（FASTA文件，如果在map表存在多余的内容会有提示）。              

**示例：**

比如 `eexample/map.txt` 是旧ID（第一列）和新ID（第二列）的对应表格：
```
KAF7154833.1	a
KAF7152831.1	b
aaa	c
```
`example/text.fa` 是所有序列：
```
>KAF7112153.1 hypothetical protein RHSIM_RhsimUnG0257300 [Rhododendron simsii]
MASVKNRVRNKLFKCFRPAAIDDDPIKPDATDGPGNSVFTSISGKGKSGKISNLLSGEKGKVYSEGGDAGGDRSNKERSH...
>KAF7112159.1 hypothetical protein RHSIM_RhsimUnG0256100 [Rhododendron simsii]
MASNTQSSFEDFLPIMAHKLGGEALIGELCNGFRLLMDGDKGVITFDSLKKNAAVLGLQELTDGDLRSMLREGDFDGDGA...
...
>KAF7152831.1 hypothetical protein RHSIM_Rhsim01G0241100 [Rhododendron simsii]
MASTHITPQTNFSSFSKAQFMASSATSFTDLLAGDYPSSSAVSRGLSDRIAERTGSGVPKFKSIPPPSIPTSPHAVSPSF...
```
执行命令：
```bash
python ExAndRename.py example/map.txt example/text.fa
``` 
即可生成：
```
>a
MFRFAMWNRGWSWWTSPTDKERVDVVMETKGGKKKSSSSSTSTSSSRSSSLQYEAPLGYSIEDIRPNGGIEKFRSAAYSN...

>b
MASTHITPQTNFSSFSKAQFMASSATSFTDLLAGDYPSSSAVSRGLSDRIAERTGSGVPKFKSIPPPSIPTSPHAVSPSF...
```
需要注意的是aaa序列不存在，因此没有提取。   
       
### 2.10 `BatchFastaToPam.py [FASTA_FILE_DIR]`

**功能描述：** 批量将比对过的FASTA文件转换为paml比对文件。

- **FASTA_FILE_DIR：** 文件夹路径名，在该目录下包含需要转换的FASTA格式的比对文件。

**注意事项：** 文件夹中不能包含未比对的序列文件，也不能有其他文件，否则将会报错！

**生成文件：** 
- `pamlfile`（文件夹，其中包含需要转换的fasta文件名+pam后缀）。      

**示例：**

比如 `example/ali_fasta` 文件夹中包含需要转换的fasta文件：
```
example/
└── ali_fasta/
    ├── OG0002719.fa   
    └── OG0002724.fa
```
执行命令：
```bash
python BatchFastaToPam.py example/ali_fasta
```
即可输出对应的结果于文件夹 `pamlfile` 中：
```
pamlfile/
├── OG0002719.fa.pam   
└── OG0002724.fa.pam
```

### 2.11 `ReassignSequence.py [IN_FASTA_FILE_DIR] [MATRIX_FILE] [OUT_FASTA_FILE_DIR]`

**功能描述：** 将fasta文件中的序列按照要求分配到不同的fasta文件中。

- **IN_FASTA_FILE_DIR：** 文件夹路径名，在该目录下包含需要重新分配的fasta格式序列文件，可以是DNA、CDS、转录本、蛋白质或其他序列。
- **MATRIX_FILE：** 矩阵文件位置，制表符隔开，包含标题行！每一行的第一个项目是新分配后的文件名，其余位置是该文件中包含的序列名称。
- **OUT_FASTA_FILE_DIR：** 文件夹路径名，输出路径。

**使用场景：** ①单拷贝同源基因每个基因家族的序列提取过程中，将下载的CDS序列按照基因家族分组将CDS分别归属到新的不同的文件中，用于后续CDS和蛋白质序列的匹配，矩阵文件是Orthogroups/Orthogroups.tsv（MATRIX_FILE，可以参照示例文件example/seq_matrix2.txt），你只需要从NCBI下载每个物种的fna文件（重要：需要使用cut命令分列并保留第一列，使得每个序列的名称只包含ID号！）放置在同一文件夹中（IN_FASTA_FILE_DIR），然后指定输出文件就可以将不同物种的CDS文件分配到已基因家族名称命名的fasta文件中；②提取同一基因家族的基因进行合并分析。       

**注意事项：** 索引表格一定要包含标题行，可以是标准的同行数同列数的矩阵，但不强制要求。

**生成文件：** 
- `<OUT_FASTA_FILE_DIR参数>` (文件夹，其中包含重新分配后的序列)       

**示例：**

比如 `example/ali_fasta` 文件夹中包含需要重新分配的fasta文件：
```
example/
└── ali_fasta/
    ├── OG0002719.fa   
    └── OG0002724.fa
```
`example/seq_matrix.txt` 是对fasta文件所有序列指定分组，第一行内容不重要：
```
Orthogroup	A	B	C	
OG01	XP_010706234.2	XP_032302195.1	jirou002500.1	
OG02	NP_001026572.1	XP_038029232.1		
OG03	XP_032302195.1	XP_048781468.1		
OG04	jirou002516.1	XP_015134329.2	XP_035425170.1	XP_035170945.1
```
执行命令：
```bash
python ReassignSequence.py example/ali_fasta example/seq_matrix.txt out
``` 
即可从所有fasta文件中找到相应的序列提取到 `out` 的不同文件中：
```
out/
├── OG01.fna   
├── OG02.fna 
├── OG03.fna 
└── OG04.fna

#OG01
>XP_010706234.2	
...
>XP_032302195.1	
...
>jirou002500.1
...

#OG02
>NP_001026572.1	
...
>XP_038029232.1	
...

...
```

### 2.12 `BatchAlignedProteinToDNA.py [-h] [-c CODON] [-m MAPFILE] [-p PEP] [-C CDS] [-s SUFFIX_P] [-S SUFFIX_C]`

**功能描述：** 假如你有蛋白质的比对文件，想要得到对应CDS的密码子比对文件可以使用此脚本，简单来说是批量将比对过的蛋白质序列转换为DNA序列，通过本脚本可以过滤掉：①CDS系列长度不为3的倍数的序列；②CDS-蛋白序列不匹配的序列；③含有未知碱基N的序列。

**参数说明：** 

```bash
options:
  -h, --help            显示帮助信息
  -c CODON, --codon 密码子表文件，第一列为氨基酸单字母缩写，第二列是对应的密码子，示例文件中cod.txt为标准密码子表。
  -m MAPFILE, --mapfile 索引表文件，蛋白质序列名称及其对应的CDS序列名称表。第一列是蛋白质名称，第二列是对应CDS名称。
  -p PEP, --pep 包含所有蛋白质序列的目录，蛋白质系列需要是被比对过的。
  -C CDS, --cds 包含所有CDS序列的目录，推荐使用脚本2.11生成的。
  -s SUFFIX_P, --suffix_p 蛋白质序列的扩展名，即蛋白质序列文件最后的.后的内容，默认是fa。
  -S SUFFIX_C, --suffix_c CDS序列的扩展名，即CDS序列文件最后的.后的内容，默认是fna。
``` 

**使用场景：** 通过OrthoFinder软件对多个物种的同源基因家族进行搜索期间会在WorkingDirectory/Alignments_ids目录生成单拷贝正交基因蛋白序列的比对文件，从其中提取单拷贝正交基因家族（单拷贝基因家族列表在Orthogroups/Orthogroups_SingleCopyOrthologues.txt，可以使用for循环提取）存放到文件夹中（PEP参数），从NCBI等数据库下载CDS序列（CDS序列编号和蛋白序列编号是相同的），使用脚本2.11提取蛋白序列对应的CDS序列（未比对）存放到文件夹中（CDS参数），OrthoFinder结果文件中WorkingDirectory下的SequenceIDs.txt即为蛋白质名称-CDS名称对照表（MAPFILE参数）。

**注意事项：** 由软件自动生成的SequenceIDs.txt需要手动按照冒号和空格分列，删除多余的部分，详细可以查看示例文件。

**生成文件：** 
- `output`（文件夹，用于存放比对过的CDS序列，运行上述命令生成的文件参考example/output）。
- `err_cds.txt`（错误日志文件，显示过滤掉的序列，如果没有错误的序列将不生成）。

**示例：**

比如 `example` 文件夹中包含需要的文件：
```
```
example/
├── cod.txt
├── SequenceIDs.txt
├── cds/
│  ├── OG0002719.fna  
│  ├── ... 
│  └── OG0002837.fna
└── pep/
    ├── OG0002719.fa  
    ├── ... 
    └── OG0002837.fa

#cod.txt
A	GCG 
A	GCA 	
A	GCT 
...
Y	TAT 
Y	TAC 
*	TGA 
*	TAG
*	TAA

#SequenceIDs.txt
0_0	XP_010706234.2
1_7	XP_032302195.1
2_3	XP_021240136.1
3_3	XP_040400452.1
...
7_222	XP_027313668.2
8_291	NP_001025904.2
9_249	XP_048815064.1
10_2438	jirou002303.1
```
蛋白质序列后缀是.fa，CDS序列后缀是.fna，执行命令：
```bash
python BatchAlignedProteinToDNA.py -c example/cod.txt -m example/SequenceIDs.txt -p example/pep -C example/cds -s "fa" -S "fna"
```
即可得到CDS的比对文件存放在 `output` 的不同文件中：
```
output/
├── OG0002719.fa   
├── OG0002724.fa 
└── OG0002729.fa
```  
也会有部分序列存在问题，在 `err_cds.txt` 可以看到具体问题：
```
OG0002721.fa	Sequence mismatch
OG0002761.fa	There is N in the CDS.
OG0002837.fa	The CDS is not a multiple of 3.
```  

### 2.13 `Extract4DTv.py [-h] [-c CODON] [-m MAPFILE] [-p PEP] [-C CDS] [-s SUFFIX_P] [-S SUFFIX_C]`

**功能描述：** 批量提取蛋白质序列比对结果中的4DTv（四倍简并位点）。

**参数说明：** 所有参数均与脚本2.12一致，代码内容其实差不多，只是生成的文件名称不同。

```bash
options:
  -h, --help            显示帮助信息
  -c CODON, --codon 密码子表文件，第一列为氨基酸单字母缩写，第二列是对应的密码子，示例文件中cod.txt为标准密码子表。
  -m MAPFILE, --mapfile 索引表文件，蛋白质序列名称及其对应的CDS序列名称表。第一列是蛋白质名称，第二列是对应CDS名称。
  -p PEP, --pep 包含所有蛋白质序列的目录，蛋白质系列需要是被比对过的。
  -C CDS, --cds 包含所有CDS序列的目录，推荐使用脚本2.11生成的。
  -s SUFFIX_P, --suffix_p 蛋白质序列的扩展名，即蛋白质序列文件最后的.后的内容，默认是fa。
  -S SUFFIX_C, --suffix_c CDS序列的扩展名，即CDS序列文件最后的.后的内容，默认是fna。
``` 

**使用场景：** 同源基因建树。

**生成文件：** 
- `4dtv`（文件夹，用于存放提取到的4DTv位点，运行上述命令生成的文件参考example/4dtv）。 
- `err_4dtv.txt`（错误日志文件，显示过滤掉的序列，如果没有错误的序列将不生成）。

**示例：**

比如 `example` 文件夹中包含需要的文件：
```
```
example/
├── cod.txt
├── SequenceIDs.txt
├── cds/
│  ├── OG0002719.fna  
│  ├── ... 
│  └── OG0002837.fna
└── pep/
    ├── OG0002719.fa  
    ├── ... 
    └── OG0002837.fa

#cod.txt
A	GCG 
A	GCA 	
A	GCT 
...
Y	TAT 
Y	TAC 
*	TGA 
*	TAG
*	TAA

#SequenceIDs.txt
0_0	XP_010706234.2
1_7	XP_032302195.1
2_3	XP_021240136.1
3_3	XP_040400452.1
...
7_222	XP_027313668.2
8_291	NP_001025904.2
9_249	XP_048815064.1
10_2438	jirou002303.1
```  
蛋白质序列后缀是.fa，CDS序列后缀是.fna，执行命令：
```bash
python Extract4DTv.py -c example/cod.txt -m example/SequenceIDs.txt -p example/pep -C example/cds -s "fa" -S "fna"
``` 
即可提取到4DTv位点存放在 `4dtv` 的不同文件中：
```
4dtv/
├── OG0002719.fa   
├── OG0002724.fa 
└── OG0002729.fa
```  
也会有部分序列存在问题，在 `err_4dtv.txt` 可以看到具体问题：
```
OG0002721.fa	Sequence mismatch
OG0002761.fa	There is N in the CDS.
OG0002837.fa	The CDS is not a multiple of 3.
```  

### 2.14 `MergeSequences.py [MATRIX_FILE] [FASTA_FILE_DIR] [SUFFIX] [ORDER_LIST（可选参数）]`

**功能描述：** 进阶版合并序列脚本。

- **MATRIX_FILE：** 矩阵文件位置，制表符隔开，包含标题行！每一列是一个样品，每一行的第一个项目是对应的序列名称（fasta文件名,不包含后缀），行和列可以确定每个样品对应序列的序列名称。
- **FASTA_FILE_DIR：** 文件夹路径名，在该目录下包含需要合并的fasta格式的比对文件，文件名没有要求，只要包含MATRIX_FILE中所有序列名即可。
- **ORDER_LIST：** 指定连接顺序，通过指定连接顺序既可以排除某个序列，也可以指定连接顺序，如果不指定则默认按照序列名称的哈希值为序全部连接。

**注意事项：** 文件夹中不能包含未比对的序列文件，可能会发生连接错误！

**生成文件：** 
- `<FASTA_FILE_DIR的名称>.fasta` （FASTA文件，每个序列名称为第一行的样品名称）。 
- `order.true` （实际合并顺序）。

**示例：**

比如 `example` 文件夹中包含需要的文件：
```
```
example/
├── seq_matrix.txt
├── order.txt
└── 4dtv/
    ├── OG0002719.fa  
    ├── OG0002724.fa
    └── OG0002729.fa

#seq_matrix.txt
Orthogroup	s1	s2	s3	s4	s5	...
OG0002719	XP_010706234.2	XP_032302195.1	XP_021240136.1	XP_040400452.1	XP_032063692.1	...
OG0002724	XP_010727090.1	XP_015706975.1	XP_021239881.1	XP_040400939.1	XP_032038059.1	...
OG0002729	XP_010706070.1	XP_015712434.1	XP_021239916.1	XP_040401487.1	XP_032053636.1	...

#order.txt
OG0002729
OG0002724
```  
执行命令： 
```bash
# 运行下列代码将不指定顺序全连接：
python MergeSequences.py example/seq_matrix.txt example/4dtv

#若指定连接顺序运行下列代码：
python MergeSequences.py example/seq_matrix.txt example/4dtv example/order.txt
``` 
即可生成合并后序列文件和实际合并顺序文件，其中合并后的序列文件：
```
>s1
...
>s2
...
``` 

### 2.15 `BatchGenerationCodeML_CTL.py [PAML_FILE_DIR] [TREE_FILE]`

**功能描述：** 批量生成CodeML的配置文件。

- **PAML_FILE_DIR：** PAML格式的比对文件所在目录，在运行本脚本时要求目录中必须含有需要进行选择压力分析的比对文件，并且尽量不使用相对路径，否则将无法读取需要比对文件路径。
- **TREE_FILE：** 树文件路径（相对于CodeML运行时的路径），不要求在本脚本运行时该文件存在，但是务必要保证在运行CodeML程序时程序可以读取到该路径。

**注意事项：** 本脚本只是生成配置文件，请务必注意脚本导入树文件路径并不是CodeML程序运行时树文件路径！配置文件模板选择的是Branch model模型，如果有其他需求可以直接修改配置文件。

**生成文件：** 
- `codemlnull` （文件夹，基于无效假设的配置文件） 。 
- `codeml2`（文件夹，基于替代假设的配置文件） 。

**示例：**

比如 `example` 文件夹中包含需要的文件夹 `paml_file`：
```
example/
└── paml_file/
    ├── OG0005572.fa.nuc  
    ├── OG0005964.fa.nuc
    ├── OG0008612.fa.nuc
    └── OG0010932.fa.nuc

#OG0005572.fa.nuc
11	201
s0  
ATGATCATCCCGGTCAGGTGTTTCACGTGCGGCAAAATCGTCGGA...
s1  
ATGATCATCCCGGTGCGATGCTTCACGTGCGGCAAGATCGTGGGC...
...
s10  
ATGATCATCCCGGTCAGGTGCTTCACGTGCGGCAAAATCGTTGGA...
```  
执行命令： 
```bash
python BatchGenerationCodeML_CTL.py example/paml_file "./out/a.tree"
```
注意"./out/a.tree"并不是本脚本需要的文件，而是需要写入到配置文件时树的路径生成以下文件夹：
```
#基于无效假设的配置文件
codemlnull/
├── OG0005572.fa.nuc.ctl  
├── OG0005964.fa.nuc.ctl
├── OG0008612.fa.nuc.ctl
└── OG0010932.fa.nuc.ctl

#基于替代假设的配置文件
codeml2/
├── OG0005572.fa.nuc.ctl  
├── OG0005964.fa.nuc.ctl
├── OG0008612.fa.nuc.ctl
└── OG0010932.fa.nuc.ctl

#举个例子，基于无效假设的配置文件：OG0005572.fa.nuc.ctl

      seqfile = ../example/paml_file/OG0005572.fa.nuc  * sequence data filename
     treefile = ./out/a.tree  * tree file name

      outfile = ./output0/OG0005572.fa.nuc/abc.txt           * main result file name
   
        noisy = 9  * 0,1,2,3,9: how much rubbish on the screen
      verbose = 2  * 0: concise; 1: detailed, 2: too much
      runmode = 0  * 0: user tree;  1: semi-automatic;  2: automatic
                   * 3: StepwiseAddition; (4,5):PerturbationNNI; -2: pairwise

      seqtype = 1  * 1:codons; 2:AAs; 3:codons-->AAs
    CodonFreq = 2 * 0 : 1/61 each, 1:F1X4, 2:F3X4, 3:codon table
                   * 4:F1x4MG, 5:F3x4MG, 6:FMutSel0, 7:FMutSel
        model = 0
                   * models for codons:
                      * 0:one, 1:b, 2:2 or more dN/dS ratios for branches, 6:FromCodon
                   * models for AAs or codon-translated AAs:
                      * 0:poisson, 1:proportional, 2:Empirical, 3:Empirical+F
                      * 6:FromCodon, 7:AAClasses, 8:REVaa_0, 9:REVaa(nr=189)

      NSsites = 0 * 23 24 25 26   * 23 24 25 26 * 0:one w; 1:NearlyNeutral; 2:PositiveSelection; 3:discrete;
                   * 4:freqs; 5:gamma; 6:2gamma; 7:beta; 8:beta&w+; 9:beta&gamma;
                   * 10:beta&gamma+1; 11:beta&normal>1; 12:0&2normal>1;
                   * 13:3normal>0; 
                   * 22:M2a_Old(M2a_rel); 
                   * 23:Tgamma; 24:Tinvgamma; 25:Tgamma+1; 26:Tinvgamma+1.

        clock = 0  * 0:no clock, 1:global clock; 2:local clock
       aaDist = 0  * 0:equal, +:geometric; -:linear, 1-6:G1974,Miyata,c,p,v,a
   aaRatefile = ../dat/wag.dat * for aa seqs under model = 3 (empirical+F)
                   * dayhoff.dat, jones.dat, wag.dat, mtmam.dat, or your own

    fix_kappa = 0  * 1: kappa fixed, 0: kappa to be estimated
        kappa = 3  * initial or fixed kappa
    fix_omega = 0  * 1: omega or omega_1 fixed, 0: estimate
        omega = 1  * initial or fIf yoixed omega, for codons or codon-based AAs

    fix_alpha = 1  * 0: estimate gamma shape parameter; 1: fix it at alpha
        alpha = 0. * initial or fixed alpha, 0:infinity (constant rate)
       Malpha = 0  * different alphas for genes
        ncatG = 10  * # of categories in dG of NSsites models

        getSE = 0  * 0: don't want them, 1: want S.E.s of estimates
 RateAncestor = 0  * (0,1,2): rates (alpha>0) or ancestral states (1 or 2)
   Small_Diff = 1e-8
*    cleandata = 1  * remove sites with ambiguity data (1:yes, 0:no)?
*  fix_blength = 1  * 0: ignore, -1: random, 1: initial, 2: fixed
*       method = 0  * Optimization method 0: simultaneous; 1: one branch a time

* Genetic codes: 0:universal, 1:mammalian mt., 2:yeast mt., 3:mold mt.,
* 4: invertebrate mt., 5: ciliate nuclear, 6: echinoderm mt., 
* 7: euplotid mt., 8: alternative yeast nu. 9: ascidian mt., 
* 10: blepharisma nu., 11: Yang's regularized code 
* These codes correspond to transl_table 1 to 11 of GenBank.
```  

### 2.16 `ParsingCodeMLResults.py [MOD0_DIR] [MOD2_DIR] `

**功能描述：** 批量解析CodeML结果，如果以2.15生成的脚本运行CodeML，结果会生成在m0和m2文件夹中。

- **MOD0_DIR：** 基于无效假设生成的结果。
- **MOD2_DIR：** 基于替代假设生成的结果。

**生成文件：** 
- `result.txt` （表格，可能需要手动整理） 。

**示例：**

比如 `example/codeml` 文件夹中包含两种假设下的CodeML结果：
```
example/
└── codeml/
        ├── m0/
        │     ├── OG0002719_m0.txt  
        │     ├── OG0002724_m0.txt
        │     └── OG0002729_m0.txt
        └── m2/
               ├── OG0002719_m2.txt  
               ├── OG0002724_m2.txt
               └── OG0002729_m2.txt
```  
执行命令： 
```bash
python ParsingCodeMLResults.py example/codeml/m0 example/codeml/m2
```
即可生成结果文件 `result.txt` ：
```
path	flag	ntime	np	lnL	omega
example/codeml/m0/OG0002719_m0.txt	null	20	22	-5245.294651	0.23258
example/codeml/m0/OG0002724_m0.txt	null	20	22	-6740.507258	0.04957
example/codeml/m0/OG0002729_m0.txt	null	20	22	-3588.001403	0.07700
example/codeml/m2/OG0002719_m2.txt	m2	20	23	-5237.515508	0.18756 0.61602
example/codeml/m2/OG0002724_m2.txt	m2	20	23	-6753.685334	0.03988 0.06959
example/codeml/m2/OG0002729_m2.txt	m2	20	23	-3584.953121	0.08111 0.00010
```   

> ## 比较基因组学-同源基因建树和选择压力分析流程（一）          
> 在比较基因组学分析中对同源基因进行扫描后需要进行4DTv或建树分析，提取4DTv位点的过程可以使用2.11、2.13和2.14脚本。除此之外还会使用PAML软件包的CodeML程序对筛选出的单拷贝基因进行选择压力分析，首先需要使用2.10将2.12得到的文件进行格式转化，然后需要配置ctl文件，比较繁琐可以使用脚本2.15批量生成配置文件，然后使用循环批量运行程序，程序运行完成后使用脚本2.16解析结果，将m0和m2的结果对应起来，得到lnL0、lnL2，（lnL2-lnL0）×2的绝对值服从自由度np2-np0自由度的卡方分布，使用excel的CHISQ.DIST.RT函数可以得到显著性。         

### 2.17 `SplitAXT.py [AXT_FILE]`
     
**功能描述：** 将单个AXT格式文件拆分为多个AXT文件，使得每个文件中只包含一对序列比对。

- **AXT_FILE：** 需要拆分的AXT文件。

**使用场景：** 脚本2.12生成的密码子比对文件后，如果需要进一步进行4dtv分析，需要使用摘抄代码convert_fasta_to_axt.pl（做了适应性修改）将其转换为AXT文件，本脚本可以把上述代码生成的AXT文件按照序列对进行拆分。

**注意事项：** 本脚本只支持序列对名称中含有数字的AXT文件。

**生成文件：** 
- `<序列对>.axt-split`（多个axt文件） 。

**示例：**

比如 `example/test.axt` 文件是需要拆分的AXT文件，内容为：
```
5_13054-1_13901
------ ... CTGCAAAGAAGGAT
------ ... CCGCAAAGAAGGAC

5_13054-8_15414
------ ... CTGCAAAGAAGGAT
------ ... CTGCAAAGAAGGAT
```  
执行命令： 
```bash
python SplitAXT.py example/test.axt
          
# 有时你也许需要批处理。
for i in `ls *axt`;do python SplitAXT.py $i ;done
```
示例中会生成两个文件：
```
#5_13054-1_13901.axt-split
------ ... CTGCAAAGAAGGAT
------ ... CCGCAAAGAAGGAC

#5_13054-8_15414.axt-split
------ ... CTGCAAAGAAGGAT
------ ... CTGCAAAGAAGGAT
```  

> ## 比较基因组学-同源基因建树和选择压力分析流程（二）          
> 你可以参考 https://yanzhongsino.github.io/2022/09/07/bioinfo_Ks_batch.calculation.Ks 来计算 Ka、Ks和4dtv值，由于calculate_4DTV_correction.pl脚本只支持一对序列的4dtv计算，因此可以使用脚本2.17对AXT文件进行拆分。                 

### 2.18 `BaseSiteInformation.py [GFF_FILE] [Q_FILE]`

**功能描述：** 根据指定染色体位置及碱基位点信息，抽取相应的基因数据，比如位点在哪一个转录本上的哪一个CDS区间中，以及CDS或转录本的位置信息，方便后续注释分析。

- **GFF_FILE：** 基因组GFF文件，只需要保留mRNA和CDS特征，并且每个mRNA需要位于其包含CDS特征的上方，可以选择在运行代码前手动将GFF文件排序！
- **Q_FILE：** 查找的条目表格，需要包括标题行，至少包含两列：第一列必须是染色体编号，第二列是对应于染色体上的位置。

**使用场景：** 有进阶版本在2.22和2.23，通过随机森林等算法找到不同种群或不同品种的变异位点，需要定位到该位点所在基因。

**生成文件：** 
- `out_<Q_FILE参数值>.xls`（表格，第一、四列为基因名称，第二列是是否为CDS区域CDS/noCDS，第三列为CDS的起始终止位置以及ORF起始位点，第五列是染色体ID，然后是基因起始位置、得分以及基因CDS数目） 。

**示例：**

比如 `example` 文件夹中包含两个文件：
```
example/
├── genome.gene.gff   
└── base_loc.txt

#genome.gene.gff
chr6	mod	mRNA	61479002	61483066	0.999299	-	.	ID=shibie_GLEAN_10005360;
chr6	mod	CDS	61482857	61483066	.	-	0	Parent=shibie_GLEAN_10005360;
chr6	mod	CDS	61480913	61481015	.	-	0	Parent=shibie_GLEAN_10005360;
chr6	mod	CDS	61480545	61480595	.	-	2	Parent=shibie_GLEAN_10005360;
chr6	mod	CDS	61479002	61480122	.	-	2	Parent=shibie_GLEAN_10005360;
...
unplaced_scaffold9	mod	CDS	9320	9504	.	-	0	Parent=shibie_GLEAN_10000001;
unplaced_scaffold9	mod	CDS	7041	7117	.	-	1	Parent=shibie_GLEAN_10000001;
unplaced_scaffold9	mod	CDS	6377	6435	.	-	2	Parent=shibie_GLEAN_10000001;
unplaced_scaffold9	mod	CDS	4737	5270	.	-	0	Parent=shibie_GLEAN_10000001;

#base_loc.txt
CHROM	POS	IncMSE(Importance)	IncNodePurity	CHROM	POS	REF	ALT	BYQ10	BYQ3
chr6	1508314	-1.134209981	229.6628618	chr6	1508314	A	T	W	W
chr6	2238474	1.503310682	85.34757716	chr6	2238474	G	C	G	G
chr6	2692990	0.23640024	195.3846105	chr6	2692990	G	A	R	R
chr6	2914183	-0.436014622	115.9339111	chr6	2914183	C	A	C	M
chr6	3013236	0.922900751	815.7366022	chr6	3013236	T	C	T	T
...
chr8	51046810	1.229196235	487.9762709	chr8	51046810	C	T	C	C
chr8	51530461	1.487830764	1463.658822	chr8	51530461	C	T	C	C
chr8	53281836	1.090568252	684.2414242	chr8	53281836	C	A	C	C
chr8	53557595	0.954201007	510.2543934	chr8	53557595	T	G	T	T
```  
执行命令： 
```bash
python BaseSiteInformation.py example/genome.gene.gff example/base_loc.txt
```
即可生成结果文件 `out_base_loc.txt.xls` ：
```
gene_name	CDS/noCDS	CDS(start,end,codon start pos)	gene	ChrID	gene_start_pos	gene_end_pos	score	CDS_num	CHROM	POS	IncMSE(Importance)	IncNodePurity	CHROM	POS	REF	ALT	BYQ10	BYQ3
shibie_GLEAN_10003636	noCDS	-	shibie_GLEAN_10003636	chr6	1479415	1511307	0.99885	21	chr6	1508314	-1.134209981	229.6628618	chr6	1508314	A	T	W	W
shibie_GLEAN_10003659	CDS	(2238236, 2238538, '2')	shibie_GLEAN_10003659	chr6	2227463	2239321	0.999821	7	chr6	2238474	1.503310682	85.34757716	chr6	2238474	G	C	G	G
-	-	-	-	-	-	-	-	-	chr6	2692990	0.23640024	195.3846105	chr6	2692990	G	A	R	R
...
shibie_GLEAN_10001336	noCDS	-	shibie_GLEAN_10001336	chr8	51009683	51060709	0.998932	23	chr8	51046810	1.229196235	487.9762709	chr8	51046810	C	T	C	C
-	-	-	-	-	-	-	-	-	chr8	51530461	1.487830764	1463.658822	chr8	51530461	C	T	C	C
shibie_GLEAN_10001391	noCDS	-	shibie_GLEAN_10001391	chr8	53278535	53293780	0.847545	8	chr8	53281836	1.090568252	684.2414242	chr8	53281836	C	A	C	C
shibie_GLEAN_10001401	noCDS	-	shibie_GLEAN_10001401	chr8	53548014	53561536	0.9986	10	chr8	53557595	0.954201007	510.2543934	chr8	53557595	T	G	T	T
```   

### 2.19 `MaskSeq.py [FASTA_FILE] [TABLE_FILE] [TARG 可选参数]`
       
***待优化！***

**功能描述：** 对Fasta文件中的某些区间进行屏蔽（替换为TARG）。

- **FASTA_FILE：** Fasta文件，里边包含许多序列，对于基因组来说其中包括许多染色体序列，>后边的内容为序列名称。                        
- **TABLE_FILE：** 三列表格，不需要包括标题行，第一列是序列名称（注意和fasta文件名称完全一致），第二、三列分别是屏蔽起始和终止位置（从1开始计数，可以从gff文件中直接复制）。            
- **TARG：** 屏蔽字符，将指定部分碱基替换为该字符，默认是将指定位置的碱基替换为N，你也可以指定替换的字符。
   
**使用场景：** 基因组分析中对基因组的一些序列（比如重复序列）进行屏蔽（ mask）以节约分析过程的算力。

**注意事项：** TARG参数只能为单一字符。

**生成文件：** 
- `maskseq_<FASTA_FILE>` （屏蔽部分序列的FASTA文件） 。    

**示例：**

比如 `example` 文件夹中包含两个文件：
```
example/
├── Chr.fa   
└── masktbl.txt

#Chr.fa
>Chr1
ATCGGCATATATCTTATTATATTTCCCCAAA
>Chr2
ATCGGCATATATCTTATTATATTTCCCCAAA
TTCCATCA
>MT
ATCGGCATATATCTTATTATATTTCCCCAAA

#masktbl.txt
Chr1	2	8
Chr2	1	5
Chr2	7	10
Chr3	10	20
```  
执行命令： 
```bash
# 默认替换为N。
python MaskSeq.py example/Chr.fa example/masktbl.txt

# 替换为?。
python MaskSeq.py example/Chr.fa example/masktbl.txt "?"
```
即可完成片段屏蔽：
```
#默认替换为N
>Chr1
ANNNNNNNATATCTTATTATATTTCCCCAAA
>Chr2
NNNNNCNNNNATCTTATTATATTTCCCCAAATTCCATCA
>MT
ATCGGCATATATCTTATTATATTTCCCCAAA

#替换为?
>Chr1
A???????ATATCTTATTATATTTCCCCAAA
>Chr2
?????C????ATCTTATTATATTTCCCCAAATTCCATCA
>MT
ATCGGCATATATCTTATTATATTTCCCCAAA
```  

### 2.20 `BaseCompositionCalculation.py [FASTA_FILE] [TER_CODE 可选参数]`
       
**功能描述：** 计算CDS序列中各个序列的各个位点的碱基数目，如A1、T1、G1、G3等。

- **FASTA_FILE：** Fasta文件，里边包含许多序列，要求是核酸序列。
- **TER_CODE：** 终止密码子列表，默认是标准密码子表的TAG,TAA,TGA，如果需要指定，需要保证每个终止密码子之间用半角英文逗号隔开且不含有过多空白，如果你希望统计到终止密码子你可以输入NNN。

**使用场景：** 进行密码子偏好分析时需要获取GC12和GC3等参数可以通过本脚本结果进一步计算。          

**生成文件：** 
- `BaseComposition.txt`（表格文件，包括各个位点的碱基数目，最后一列是碱基总数） 。

**示例：**

比如 `example/base_cds.fa` 文件是包括全部CDS序列的fasta文件：
```
>1
AAAATAG
>2
ATTATTTAG
>3
ATCGATCGATCGTAG
```  
执行命令： 
```bash
# 默认去除标准终止密码：
python BaseCompositionCalculation.py example/base_cds.fa

# 希望统计到终止密码：
python BaseCompositionCalculation.py example/base_cds.fa NNN

# 自定义终止密码：
python BaseCompositionCalculation.py example/base_cds.fa TGA,TAA
```
即可完成统计：
```
#默认去除标准终止密码：
name	A1	T1	G1	C1	A2	T2	G2	C2	A3	T3	G3	C3	all
1	-	-	-	-	-	-	-	-	-	-	-	-	-
2	2	0	0	0	0	2	0	0	0	2	0	0	6	
3	1	1	1	1	1	1	1	1	1	1	1	1	12	

#希望统计到终止密码：
name	A1	T1	G1	C1	A2	T2	G2	C2	A3	T3	G3	C3	all
1	-	-	-	-	-	-	-	-	-	-	-	-	-
2	2	1	0	0	1	2	0	0	0	2	1	0	9	
3	1	2	1	1	2	1	1	1	1	1	2	1	15	

#自定义终止密码：
name	A1	T1	G1	C1	A2	T2	G2	C2	A3	T3	G3	C3	all
1	-	-	-	-	-	-	-	-	-	-	-	-	-
2	2	1	0	0	1	2	0	0	0	2	1	0	9	
3	1	2	1	1	2	1	1	1	1	1	2	1	15	
```  

### 2.21 `GFFSimplifier.py [GFF_FILE] [ITEM_1 可选参数] [ITEM_2 可选参数] ... [ITEM_n 可选参数]`
       
**功能描述：** 简化GFF文件的attributes的内容，过滤不关注的信息，以减少GFF文件大小。

- **GFF_FILE：** GFF文件路径，需要是GFF3格式的文件，attributes需要以”;“分隔，键和值之间以”=“连接。
- **ITEM_X：** 需要保留的attributes key，其中ID和Parent由于常用无需指定，不同的key作为不同参数输入。 

**使用场景：** 进行GFF文件部分信息的简化可以减小文件大小，为后续分析提供便利。             

**注意事项：** ID和Parent无需指定，不要重复指定项目，否则生成的文件会有重复的内容。          

**生成文件：** 
- `simp_<GFF_FILE>`（GFF文件，简化后的文件） 。

**示例：**

比如 `example/maize.gff3` 文件是玉米参考基因组B73 RefGen_v4的GFF文件部分内容：
```
###
3	gramene	gene	125560575	125561600	.	-	.	ID=gene:Zm00001d041518
3	gramene	mRNA	125560575	125561600	.	-	.	ID=transcript:Zm00001d041518_T001;Parent=gene:Zm00001d041518
3	gramene	exon	125560575	125561600	.	-	.	Parent=transcript:Zm00001d041518_T001
3	gramene	CDS	125560575	125561600	.	-	0	ID=CDS:Zm00001d041518_P001;Parent=transcript:Zm00001d041518_T001
###
...
NC_024460.2	RefSeq	CDS	40178	41023	.	-	0	ID=cds-ONM11916.1;Parent=rna-gnl|WGS:LPUQ|mrna.ZEAMMB73_Zm00001d001763;Dbxref=NCBI_GP:ONM11916.1;Name=ONM11916.1;gbkey=CDS;locus_tag=ZEAMMB73_Zm00001d001763;orig_transcript_id=gnl|WGS:LPUQ|mrna.ZEAMMB73_Zm00001d001763;product=putative methyltransferase;protein_id=ONM11916.1
NC_024460.2	RefSeq	gene	99801	117243	.	-	.	ID=gene-ZEAMMB73_Zm00001d001765;Name=ZEAMMB73_Zm00001d001765;gbkey=Gene;gene_biotype=protein_coding;locus_tag=ZEAMMB73_Zm00001d001765;old_locus_tag=GRMZM2G046590%2CGRMZM2G074530
```  
内容是为了测试截取的片段，应该和实际下载的不太一致，但无伤大雅，执行命令： 
```bash
# 只保留ID和Parent：
python GFFSimplifier.py example/maize.gff3
 
# 还希望保留chromosome： 
python GFFSimplifier.py example/maize.gff3 chromosome  

# 希望保留chromosome、country、ID和Parent： 
python GFFSimplifier.py example/maize.gff3 chromosome country  
```  
即可完成简化：
```
#只保留ID和Parent
#Simplified by https://github.com/shueho/BioDataTools.
###
3	gramene	gene	125560575	125561600	.	-	.	ID=gene:Zm00001d041518
3	gramene	mRNA	125560575	125561600	.	-	.	ID=transcript:Zm00001d041518_T001;Parent=gene:Zm00001d041518
3	gramene	exon	125560575	125561600	.	-	.	Parent=transcript:Zm00001d041518_T001
3	gramene	CDS	125560575	125561600	.	-	0	ID=CDS:Zm00001d041518_P001;Parent=transcript:Zm00001d041518_T001
###   
...
NC_024460.2	RefSeq	CDS	40178	41023	.	-	0	ID=cds-ONM11916.1;Parent=rna-gnl|WGS:LPUQ|mrna.ZEAMMB73_Zm00001d001763
NC_024460.2	RefSeq	gene	99801	117243	.	-	.	ID=gene-ZEAMMB73_Zm00001d001765

#还希望保留chromosome：
...

#希望保留chromosome、country、ID和Parent：
...
```  

### 2.22 `BaseSiteFeatureFinder.py [GFF_FILE] [LOC_FILE] [DISTANCE] [FEATURE (可选参数)]`
       
**功能描述：** 批量获取碱基附件的特征。

- **GFF_FILE：** GFF文件路径，需要是GFF3格式的文件，attributes需要以”;“分隔。  
- **LOC_FILE：** 描述位点位置的表格，需要有三列：位点名称/染色体名称/在染色体上的位置。注意：不能有标题行，染色体名称需要和GFF文件严格照应。   
- **DISTANCE：** 以碱基位点开始，向外扩展的距离。如果是0则代表搜索该碱基是否位于某一特征，此时是代码2.18的替代。  
- **FEATURE：** 需要扫描的特征，默认是”gene“，可以选择输入”gene/mRNA/CDS/exon/...“中的其中之一，也可以是其他类型的特征，详见GFF文件。  

**使用场景：** GWAS分析或其他分析得到显著关联SNP位点后搜索候选基因。             

**注意事项：** FEATURE不填写默认扫描基因，如果是”mRNA“则扫描转录本，切记单词不要拼错。          

**生成文件：** 
- `dis_<DISTANCE>_<FEATURE>_<LOC_FILE>`（表格，各列分别表示：位点名称/染色体/位置/基因名称/位点与特征起始的距离/位点与特征结束的距离/基因与位点区间的关系，关系包括Left、Right、To_include和Be_include，分别表示基因在区间左侧、基因在区间右侧、基因覆盖区间以及区间覆盖基因） 。

**示例：**

比如 `example/maize.gff3` 文件是玉米参考基因组B73 RefGen_v4的GFF文件部分内容同2.21，`example/base_loc.txt` 包含关注的位点信息：
```
S1_4399947	1	4399947
S1_4399947	1	4399947
S1_44365387	1	44365387
S3_115984758	3	115984758
S3_125574288	3	125574288
S3_125574288	3	125574288
```  
位点信息第一列为位点名称，只需设定唯一值即可，随后可以执行：
```bash
# 获取显著位点14000距离gene：
python BaseSiteFeatureFinder.py example/maize.gff3 example/base_loc.txt 14000    
 
# 获取显著位点14000距离mRNA： 
python BaseSiteFeatureFinder.py example/maize.gff3 example/base_loc.txt 14000 mRNA  

# 判断位点是否在基因上： 
python BaseSiteFeatureFinder.py example/maize.gff3 example/base_loc.txt 0  

# 判断位点是否在CDS上： 
python BaseSiteFeatureFinder.py example/maize.gff3 example/base_loc.txt 0 CDS  
```
即可生成结果文件：
```
#获取显著位点14000距离gene：dis_14000_gene_base_loc.txt
site_name	site_chr	site_pos	gene_name	star_dis	end_dis	position
S1_4399947	1	4399947	gene:Zm00001d027399	-2365	-4493	Be_include
S1_4399947	1	4399947	gene:Zm00001d027399	-2365	-4493	Be_include
S1_44365387	1	44365387	,-	-	-	-
S3_115984758	3	115984758	,-	-	-	-
S3_125574288	3	125574288	gene:Zm00001d041518	13713	12688	Be_include
S3_125574288	3	125574288	gene:Zm00001d041519	10670	10005	Be_include
S3_125574288	3	125574288	gene:Zm00001d041518	13713	12688	Be_include
S3_125574288	3	125574288	gene:Zm00001d041519	10670	10005	Be_include 

#获取显著位点14000距离mRNA：dis_14000_mRNA_base_loc.txt
site_name	site_chr	site_pos	gene_name	star_dis	end_dis	position
S1_4399947	1	4399947	transcript:Zm00001d027399_T001	-2365	-4493	Be_include
S1_4399947	1	4399947	transcript:Zm00001d027399_T002	-2716	-4493	Be_include
S1_4399947	1	4399947	transcript:Zm00001d027399_T003	-2720	-4383	Be_include
S1_4399947	1	4399947	transcript:Zm00001d027399_T001	-2365	-4493	Be_include
S1_4399947	1	4399947	transcript:Zm00001d027399_T002	-2716	-4493	Be_include
S1_4399947	1	4399947	transcript:Zm00001d027399_T003	-2720	-4383	Be_include
S1_44365387	1	44365387	,-	-	-	-
S3_115984758	3	115984758	,-	-	-	-
S3_125574288	3	125574288	transcript:Zm00001d041518_T001	13713	12688	Be_include
S3_125574288	3	125574288	transcript:Zm00001d041519_T001	10670	10005	Be_include
S3_125574288	3	125574288	transcript:Zm00001d041518_T001	13713	12688	Be_include
S3_125574288	3	125574288	transcript:Zm00001d041519_T001	10670	10005	Be_include 

#判断位点是否在基因上： dis_0_gene_base_loc.txt
site_name	site_chr	site_pos	gene_name	star_dis	end_dis	position
S1_4399947	1	4399947	,-	-	-	-
S1_4399947	1	4399947	,-	-	-	-
S1_44365387	1	44365387	,-	-	-	-
S3_115984758	3	115984758	,-	-	-	-
S3_125574288	3	125574288	,-	-	-	-
S3_125574288	3	125574288	,-	-	-	-

#判断位点是否在CDS上： dis_0_CDS_base_loc.txt
site_name	site_chr	site_pos	gene_name	star_dis	end_dis	position
S1_4399947	1	4399947	,-	-	-	-
S1_4399947	1	4399947	,-	-	-	-
S1_44365387	1	44365387	,-	-	-	-
S3_115984758	3	115984758	,-	-	-	-
S3_125574288	3	125574288	,-	-	-	-
S3_125574288	3	125574288	,-	-	-	-
```

### 2.23 `IntervalFeatureFinder.py [GFF_FILE] [LOC_FILE] [FEATURE (可选参数)]`
       
**功能描述：** 批量获取指定区间内的特征。

- **GFF_FILE：** GFF文件路径，需要是GFF3格式的文件，attributes需要以”;“分隔。  
- **LOC_FILE：** 描述区间位置的表格，需要有四列：位点名称/染色体名称/在染色体上的起始位置/终止位置。注意：不能有标题行，染色体名称需要和GFF文件严格照应。   
- **FEATURE：** 需要扫描的特征，默认是”gene“，可以选择输入”gene/mRNA/CDS/exon/...“中的其中之一，也可以是其他类型的特征，详见GFF文件。  

**使用场景：** QTL定位或其他分析得到显著关联QTL区域后后搜索候选基因。可以认为是2.18和2.22的进阶版本，当输入位置表格第3、4列相同等同于2.18的实现，当输入表格区间长度相等等同于2.22的实现。             

**注意事项：** FEATURE不填写默认扫描基因，如果是”mRNA“则扫描转录本，切记单词不要拼错。          

**生成文件：** 
- `Inter_<FEATURE>_<LOC_FILE>`（表格，各列分别表示：位点名称/染色体/区间起始位置/区间终止位置/基因名称/特征起始位置/特征结束位置/基因与位点区间的关系，关系包括Left、Right、To_include和Be_include，分别表示基因在区间左侧、基因在区间右侧、基因覆盖区间以及区间覆盖基因） 。

**示例：**

比如 `example/maize.gff3` 文件是玉米参考基因组B73 RefGen_v4的GFF文件部分内容同2.21，`example/base_loc.txt` 包含关注的区间信息：
```
a	1	4385947	4413947
b	1	4399947	4399947
c	1	44351387	44379387
d	3	115970758	115998758
e	3	125560288	125588288
f	3	125574288	125574288
```  
区间信息第一列为区间名称，只需设定唯一值即可，随后可以执行：
```bash
# 获取区间内gene：
python IntervalFeatureFinder.py example/maize.gff3 example/base_loc.txt    
 
# 获取区间内mRNA： 
python IntervalFeatureFinder.py example/maize.gff3 example/base_loc.txt mRNA  
``` 
即可生成结果文件： 
```
#获取区间内gene：Inter_gene_base_loc.txt
site_name	site_chr	site_s	site_e	gene_name	gene_s	gene_e	position
a	1	4385947	4413947	gene:Zm00001d027399	4402312	4404440	Be_include
b	1	4399947	4399947	,-	-	-	-
c	1	44351387	44379387	,-	-	-	-
d	3	115970758	115998758	,-	-	-	-
e	3	125560288	125588288	gene:Zm00001d041518	125560575	125561600	Be_include
e	3	125560288	125588288	gene:Zm00001d041519	125563618	125564283	Be_include
f	3	125574288	125574288	,-	-	-	-
 
#获取区间内mRNA：Inter_mRNA_base_loc.txt 
site_name	site_chr	site_s	site_e	gene_name	mRNA_s	mRNA_e	position
a	1	4385947	4413947	transcript:Zm00001d027399_T001	4402312	4404440	Be_include
a	1	4385947	4413947	transcript:Zm00001d027399_T002	4402663	4404440	Be_include
a	1	4385947	4413947	transcript:Zm00001d027399_T003	4402667	4404330	Be_include
b	1	4399947	4399947	,-	-	-	-
c	1	44351387	44379387	,-	-	-	-
d	3	115970758	115998758	,-	-	-	-
e	3	125560288	125588288	transcript:Zm00001d041518_T001	125560575	125561600	Be_include
e	3	125560288	125588288	transcript:Zm00001d041519_T001	125563618	125564283	Be_include
f	3	125574288	125574288	,-	-	-	-
``` 

### 2.24 `ExtractFastaWithGene.py [FASTA_FILE] [LIST_FILE]`

**功能描述：** 依据提供的基因ID列表，该脚本能从全FASTA文件中抽取出基因对应的全部转录本/蛋白质/cdna序列，生成子FASTA文件。    

- **FASTA_FILE：** Fasta格式的序列文件，也就是包括所有序列的文件，比如全基因组的pep或者cdna序列。
- **LIST_FILE：** 需要提取的基因列表，比如基因：G001，可以提取所有以G001_开头的序列。

**使用场景：** 已知基因列表，想要获取每个基因全部的转录本/蛋白质/cdna序列。

**生成文件：** 
- `out_match_seq.fasta`（FASTA文件）。

**示例：**

比如 `example/pro.fasta` 是完整的蛋白质FASTA文件：
```
>Zm00001eb423440_P001
MPNGGGKRWLLLLPLSRYVEVDEQQGVQLFYYFVRSERDPYEDPLLLWLSGGPGCSGISG...
>Zm00001eb423440_P004
MPNGGGKRWLLLLPLSRWVLLLGSLQLPAVGGSGHVVTRMRGFDGPLPFYLETGYVEVDE...
...
>Zm00001eb400040_P001
MASLCMFTISSTPHVPQGCRRRCSDAVSSRPRSYLVCQSHLPSGPPASGGGGGGGGEEKT...
``` 
`example/list.txt` 是提取的基因列表：
```
Zm00001eb423440
Zm00001eb413340
``` 
执行命令：
```bash
python ExtractFastaWithGene.py example/pro.fasta example/list.txt    
```    
即可生成结果文件 `out_match_seq.fasta`：
```
>Zm00001eb423440_P001
MPNGGGKRWLLLLPLSRYVEVDEQQGVQLFYYFVRSERDPYEDPLLLWLSGGPGCSGISG...
>Zm00001eb423440_P004
MPNGGGKRWLLLLPLSRWVLLLGSLQLPAVGGSGHVVTRMRGFDGPLPFYLETGYVEVDE...
...
>Zm00001eb413340_P004
MQQIISACKLPHTQRAAAFLPPRPSLRRLPVPGLDRPGGAPPPRRLVVRRRCQEENKQQQ...
``` 

### 2.25 `CorrespondingNucleotideProteinFasta.py [FASTA_N] [FASTA_P]`

**功能描述：** 将转录本序列和蛋白质序列对应到表格文件。    

- **FASTA_N：** Fasta格式的核酸序列文件，cdna或转录本序列数据，命名规则【基因名_Txxx】。
- **FASTA_P：** Fasta格式的氨基酸序列文件，蛋白质序列数据，命名规则【基因名_Pxxx】。

**生成文件：** 
- `out_match_seq.tab`（表格文件，分别为：基因/转录本或蛋白质编号/核苷酸序列/氨基酸序列，没有找到对应的序列以“-”标注）。

**示例：**

比如 `example/pro.fasta` 是完整的蛋白质FASTA文件，格式同2.25，`example/pro.fasta是cdna数据：
```
#example/pro.fasta
>Zm00001eb423440_P001
MPNGGGKRWLLLLPLSRYVEVDEQQGVQLFYYFVRSERDPYEDPLLLWLSGGPGCSGISG...
>Zm00001eb423440_P004
MPNGGGKRWLLLLPLSRWVLLLGSLQLPAVGGSGHVVTRMRGFDGPLPFYLETGYVEVDE...
...
>Zm00001eb400040_P001
MASLCMFTISSTPHVPQGCRRRCSDAVSSRPRSYLVCQSHLPSGPPASGGGGGGGGEEKT...

#example/pro.fasta
>Zm00001eb423440_T001
GTTTATTTCTCTATTTGGTGCTTGCATGCCAACACATCTGTTTTTATATATTTTTAGTGG...
>Zm00001eb423440_T004
ATAGGGACCGGAGTGGCATTTGACCAGCTGAAGTCAACAGGCATGCCGAACGGTGGCGGC...
...
>Zm00001eb181160_T001
ATATGGGAAATGTATTTTACTCTTCATGCTTTTCCCCTTCGTGCAAGCAAAGCTAAACAA...
``` 
执行命令：
```bash
python CorrespondingNucleotideProteinFasta.py example/cdna.fasta example/pro.fasta   
```   
即可生成结果文件 `out_match_seq.tab`：
```
Zm00001eb413340	Zm00001eb413340_X001	GCCTCAACGG...	MQQIISACK...
Zm00001eb181160	Zm00001eb181160_X001	ATATGGGAAA...	-
Zm00001eb413340	Zm00001eb413340_X004	GCCTCAACGG...	MQQIISACK...
...
```   

### 2.26 `BatchModificationSequence.py [FASTA_FILE] [FIX_SEQ] [NEW_SEQ]`

**功能描述：** 批量将固定序列前的序列替换为指定序列。    

- **FASTA_FILE：** Fasta格式的核酸序列文件，即需要修改的所有序列。
- **FIX_SEQ：** 固定序列。
- **NEW_SEQ：** 替换成为的序列。 

**使用场景：** 通过某种方法使得序列中包含固定的序列，固定序列前的序列必须修改为特定的序列才能正常翻译（可能是这个概念）。

**生成文件：** 
- `modif_seq.tab`（表格文件，分别为：序列名称/原始序列/固定序列起始位置/固定序列终止位置/替换后的序列，没有找到固定序列最后三列以“-”标注）。

**示例：**

比如 `example/modif_seq.fasta` 是需要修改的序列fasta文件：
```
>pAbAi-GSL4-67
NGCACGTAGACCATACGACGTACCAGATTAC...
>pAbAi-GSL4-24
CCCGTGAAGAACCATACGACGTACCAGATTA...
...
>pAbAi-GSL4-82
NCCCGATGACCATACGACGTACCAGATTACG...
``` 
执行命令：
```bash
# 比如需要把ATACGACGTACCAGATTACGCTCATATG序列前边的部分替换为ATGGAGTACCC   
python BatchModificationSequence.py example/modif_seq.fasta ATACGACGTACCAGATTACGCTCATATG ATGGAGTACCC     

# 搞笑的是如果后边两个参数设定为不存在的字符，本代码可以实现fasta文件转换为table文件。。。运行完把除了第一二列删除！   
python BatchModificationSequence.py example/modif_seq.fasta - -
```  
即可生成结果文件 `modif_seq.tab`：
```
#比如需要把ATACGACGTACCAGATTACGCTCATATG序列前边的部分替换为ATGGAGTACCC   
pAbAi-GSL4-67	NGCACGTAGACCATACGACGTA...	13	40	ATGGAGTACCCATACGACGTACC...
pAbAi-GSL4-24	CCCGTGAAGAACCATACGACGT...	14	41	ATGGAGTACCCATACGACGTACC...
pAbAi-GSL4-3	CATACGCACGTACCAGTATTAC...	-	-	-
...

#本代码可以实现fasta文件转换为table文件。把除了第一二列删除！   
pAbAi-GSL4-67	NGCACGTAGACCATACGACGTA...	-	-	-
pAbAi-GSL4-24	CCCGTGAAGAACCATACGACGT...	-	-	-
pAbAi-GSL4-3	CATACGCACGTACCAGTATTAC...	-	-	-
...
```      

### 2.27 `TableToMultipleFasta.py [TABLE_FILE]`

**功能描述：** 将表格按照行转换为Fasta文件，每一行中多个序列放置在相同文件中。    

- **TABLE_FILE：** 表格文件，每一行将生成一个单独的Fasta文件，同一行的序列拆分到同一Fasta文件中，第一列是Fasta文件名。

**使用场景：** 快速拆分多个来源（不同物种、不同转录本、不同样品或不同基因家族等）同一序列（基因或氨基酸）用于后续分析。比如你如果想要快速完成每个Fasta文件的比对，可以使用CLUSTALW的命令行批量对输出文件夹的Fasta文件进行比对。  

**注意事项：** 表格第一列为拆分后的FASTA文件名称，不要重复!!!需要按照系统文件命名规则不能使用特殊符号。          

**生成文件：** 
- `out_fastas`（文件夹，其中有许多Fasta文件，文件命名是表格第一列的内容）。

**示例：**

比如 `example/fasta_per_row.txt` 是需要的文件：
```
Work-001	MEYPYDVPDYAHMTSLYKKVGRGQ...	MAANSTATKHAFKRILTSLI...		
Work-002	MEYPYDVPDYAHMTSLYKKVGSRP...	CRPCTALIPCRQQQRWRRGY...	WRRGYRRPISTSTSPR...	
Work-003	MEYPYDVPDYAHMTSLYKKVGSSP...			
...
``` 
执行命令：
```bash
python TableToMultipleFasta.py example/fasta_per_row.txt
```    
即可生成多个fasta文件：
```
out_fastas/
├── Work-001.fa  
├── Work-002.fa
├── ...
└── Work-005.fa

#Work-001.fa
>Work-001_1
MEYPYDVPDYAHMTSLYKKVGRGQ...
>Work-001_2
MAANSTATKHAFKRILTSLI...
``` 

### 2.28 `MultipleFastaToTable.py [FASTA_DIR]`

**功能描述：** 将多个Fasta文件转化为一个表格，同一文件的序列存放到同一行中（2.27的反转换）。    

- **FASTA_DIR：** 文件夹路径，该文件夹下存放用于合并的Fasta文件。

**使用场景：** 快速合并多个来源（不同物种、不同转录本、不同样品或不同基因家族等）同一序列（基因或氨基酸）用于后续分析。  

**注意事项：** 生成的表格中各个序列包含原来的名称，如果想转换为纯序列可以使用EXCEL打开，替换`*~~`为空白，切记一定要两个波浪线！文件夹中不能有其他文件。          

**生成文件：** 
- `merge.tab`（表格文件，第一列为Fasta文件名，后续各列是这个文件中的所有序列）。

**示例：**

有多个fasta文件：
```
example/
├── Work-001.fa  
├── Work-002.fa
├── ...
└── Work-005.fa

#Work-001.fa
>Work-001_1
MEYPYDVPDYAHMTSLYKKVGRGQ...
>Work-001_2
MAANSTATKHAFKRILTSLI...
``` 
可以执行：
```bash
python MultipleFastaToTable.py example/mul_fastas
```  
即可生成结果文件 `merge.tab`：
```
Work-001	MEYPYDVPDYAHMTSLYKKVGRGQ...	MAANSTATKHAFKRILTSLI...		
Work-002	MEYPYDVPDYAHMTSLYKKVGSRP...	CRPCTALIPCRQQQRWRRGY...	WRRGYRRPISTSTSPR...	
Work-003	MEYPYDVPDYAHMTSLYKKVGSSP...			
...
```
可以看出本脚本是2.28的逆操作！        
   
### 2.29 `AlignConsistencyChecker.py [FASTA_DIR]`

**功能描述：** 将比对后的Fasta文件，将每个位点对应，并比较是否有完全一致的位点。    

- **FASTA_DIR：** 文件夹路径，该文件夹下存放多个经过序列比对的Fasta文件。

**注意事项：** 生成的文件需要用EXCEL打开，并且将文字字体改为宋体等等宽字体！务必使用经过比对过的结果！文件夹中不能有其他文件。          

**生成文件：** 
- `aln_res.txt`（文本文件，建议用EXCEL打开，并调整为宋体字体查看，不同比对结果用空白行隔开，“**ALN**”行为序列比较结果，完全一致的位点为“*”，不一致的位点为“_”）。

**示例：**

有多个比对过的fasta文件：
```
example/
├── Work-001.fa  
├── Work-002.fa
└── Work-003.fa

#Work-001.fa
>Work-001_1
------------------------------------------------------------...
>Work-001_2
MAANSTATKHAFKRILTSLIKPGGGEYGKFFSLPALNDPRIDKLPYSIRVLLESAIRHCD...
>Work-001_3
MAANSTAT--AFKRILTSLIKPKGGEYGKFFSLPALNDPRIDKLPYSIRVLLESAIRHCD...
``` 
可以执行：
```bash
python AlignConsistencyChecker.py example/aln_fasta
``` 
即可生成结果文件 `aln_res.txt`：
```
Work-001.fa
Work-001_1	------------------------------------------------------------...
Work-001_2	MAANSTATKHAFKRILTSLIKPGGGEYGKFFSLPALNDPRIDKLPYSIRVLLESAIRHCD...
Work-001_3	MAANSTAT--AFKRILTSLIKPKGGEYGKFFSLPALNDPRIDKLPYSIRVLLESAIRHCD...
**ALN**	_________________________________________________________...
Work-002.fa
...		
```    

### 2.30 `MergeMultipleFasta.py [FASTA_1] [FASTA_2] ... [FASTA_n]`

**功能描述：** 将多个Fasta文件合并，并将重复的序列去冗余。    

- **FASTA_1/2/.../n：** Fasta文件路径，需要至少指定1个参数。

**使用场景：** 1.只指定1个Fasta文件时，相当于将单个Fasta文件中的序列去冗余；2.指定多个Fasta文件时，不仅可以将序列去冗余，还能得到不同Fasta文件中序列ID的对照表。  

**注意事项：** 至少指定1个参数。当指定1个参数时，不要和1.02搞混，1.02是将序列重新编号（无论序列是否一致都会赋予不同的ID）；而本脚本是将重复序列赋予统一ID，如果原本文件中有相同的ID（无论是否是相同序列）都只保留最后一个。         

**生成文件：** 
- `merge.fasta`（Fasta文件）。  
- `GeneIDMatch.table`（表格文件，各个序列在不同Fasta文件中的ID对照表）。   

**示例：**

有多个比对过的fasta文件：
```
example/merge_fasta/
├── File1.fasta  
├── File2.fasta
└── File3.fasta
``` 
可以执行：
```bash
# 只指定1个参数，单个文件去冗余   
python MergeMultipleFasta.py example/merge_fasta/File1.fasta     

# 指定2个参数，对比两个文件中的序列ID  
python MergeMultipleFasta.py example/merge_fasta/File1.fasta example/merge_fasta/File2.fasta

# 指定3个参数，对比三个文件中的序列ID
python MergeMultipleFasta.py example/merge_fasta/File1.fasta example/merge_fasta/File2.fasta example/merge_fasta/File3.fasta
```     
即可生成合并结果文件`merge.fasta`和去冗余概述文件 `GeneIDMatch.table`，以三个fasta文件合并为例：
```
#merge.fasta
>N_0000000001 
CCAAAAAACCCCC
>N_0000000002 
TTAAAGGG
>N_0000000003 
ATCGGCTA
>N_0000000004 
AGGAACCGG
>N_0000000005 
ATGGATTTTTAACG
>N_0000000006 
CCGGTTAAAAAA
>N_0000000007 
CCGAATTTGGGC
>N_0000000008 
AATTGGCAATTGGC

#GeneIDMatch.table
Nid	example/merge_fasta/File1.fasta	example/merge_fasta/File2.fasta	example/merge_fasta/File3.fasta
N_0000000001 	-	UniSeq	-
N_0000000002 	Seq	Seq	-
N_0000000003 	SameNameSameSeq	SameNameSameSeq	SameNameSameSeq
N_0000000004 	-	-	SameNameDifSeq
N_0000000005 	SameNameDifSeq	-	-
N_0000000006 	UniSeq	-	-
N_0000000007 	DifNameSameSeq1	DifNameSameSeq2	-
N_0000000008 	Seq2/Seq3	-	-
```  

### 2.31 `MitosToGFF.py [MITOS_FILE]`

**功能描述：** 将Mitos注释结果转换为GFF文件格式。    

- **MITOS_FILE：** 由Mitos生成的.mitos文件。   
        
**生成文件：** 
- `result_mitos.gff`（GFF文件）。

**示例：**

比如 `example/result.mitos` 是由MITOS软件生成的注释结果：
```
test	rep_origin	OL	mitfi	34	62	-1	3.70E-05	24.8	-	None	.	.	(((((((((...........)))))))))
test	rep_origin	OH	mitos	244	898	1	13308146.4	.	-	-	.	.	.
...
test	tRNA	trnE	mitfi	16617	16685	-1	5.90E-10	60.2	TTC	29	.	.	(((((((..((((....)))).(((((.......)))))....(((((........)))))))))))).
``` 
执行命令：
```bash
python MitosToGFF.py example/result.mitos
```  
即可生成结果文件 `result_mitos.gff`：
```
test	mitfi	rep_origin	35	63	.	-	.	ID=OL
test	mitos	rep_origin	245	899	.	+	.	ID=OH
test	mitfi	tRNA	1155	1222	.	+	.	ID=trnF-GAA
test	mitfi	rRNA	1222	2188	.	+	.	ID=rrnS
...
test	mitos	gene	16095	16616	.	-	.	ID=nad6
test	mitfi	tRNA	16618	16686	.	-	.	ID=trnE-TTC		
```  
  
### 2.32 `MitosToFasta.py [MITOS_FILE] [FASTA_FILE]`

**功能描述：** 将Mitos注释结果转换为GFF文件格式。    

- **MITOS_FILE：** 由Mitos生成的.mitos文件。  
- **FASTA_FILE：** 导入Mitos程序/网页的Fasta文件，也就是用于基因组注释的文件。   
        
**生成文件：** 
- `result_mitos.fasta`（Fasta文件，对于tRNA在序列ID上注明了反密码子和二级结构）。

**示例：**

比如 `example/result.mitos` 是由MITOS软件生成的注释结果：
```
test	rep_origin	OL	mitfi	34	62	-1	3.70E-05	24.8	-	None	.	.	(((((((((...........)))))))))
test	rep_origin	OH	mitos	244	898	1	13308146.4	.	-	-	.	.	.
...
test	tRNA	trnE	mitfi	16617	16685	-1	5.90E-10	60.2	TTC	29	.	.	(((((((..((((....)))).(((((.......)))))....(((((........)))))))))))).
``` 
对应的test的fasta序列是`example/mitos.fasta` 执行命令：
```bash
python MitosToFasta.py example/result.mitos example/mitos.fasta  
```    
即可生成每一个特征的序列文件 `result_mitos.fasta`：
```
>OL
TACCCCCCCTGGGGGGGAAAGGGGGGGTA

>OH
TCCCCCCCCAAGGCACCTAATCTATGAATGGTCACAGGACATA...
...

>nad6
ATGACTTATTTTGTGATTTTTTTGGGAGTTAGTTTTGCATTAGG...

>trnE-TTC (((((((..((((....)))).(((((.......)))))....(((((........)))))))))))).
GTTCCCGTAGTTGAGAACAACGATGGCTTTTCAAGCCGTAGTCCTTGGAGTTTAGGCCAAGCGGGAATA	
```  

### 2.33 `SsToFold.py [SS_FILE]`

**功能描述：** 将tRNAscan-SE产生的二级结构文件（.ss）转换为RNAplot程序支持的fold格式（与由RNAfold程序生成的文件相同格式）。   

将文件：   
```    
NC_020585.1.trna1 (1155-1222)	Length: 68 bp
Type: Phe	Anticodon: GAA at 32-34 (1186-1188)	Score: 73.8
         *    |    *    |    *    |    *    |    *    |    *    |    *  
Seq: GCCCACATAGCTTAACCCAAAGCATGACACTGAAGATGTTAAGATGGTACCCATACTACCTGTGGACA
Str: >.>>>>>..>>>>......<<<<.>>>>>.......<<<<<....>>>>.......<<<<<<<<<.<.

NC_020585.1.trna2 (2188-2258)	Length: 71 bp
Type: Val	Anticodon: TAC at 33-35 (2220-2222)	Score: 81.3
         *    |    *    |    *    |    *    |    *    |    *    |    *    |
Seq: CAAGGCGTAGCTATAAACCAAAGCACTCAGCTTACACCTGAAAGATGCCTTCAAAgaTAAGGTCGCCTTGA
Str: >>>>>>>..>>>.........<<<..>>>>.......<<<<.....>>>>.........<<<<<<<<<<<.

NC_020585.1.trna3 (3876-3949)	Length: 74 bp
Type: Leu	Anticodon: TAA at 36-38 (3911-3913)	Score: 111.8
         *    |    *    |    *    |    *    |    *    |    *    |    *    |   
Seq: GCTAGCGTGGCAGAGCTcGGTaAATGCAAAAGGCTTAAGCCCTTTCCCCAGAGGTTCAAATCCTCTCCCTAGCT
Str: >>>>>.>..>>>............<<<.>>>>>.......<<<<<....>>>>>.......<<<<<<.<<<<<.

```

转换为    
```
>trnF-1155-1222
GCCCACATAGCTTAACCCAAAGCATGACACTGAAGATGTTAAGATGGTACCCATACTACCTGTGGACA
(.(((((..((((......)))).(((((.......)))))....((((.......))))))))).).
>trnV-2188-2258
CAAGGCGTAGCTATAAACCAAAGCACTCAGCTTACACCTGAAAGATGCCTTCAAAgaTAAGGTCGCCTTGA
(((((((..(((.........)))..((((.......)))).....((((.........))))))))))).
>trnL1-3876-3949
GCTAGCGTGGCAGAGCTcGGTaAATGCAAAAGGCTTAAGCCCTTTCCCCAGAGGTTCAAATCCTCTCCCTAGCT
(((((.(..(((............))).(((((.......)))))....(((((.......)))))).))))).
>trnI-4934-5004
GGAAGCGTGCCTGAATAAAAGGACCACTATGATAAAGTGGACATAGAGGTAAAacAATCCTCTCGCCTCCT
(((.(((..(((.......))).(((((.......)))))....(((((.........)))))))).))).
```

可以看到该脚本会将氨基酸三字母缩写改为单字母缩写。   

- **SS_FILE：** 由tRNAscan-SE生成的.ss文件。  

**视频教学：** https://www.bilibili.com/video/BV1fwDjYVEx9/  
        
**生成文件：** 
- `plot.fold`（与RNAfold程序生成的文件格式一致，支持RNAplot程序批量绘图每个序列包含三行，第一行为序列名称/第二行为碱基序列/第三行为二级结构式）。

**示例：**

```bash
python SsToFold.py example/trnascanse.ss  

#后续可以使用RNAplot包进行绘制tRNA二级结构图。
#RNAplot -f svg plot.fold    

#将所有的svg文件整理到一个文件中，可以使用代码4.03进行美化。
```     

### 2.34 `RSCUPlot.R`

**功能描述：** 得到蛋白编码基因的密码子偏好性，绘制RSCU柱形图。  

**注意事项：** 本R脚本提供了数据统计及绘图函数，不可以直接通过命令行调用。

**视频教学：** https://www.bilibili.com/video/BV1GQnWztEzF/    

**生成文件：** 
- `01-sequences.csv`（表格文件，包含各个蛋白编码基因的序列及起始终止密码子信息）。
- `02-Codon_occurrence_in_all_gene.csv` （表格文件，所有蛋白编码基因的密码子使用频数及频率）。
- `03-Codon_occurrence_matrix.csv`（表格文件，密码子偏好矩阵）。
- `04-RSCU_matrix.csv` （表格文件，RSCU矩阵）。
- `05-<基因名>_RSCU.csv`（表格文件，指定基因的RSCU值及密码子使用频数）。
- `06-<基因名>_RSCU_plot_file.csv` （表格文件，用于自定义绘图的原始数据）。
- `07-<基因名>_RSCU_plot.pdf`（使用默认参数绘制的图形）。

**示例：**

比如 `example/pcgs.fa` 是提取到的蛋白编码基因的CDS序列：
```
>nad1
ATGACCCCACTAACCCCAATAAACCTCACAATCATAACTTTATCTTACATAATCCCAAT...
...
>nad6
ATGACTTATTTTGTGATTTTTTTGGGAGTTAGTTTTGCATTAGGGGTTTTAGCTGTAGC...
```
此外已经在本地下载了本脚本，假设将脚本放置在`xxx/xxx/RSCUPlot.R`位置，可以打开R或者RStudio,执行命令：
```bash
source("xxx/xxx/RSCUPlot.R")
# 需要注意source到脚本具体路径！

# 如果已经把工作目录设定到了脚本所在文件夹，可以直接运行：
# source("RSCUPlot.R")
``` 
如果是第一次运行可能需要下载几个R包，加载完成后可以使用下面代码或函数：
```
# 设定蛋白编码基因所在路径
pcg = "example/pcgs.fa"

# 设定密码子表，建议查看https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes，选择正确的密码子表。
# 示例选择的是第二套密码子表，因此输入数字2：
codonTable = 2

# 运行函数，即可生成7个结果文件，其中包括所有蛋白编码基因总体的RSCU柱形图。
df = main_fun(pcg,codonTable)

# 如果想导出指定基因的RSCU柱形图可以指定gene参数
# df = main_fun(pcg,codonTable,gene="nad6")
# 注意默认输出全部蛋白编码基因的结果，即gene="Total"。

# 如果对导出的图片尺寸不满意，可以调用：
# plot_rscu(rscu_d, out_path,h1=0.6,h2=6,yLim=6.2)
# 其中rscu_d是绘图用到的数据框，即main_fun函数的返回值df；
# out_path是输出文件路径；
# h1与密码子矩形垂直间隙有关，如果矩形重叠可以适当增加该值；
# h2是输出图片的高度，注意增加h2必须相应调整h1参数可以美观；
# yLim是柱形图最高限度，除了第5套密码子，各个氨基酸的RSCU值之和不超过6，因此6.2是合适的，第5套密码子Ser氨基酸对应有8个密码子，所以需要设置8左右是合适的。
# 通过作者测试h1=0.6，h2=6可以生成较好的扁平图形，h1=0.2，h2=12可以生成近似正方形的图形。
# 自定义绘图的例子：plot_rscu(df,"111.pdf",0.1,24,8.2)
# 绘制完之后建议使用PDF编辑软件，缩小密码子和柱形图的垂直距离。
# 如果觉得默认图案不太美观，可以自行修改函数！
	
```

### 2.35 `splitGB.py [GB_FILE]`

**功能描述：** 拆分多序列GenBank文件。   

- **GB_FILE：** 需要拆分的GenBank文件。  

**使用场景：** 使用NCBI批量下载工具（ https://www.ncbi.nlm.nih.gov/sites/batchentrez ）下载的GB文件是多序列GB文件，如果有拆分需求可以使用本脚本。  
        
**生成文件：** 

- `gb_output/xx.gb`（每一个序列生成一个单独的GB文件）。

**示例：**

比如 `example/sequence.gb` 文件夹包含许多序列：
```
LOCUS       NC_036066              16785 bp    DNA     circular INV 03-APR-2023
DEFINITION  Dorcadia ioffi mitochondrion, complete genome.
ACCESSION   
VERSION     NC_036066.1
DBLINK      BioProject: PRJNA927338
...
 20821 aataacgatt gtattatatt ccctattata taatacaatt tattataaaa ttaactatct
    20881 aatatatccc gtgtaattaa ttattttaat a
//

LOCUS       MW310242               18902 bp    DNA     circular INV 24-JUL-2021
DEFINITION  Xenopsylla cheopis mitochondrion, complete genome.
ACCESSION   MW310242
VERSION     MW310242.1
...
//
```
执行命令：

```bash
python splitGB.py example/sequence.gb
```     
即可生成结果文件夹 `gb_output` ：
```
codemlnull/
├── Ctenocephalides_felis_felis_MW420044.gb  
├── OG0005964.fa.nuc.ctlDorcadia_ioffi_VERSION.gb
├── Eukaryota_Metazoa_Ecdysozoa_Arthropoda_Hexapoda_Insecta_NC_040301.gb
├── Hystrichopsylla_weida_qinlingensis_NC_042380.gb
└── Xenopsylla_cheopis_MW310242.gb
```   

## 3. Gadget 一些通用的文本处理和分析工具，以及与富集注释分析相关的代码。

### 3.01 `MergeTable.py`

***图形界面的合并表格工具***

**功能描述：** 合并多个表格时，可以根据它们的第一列数据进行对应联接操作。

**参数说明：** 不需要配置参数。将所有需要依据首列进行合并的表格逐一导入，并通过相应功能一键实现按第一列内容的合并操作。

**注意事项：** 只支持图形化系统，表格支持制表符分隔也支持逗号分隔，如果含有制表符将认为表格是制表符分隔。  

**生成文件：** 

- `merge.txt`（合并后的表格）。 
- `error.log`（如果合并失败生成的日志文件）。

**示例：**

在有有图形化的系统中，运行下面的命令即可打开图形界面：
```bash
python MergeTable.py
``` 
点击“Open”可以添加需要合并的表格，点击“Merge！”即可开始合并，如果合并出错会报错。  
```
#在example文件夹中有一些示例

##情况1：正常合并
#sample1.tsv
ID	Name	Age
1	Alice	25
2	Bob	30
3	Charlie	35

#sample2.tsv
Nun	Height	Weight
1	165	60
2	175	75
3	160	55

#合并完成之后：
fid	Name	Age	Height	Weight
2	Bob	30	175	75
1	Alice	25	165	60
3	Charlie	35	160	55
#可见无论第一列的标识是什么都作为合并参照。

##情况2：具有缺失值的合并
#sample3.tsv
ID	Feature1	Feature2
1	Value1	ccc
3	kkk	ValueC
A	Value2	ValueB

#将三个文件同时输入：
fid	Name	Age	Height	Weight	Feature1	Feature2
A	-	-	-	-	Value2	ValueB
1	Alice	25	165	60	Value1	ccc
2	Bob	30	175	75	-	-
3	Charlie	35	160	55	kkk	ValueC
#可见无论输入文件顺序如何都可以得到内容一致的表格，但是对应的列可能有先后的区别。

#示例中只展示了制表符分隔的情况，逗号分隔表格依然适用，推荐使用制表符分隔。
#运行完成之后如果终端显示finish!说明运行成功。
#显示xxx can not merge说明表格合并失败，需要检查是否所有表格都是文本格式的文件（可以用记事本打开）。
```

### 3.02 `VLookup.py [KEY_FILE] [MAP_FILE] [KEY_LOC] [VALUE_LOC] [SEP（可选参数）]`

**功能描述：** vlookup函数的Python实现。可以自定义键值的位置。

- **KEY_FILE：** 一个文件，包含需要检索值的列。   
- **MAP_FILE：** 在其中检索的表格，需要至少有两个列，其中一个是key，另外一个是值。        
- **KEY_LOC：** 键列在MAP_FILE表格中位于的列号，比如第一列是key填写1。   
- **VALUE_LOC：** 值列在MAP_FILE表格中位于的列号，比如第一列是value填写1。    
- **SEP：** MAP的制表符，默认制表符分隔"\t"，如果是逗号分隔使用","，注意引号是英文的。   

**使用场景：** 从总注释表中提取一些基因的注释信息。注意这个只能提取一列内容。       

**生成文件：** 
- `map_<map file name>`（TABLE file）。

**示例：**

示例中有一个包含键的列表 `key.txt`：
```
ProteinA
ProteinB
ProteinC
```
另外还有包括键和值的文件 `map.txt`：
```
GeneA	Location1	ProteinA
GeneD	Location4	ProteinD
GeneC	Location3	ProteinC
```
观察到键位于索引文件的第3列所以KEY_LOC设置为3。如果想要取的值为Gene列设置VALUE_LOC为1，如果是位置列则设置为2。由于map文件为制表符分隔表格设置SEP为默认，故运行：
```bash
#提取Gene列
python VLookup.py example/key.txt example/map.txt 3 1
``` 
最后会生成结果文件：  
```
ProteinA	GeneA
ProteinB	-
ProteinC	GeneC
```

### 3.03 `SumByGroup.py [MAP_FILE] [MATRIX_FILE] [KEY_COL_ID] [VALUE_COL_ID]`

**功能描述：** 分组求和的进阶版。

- **MAP_FILE：** 在进行数据处理时，所使用的表格需包含分组列以及该组内所有成员列。分组和成员关系可以是一对一、一对多、多对一或多对多的形式。分组及其成员之间用逗号分隔，例如："A,B" 表示 A 组和 B 组都包含相同的成员 "a"；而 "A a,b" 则表示 A 组内包含成员 "a" 和 "b"。
- **MATRIX_FILE：** 丰度表或类似的矩阵，请确保矩阵文件包含标题行，其中第一列的元素必须与MAP_FILE中的成员值（不是分组）相匹配。举例来说，在基因丰度矩阵中，第一列通常是基因名称，这些基因属于不同的基因家族，并且矩阵中还包含了针对各个样品的丰度数据列。
- **KEY_COL_ID：** 在MAP文件中，指定组名所在的列编号，其中0代表第一列，1代表第二列，以此类推，用于指示每一行记录中的组别信息所在位置。
- **VALUE_COL_ID：** 在MAP文件中，指定成员名所在的列编号，其中0代表第一列，1代表第二列，以此类推，用于指示每一行记录中的成员信息所在位置。

**使用场景：** 在处理数据时，假如你拥有一份map表，该表记录了每个基因与其所属基因家族的关系；同时你还有一份matrix表，其中列出了各基因的丰度数据。此时，你需要通过联合这两份表，来计算出每个基因家族总的丰度值，物种丰度表同理。                 

**注意事项：** 务必确保map表和matrix表均包含标题行以便正确识别列信息。另外，在进行相对丰度计算时，应当使用all.count的总计数值作为计算每个序列丰度的分母。

**生成文件：** 
- `out.count`（TABLE file, 分组求和表）。
- `all.count`（TABLE file, 总求和表）。

**示例：**

比如 `example` 里边有map文件和matrix文件：
```
#map.txt
value	key
a1	A
a2	A
b1,d1	B,D
c1	C
c2	C
e1	E

#matrix.txt
value	a	b	c	d
a1	123	5	6	100
a2	1	1	0	0.555
b1	0.1	0.2	0.3	0.4
c1	0	2	1.1	4.1
d1	0	0	1.2	1.0
```
观察到key列位于第二列（对应1），value列对应第一列（对应0）,执行命令：
```bash
python SumByGroup.py example/map.txt example/matrix.txt 1 0
```
最后会生成结果文件：  
```
#out.count
value	a	b	c	d
A	124.0	6.0	6.0	100.555
B	0.1	0.2	1.5	1.4
D	0.1	0.2	1.5	1.4
C	0.0	2.0	1.1	4.1
E	0.0	0.0	0.0	0.0

#all.count
value	a	b	c	d
all_gene	124.1	8.2	8.6	106.055
```
将矩阵结果每一列的值（绝对丰度）除以总计数值可以得到相对丰度。

### 3.04 `CountByGroup.py [-h] [-a MAPA] [-b MAPB] [-k KEA] [-K KEB] [-v VAA] [-V VAB] [-s SEA] [-S SEB] [--seka SEKA] [--sekb SEKB] [--seva SEVA] [--sevb SEVB] [-n HEADA] [-N HEADB]`
         
**功能描述：** 针对具有三层映射关系A-B-C的数据结构，任务是在A层中寻找关联到C层的所有元素，并统计这些元素的数量。

**参数说明：** 

```bash
options:
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

**使用场景：** 比如在生物过程中包括三个GO术语，这三个术语之间存在交集基因，你想统计生物过程下一共的基因数目（去重的），大表格是。

**注意事项：** -a和-b参数是必需的，其他参数都有默认值！

**生成文件：** 
- `count_Map.txt`（表格文件）。

**示例：**

比如 `example` 里边有大表格map文件和小表格map文件：
```
#map.txt
value	key
a1	A
a2	A
b1,d1	B,D
c1	C
c2	C
e1	E

#map2.txt
a1	i1,i2,i3
a2	i2,i4
b1	i5,i6
b2	i1
c1,a1	i3,i5
```
观察到大表格key列位于第二列（对应k为1），value列位于第一列（对应v为0）；小表格key列位于第一列（对应K为0，默认），value位于第二列（对应V为1，默认），大表格包含一行标题行（对应n为1）,执行命令：
```bash
python CountByGroup.py -a example/map.txt -b example/map2.txt -n 1 -k 1 -v 0
```
随后会生成结果文件：  
```
A	5	i2;i3;i5;i1;i4
B	2	i5;i6
D	2	i5;i6
C	2	i5;i3
E	0	
```

### 3.05 `FastaSplitter.py [FASTA_FILE_PATH] [Number_of_split_files]`
       
**功能描述：** 针对含有大量序列的FASTA文件，可根据序列数量对其进行分割，形成多个较小的FASTA文件。

- **FASTA_FILE_PATH：** 要分割的FASTA文件的路径。
- **Number_of_split_files：** 分割完成后每个文件包含的序列数。

**使用场景：** 例如，在进行在线KEGG注释时，KEGG服务可能对一次上传的序列数目有所限制，通过预先分割大的FASTA文件，可以确保符合上传要求并顺利完成注释任务。

**生成文件：** 
- `<拆分后的文件编号>_<原FASTA文件>`（多个FASTA文件）。   

**示例：**

运行下列代码将7个序列的fasta文件 `example/text.fa`分为3个2序列的文件（不够整除最后一个文件只有一个序列）。
```bash
python FastaSplitter.py example/text.fa 2
```
随后会生成三个fasta文件。

### 3.06 `KeggAnnotationParser.py [KEG_FILE]`
   
**功能描述：** 解析KEG文件。可以解析从KEGG网页下载的.keg注释文件，用于富集分析或基因注释时手动构建背景基因集。

- **KEG_FILE：** 从KEGG数据库下载的KEG文件比如通用的：ko00001.keg或者人类KEG文件：hsa00001.keg。

**使用场景：** 通过本脚本你可以得到KEGG数据库每个ko或者每个物种的通路ID的简易化表格，①用于在KEGG在线注释网站得到的KEGG注释的解析；②用于解析KEGG通路数据库中模式生物或通用注释表的解析。
                 
> 你可以点击链接下载通用KEG文件：https://www.kegg.jp/kegg-bin/download_htext?htext=ko00001&format=htext&filedir=
> 将上述网址中的htext=ko00001中的ko替换为物种缩写可以下载特定物种的KEG文件，比如替换为hsa https://www.kegg.jp/kegg-bin/download_htext?htext=hsa00001&format=htext&filedir= 即是人类的KEG文件。
> 物种缩写你可以参照：  https://www.genome.jp/kegg/catalog/org_list.html   比如老鼠的缩写是mmu。

**注意事项：** 在示例文件中有从KEGG网址下载的人类和通用keg文件，为保证数据库的最新建议手动下载。  

**生成文件：** 
- `output_\<你的keg文件名>`（表格文件）
- `<你的keg前缀（物种缩写）>_map.txt` （表格文件，如果需要进行KEGG富集分析，你可以使用excel的Vlookup函数对完成背景基因文件）

**示例：**

```bash
# 比如解析通用keg文件：
python KeggAnnotationParser.py example/ko00001.keg

# 比如解析人类keg文件：
python KeggAnnotationParser.py example/hsa00001.keg
```
将生成结果文件：
```
##解析通用keg文件：
#output_ko00001.txt
A-PATH	LEVEL-A	B-PATH	LEVEL-B	ID (C-PATH)	LEVEL-C	D-KO
09100	Metabolism	09101	Carbohydrate metabolism	ko00010	Glycolysis / Gluconeogenesis	K00844  HK; hexokinase [EC:2.7.1.1]
09100	Metabolism	09101	Carbohydrate metabolism	ko00010	Glycolysis / Gluconeogenesis	K12407  GCK; glucokinase [EC:2.7.1.2]
...

#ko_map.txt
ko	Level-A	Level-B	Level-C
ko02026	Cellular Processes	Cellular community - prokaryotes	Biofilm formation - Escherichia coli
ko00522	Metabolism	Metabolism of terpenoids and polyketides	Biosynthesis of 12-, 14- and 16-membered macrolides
ko04061	Environmental Information Processing	Signaling molecules and interaction	Viral protein interaction with cytokine and cytokine receptor
...

##解析人类keg文件：
#output_hsa00001.txt
A-PATH	LEVEL-A	B-PATH	LEVEL-B	ID (C-PATH)	LEVEL-C	D-GENES	D-KO
09100	Metabolism	09101	Carbohydrate metabolism	hsa00010	Glycolysis / Gluconeogenesis	3101 HK3; hexokinase 3	K00844 HK; hexokinase [EC:2.7.1.1]
09100	Metabolism	09101	Carbohydrate metabolism	hsa00010	Glycolysis / Gluconeogenesis	3098 HK1; hexokinase 1	K00844 HK; hexokinase [EC:2.7.1.1]
...

#hsa_map.txt
hsa	Level-A	Level-B	Level-C
hsa04370	Environmental Information Processing	Signal transduction	VEGF signaling pathway
hsa00590	Metabolism	Lipid metabolism	Arachidonic acid metabolism
hsa00053	Metabolism	Carbohydrate metabolism	Ascorbate and aldarate metabolism
```

### 3.07 `KEGGPathwayCounter.py [3.06_生成文件_1] [GENE_KO]`
    
**功能描述：** KEGG通路基因数量统计，导出用于KEGG注释富集绘图的数据。

- **3.06_ 生成文件_1：** 脚本3.06的生成文件。
- **GENE_KO：** GENE-KO映射表，第一列是基因ID或名称，第二列为ko编号（或其他通路编号），多个ko编号可以用逗号隔开，可参考示例文件。  

**生成文件：** 
- A.txt (all_gene is the total number of genes, and you can use this number to find the gene ratio. TABLE file)  
- A-B.txt (TABLE file)   
- A-C.txt (TABLE file)   
- err.txt (There is no matching KO number. TABLE file)

**示例：**

比如 `example` 里边需要的文件：
```
#脚本3.06生成的文件：output_ko00001.txt
A-PATH	LEVEL-A	B-PATH	LEVEL-B	ID (C-PATH)	LEVEL-C	D-KO
09100	Metabolism	09101	Carbohydrate metabolism	ko00010	Glycolysis / Gluconeogenesis	K00844  HK; hexokinase [EC:2.7.1.1]
09100	Metabolism	09101	Carbohydrate metabolism	ko00010	Glycolysis / Gluconeogenesis	K12407  GCK; glucokinase [EC:2.7.1.2]
...

#基因ko注释结果：gene_ko.txt
g03.1	ko04391,ko04392
g04.1	ko04142
g05.1	ko03022
g06.1	ko03320,ko04360,ko04510,ko05100,ko05131,ko05213
g08.1	ko04120
g13.1	ko05010
```
执行命令：
```bash
python KEGGPathwayCounter.py example/output_ko00001.txt example/gene_ko.txt
```
将生成结果文件：
```
#A.txt
A	num
all_gene	6
Environmental Information Processing	1
Cellular Processes	2
Genetic Information Processing	2
Human Diseases	2
Organismal Systems	1

#A-B.txt
A	B	num
Environmental Information Processing	Signal transduction	1
Cellular Processes	Transport and catabolism	1
Genetic Information Processing	Transcription	1
Human Diseases	Infectious disease: bacterial	1
Organismal Systems	Endocrine system	1
Cellular Processes	Cellular community - eukaryotes	1
Human Diseases	Cancer: specific types	1
Organismal Systems	Development and regeneration	1
Genetic Information Processing	Folding, sorting and degradation	1
Human Diseases	Neurodegenerative disease	1

#A-C.txt
A	B	C	num
Environmental Information Processing	Signal transduction	Hippo signaling pathway - fly	1
Environmental Information Processing	Signal transduction	Hippo signaling pathway - multiple species	1
Cellular Processes	Transport and catabolism	Lysosome	1
Genetic Information Processing	Transcription	Basal transcription factors	1
Organismal Systems	Endocrine system	PPAR signaling pathway	1
Organismal Systems	Development and regeneration	Axon guidance	1
Cellular Processes	Cellular community - eukaryotes	Focal adhesion	1
Human Diseases	Infectious disease: bacterial	Bacterial invasion of epithelial cells	1
Human Diseases	Infectious disease: bacterial	Shigellosis	1
Human Diseases	Cancer: specific types	Endometrial cancer	1
Genetic Information Processing	Folding, sorting and degradation	Ubiquitin mediated proteolysis	1
Human Diseases	Neurodegenerative disease	Alzheimer disease	1

#err.txt
```

### 3.08 `GOoboAnnotationExtractor.py [obo_FILE]`

**功能描述：** 从obo文件读取并解析GO号对应的描述及分类，生成GO编号\t描述信息\t分类的三列表格，你可以直接使用示例文件中的go_term_list.txt，要注意这个文件可能不是最新的版本，因此推荐使用该脚本提取最新的GO注释信息。

- **obo_FILE：** GO网站上下载的obo文件路径（打开网址：https://purl.obolibrary.org/obo/go/go-basic.obo 推荐打开网页后，右键，点击另存为，保存为文本文件） 。

**注意事项：** 由于网页加载可能不全因此不推荐将网页CTRL+A全选CTRL+C复制，新建txt文件并打开CTRL+V粘贴。

**生成文件：** 
- `<版本号>_go_term_list.txt`（TABLE文件，第一列是GO号，第二列是描述信息，第三列是分类）

**示例：**

比如你将网页复制或保存到了abc.txt，你可以运行下方代码：
```bash
python GOoboAnnotationExtractor.py abc.txt
```
因为文件实时更新所以未放置实时的示例文件。

### 3.09 `GOTableConverter.py [GENE_GOs_MAP]`
                 
**功能描述：** 转换GO注释表格：  
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

- **GENE_GOs_MAP：** 二列表格，第一列是基因名称，第二列是对应的许多GO号，每一行都是一对多的形式。

**生成文件：** 
- `g-go.txt`（TABLE文件，第一列是geneid，第二列是GOID）。     

**示例：**

比如 `example/seq_gos.txt` 是所需文件：
```
Accession_id	go
a0	"GO:0004176(molecular_function:ATP-dependent peptidase activity); GO:0004252(molecular_function:serine-type endopeptidase activity)"
a1	"GO:0043169(molecular_function:cation binding); GO:0004497(molecular_function:monooxygenase activity)"
a2	"GO:0001234; GO:GO:0004497"
```
执行命令：
```bash
python GOTableConverter.py example/seq_gos.txt
```
将生成结果文件：
```
a0	GO:0004176
a0	GO:0004252
a1	GO:0043169
a1	GO:0004497
a2	GO:0001234
a2	GO:0004497
```
      
### 3.10 `AddGOAnnotations.py [go_term_list] [GENE_GO_MAP]`
                 
**功能描述：** 给gene-go文件加上GO注释的描述和分类内容。通过运行这个命令生成的文件配合R包clusterProfiler完成富集分析的内容。

- **go_term_list：** 推荐是使用3.08脚本生成的go_term_list.txt文件，包含所有GO术语的描述信息。
- **GENE_GO_MAP：** 推荐是3.09生成的文件，第一列是基因名称，第二列是对应的GO号。

**注意事项：** 有时自己注释的表格是某一列是geneID，还有一列是很多GO号。你可以通过代码3.09（推荐）或者下面的代码把一个基因对应多个GO号的文件转换为一一对应的格式！如果是go号之间是逗号隔开，把下边的分号改为分号即可，注意需要是英文的！input_file是你输入的文件名，也就是一个gene对应很多GO编号的表格，output_file是指输出的文件名，注意不要和已有文件相同。
```bash
awk -F'\t' '{split($2, arr, ";"); for (j in arr) print $1 "\t" arr[j]}' input_file > output_file
```
**生成文件：** 
- `gene_GO_info.txt`（TABLE文件，第一列是geneid，第二列是GOID，第三列是描述信息，第四列是GO三大类的分类）。

**示例：**

使用时需要按照3.08生成表格文件xxx-go_term_list.txt，示例中的2024-01-17_go_term_list.txt是版本2024-01-17。建议通过3.08代码获取最新的版本。文件格式：
```
#2024-01-17_go_term_list.txt
GO:0000001	mitochondrion inheritance	biological_process
GO:0000002	mitochondrial genome maintenance	biological_process
GO:0000003	reproduction	biological_process
GO:0019952	reproduction	biological_process
GO:0050876	reproduction	biological_process
GO:0000005	obsolete ribosomal chaperone activity	molecular_function
GO:0000006	high-affinity zinc transmembrane transporter activity	molecular_function
GO:0000007	low-affinity zinc ion transmembrane transporter activity	molecular_function
...

#gene_go.txt
gene1	GO:0000002
gene1	GO:0000003
gene1	GO:0000005
gene1	GO:0000006
gene2	GO:0000005
gene2	GO:0000007
```
执行命令：
```bash
python AddGOAnnotations.py example/2024-01-17_go_term_list.txt example/gene_go.txt
```
将生成结果文件：
```
gene_id	ID	Description	ONTOLOGY
gene1	GO:0000002	mitochondrial genome maintenance	biological_process
gene1	GO:0000003	reproduction	biological_process
gene1	GO:0000005	obsolete ribosomal chaperone activity	molecular_function
gene1	GO:0000006	high-affinity zinc transmembrane transporter activity	molecular_function
gene2	GO:0000005	obsolete ribosomal chaperone activity	molecular_function
gene2	GO:0000007	low-affinity zinc ion transmembrane transporter activity	molecular_function
```

> ## 无参GO/KEGG富集分析流程    
> 当你已经得到所有基因/蛋白质的GO注释结果，①如果原始注释表格是gene-GOs一对多的格式，使用3.09转换为gene-GO一对一的格式；②使用3.08下载并解析所有GO术语描述信息表；③使用3.10为每个gene添加GO注释信息；④使用R包clusterProfiler 计算受关注基因（比如差异基因/正选择基因/扩张基因等）的GO术语富集到背景基因（所有注释基因/蛋白质）GO术语的结果。比较常见的富集结果（气泡图的横坐标）有基因比例（gene Ratio）、富集得分（enrichment score，又称fold enrichment富集倍率）和富集因子（rich factor），比如clusterProfiler计算得到的GeneRatio是20/100（表示100个关注基因富集到某术语20个gene），BgRatio是50/150（表示所有的150个基因富集到某术语50个gene）那么，基因比例即为20/100=0.20，富集得分为两个比例的比值即为(20/100)/(50/150)=0.6，富集因子是两个分子的比值即为20/50=0.4。注意如小鼠、人等模式生物，由于自己注释出的背景基因很可能不全面，因此推荐使用专门的富集网站或者富集工具包完成。    
>无参KEGG富集分析流程与GO富集类似。
> 富集分析R代码参考的是知乎文章  https://zhuanlan.zhihu.com/p/561522453 中的无参GO富集分析部分，并对部分内容进行修改，使之同时适合KEGG和GO无参富集分析。    
> **文件1 背景基因注释分组文件 gene_ID.txt**    
> 第一列是gene或蛋白质的名称（可以不唯一）；第二列是GO号或ko号；第三列是描述信息，对于GO富集分析是GO术语的详细解释（level2），对于KEGG分析是levelC的描述信息；第四列是分组信息，对于GO是指GO的三大类，对于KEGG可以选择levelC所属的levelA或levelB的描述信息。      
> GO富集分析的文件可以使用脚本3.10生成，但是需要按照下列格式修改：            
> | gene_id | ID | Description | GROUP |            
> | --- | --- | --- | --- |        
> | GeneA | GO:000001 | mitochondrion inheritance | biological_process |        
> | GeneA | GO:000002 | mitochondrial genome maintenance | biological_process |         
> | GeneB | GO:000006 | high-affinity zinc transmembrane transporter activity | molecular_function |        
> | ... | ... | ... | ... |        

> KEGG富集分析的文件需要按照下列格式修改可以使用代码3.05和EXCEL的vlookup函数生成该文件：           
> | gene_id | ID | Description | GROUP |            
> | --- | --- | --- | --- |        
> | GeneA | ko00010 | Glycolysis / Gluconeogenesis | Metabolism |        
> | GeneA | ko00020 | Citrate cycle (TCA cycle) | Metabolism |         
> | GeneB | ko04016 | MAPK signaling pathway - plant | Environmental Information Processing |        
> | ... | ... | ... | ... |        

> **文件2 关注的基因（差异基因/特异基因/正选择基因等）列表 gene.txt**      
> 至少有一列是以gene_id为列名的列，注意该列不得有重复的基因，否则计算将错误。       
> | gene_id |                   
> | --- |           
> | GeneA |     
> | GeneB |        
> | GeneD |         
> | ... |           

> 准备好上述两个文件，即可使用下列代码计算富集统计数，基于富集统计数即可绘制气泡图。       
> ```bash
> #富集分析R代码参考的是知乎文章  https://zhuanlan.zhihu.com/p/561522453 中的无参GO富集分析部分。      
> 
> library(clusterProfiler)        
> #读取手动准备好的背景基因集
> gene_ID <- read.delim('gene_ID.txt', stringsAsFactors = FALSE)
> #读取基因列表文件中的基因名称
> genes <- read.delim('gene.txt', stringsAsFactors = FALSE)$gene_id
> #GO/KEGG 富集分析
> gene_rich <- enricher(gene = genes,  #待富集的基因列表
>     TERM2GENE = gene_ID[c('ID', 'gene_id')],  #背景基因集
>     TERM2NAME = gene_ID[c('ID', 'Description')], 
>     pAdjustMethod = 'BH',  #指定 p 值校正方法
>     pvalueCutoff = 0.05,  #指定 p 值阈值（可指定 1 以输出全部）
>     qvalueCutoff = 0.2)  #指定 q 值阈值（可指定 1 以输出全部）
> #输出富集结果
> write.table(gene_rich, 'gene_rich.txt', sep = '\t', row.names = FALSE, quote = FALSE)
> #再把 GO Ontology或KEGG levelA 信息添加在上述富集结果中
> tmp <- read.delim('gene_rich.txt')
> gene_ID <- gene_ID[!duplicated(gene_GO$ID), ]
> tmp <- merge(tmp, gene_GO[c('ID', 'GROUP')], by = 'ID')
> tmp <- tmp[c(10, 1:9)]
> tmp <- tmp[order(tmp$pvalue), ]
> #输出
> write.table(tmp, 'gene_rich.add_Ontology.txt', sep = '\t', row.names = FALSE, quote = FALSE)
> ```       

### 3.11 `VectorTableMerger.py [A-Bs] [B-Cs] [s1（可选）] [s2（可选）]`
                 
**功能描述：** 连接向量表：  
将表格：    
| GENE | CLA1 |          
| --- | --- |      
| G1 | A01;A02; A03 |      
| G2 | A02 |      
| G3 |   |      
| G4 | A04 |      
| G4 | A05 |   

以及     
| CLA1 | CLA2 |          
| --- | --- |      
| A01 | B1;B2 |      
| A02 |   |      
| A03 | B1;B3 |      
| G05 | B4 |    

合并为：    
| GENE | CLA2 |       
| --- | --- |     
| G1 | B3;B1;B2 |      
| G2 |   |      
| G3 |   |      
| G4 |   |      
| G4 | B4 |    

其中：原始表格第一列和第二列之间需要制表符隔开，第二列的项目分隔符不一定为”;“，可以自行指定。

- **A-Bs：** 表格一路径。 
- **B-Cs：** 表格二路径。 
- **s1：** 表格一第二列的分隔符。 
- **s2：** 表格二第二列的分隔符。  

**使用场景：** 当你获得了基因在X数据库中的注释信息（包括特定位点编号或基因名称），并且也知道X数据库中每个条目在Y数据库中的对应编号或名称时，可以使用本代码来获取基因在Y数据库中的对应名称。你可以将本代码视为VLOOKUP函数的一种变体，它同样适用于从A-B映射与B-C映射中推导出A-C映射的场景。      

**注意事项：** s1和s2参数必须同时指定！推荐不使用标题行，因为最后生成的内容标题行不一定出现在哪一行了！       

**生成文件：** 
- `A-Cs.table`（TABLE file, 连接后的表格）。
- `A-Cs_err.txt`（TABLE file, 无法在第二个表中匹配到的项目）。 

**示例：**

比如 `example` 有两个文件：
```
#A-Bs.txt
GENE	CLA1
G1	A01; A02; A03
G2	A02
G3	
G4	A04
G5	A05

#B-Cs.txt
CLA1	CLA2
A01	B1 ;B2
A02	
A03	B1;B3
A05	B4
```
执行命令：
```bash
#不指定第二列分隔符
python VectorTableMerger.py example/A-Bs.txt example/B-Cs.txt

#指定第二列分隔符（按照实际情况指定，本例都是分号）
python VectorTableMerger.py example/A-Bs.txt example/B-Cs.txt ; ;
```
将生成结果文件：
```
#A-Cs.table
GENE	CLA2
G1	B1;B3;B2
G2	
G3	
G4	
G5	B4

#A-Cs_err.txt
GENE	CLA1: not found!
G1	A01: not found!
G1	A03: not found!
G5	A05: not found!
```
  
## 4.Plotscript 绘图代码工具集。     

### 4.01 `GeneArrangementMap.py [GENE_LIST] [COLOR_CONFIG] [Vertical_spacing]`
     
**功能描述：** 根据不同的颜色来区分基因的线性排列，你可以使用其他更专业的工具绘制。

- **GENE_LIST：** List of gene sequences, TAB delimited. Each row represents a linear order of a genome. Different lines represent different genomes.
- **COLOR_CONFIG：** Color configuration table, TAB delimited. The RGB hexadecimal representation of the colors in the first column and the gene names in the remaining columns.
- **Vertical_spacing：** Spacing of adjacent row genomes, default 50.

**注意事项：** 本脚本仅供娱乐，不能反映特征的编码方向，只是使用简单的圆圈和方框进行简单拼接，适合在构建好系统发育树之后与本图片拼接到一起，后续会重写更具有观感的基因重排可视化脚本，本脚本不再更新。

**生成文件:** 
- `out.svg` （SVG file）。

**示例：**

比如 `example` 有两个文件：
```
#基因排布式：gene.txt
F	12S	V	16S	L	ND1	I	Q	M	ND2	W	A	N	C	Y	COX1	S	D	COX2	K	ATP8	ATP6	COX3	G	ND3	R	ND4L	ND4	H	S	L	ND5	CYTB	T	P	ND6	E	D-loop
F	12S	V	16S	L	ND1	I	Q	M	ND2	W	A	N	C	Y	COX1	S	D	COX2	K	ATP8	ATP6	COX3	G	ND3	R	ND4L	ND4	H	S	L	ND5	CYTB	T	P	ND6	E	D-loop
F	12S	V	16S	L	ND1	I	Q	M	ND2	W	A	N	C	Y	COX1	S	D	COX2	K	ATP8	ATP6	COX3	G	ND3	R	ND4L	ND4	H	S	L	ND5	CYTB	T	P	ND6	E	D-loop
...

#特征填充色：color.txt
#FFD966	F	V	L	I	Q	M	W	A	N	C	Y	S	D	K	G	R	H	S	L	T	P	E
#DDEBF7	12S	16S																				
#FFFF00	ND1	ND2	ND3	ND4L	ND4	ND5	ND6															
#FCE4D6	 COX1	 COX2	 COX3																			
#70AD47	ATP8	ATP6																				
#2F75B5	CYTB																					
#E7E6E6	D-loop	
```
执行命令：
```bash 
python GeneArrangementMap.py example/gene.txt example/color.txt 50
```
将生成svg文件，使用浏览器打开即可。

### 4.02 `TrnaStructureBeautifier.py [-h] -i INPUT [-s SIZE_WEIGHT] [-p PER_ROW] [-hg HORIZONTAL_GAP] [-vg VERTICAL_GAP] [-ac ADJACENT_COLOR] [-pc PAIR_COLOR] [-bf BASE_FILL] [-bs BASE_STROKE] [-A BASE_A] [-U BASE_U] [-G BASE_G] [-C BASE_C]`
         
**功能描述：** 对使用ViennaRNA包的RNAplot功能绘出的tRNA二级结构进行美化，如Mitos的注释结果非常适用本脚本。

**参数说明：** 

```bash
options:
  -h, --help            show this help message and exit
  -i, --input INPUT     SVG文件或者SVG文件存放的文件夹路径
  -s, --size-weight SIZE_WEIGHT
                        图形缩放比例（默认 1.4）
  -p, --per-row PER_ROW
                        每行图片数量（默认 4）
  -hg, --horizontal-gap HORIZONTAL_GAP
                        图片水平间隔（默认 8）
  -vg, --vertical-gap VERTICAL_GAP
                        图片垂直间隔（默认 5）
  -ac, --adjacent-color ADJACENT_COLOR
                        相邻碱基连线颜色（支持名称或 HEX，如 "blue" 或 "#00FF00"，默认 "blue"）
  -pc, --pair-color PAIR_COLOR
                        配对碱基连线颜色（支持名称或 HEX，如 "red" 或 "#FF0000"，默认 "red"）
  -bf, --base-fill BASE_FILL
                        碱基圆圈填充色（默认 "white"）
  -bs, --base-stroke BASE_STROKE
                        碱基圆圈轮廓色（默认 "black"）
  -A, --base-a BASE_A   美化A碱基圆圈填充色（默认 "red"）
  -U, --base-u BASE_U   美化U/T碱基圆圈填充色（默认 "blue"）
  -G, --base-g BASE_G   美化G碱基圆圈填充色（默认 "green"）
  -C, --base-c BASE_C   美化C碱基圆圈填充色（默认 "yellow"）        
```

**使用场景：** 已经得到SVG版本的tRNA二级结构初稿图，有美化和合并需求。

**注意事项：** ①脚本以第一个“-”前的文字做为RNA的名称（如果没有则是文件名称），在使用脚本之前需要注意调整文件名称格式；②只适合调用RNAplot绘制的二级结构图（比如Miotos软件）美化；③-i参数是必需的，可以是单个SVG文件，也可以是包含很多SVG文件的文件夹其他参数都有默认值可以根据出图效果调整参数！ ④如果出图有文字覆盖情况可以调整图片间隙和缩放比例，如果是微调建议使用adobe illustrator等软件对SVG文件进行编辑；⑤如果-i指定的是一个文件夹，文件夹里可以包含其他文件或文件夹，但是不能包含额外的SVG文件，比如使用Mitos绘图在plot文件夹里还包含rRNA的二级结构，需要将这些文件移除；⑥如果需要再次运行脚本可以将原来的modified文件夹清空或删除，虽然再次运行会对上次运行的结果产生覆盖，但是会多出莫名其妙的文件。

**视频教学：** https://www.bilibili.com/video/BV1FzbRzjERa/  

**生成文件：** 
- `modified`（文件夹，①modified_X.svg文件是单个二级结构的美化与原始文件一一对应，X处为原始文件名第一个“-”前的部分；②group_X.svg文件是同一行的组合图片；③final.svg文件是没有为碱基上色的组合图版本，个人比较偏向该版本的使用；④final_color.svg文件是为碱基上色的版本）。

**示例：**

文件夹中 `example/mitos_RNA_plot`是所有的tRNA二级结构图，`example/trnG.svg` 是单个图：
```bash
# 使用默认参数美化图片
python TrnaStructureBeautifier.py -i example/mitos_RNA_plot #指定一个文件夹  
python TrnaStructureBeautifier.py -i example/trnG.svg #指定一个文件  

# 使用全部配置参数
python TrnaStructureBeautifier.py -i example/mitos_RNA_plot -s 1.8 -p 6 -hg 12 -vg 7 -ac "red" -pc "#FF0000" -bf "#FFFF00" -bs "#000000" -A "#FF0000" -U "#0000FF" -G "#00FF00" -C "#FFFF00" 
```
即可在输出文件夹中生成结果，注意如果在组图中看到有tRNA缺失请不要惊慌，或许您通过浏览器打开用滚轮缩小界面就可以看到完整的图片了！  

## 5.BioDataSpider 生物学数据库爬虫工具模块。  

### 5.01 `GenoSpider`

**功能描述：** 基因组数据爬虫，详细说明见硕士毕业论文！  

**参数说明：** 

```bash
#工具包括两种执行方式，分为交互模式和命令行模式。其中命令行模式只支持单一分类流程化输入和输出，交互式包含更个性化的运行方式。

#命令行模式
python GenoSpider.py [-h] [-s] [-f {jpg,png,svg,eps}] [-p PIXELS] [-r] [-u] [-w WIDTH] [-H HEIGHT] [-g GAP] [-n NAME] [-i TID] [-l LEVEL]

##输入“python GenoSpider.py -n Aves -u -r -l superorder”即可得到鸟纲的所有参考基因组信息

##GenoSpider.py -h=[输出帮助信息] -s=[简化组装信息表信息，开关参数，默认否]
##-f=[输出图片格式，可选择jpg, png, svg, eps中的一种，默认jpg]
##-p=[输出图像像素，默认300] -r=[只输出参考基因组，开关参数，默认否]
##-u=[离线模式，开关参数，默认否] -l=[输出图像所统计的阶元等级]
##-w=[图片宽度，默认8] -H=[图片高度，默认10] -g=[子图间隔，默认0.4]
##-n=[拉丁名，与-i只需指定其中一个] -i=[物种ID，与-u只需指定其中一个]

#交互模式
python GenoSpider.py

##不加参数运行“python GenoSpider.py”启用交互模式，进入交互模式可以在面板中输入对应的功能序号或者功能名称执行对应操作。

>> 功能序号	功能名称	对应操作
>> 1    getTaxInfoFromName      Get taxonomic information for Scientific name of species.
>> 2    getTaxInfoFromNameList  Get taxonomic information for all species in a list.
>> 3    getTaxInfoFromTid       Get taxonomic information for Tax ID of species.
>> 4    getTaxInfoFromTidList   Get taxonomic information for Tax ID in a list.
>> 5    getAssembleFromName     Get information about all genomes in a given category. It is not recommended due to the occurrence of species with the same name.
>> 6    getAssembleFromTid      Get information about all genomes in a given Tax ID.
>> 7    getAssembleFromTidList  Get information about all genomes in a given Tax ID in a list.
>> 8    getTaxInfoFromAssemble  The taxonomic information is obtained from the assembly information file. This is equivalent to the getTaxInfoFromTidList being triggered automatically after manually executing the command to get the assembly information.
>> 9    mergeAssemble_TaxInfo   Merge assembly information and species classification information files.
>> p    dataVisualization       Output visual image.
>> c    com     Output a list of all functions.
>> h    help    Get complete help information.
>> f    settingOutputFormat     View or configure the output format.
>> e    exit    exit the program.
```

**注意事项：** 需要安装requests、pandas和matplotlib库！  

### 5.02 `PrideSpider.py [SP_LIST]`   

**功能描述：** 用于爬取PRIDE数据库信息的爬虫！  

- **SP_LIST：** 物种拉丁名/常用名，每一行是一个物种。

**注意事项：** 目前实现了批量下载json格式结果，后续会更新解析json的功能。  

**生成文件：** 
- log.txt (日志文件，可以查看物种拉丁名/常用名下有多少个信息条目，如果由于网络原因，可以查看哪些物种已经跑过了就不用重复请求数据)  
- json_result (文件夹，内含爬取的json格式信息，文件名以“拉丁名-页码”的形式命名)   

**示例：**

文件夹中 `example/sp.txt`是几个物种的拉丁名：
```
Acipenser ruthenus
Danio rerio
Leucoraja erinaceus
```
执行命令：
```bash
python PrideSpider.py example/sp.txt
```
就可以下载所有内容了，爬取的内容是json格式，你可以使用AI编写一个解析脚本，也可以直接应用在你的网页中。




==============      
**Author: Hao Xue**     
**E-mail: studid@163.com**   
**引用：没有文献可以引用，如果对您科研工作有帮助的话，偷偷夸我厉害就行。**   
如果必须要引用可以在您的著作中添加："我们使用了 BioDataTools 工具 (https://github.com/shueho/BioDataTools) 进行生物信息学分析"    
如果是英文著作："We used BioDataTools (https://github.com/shueho/BioDataTools) for sequence analysis."    
如果在毕业论文中引用：  
[1] 薛浩,  大石鸡（Alectoris magna）基因组结构与比较基因组分析[D]. 烟台: 烟台大学, 2024.               
        
<a href="https://orcid.org/0000-0001-9708-3575" target="_blank" rel="noopener noreferrer me">
  <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" alt="ORCID iD icon" style="width: 1em; margin-inline-start: 0.5em" />
  https://orcid.org/0000-0001-9708-3575
</a>


