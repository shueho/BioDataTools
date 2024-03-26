library(clusterProfiler)

#读取手动准备好的背景基因集
gene_GO <- read.delim('gene_GO.txt', stringsAsFactors = FALSE)

#读取基因列表文件中的基因名称
genes <- read.delim('gene.txt', stringsAsFactors = FALSE)$gene_id

#GO 富集分析
go_rich <- enricher(gene = genes,  #待富集的基因列表
                    TERM2GENE = gene_GO[c('ID', 'gene_id')],  #背景基因集
                    TERM2NAME = gene_GO[c('ID', 'Description')], 
                    pAdjustMethod = 'BH',  #指定 p 值校正方法
                    pvalueCutoff = 1,  #指定 p 值阈值（可指定 1 以输出全部）
                    qvalueCutoff = 1)  #指定 q 值阈值（可指定 1 以输出全部）

#输出富集结果
write.table(go_rich, 'go_rich.txt', sep = '\t', row.names = FALSE, quote = FALSE)

#再把 GO Ontology 信息添加在上述 GO 富集结果中
tmp <- read.delim('go_rich.txt')
gene_GO <- gene_GO[!duplicated(gene_GO$ID), ]
tmp <- merge(tmp, gene_GO[c('ID', 'ONTOLOGY')], by = 'ID')
tmp <- tmp[c(10, 1:9)]
tmp <- tmp[order(tmp$pvalue), ]

#输出
write.table(tmp, 'go_rich.add_Ontology.txt', sep = '\t', row.names = FALSE, quote = FALSE)

