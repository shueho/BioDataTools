
library(ggplot2)
library(patchwork)
df <- read.csv("PLOT.txt",header = T,sep = "\t")
genes = unique(df$GENE)


plotGC123 = function(gene){
  l = function(x){return(x)}
  tem = df[df$GENE==gene,]
  p=ggplot(tem,aes(x=GC3,y=GC12))+
    geom_point(aes(color=GROUP),size=1,alpha=0.8)+
    geom_smooth(method = "lm",formula = y~x, se=F,color="black",,size=0.5)+
    stat_function(fun=l,size=0.5,linetype="dashed")+
    xlim(0,1)+
    ylim(0,1)+labs(x="GC3",y="GC12")+theme_classic()+
    scale_color_manual(values = c("#DF536B","#6199C4","#29C7C7","#FDB462","#B276B2","#888888"))+
    annotate("text", x = 0.03, y = 0.97, label = gene, hjust = 0, vjust = 1, size = 5, family = "serif",fontface = "italic") +
    theme(text=element_text(size=10,family = "serif"))
  return(p)
}

ENC = function(x){
  return(2+x+29/(x^2+(1-x)^2))
}

plotENC = function(gene){
  tem = df[df$GENE==gene,]
  p=ggplot()+
    geom_point(data=tem,aes(x=GC3s,y=ENC,color=GROUP),size=1,alpha=0.8)+
    stat_function(fun=ENC,size=0.5)+
    scale_color_manual(values = c("#DF536B","#6199C4","#29C7C7","#FDB462","#B276B2","#888888"))+
    xlim(0,1)+
    ylim(0,70)+
    labs(x="GC3s",y="ENC")+theme_classic()+
    annotate("text", x = 0.03, y = 68, label = gene, hjust = 0, vjust = 1, size = 5, family = "serif",fontface = "italic") +
    theme(text=element_text(size=10,family = "serif"))
  return(p)
}

plotPR2=function(gene){
  tem = df[df$GENE==gene,]
  p=ggplot(tem,aes(x=G3/(G3+C3),y=A3/(A3+T3)))+
    geom_point(aes(color=GROUP),size=1,alpha=0.8)+
    xlim(0,1)+ylim(0,1)+labs(x="G3/(G3+C3)",y="A3/(A3+T3)")+theme_classic()+
    geom_hline(yintercept = 0.5,linetype="dashed",color="red")+
    geom_vline(xintercept = 0.5,linetype="dashed",color="red")+
    annotate("text", x = 0.03, y = 0.97, label = gene, hjust = 0, vjust = 1, size = 5, family = "serif",fontface = "italic") +
    #theme(legend.position = "none")+
    scale_color_manual(values = c("#DF536B","#6199C4","#29C7C7","#FDB462","#B276B2","#888888"))+
    theme(text=element_text(size=10,family = "serif"))
  return(p)
}
printsummary = function(gene){
  tem = df[df$GENE==gene,]
  m=lm(GC3~GC12,data=tem)
  summary(m)
  cor(df$GC12,df$GC3)
}

gene="cox1"
plotENC(gene) 
plotGC123(gene)
plotPR2(gene)


ENC_list <- lapply(genes, plotENC)
ENC_plot <- wrap_plots(ENC_list, ncol = 5, guides = "collect")

GC123_list <- lapply(genes, plotGC123)
GC123_plot <- wrap_plots(GC123_list, ncol = 5, guides = "collect")

PR2_list <- lapply(genes, plotPR2)
PR2_plot <- wrap_plots(PR2_list, ncol = 5, guides = "collect")

ggsave(ENC_plot,filename = "ENC_plot.pdf",width = 15,height = 8)
ggsave(GC123_plot,filename = "GC123_plot.pdf",width = 15,height = 8)
ggsave(PR2_plot,filename = "PR2_plot.pdf",width = 15,height = 8)


