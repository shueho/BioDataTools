#!/usr/bin/env Rscript
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/10/4 17:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : PiSlidingWindowPlot.R
#
# Script for plotting sliding window analysis of nucleotide variability in gene coding regions. 

if (!require(ggplot2)) install.packages("ggplot2")
if (!require(dplyr)) install.packages("dplyr")
library(ggplot2)
library(dplyr)

piPath = "example/Dnasp_result.txt"
regPath = "example/regions.txt"

data = read.csv(piPath,header = T,sep = "\t")
features = read.csv(regPath,header = T,sep = "\t")
features = features[order(features$start),]
x_max = round(max(data$Midpoint) / 1000) * 1000  # 可以自行设置横坐标最大值
y_max <- max(data$Pi) * 1.2  # 可以自行设置纵坐标最大值

features <- features %>%
  mutate(
    y_position = ifelse(row_number() %% 2 == 1, 0.93 * y_max, 0.89 * y_max),
    y_text = ifelse(row_number() %% 2 == 1, 0.96*y_max, 0.86 * y_max),
    end = ifelse(end>x_max,x_max,end)
  )  # 设置基因名称及及区间线条的纵坐标位置，修改时需要注意保证线条错落排布，且基因名称与线条位置统一。

rect_data <- features %>%
  mutate(
    ymin = y_position - 0.005 * y_max,
    ymax = y_position + 0.005 * y_max
  )  # 设置线条粗细

window_split <- strsplit(data$Window, "-")
data$Start <- as.numeric(sapply(window_split, `[`, 1))
data$End   <- as.numeric(sapply(window_split, `[`, 2))

p = ggplot() +
  geom_area(data=data, aes(x = Midpoint, y = Pi),
    fill = "#00BFFF", 
    alpha = 0.8
  ) +
  geom_line(data=data, aes(x = Midpoint, y = Pi),
    color = "#0000FF", 
    alpha = 0.8
  ) +
  geom_rect(
    data = rect_data,
    aes(xmin = start, xmax = end, ymin = ymin, ymax = ymax),
    fill = "black",  # 橙红色
    #alpha = 0.4,
    color = "white",
    linewidth = 0.5
  ) +
  geom_text(
    data = rect_data,
    aes(x = (start + end) / 2, y = y_text, label = FeatureName),
    size = 5,
    hjust = 0.5,
    color = "black",
    fontface = "italic",
    family="serif"
  ) +
  scale_x_continuous(
    breaks = seq(0, x_max, by = x_max/20),
    limits = c(0, x_max),
    expand = expansion(mult = c(0, 0.05))
  ) +
  scale_y_continuous(
    limits = c(0, y_max),
    expand = expansion(mult = 0)
  ) +
  labs(
    y = "Pi (Nucleotide Diversity)",
    x = "Nucleotide Position"
  ) +
  theme_classic()+
  theme(
    text = element_text(family = "serif"), 
    axis.text = element_text(family = "serif"),  
    axis.title = element_text(family = "serif") 
  )
p
ggsave("Pi.pdf",p,width = 10,height = 5)
