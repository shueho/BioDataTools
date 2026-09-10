# 包安装
if (!requireNamespace("tidyverse", quietly = TRUE)) {
  install.packages("tidyverse")
}
if (!requireNamespace("dendextend", quietly = TRUE)) {
  install.packages("dendextend")
}
if (!requireNamespace("ggpubr", quietly = TRUE)) {
  install.packages("ggpubr")
}
if (!requireNamespace("patchwork", quietly = TRUE)) {
  install.packages("patchwork")
}

# if (!require("BiocManager", quietly = TRUE)) install.packages("BiocManager")
# BiocManager::install(c("ggtree", "treeio"), ask = FALSE)

library(tidyverse)
library(dendextend)
library(ggpubr)
library(ggtree)
library(treeio)
library(patchwork)

if (!exists("is.waive")) {
  is.waive <- function(x) inherits(x, "waiver")
}


# ==================== 参数配置 ====================
#setwd("你的工作目录")
featureFile <- "feature-table.tsv"
metadataFile <- "metadata.tsv"
groupCol <- 2
top_ <- 20          # 0=全部显示，正数取top个物种，其余合并为Other
taxa_choice <- 6    # 0=Domain,1=Kingdom,2=Phylum,3=Class,4=Order,5=Family,6=Genus,7=Species

tip_l <- 1.15  # 样本标签被截断增加该值
top_font_size <- 4  # 样本标签字号
color_branch_by_group <- TRUE  # 是否对样本上色
tree_main_color <- "#7995D8" # 树主干颜色
legend_text_size <- 8  # 图例字体大小


border_color <- "grey50"
group_palette <- c("#66C2A5", "#FC8D62", "#8DA0CB", "#E78AC3",
                   "#A6D854", "#FFD92F", "#E5C494", "#FDB462")
color_unclassified <- "#999999"
color_other <- "#CCCCCC"


# ==================== 参数字典 ====================
taxa_levels_all <- c("Domain", "Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species")
if (taxa_choice < 0 | taxa_choice > 7) stop("taxa_choice 必须为0-7")
plot_level <- taxa_levels_all[taxa_choice + 1]
# ==================== 创建输出目录 ====================
dir.create("01_split", showWarnings = FALSE)
dir.create("02_level", showWarnings = FALSE)
dir.create("03_group", showWarnings = FALSE)
dir.create("04_rel_sample", showWarnings = FALSE)
dir.create("05_rel_group", showWarnings = FALSE)
# ==================== 数据预处理 ====================
df <- read_tsv(featureFile, show_col_types = FALSE)
metadata <- read_tsv(metadataFile, show_col_types = FALSE)
sample_names <- metadata[[1]]
group_vec <- metadata[[groupCol]]
names(group_vec) <- sample_names
first_col <- colnames(df)[1]
df_split <- df %>%
  mutate(
    Domain = str_extract(get(first_col), "(?<=d__)[^;]+"),
    Kingdom = str_extract(get(first_col), "(?<=k__)[^;]+"),
    Phylum  = str_extract(get(first_col), "(?<=p__)[^;]+"),
    Class   = str_extract(get(first_col), "(?<=c__)[^;]+"),
    Order   = str_extract(get(first_col), "(?<=o__)[^;]+"),
    Family  = str_extract(get(first_col), "(?<=f__)[^;]+"),
    Genus   = str_extract(get(first_col), "(?<=g__)[^;]+"),
    Species = str_extract(get(first_col), "(?<=s__)[^;]+")
  ) %>%
  select(-!!sym(first_col)) %>%
  select(Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species, everything())
write_tsv(df_split, "01_split/01.feature-table_split.tsv")
sample_cols <- df_split %>%
  select(-Domain, -Kingdom, -Phylum, -Class, -Order, -Family, -Genus, -Species) %>%
  colnames()
taxa_levels <- c("Domain", "Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species")
# ==================== 生成各分类级别绝对丰度表 ====================
for (i in seq_along(taxa_levels)) {
  level <- taxa_levels[i]
  df_grouped <- df_split %>%
    group_by(!!sym(level)) %>%
    summarise(across(all_of(sample_cols), ~ sum(.x, na.rm = TRUE))) %>%
    ungroup() %>%
    mutate(!!sym(level) := if_else(is.na(!!sym(level)), "Unclassified", !!sym(level)))
  write_tsv(df_grouped, file.path("02_level", paste0("02-", i, "_", level, ".tsv")))
}
# ==================== 生成分组绝对丰度表 ====================
for (i in seq_along(taxa_levels)) {
  level <- taxa_levels[i]
  input_file <- file.path("02_level", paste0("02-", i, "_", level, ".tsv"))
  df_level <- read_tsv(input_file, show_col_types = FALSE)
  taxa_col <- colnames(df_level)[1]
  sample_cols <- colnames(df_level)[-1]
  missing <- setdiff(sample_cols, names(group_vec))
  if (length(missing) > 0) {
    stop("在 ", level, " 中以下样本在 metadata 中未找到: ", paste(missing, collapse = ", "))
  }
  mat <- df_level %>% column_to_rownames(var = taxa_col) %>% as.matrix()
  groups <- group_vec[sample_cols]
  grouped_mat <- t(rowsum(t(mat), group = groups, na.rm = TRUE))
  df_grouped <- as.data.frame(grouped_mat) %>% rownames_to_column(var = taxa_col)
  write_tsv(df_grouped, file.path("03_group", paste0("03-", i, "_", level, "_group.tsv")))
}
# ==================== 生成样本相对丰度表 ====================
for (i in seq_along(taxa_levels)) {
  level <- taxa_levels[i]
  input_file <- file.path("02_level", paste0("02-", i, "_", level, ".tsv"))
  df_abs <- read_tsv(input_file, show_col_types = FALSE)
  taxa_col <- colnames(df_abs)[1]
  mat <- df_abs %>% column_to_rownames(var = taxa_col) %>% as.matrix()
  rel_mat <- sweep(mat, 2, colSums(mat), FUN = "/")
  df_rel <- as.data.frame(rel_mat) %>% rownames_to_column(var = taxa_col)
  write_tsv(df_rel, file.path("04_rel_sample", paste0("04-", i, "_", level, "_rel_sample.tsv")))
}
# ==================== 生成分组相对丰度表 ====================
for (i in seq_along(taxa_levels)) {
  level <- taxa_levels[i]
  input_file <- file.path("03_group", paste0("03-", i, "_", level, "_group.tsv"))
  df_abs <- read_tsv(input_file, show_col_types = FALSE)
  taxa_col <- colnames(df_abs)[1]
  mat <- df_abs %>% column_to_rownames(var = taxa_col) %>% as.matrix()
  rel_mat <- sweep(mat, 2, colSums(mat), FUN = "/")
  df_rel <- as.data.frame(rel_mat) %>% rownames_to_column(var = taxa_col)
  write_tsv(df_rel, file.path("05_rel_group", paste0("05-", i, "_", level, "_group.tsv")))
}
# ==================== 绘图 ====================
level_idx <- match(plot_level, taxa_levels)
if (is.na(level_idx)) stop("plot_level 无效")
file_sample <- file.path("04_rel_sample", paste0("04-", level_idx, "_", plot_level, "_rel_sample.tsv"))
df_sample <- read_tsv(file_sample, show_col_types = FALSE)
taxa_col <- colnames(df_sample)[1]
df_long_sample <- df_sample %>%
  pivot_longer(cols = -all_of(taxa_col), names_to = "Sample", values_to = "RelAbundance") %>%
  rename(Taxon = !!sym(taxa_col))
taxon_sum_sample <- df_long_sample %>%
  group_by(Taxon) %>%
  summarise(Total = sum(RelAbundance)) %>%
  arrange(desc(Total))
normal_taxa_all <- taxon_sum_sample$Taxon[!taxon_sum_sample$Taxon %in% c("Other", "Unclassified")]
if (top_ > 0) {
  top_taxa <- normal_taxa_all[1:min(top_, length(normal_taxa_all))]
  df_long_sample <- df_long_sample %>%
    mutate(Taxon = case_when(
      Taxon %in% top_taxa ~ Taxon,
      Taxon == "Unclassified" ~ "Unclassified",
      TRUE ~ "Other"
    ))
} else {
  top_taxa <- normal_taxa_all
}
df_long_sample <- df_long_sample %>%
  left_join(tibble(Sample = names(group_vec), Group = group_vec), by = "Sample") %>%
  group_by(Sample, Group, Taxon) %>%
  summarise(RelAbundance = sum(RelAbundance), .groups = "drop")
mat_sample <- df_sample %>%
  column_to_rownames(var = taxa_col) %>%
  as.matrix()
dist_sample <- dist(t(mat_sample), method = "euclidean")
hc_sample <- hclust(dist_sample, method = "ward.D2")

tree <- ape::as.phylo(hc_sample)

dend <- as.dendrogram(hc_sample)
group_levels <- unique(group_vec)
group_color <- setNames(rep(group_palette, length.out = length(group_levels)), group_levels)
labels_colors(dend) <- group_color[group_vec[labels(dend)]]
if(color_branch_by_group){
  dend <- color_branches(dend, clusters = group_vec[labels(dend)], col = group_color)
}
pdf("06_sample_tree.pdf", width = 6, height = 10, family = "serif")
plot(dend, main = "Sample Hierarchical Clustering", horiz = TRUE)
legend("topright", legend = names(group_color), fill = group_color, bty = "n")
dev.off()

meta_tip <- enframe(group_vec, name = "label", value = "Group")
p_tree_data <- ggtree(tree)$data
max_tip_x <- max(p_tree_data$x)
x_upper <- max_tip_x * tip_l

p_tree <- ggtree(tree, layout = "rectangular") %<+% meta_tip +
  geom_tree(linewidth = 0.8, color = tree_main_color) +
  geom_tree(aes(color = Group), subset = isTip, linewidth = 0.8) +
  geom_tippoint(aes(color = Group), size = 2, show.legend = FALSE) +
  geom_tiplab(aes(color = Group), hjust = -0.3, size = top_font_size, offset = 0.01, show.legend = FALSE,family = "serif") +
  scale_color_manual(values = group_color, name = "Sample group", na.translate = FALSE) +
  guides(color = guide_legend(
    order = 1,
    override.aes = list(linetype = 1, linewidth = 0.8, shape = 19, size=3)
  )) +
  xlim(NA, x_upper)+ 
  theme_tree2() +
  theme(
    axis.title.y = element_blank(),
    axis.text.x = element_text(color = "black"),
    text = element_text(family = "serif", color = "black"),
    #panel.clip = "off"
  )

tip_data <- p_tree$data %>% filter(isTip == TRUE)
tip_order <- tip_data %>% arrange(y) %>% pull(label) %>% trimws()
taxon_order <- df_long_sample %>%
  group_by(Taxon) %>%
  summarise(Total = sum(RelAbundance)) %>%
  arrange(desc(Total)) %>%
  pull(Taxon)
normal <- setdiff(taxon_order, c("Other", "Unclassified"))
special <- if ("Other" %in% taxon_order) c("Unclassified", "Other") else "Unclassified"
taxon_order <- c(normal, special)
taxon_order <- unique(taxon_order)
df_long_sample$Taxon <- factor(df_long_sample$Taxon, levels = taxon_order)
df_long_sample$Sample <- factor(df_long_sample$Sample, levels = tip_order)
n_normal <- length(normal)
normal_colors <- rep(group_palette, length.out = n_normal)
color_vec <- c(normal_colors, "Unclassified" = color_unclassified)
if ("Other" %in% taxon_order) {
  color_vec <- c(color_vec, "Other" = color_other)
}
names(color_vec) <- taxon_order


p_bar_combine <- ggplot(df_long_sample, aes(x = RelAbundance, y = Sample, fill = Taxon)) +
  geom_col(position = "fill", width = 0.8, color = border_color, linewidth = 0.2) +
  scale_x_continuous(labels = scales::percent, expand = expansion(mult = c(0,0.05))) +
  scale_fill_manual(values = color_vec, name = plot_level) +
  guides(fill = guide_legend(order = 2),keyheight = unit(0.4, "cm"),) +
  labs(x = "Relative Abundance") +
  theme_bw() +
  theme(
    text = element_text(family = "serif"),
    axis.text.x = element_text(color = "black"),
    axis.text.y = element_blank(),
    axis.ticks.y = element_blank(),
    axis.title.y = element_blank(),
    panel.grid = element_blank(),
    legend.key.size = unit(0.3, "cm"),
    plot.margin = margin(2, 5, 2, 2)
  )
font_size_axis_title <- 12
font_size_axis_text  <- 10
p_bar_single <- ggplot(df_long_sample, aes(x = RelAbundance, y = Sample, fill = Taxon)) +
  geom_col(position = "fill", width = 0.8, color = border_color, linewidth = 0.2) +
  scale_x_continuous(labels = scales::percent, expand = expansion(mult = c(0,0.05))) +
  scale_fill_manual(values = color_vec) +
  labs(
    x = "Relative Abundance",
    y = "Sample",
    fill = plot_level
  ) +
  theme_bw() +
  theme(
    text = element_text(family = "serif"),
    axis.text.y = element_text(size = font_size_axis_text, hjust = 1, color = "black"),
    axis.text.x = element_text(size = font_size_axis_text, color = "black"),
    axis.title.y = element_text(size = font_size_axis_title, color = "black"),
    axis.title.x = element_text(size = font_size_axis_title, color = "black"),
    axis.ticks.y = element_line(),
    panel.grid = element_blank(),
    legend.key.size = unit(0.3, "cm"),
    plot.margin = margin(2, 5, 2, 2)
  )
ggsave("07_sample_barplot.pdf", p_bar_single + theme(legend.text = element_text(size = legend_text_size)), width = 8, height = 10)
p_combine <- p_tree + plot_spacer() + p_bar_combine +
  plot_layout(ncol = 3, widths = c(1.4, 0.05, 2), guides = "collect") &
  theme(legend.text = element_text(size = legend_text_size))
ggsave("08_combineplot.pdf", p_combine, width = 13, height = 10)

