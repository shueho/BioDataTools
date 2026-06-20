#!/usr/bin/env Rscript
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2026/6/20 14:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : CodonPositionBaseStats.R
#
# Calculate the count or frequency of A/T/G/C nucleotides at the three positions of each codon, with optional codon filtering. 

pcg = "pcgs.fa" #cds序列路径
codonTable = 5 # 密码子表
stp_del = TRUE  # 是否删除终止密码子，FALSE是不删除
codon_del = 2 # 进行密码子过滤，0不过滤，1过滤单氨基酸密码子，2过滤非四倍简并密码子

packages <- c("seqinr", "dplyr")
cran_mirror <- "https://mirrors.tuna.tsinghua.edu.cn/CRAN/"
for (pkg in packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    cat("Installing package:", pkg, "\n")
    install.packages(pkg, dependencies = TRUE, repos = cran_mirror)
  }
}
invisible(lapply(packages, require, character.only = TRUE))


library(seqinr) #READFASTA
library(dplyr)


# 01.读取fasta文件，得到PCGs的CDS序列
extract_first_three <- function(strings) {
  substr(strings, 1, 3)
}
extract_last_chars <- function(strings) {
  len <- nchar(strings)
  remainder <- len %% 3
  start_pos <- len - (ifelse(remainder == 0, 2, remainder - 1))
  substr(strings, start_pos, len)
}
read_fasta_to_df <- function(fasta_file) {
  sequences <- read.fasta(fasta_file, as.string = TRUE)
  result_df <- data.frame(
    GENE = names(sequences),
    SEQ = as.character(gsub("T", "U", toupper(sequences))),
    LEN = nchar(as.character(sequences)),
    stringsAsFactors = FALSE
  )
  result_df$STA = extract_first_three(result_df$SEQ)
  result_df$TER = extract_last_chars(result_df$SEQ)
  return(result_df)
}

fasta_df <- read_fasta_to_df(pcg)
write.csv(fasta_df, file = "01-sequences.csv", row.names = FALSE)

# 02.获得所有PCGs的密码子使用情况
calculate_gene_codon_frequency <- function(gene_data) {
  gene_name_col <- colnames(gene_data)[1]
  sequence_col <- colnames(gene_data)[2]
  result_list <- list()
  for (i in 1:nrow(gene_data)) {
    gene_name <- as.character(gene_data[[gene_name_col]][i])
    seq <- as.character(gene_data[[sequence_col]][i])
    len <- nchar(seq)
    full_length <- len - (len %% 3)
    codons <- strsplit(substr(seq, 1,full_length), "(?<=.{3})", perl = TRUE)
    codon_count <- table(codons)
    total_codons <- sum(codon_count)
    codon_freq <- codon_count / total_codons
    gene_freq <- data.frame(
      gene_name = gene_name,
      #codon = names(codon_freq),
      count = codon_count,
      frequency = as.numeric(codon_freq),
      stringsAsFactors = FALSE
    )
    result_list[[i]] <- gene_freq
  }
  result <- do.call(rbind, result_list)
  rownames(result) <- NULL
  return(result)
}
codon_freq <- calculate_gene_codon_frequency(fasta_df)
write.csv(codon_freq, file = "02-Codon_occurrence_in_all_gene.csv", row.names = FALSE)

# 03.获得所有PCGs，以及整体的密码子使用情况
#translate(as.character(codon_freq$count.codons),numcode=codonTable)
codon_freq$A = translate(unlist(strsplit(gsub("U","T",codon_freq$count.codons), "")),numcode = codonTable)
codon_freq$AAA = aaa(codon_freq$A)
#write.csv(codon_freq, file = "02-Codon_Freq.csv", row.names = FALSE

generate_codon_list <- function() {
  bases <- c("U", "C", "A", "G")
  codons <- character()
  
  # 三重循环生成所有密码子组合
  for (i in 1:length(bases)) {
    for (j in 1:length(bases)) {
      for (k in 1:length(bases)) {
        codon <- paste(bases[j], bases[i], bases[k], sep = "")
        codons <- c(codons, codon)
      }
    }
  }
  
  # 返回标准顺序的密码子列表
  return(codons)
}
getCodonList = function(con_num){
  codon_list <- generate_codon_list()
  dic = data.frame(codon=codon_list)
  dic$A = translate(unlist(strsplit(gsub("U","T",dic$codon), "")),numcode = con_num)
  dic$AAA = aaa(dic$A)
  return(dic)
}
all_codon = getCodonList(codonTable)
all_codon$group = paste0(substr(all_codon$codon,1,2),"-",all_codon$AAA)
all_codon <- all_codon %>%
  group_by(group) %>%
  mutate(Freq = n()) %>%  # n() 统计当前group有多少行
  ungroup()

if(stp_del){all_codon = all_codon[all_codon$AAA != "Stp",]}
if(codon_del == 1){all_codon=all_codon[all_codon$Freq != 1,]}
if(codon_del == 2){all_codon=all_codon[all_codon$Freq == 4,]}
#codon_freq$group = paste(substr(codon_freq$count.codons,1,2),"-",codon_freq$AAA,sep = "")
std_codon_vec <- unique(all_codon$codon)
codon_freq <- codon_freq[codon_freq$count.codons %in% std_codon_vec, ]





codon_freq$A1 = ifelse(substr(codon_freq$count.codons,1,1) == "A", codon_freq$count.Freq, 0)
codon_freq$T1 = ifelse(substr(codon_freq$count.codons,1,1) == "U", codon_freq$count.Freq, 0)
codon_freq$G1 = ifelse(substr(codon_freq$count.codons,1,1) == "G", codon_freq$count.Freq, 0)
codon_freq$C1 = ifelse(substr(codon_freq$count.codons,1,1) == "C", codon_freq$count.Freq, 0)

codon_freq$A2 = ifelse(substr(codon_freq$count.codons,2,2) == "A", codon_freq$count.Freq, 0)
codon_freq$T2 = ifelse(substr(codon_freq$count.codons,2,2) == "U", codon_freq$count.Freq, 0)
codon_freq$G2 = ifelse(substr(codon_freq$count.codons,2,2) == "G", codon_freq$count.Freq, 0)
codon_freq$C2 = ifelse(substr(codon_freq$count.codons,2,2) == "C", codon_freq$count.Freq, 0)

codon_freq$A3 = ifelse(substr(codon_freq$count.codons,3,3) == "A", codon_freq$count.Freq, 0)
codon_freq$T3 = ifelse(substr(codon_freq$count.codons,3,3) == "U", codon_freq$count.Freq, 0)
codon_freq$G3 = ifelse(substr(codon_freq$count.codons,3,3) == "G", codon_freq$count.Freq, 0)
codon_freq$C3 = ifelse(substr(codon_freq$count.codons,3,3) == "C", codon_freq$count.Freq, 0)


codon_freq = codon_freq[c("gene_name","count.codons","A1","T1","G1","C1","A2","T2","G2","C2","A3","T3","G3","C3")]
df_sum <- codon_freq %>%
  group_by(gene_name) %>%
  summarise(
    across(A1:C3, sum), # A1到C3所有列全部求和
    .groups = "drop"
  )
write.csv(df_sum, file = "03-Base_Sum.csv", row.names = FALSE)


df_freq <- df_sum %>%
  rowwise(gene_name) %>%
  mutate(
    # 第一位频率
    across(c(A1,T1,G1,C1), ~ .x / sum(c(A1,T1,G1,C1)), .names = "{.col}_f"),
    # 第二位频率
    across(c(A2,T2,G2,C2), ~ .x / sum(c(A2,T2,G2,C2)), .names = "{.col}_f"),
    # 第三位频率
    across(c(A3,T3,G3,C3), ~ .x / sum(c(A3,T3,G3,C3)), .names = "{.col}_f")
  ) %>%
  ungroup()%>%
  select(gene_name, ends_with("_f"))
df_freq$GC3 = df_freq$G3_f+df_freq$C3_f
df_freq$GC12 = (df_freq$G1_f+df_freq$C1_f+df_freq$G2_f+df_freq$C2_f)/2

write.csv(df_freq, file = "04-Base_Freq.csv", row.names = FALSE)

