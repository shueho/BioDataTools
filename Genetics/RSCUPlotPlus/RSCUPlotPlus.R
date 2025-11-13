#!/usr/bin/env Rscript
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/11/13 17:50
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : RSCUPlotPlus.R
#
# Drawing of multi-species RSCU bar charts and statistical analysis of codon usage. 

packages <- c("seqinr", "ggplot2", "aplot", "dplyr", "tidyr")

cran_mirror <- "https://mirrors.tuna.tsinghua.edu.cn/CRAN/"
for (pkg in packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    cat("Installing package:", pkg, "\n")
    install.packages(pkg, dependencies = TRUE, repos = cran_mirror)
  }
}
invisible(lapply(packages, require, character.only = TRUE))

# ord = "order.txt"
# codonTable = 2
# gene = "Total"

library(seqinr)
library(ggplot2)
library(aplot)
library(dplyr)
library(tidyr)

get_name <- function (x) {
  x1 = sub("([^.]+)\\.[[:alnum:]]+$", "\\1", basename(x))
  x2 = sub(" ","_",x1)
  return(x2)
}
plot_rscu = function(rscu_d, out_path,h1=0.6,h2=6,yLim=6.2){
  colnames(rscu_d) = c("V1","V2","V3","V4")
  p1<-ggplot(rscu_d,
             aes(fill=as.character(V4),x=V2,y=V3))+
    geom_bar(position = "stack",
             stat="identity")+
    theme_bw()+
    scale_y_continuous(expand=c(0,0),
                       limits = c(0,yLim))+
    labs(y="RSCU",
         x="")+
    theme_classic()+
    theme(legend.position = "none",
          axis.text = element_text(family = "serif",size = 20),
          axis.title.y = element_text(family = "serif",size = 20),
          axis.text.x = element_text(margin = margin(t = 8)),
          axis.text.y = element_text(margin = margin(r = 8))
    )
  p2<-ggplot(rscu_d,
             aes(x=V2,y=V4))+
    geom_label(aes(label=V1,fill=as.character(V4)),
               size=5.5,
               family = "serif")+
    labs(x="",y="")+
    ylim(0,10)+
    theme_minimal()+
    theme(legend.position = "none",
          axis.text = element_blank(),
          axis.ticks = element_blank(),
          panel.grid = element_blank())

  p=insert_bottom(p1,p2,height = h1)
  ggsave(p,filename= out_path,width = 15,height = h2)
  #Saving 5.99 x 4.42 in image
}


main_fun_one = function(pcg,codonTable,gene="Total"){
  sam = get_name(pcg)
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
  write.csv(fasta_df, file = paste(sam, "_01-sequences.csv",sep=""), row.names = FALSE)
  
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
  write.csv(codon_freq, file = paste(sam, "_02-Codon_occurrence_in_all_gene.csv",sep=""), row.names = FALSE)
  
  # 03.获得所有PCGs，以及整体的密码子使用情况
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
  getCoutMatrix = function(con_num){
    #con_num = 2
    co_matrix = t(spread(codon_freq[c(1,2,3)], key = count.codons, value = count.Freq))
    new_colnames <- as.character(co_matrix[1,])
    co_matrix = data.frame(codon = rownames(co_matrix[-1,]), co_matrix[-1,])
    colnames(co_matrix) = c("codon",new_colnames)
    tem = data.frame(codon=generate_codon_list())
    co_matrix = merge(tem, co_matrix, by = "codon",all=TRUE)
    co_matrix[is.na(co_matrix)] <- 0
    co_matrix[, -1] <- lapply(co_matrix[, -1], as.numeric) 
    co_matrix$Total <- rowSums(co_matrix[, -1])
    co_matrix = merge(getCodonList(con_num), co_matrix, by = "codon",all=TRUE)
    co_matrix$codon = factor(co_matrix$codon,levels = generate_codon_list())
    co_matrix = co_matrix[order(co_matrix$codon),]
    return(co_matrix)
  }
  coMatrix = getCoutMatrix(codonTable)
  write.csv(coMatrix, file = paste(sam, "_03-Codon_occurrence_matrix.csv",sep=""), row.names = FALSE)
  
  # 04.获取RSCU矩阵
  RSCUMatrix <- coMatrix %>%
    group_by(AAA) %>%
    mutate(
      across(
        .cols = -c(1,2),
        .fns = list(
          result = ~ .x / sum(.x) * n()
        )
      )
    ) %>%
    ungroup()
  write.csv(RSCUMatrix, file = paste(sam, "_04-RSCU_matrix.csv",sep=""), row.names = FALSE)
  
  # 05.指定基因的密码子使用情况
  gene_RSCU = data.frame(RSCUMatrix[c("codon","A","AAA",gene,paste(gene,"_result",sep=""))])
  write.csv(gene_RSCU, file = paste(sam,"_05-",gene,"_RSCU.csv",sep=""), row.names = FALSE)
  
  # 06.导出绘图数据模板
  df = gene_RSCU[c(1,3,5)]
  df <- df[df$AAA != "Stp", ]
  df$flag <- NA
  df$flag[1] <- 8
  for (i in 2:nrow(df)) {
    if (df$AAA[i] == df$AAA[i-1]) {
      df$flag[i] <- df$flag[i-1] -2
    } else {
      df$flag[i] <- 8
    }
    if (df$flag[i] < 2) df$flag[i] <- 8
  }
  
  df <- df %>%
    group_by(AAA) %>%
    mutate(
      row_num = row_number(),
      AAA = ifelse(n() > 4 & row_num <= 4, paste0(AAA, "1"),
                   ifelse(n() > 4 & row_num > 4, paste0(AAA, "2"), AAA))
    ) %>%
    ungroup() %>%
    select(-row_num)
  write.csv(df, file = paste(sam,"_06-",gene,"_RSCU_plot_file.csv",sep=""), row.names = FALSE)
  
  # 07.默认参数绘制RSCU图
  plot_rscu(df,paste(sam,"_07-",gene,"_RSCU_plot.pdf",sep=""),yLim = ifelse(codonTable == 5, 8, 6.2))
  df$V5 = sam
  return(df)
}
main_fun = function(ord,codonTable,gene="Total",h1=0.6,h2=6,c="#FFFFFF"){
  yLim = ifelse(codonTable == 5, 8, 6.2)
  pcgs = readLines(ord)
  dfs = data.frame()
  w = 0.8/length(pcgs)
  f = 0
  for (pcg in pcgs) {
    df = main_fun_one(pcg,codonTable,gene="Total")
    colnames(df) = c("V1","V2","V3","V4","V5")
    df$V6 = match(df$V2,unique(df$V2)[order(unique(df$V2))])
    df$V7 = df$V6-0.4+w/2+f*w
    dfs=rbind(dfs,df)
    f=f+1
  }
  levels(dfs$V5) = unique(dfs$V5)
  write.csv(dfs, file = paste(gene,"_RSCU_plot_file.csv",sep=""), row.names = FALSE)

  p1<-ggplot(dfs,
             aes(fill=as.character(V4),x=V7,y=V3))+
    geom_bar(position = "stack",
             stat="identity",width=w,,colour = "#FFFFFF")+
    theme_bw()+
    scale_y_continuous(expand=c(0,0),
                       limits = c(0,yLim))+
    scale_x_continuous(breaks = seq(length(unique(df$V2))),labels = unique(df$V2)[order(unique(df$V2))])+
    labs(y="RSCU",
         x="")+
    theme_classic()+
    theme(legend.position = "none",
          axis.text = element_text(family = "serif",size = 20),
          axis.title.y = element_text(family = "serif",size = 20),
          axis.text.x = element_text(margin = margin(t = 8)),
          axis.text.y = element_text(margin = margin(r = 8)))
  p2<-ggplot(dfs,
             aes(x=V6,y=V4))+
    geom_label(aes(label=V1,fill=as.character(V4)),
               size=5.5,
               family = "serif")+
    labs(x="",y="")+
    ylim(0,10)+
    xlim(0.2,length(unique(df$V2))+0.2)+
    theme_minimal()+
    theme(legend.position = "none",
          axis.text = element_blank(),
          axis.ticks = element_blank(),
          panel.grid = element_blank())
  p=insert_bottom(p1,p2,height = h1)
  ggsave(p,filename= paste(gene,"_RSCU_plot.pdf",sep=""),width = 15,height = h2)
  #Saving 5.99 x 4.42 in image
  write.csv(levels(dfs$V5), file = "Bar_order.csv", row.names = FALSE)
  return(dfs)
}
print("示例：df = main_fun(ord,codonTable)")


