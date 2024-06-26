# BioDataTools

这是一套生物信息学脚本，结合了组学和生态遗传分析，支持多种数据处理工具，适应广泛的研究需求。

## 1. Metagenome 宏基因组分析相关脚本
   
### 1.01 `get_sum.py [DIR_PATH]`

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
python get_sum.py example/quast
```
输出结果文件 `summary.tsv`，内容示例：
```
Sample    N50    Total Length    # Contigs    Largest Contig    GC (%)    ...
sp1       10000   5000000         100           25000       42.3      ...
sp2       12000   5500000         85            30000       41.7      ...
sp3       15000   6000000         70            40000       43.1      ...
```

### 1.02 `fasta_rename.py [FASTA_FILE_PATH]` 

**功能描述：** 对FASTA格式序列文件中各个序列标头进行统一命名规范，确保每个序列标识唯一且编号连续。

- **FASTA_FILE_PATH：** 原FASTA文件路径。

**使用场景：** 在宏基因组等组学分析项目中，该脚本通过统一重命名各FASTA文件中的序列ID为连续数字（1, 2, 3...），确保合并样品组装数据时标识唯一性，为后续基因丰度分析及注释规范序列名称，便于差异基因追踪及原始序列比对。

**注意事项：** 本代码只适用于后续不再讨论原始序列标识的场景，切勿在定量、注释等下游分析后使用该脚本！

**生成文件：** 
- `out_<原始FASTA文件名称>`（FASTA文件，各个序列被重新编码）。    

**示例：**

比如 `example/origin_seq.fa` 文件中包含重复标识的序列，执行命令：
```bash
python fasta_rename.py example/origin_seq.fa
``` 
输出结果文件 `out_origin_seq.fa` ，即为序列标识唯一的FASTA文件。

### 1.03 `mergeMpa.py  [MPA_PATH]` 

**功能描述：** 此脚本能够将多个MPA文件转换为单一的物种丰度矩阵。

- **MPA_PATH：** 存放所有样品的MPA文件的路径。

**注意事项：** 本脚本支持处理由Kraken 1、Kraken 2或Bracken输出的MPA文件目录。运行前，请先利用kreport2mpa.py脚本将结果转换为MPA格式。重要的是，所有MPA文件必须基于相同的核酸数据库生成，因为物种丰度的排列顺序取决于所选数据库，确保数据一致性。

**生成文件：** 
- `mpaMatrix.txt`（表格文件，物种丰度表，每一列都表示一个样品）。   

**示例：**

比如 `example/mpa` 文件中包含重复标识的序列，执行命令：
```bash
python mergeMpa.py example/mpa
``` 
输出结果文件 `mpaMatrix.txt` 即为物种丰度矩阵。

### 1.04 `splitFromLevel.py [MPA_MERGE_FILE] [SPLIT_LEVEL]` 

**功能描述：** 该脚本物种丰度表中提取各分类阶元的物种丰度数据并构建相应的丰度矩阵。

- **MPA_MERGE_FILE：** 由 `1.03 mergeMpa.py` 脚本生成的 `mpaMatrix.txt` 文件路径，也可以将您的丰度表修改为示例文件的样式。
- **SPLIT_LEVEL：** 要指定输出的物种丰度表格的分类级别，可使用以下单个字母标识：'a'（全级别）、'K'（界）、'P'（门）、'C'（纲）、'O'（目）、'F'（科）、'G'（属）、'S'（种），其中'a'表示输出所有分类阶元的丰度表。大写或小写字母均可。

**生成文件：** 
- `taxLevel_<指定的阶元等级（大写）>_output.<丰度矩阵文件名>`（一个或多个表格文件，物种丰度表）。

**示例：**

比如 `example/mpaMatrix.txt` 文件中包含物种丰度信息，执行命令：
```bash
# 生成所有阶元等级的丰度数据运行：
python splitFromLevel.py example/mpaMatrix.txt a
# 输出7个阶元的结果文件：taxLevel_K/P/C/O/F/G/S_output.mpaMatrix.txt。

# 只生成科阶元的丰度数据运行：
python splitFromLevel.py example/mpaMatrix.txt f
# 只输出一个结果文件：taxLevel_F_output.mpaMatrix.txt。
```
即可输出对应的1个或7个结果。

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
             

## 2. Genetics 用于基因组和比较基因组学研究中的数据处理，涵盖从NCBI批量获取数据，以及批量提取和批量转化数据信息内容的脚本。           
 
### 2.01 `Get_gb_by_gi.py [GI_LIST_DIR]`

**功能描述：** 通过GI编号批量下载fasta文件。

- **GI_LIST_DIR：** 存放GI编号的目录路径，脚本自动检测并读取文件夹内所有以 `_gi.txt` 为扩展名的文本文件。这些 `_gi.txt` 文件包含待下载序列的GI编号。

**使用场景：** 为批量下载大量GenBank（gb）文件，您仅需简便地创建若干个“xxx_gi.txt”文件，每文件内粘贴相应的GI编号列表。此设计灵活性高，根据不同的GI编号列表文件，以列表文件名对结果文件进行区分。方便后续将不同分组文件分类归档，极大便利了群体遗传学中常见的单倍型分析任务。

**注意事项：** 需要安装requests库！

**生成文件：** 
- `gb/<列表名称>_<GI编号>.gb`（在 `gb` 文件夹下生成多个GENEBANK文件）。

**示例：**

比如 `example/gi` 文件中存放有需要下载序列的GI编号，执行命令：
```bash
python Get_gb_by_gi.py example/gi
``` 
输出文件夹 `gb` ，其中包括以列表名称为前缀的5个gb文件，示例文件 `example/gb_isolate` 即为生成结果参考。

### 2.02 `Name_gb_by_isolate.py [GB_DIR] [INFO_NAME]`

**功能描述：** 读取GB文件内的某一样品信息（如isolate信息），并依据这一信息为对应的GB文件重新命名，适用于群体遗传学分析中对大批量GB文件进行统一管理和组织。

- **GB_DIR：** 存放GB文件的目录路径。
- **INFO_NAME：** 需要对GB文件名称修改的参考信息，务必保证不同GB文件中该样品信息是唯一的。

**注意事项：** 务必使用可以区分所有GB文件的信息！每次运行最好手动将上次运行产生的文件删除或重命名。

**生成文件：** 
- `output/<样品信息对应的值（空格以下划线替换）>.gb`（`output` 文件夹下的多个GENEBANK文件）。

**示例：**

比如 `example/gb_isolate` 文件和 `example/gb_orgnism` 文件中分别包含以 `isolate` 和 `orgnism` 信息区分的多个样品GB文件，可以执行：
```bash
# 以isolate信息命名运行：
python Name_gb_by_info.py example/gb_isolate isolate

# 以orgnism信息命名运行：
python Name_gb_by_info.py example/gb_organism organism
```
即可输出对应的结果于文件夹 `output` 中。
     
### 2.03 `gb_to_fasta.py [GB_DIR]
`
**功能描述：** 批量地将GB文件转换为FASTA格式，并且在转换过程中，将原GB文件的文件名插入到FASTA格式序列记录的描述行（“>”后面的部分），以便于追踪源文件信息。这对于高效处理大量的GB文件，在进行诸如群体遗传学分析等工作时尤为重要。

- **GB_DIR：** 存放GB文件的目录路径。

**生成文件：** 
- `output/<原GB文件名>.fas`（多个FASTA文件）。 

**示例：**

比如需要将 `example/gb_isolate` 文件中GB文件转换为FASTA文件，执行命令：
```bash
python gb_to_fasta.py example/gb_isolate
``` 
即可输出对应的结果于文件夹 `output` 中。

> ## 群体遗传学分析快速下载数据流程          
> 比如要从NCBI下载特定多个群体的 `cox1` 基因，可以先创建一个文件夹，分别列出该群体不同个体的 `cox1` 基因的GI编号（可以在NCBI直接导出），并将每个群体的编号保存在独立的xxx_gi.txt文件中；接着运行脚本2.01来下载相应的GB文件；再运行脚本2.02，依据isolate或其他标签对下载的GB文件进行重命名；最后执行脚本2.03，从而生成以标签值为名称的最终FASTA格式序列文件。

### `2.04 Merge_dif_seq.py [FASTA_FILE_1] [FASTA_FILE_2]`

**功能描述：** 合并序列的低级版本，后续会提供该脚本的进阶版本（脚本2.14）。

- **FASTA_FILE_1：** 第一个序列。
- **FASTA_FILE_2：** 第二个序列。

**使用场景：** 假设你有来自样本A、B和C的16S和COI序列，出于某种目的，你想要结合来自不同样本的16S和COI序列。您可以使用这个脚本。

**多次调用：** 如果要合并多个序列，可以重复调用此脚本。

**注意事项：** 务必在比对后的序列文件中使用该脚本！

**生成文件：** 
- `merge.fas`（合并后的FASTA文件）。

**示例：**

比如 `example/fasta_merge` 目录中包含需要合并的序列 `16s.fasta` 和 `co1.fasta`，执行命令：
```bash
python Merge_dif_seq.py example/fasta_merge/16s.fasta example/fasta_merge/co1.fasta
``` 
输出结果文件 `merge.fas` ，即为16s+co1合并序列。

### 2.05 `S_to_H.py -p [FASTA_FILE_NAME] -l [LIST_NAME]`

**功能描述：** 将FASTA文件中多个样品序列根据单倍型归类。

- **FASTA_FILE_NAME：** 样品序列文件名（参照example/sample.fas）。
- **LIST_NAME：** 单倍型对应样品的表格（参照example/hap.list）。

**参数说明：** 使用前需要获取两个文件，一个是DnaSP导出的单倍型和样品对应的表格（可能需要手工制作）。另一个是包含所有物种序列的fasta文件。

**使用场景：** 比如，对于包含a、b、c、d、e五个样品的序列数据，其中样品a、b、c的序列完全相同，样品d和e的序列也完全一致，意味着我们拥有两个独特的单倍型。借助这段代码，能够将具有相同序列的样品合并归类为各自的单倍型，有利于后续针对不同单倍型序列进行系统发育分析。参考示例文件和示例代码！！！      

**生成文件：** 
- `out_hap.fasta`（由单倍型组成的FASTA文件）。

**示例：**

比如 `example/sample.fas` 文件是各个样品的序列文件， `example/hap.list` 文件是单倍型对应样品的表格，执行命令：
```bash
python S_to_H.py -p example/sample.fas -l example/hap.list
``` 
输出结果文件 `out_hap.fasta` ，即为单倍型序列文件。

### 2.06 `ExtractFasta.py [FASTA_FILE] [LIST_FILE] [Regular_expressions (Optional)]`

**功能描述：** 依据提供的ID列表，该脚本能从一个整合多序列的FASTA文件中抽取出相应序列，生成子FASTA文件。默认配置下，系统识别">"符号后至首个空格前的文本为ID，与列表中的条目匹配。针对复杂情况，支持自定义正则表达式以实现ID的精准匹配，确保灵活高效地筛选目标序列。

- **FASTA_FILE：** Fasta格式的序列文件，也就是包括所有序列的文件，比如全基因组的pep或者CDS序列。
- **LIST_FILE：** 列表中应包含希望提取的序列编号或名称，这部分信息可以是FASTA_FILE中每条序列“>”符号后紧跟的整个描述字段，也可以只是该描述字段中的一部分内容。
- **Regular_expressions：** 可选参数，假如你的列表中的名称与FASTA文件序列名称有所不同，你可以指定正则表达式对序列进行提取。如果没有填写，默认为："\_(.*?)".，这意味着你将“>”之后第一个空格前的内容作为ID名称。

**使用场景：** 在进行共线性分析或同源基因分群时，频繁遇到从NCBI获取的pep文件含有大量冗余数据。为优化此过程，可选择性下载仅涵盖染色体编码的非冗余蛋白质序列数据库。此脚本特地设计用来根据用户提供的序列名称，从庞大的pep文件中抽取出所需片段。此外，它还支持抽取对应的编码序列（CDS），考虑到蛋白质序列ID与CDS ID间可能存在的差异，引入正则表达式自定义匹配规则显得尤为重要。如需进一步简化流程，推荐采用升级版代码2.09，该版本同样能有效执行此类抽取任务。

**生成文件：** 
- `out_match_seq.fasta`（FASTA文件）。

**示例：**

比如 `example/text.fa` 是完整的FASTA文件，执行命令：
```bash
# 如果你所需要提取的序列名称是第一个空格前的内容，尤其是针对那些直接从NCBI下载的fasta文件，你可以直接运行：
python ExtractFasta.py example/text.fa example/list1.txt

# 常用！如果你所需要提取的序列名称是>后的所有内容，你可以直接运行：
python ExtractFasta.py example/text2.fa example/list2.txt "\>(.*)"

# 如果使用正则表达式提取：
python ExtractFasta.py example/text.fa example/list2.txt "\_(.*?) "
```
即可输出对应的子序列文件。

### 2.07 `ProteinPropertyFromExpasy.py [FASTA_FILE]`

**功能描述：** 从Expasy（ https://web.expasy.org/protparam ）中批量获得蛋白质的理化性质。

- **FASTA_FILE：** 提供蛋白质序列的FASTA格式，可以是包含多个序列的文件。

**生成文件：** 
- `expasy_output.csv`（表格文件，包含部分蛋白质序列的理化性质）。

**示例：**

比如 `example/text.fa` 是蛋白序列的FASTA文件，执行命令：
```bash
python ProteinPropertyFromExpasy.py example/text.fa
``` 
即可输出对应结果。

### 2.08 `FeaturesBaseComponents.py [FASTA_FILE] [TABLE]`

**功能描述：** 细胞器基因组专用，特征提取和碱基组成统计。如果你想基于开始和结束位置截断fasta文件，你也可以使用这个脚本!  

- **FASTA_FILE：** 只包含一个序列的fasta文件。
- **TABLE：** 表格包含特征名称、组别和起始位置的表。第一列为基因组，第二列为基因，第三列为基因起始位置，第四列为基因终止位置。基因是名义上的概念，你可以给任何片段分配分组。

**注意事项：** 如果序列中含有中间终止密码子慎用，并且如果不是+链编码的基因会提取到其反向互补序列。

**生成文件：** 
- `ex_seq.fasta`（FASTA文件，提取到的小片段序列）。
- `Base_composition.txt` （表格ATGC的碱基占比）。

**示例：**

比如 `example/all.fa` 是小片段序列的FASTA文件， `example/matrix.txt` 是特征位置矩阵，执行命令：
```bash
python FeaturesBaseComponents.py example/all.fa example/matrix.txt
``` 
即可输出对应结果。

### 2.09 `ExAndRename.py [MAP_FILE] [FASTA_FILE]`

**功能描述：** 从FASTA文件中提取部分序列，并对这些序列按照规则修改名称。

- **MAP_FILE：** 在提供的信息中，第一列所列出的是欲提取或重命名的序列名，它对应fasta文件中“>”符号之后，首个空格之前的文本内容；若无空格，则为“>”符号之后的完整序列标识符。第二列则是期望修改为目标的新名称。当第一列与第二列内容相同时，这一操作相当于执行代码2.06的功能。
- **FASTA_FILE：** Fasta格式的序列文件，也就是包括所有序列的文件，比如全基因组fa文件、pep或者CDS序列。

**使用场景：** 适用于从全基因组序列中提取染色体并修改名称。

**生成文件：** 
- `subset_fasta.faa`（FASTA文件，如果在map表存在多余的内容会有提示）。              

**示例：**

```bash
python ExAndRename.py example/map.txt example/text.fa
``` 
       
### 2.10 `BatchFastaToPam.py [FASTA_FILE_DIR]`

**功能描述：** 批量将比对过的FASTA文件转换为paml比对文件。

- **FASTA_FILE_DIR：** 文件夹路径名，在该目录下包含需要转换的FASTA格式的比对文件。

**注意事项：** 文件夹中不能包含未比对的序列文件，也不能有其他文件，否则将会报错！

**生成文件：** 
- `pamlfile`（文件夹，其中包含需要转换的fasta文件名+pam后缀）。      

**示例：**

```bash
python BatchFastaToPam.py example/ali_fasta
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

```bash
python ReassignSequence.py example/ali_fasta example/seq_matrix.txt out
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

```bash
python BatchAlignedProteinToDNA.py -c example/cod.txt -m example/SequenceIDs.txt -p example/pep -C example/cds -s "fa" -S "fna"
```  

### 2.13 `Extract4DTv.py [-h] [-c CODON] [-m MAPFILE] [-p PEP] [-C CDS] [-s SUFFIX_P] [-S SUFFIX_C]`

**功能描述：** 批量提取蛋白质序列比对结果中的4DTv（四倍简并位点）。

**参数说明：** 所有参数均与脚本2.12一致，代码内容其实差不多，只是生成的文件名称不同。

**使用场景：** 同源基因建树。

**生成文件：** 
- `4dtv`（文件夹，用于存放提取到的4DTv位点，运行上述命令生成的文件参考example/4dtv）。 
- `err_4dtv.txt`（错误日志文件，显示过滤掉的序列，如果没有错误的序列将不生成）。

**示例：**

```bash
python Extract4DTv.py -c example/cod.txt -m example/SequenceIDs.txt -p example/pep -C example/cds -s "fa" -S "fna"
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

```bash
# 运行下列代码将不指定顺序全连接：
python MergeSequences.py example/seq_matrix2.txt example/4dtv

#若指定连接顺序运行下列代码：
python MergeSequences.py example/seq_matrix2.txt example/4dtv example/order.txt
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

```bash
python BatchGenerationCodeML_CTL.py example/paml_file "./out/a.tree"
```

### 2.16 `ParsingCodeMLResults.py [MOD0_DIR] [MOD2_DIR] `

**功能描述：** 批量解析CodeML结果，如果以2.15生成的脚本，结果会生成在m0和m2文件夹中。

- **MOD0_DIR：** 基于无效假设生成的结果。
- **MOD2_DIR：** 基于替代假设生成的结果。

**生成文件：** 
- `result.txt` （表格，可能需要手动整理） 。

**示例：**

```bash
python ParsingCodeMLResults.py example/codeml/m0 example/codeml/m2
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

```bash
python SplitAXT.py example/test.axt
          
# 有时你也许需要批处理。
for i in `ls *axt`;do python SplitAXT.py $i ;done
```

> ## 比较基因组学-同源基因建树和选择压力分析流程（二）          
> 你可以参考 https://yanzhongsino.github.io/2022/09/07/bioinfo_Ks_batch.calculation.Ks 来计算 Ka、Ks和4dtv值，由于calculate_4DTV_correction.pl脚本只支持一对序列的4dtv计算，因此可以使用脚本2.17对AXT文件进行拆分。                 

### 2.18 `BaseSiteInformation.py [GFF_FILE] [Q_FILE]`

**功能描述：** 根据指定染色体位置及碱基位点信息，抽取相应的基因数据，比如位点在哪一个转录本上的哪一个CDS区间中，以及CDS或转录本的位置信息，方便后续注释分析。

- **GFF_FILE：** 基因组GFF文件，只需要保留mRNA和CDS特征，并且每个mRNA需要位于其包含CDS特征的上方，可以选择在运行代码前手动将GFF文件排序！
- **Q_FILE：** 查找的条目表格，需要包括标题行，至少包含两列：第一列必须是染色体编号，第二列是对应于染色体上的位置。

**使用场景：** 通过随机森林等算法找到不同种群或不同品种的变异位点，需要定位到该位点所在基因。

**生成文件：** 
- `out_<Q_FILE参数值>.xls`（表格，第一、四列为基因名称，第二列是是否为CDS区域CDS/noCDS，第三列为CDS的起始终止位置以及ORF起始位点，第五列是染色体ID，然后是基因起始位置、得分以及基因CDS数目） 。

**示例：**

```bash
python BaseSiteInformation.py example/genome.gene.gff example/base_loc.txt
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

```bash
# 默认替换为N。
python MaskSeq.py example/Chr.fa example/masktbl.txt

# 替换为?。
python MaskSeq.py example/Chr.fa example/masktbl.txt "?"
```

### 2.20 `BaseCompositionCalculation.py [FASTA_FILE] [TER_CODE 可选参数]`
       
**功能描述：** 计算CDS序列中各个序列的各个位点的碱基数目，如A1、T1、G1、G3等。

- **FASTA_FILE：** Fasta文件，里边包含许多序列，要求是核酸序列。
- **TER_CODE：** 终止密码子列表，默认是标准密码子表的TAG,TAA,TGA，如果需要指定，需要保证每个终止密码子之间用半角英文逗号隔开且不含有过多空白，如果你希望统计到终止密码子你可以输入NNN。

**使用场景：** 进行密码子偏好分析时需要获取GC12和GC3等参数可以通过本脚本结果进一步计算。          

**生成文件：** 
- `BaseComposition.txt`（表格文件，包括各个位点的碱基数目，最后一列是碱基总数） 。

**示例：**

```bash
# 默认去除标准终止密码：
python BaseCompositionCalculation.py example/base_cds.fa

# 希望统计到终止密码：
python BaseCompositionCalculation.py example/base_cds.fa NNN

# 自定义终止密码：
python BaseCompositionCalculation.py example/base_cds.fa TGA,TAA
```


## 3. Gadget 一些通用的文本处理和分析工具，以及与富集注释分析相关的代码。

### 3.01 `MergeTable.py`

***图形界面的合并表格工具***

**功能描述：** 合并多个表格时，可以根据它们的第一列数据进行对应联接操作。

**参数说明：** 不需要配置参数。将所有需要依据首列进行合并的表格逐一导入，并通过相应功能一键实现按第一列内容的合并操作。

**注意事项：** 只支持图形化系统。

**示例：**

```bash
python MergeTable.py
```

### 3.02 `VLookup.py [KEY_FILE] [MAP_FILE] [KEY_LOC] [VALUE_LOC] [SEP]`

**功能描述：** vlookup函数的Python实现。可以自定义键值的位置。

- **KEY_FILE：** 一个文件，包含需要检索值的列。   
- **MAP_FILE：** 在其中检索的表格，需要至少有两个列，其中一个是key，另外一个是值。        
- **KEY_LOC：** 键列在MAP_FILE表格中位于的列号，比如第一列是key填写1。   
- **VALUE_LOC：** 值列在MAP_FILE表格中位于的列号，比如第一列是value填写1。    
- **SEP：** MAP的制表符，比如制表符分隔填写"\t"，注意引号是英文的。   

**使用场景：** 从总注释表中提取一些基因的注释信息。注意这个只能提取一列内容。       

**生成文件：** 
- `map_<map file name>`（TABLE file）。

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

```bash
python SumByGroup.py example/map.txt example/matrix.txt 1 0
```

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

**使用场景：** 比如在生物过程中包括三个GO术语，这三个术语之间存在交集基因，你想统计生物过程下一共的基因数目（去重的）。

**注意事项：** -a和-b参数是必需的，其他参数都有默认值！

**生成文件：** 
- `count_Map.txt`（表格文件）。

**示例：**

```bash
python CountByGroup.py -a example/map.txt -b example/map2.txt -n 1 -k 1 -v 0
```

### 3.05 `splitFasta.py [FASTA_FILE_PATH] [Number_of_split_files]`
       
**功能描述：** 针对含有大量序列的FASTA文件，可根据序列数量对其进行分割，形成多个较小的FASTA文件。

- **FASTA_FILE_PATH：** 要分割的FASTA文件的路径。
- **Number_of_split_files：** 分割完成后每个文件包含的序列数。

**使用场景：** 例如，在进行在线KEGG注释时，KEGG服务可能对一次上传的序列数目有所限制，通过预先分割大的FASTA文件，可以确保符合上传要求并顺利完成注释任务。

**生成文件：** 
- `<拆分后的文件编号>_<原FASTA文件>`（多个FASTA文件）。   

**示例：**

运行下列代码将7个序列的fasta文件分为3个2序列的文件（不够整除最后一个文件只有一个序列）。
```bash
python splitFasta.py example/text.fa 2
```

### 3.06 `read_keg.py [KEG_FILE]`
   
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
python read_keg.py example/ko00001.keg

# 比如解析人类keg文件：
python read_keg.py example/hsa00001.keg
```

### 3.07 `KEGG_pathway_geneNum.py [3.06_生成文件_1] [GENE_KO]`
    
**功能描述：** KEGG通路基因数量统计，导出用于KEGG注释富集绘图的数据。

- **3.06_ 生成文件_1：** 脚本3.06的生成文件。
- **GENE_KO：** GENE-KO映射表，第一列是基因ID或名称，第二列为ko编号（或其他通路编号），多个ko编号可以用逗号隔开，可参考示例文件。


**生成文件：** 
- A.txt (all_gene is the total number of genes, and you can use this number to find the gene ratio. TABLE file)  
- A-B.txt (TABLE file)   
- A-C.txt (TABLE file)   
- err.txt (There is no matching KO number. TABLE file)

**示例：**

```bash
python KEGG_pathway_geneNum.py example/output_ko00001.txt example/gene_ko.txt
```

### 3.08 `read_goOBO.py [obo_FILE]`

**功能描述：** 从obo文件读取并解析GO号对应的描述及分类，生成GO编号\t描述信息\t分类的三列表格，你可以直接使用示例文件中的go_term_list.txt，要注意这个文件可能不是最新的版本，因此推荐使用该脚本提取最新的GO注释信息。

- **obo_FILE：** GO网站上下载的obo文件路径（打开网址：https://purl.obolibrary.org/obo/go/go-basic.obo 推荐打开网页后，右键，点击另存为，保存为文本文件） 。

**注意事项：** 由于网页加载可能不全因此不推荐将网页CTRL+A全选CTRL+C复制，新建txt文件并打开CTRL+V粘贴。

**生成文件：** 
- `<版本号>_go_term_list.txt`（TABLE文件，第一列是GO号，第二列是描述信息，第三列是分类）

**示例：**

比如你将网页复制或保存到了abc.txt，你可以运行下方代码：
```bash
python read_goOBO.py abc.txt
```

### 3.09 `ConvertGene-GO.py [GENE_GOs_MAP]`
                 
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

```bash
python ConvertGene-GO.py example/seq_gos.txt
```
      
### 3.10 `getGOinfo.py [go_term_list] [GENE_GO_MAP]`
                 
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

使用时需要按照3.08生成表格文件xxx-go_term_list.txt，示例中的2024-01-17_go_term_list.txt是版本2024-01-17。建议通过3.08代码获取最新的版本。
```bash
python getGOinfo.py example/2024-01-17_go_term_list.txt example/gene_go.txt
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

### 3.11 `GenoSpider`

**功能描述：** 基因组数据爬虫，详细说明待补充！       

## 4.Plotscript 绘图代码工具集。     

### 4.01 `geneArrangementMap.py [GENE_LIST] [COLOR_CONFIG] [Vertical_spacing]`
     
**功能描述：** 根据不同的颜色来区分基因的线性排列，你可以使用其他更专业的工具绘制。

- **GENE_LIST：** List of gene sequences, TAB delimited. Each row represents a linear order of a genome. Different lines represent different genomes.
- **COLOR_CONFIG：** Color configuration table, TAB delimited. The RGB hexadecimal representation of the colors in the first column and the gene names in the remaining columns.
- **Vertical_spacing：** Spacing of adjacent row genomes, default 50.

** 生成文件:** 
- `out.svg` （SVG file）。

**示例：**

```bash
python geneArrangementMap.py example/gene.txt example/color.txt 50
```





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
