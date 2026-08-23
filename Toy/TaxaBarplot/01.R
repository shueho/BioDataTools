if (!requireNamespace("tidyverse", quietly = TRUE)) {
  install.packages("tidyverse")
}
library(tidyverse)

# ==================== 参数配置 ====================
featureFile <- "feature-table.tsv"
metadataFile <- "metadata.tsv"
groupCol <- 2
top_ <- 20          # 0=全部显示，正整数=显示前N个，其余合并为"Other"

taxa_choice <- 6    # 分类等级选择：1=Kingdom, 2=Phylum, 3=Class, 4=Order, 5=Family, 6=Genus, 7=Species
sort_choice <- 1    # 排序方式：1=按最高丰度分类从小到大, 2=从大到小, 3=按分组, 4=层次聚类
border_color <- "grey50"   # 柱状图边框颜色

# 色板定义
set2_colors <- c("#66C2A5", "#FC8D62", "#8DA0CB", "#E78AC3",
                 "#A6D854", "#FFD92F", "#E5C494", "#FDB462")  
color_unclassified <- "#999999"   # Unclassified 固定颜色
color_other <- "#CCCCCC"         # Other 固定颜色

# ==================== 参数字典 ====================
taxa_levels_all <- c("Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species")
if (taxa_choice < 1 | taxa_choice > 7) stop("taxa_choice 必须为 1-7")
plot_level <- taxa_levels_all[taxa_choice]

sort_mode <- switch(as.character(sort_choice),
                    "1" = "top_taxon",
                    "2" = "top_taxon_desc",
                    "3" = "group",
                    "4" = "cluster",
                    stop("sort_choice 必须为 1-4"))

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
    Kingdom = str_extract(get(first_col), "(?<=d__)[^;]+"),
    Phylum  = str_extract(get(first_col), "(?<=p__)[^;]+"),
    Class   = str_extract(get(first_col), "(?<=c__)[^;]+"),
    Order   = str_extract(get(first_col), "(?<=o__)[^;]+"),
    Family  = str_extract(get(first_col), "(?<=f__)[^;]+"),
    Genus   = str_extract(get(first_col), "(?<=g__)[^;]+"),
    Species = str_extract(get(first_col), "(?<=s__)[^;]+")
  ) %>%
  select(-!!sym(first_col)) %>%
  select(Kingdom, Phylum, Class, Order, Family, Genus, Species, everything())
write_tsv(df_split, "01_split/01.feature-table_split.tsv")

sample_cols <- df_split %>%
  select(-Kingdom, -Phylum, -Class, -Order, -Family, -Genus, -Species) %>%
  colnames()

taxa_levels <- c("Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species")

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
  write_tsv(df_rel, file.path("05_rel_group", paste0("05-", i, "_", level, "_rel_group.tsv")))
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

if (sort_mode == "top_taxon") {
  top_taxon_name <- normal_taxa_all[1]
  taxon_abund <- df_sample %>%
    filter(!!sym(taxa_col) == top_taxon_name) %>%
    select(-!!sym(taxa_col)) %>%
    as.numeric()
  sample_order <- colnames(df_sample)[-1][order(taxon_abund)]
} else if (sort_mode == "top_taxon_desc") {
  top_taxon_name <- normal_taxa_all[1]
  taxon_abund <- df_sample %>%
    filter(!!sym(taxa_col) == top_taxon_name) %>%
    select(-!!sym(taxa_col)) %>%
    as.numeric()
  sample_order <- colnames(df_sample)[-1][order(taxon_abund, decreasing = TRUE)]
} else if (sort_mode == "cluster") {
  mat_sample <- df_sample %>%
    column_to_rownames(var = taxa_col) %>%
    as.matrix()
  dist_sample <- dist(t(mat_sample), method = "euclidean")
  hc_sample <- hclust(dist_sample, method = "ward.D2")
  sample_order <- hc_sample$labels[hc_sample$order]
} else {
  sample_order <- df_long_sample %>%
    distinct(Sample, Group) %>%
    arrange(Group, Sample) %>%
    pull(Sample)
}

df_long_sample <- df_long_sample %>%
  mutate(Sample = factor(Sample, levels = sample_order))

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

n_normal <- length(normal)
normal_colors <- if (n_normal <= length(set2_colors)) {
  set2_colors[1:n_normal]
} else {
  rep(set2_colors, length.out = n_normal)  # 循环
}
color_vec <- c(normal_colors, "Unclassified" = color_unclassified)
if ("Other" %in% taxon_order) {
  color_vec <- c(color_vec, "Other" = color_other)
}
names(color_vec) <- taxon_order

p_sample <- ggplot(df_long_sample, aes(x = Sample, y = RelAbundance, fill = Taxon)) +
  geom_bar(stat = "identity", position = "fill", width = 0.8, 
           color = border_color, linewidth = 0.2) +
  scale_y_continuous(labels = scales::percent, expand = expansion(mult = c(0, 0.05))) +
  scale_fill_manual(values = color_vec) +
  labs(x = "Sample", y = "Relative Abundance", fill = plot_level) +
  theme_bw() +
  theme(
    text = element_text(family = "serif"),
    axis.text = element_text(color = "black"),  
    axis.title = element_text(color = "black"),  
    axis.text.x = element_text(angle = 45, hjust = 1, size = 8, color = "black"),
    axis.ticks.x = element_line(),
    panel.grid = element_blank(),
    legend.text = element_text(size = 7),
    legend.key.size = unit(0.3, "cm"),
    plot.margin = margin(10, 10, 10, 10)
  ) +
  guides(fill = guide_legend(ncol = 1, reverse = FALSE))
ggsave("06_sample_barplot.pdf", p_sample, width = 12, height = 6)

file_group <- file.path("05_rel_group", paste0("05-", level_idx, "_", plot_level, "_rel_group.tsv"))
df_group <- read_tsv(file_group, show_col_types = FALSE)
taxa_col <- colnames(df_group)[1]

df_long_group <- df_group %>%
  pivot_longer(cols = -all_of(taxa_col), names_to = "Group", values_to = "RelAbundance") %>%
  rename(Taxon = !!sym(taxa_col))

if (top_ > 0) {
  df_long_group <- df_long_group %>%
    mutate(Taxon = case_when(
      Taxon %in% top_taxa ~ Taxon,
      Taxon == "Unclassified" ~ "Unclassified",
      TRUE ~ "Other"
    ))
}

df_long_group <- df_long_group %>%
  group_by(Group, Taxon) %>%
  summarise(RelAbundance = sum(RelAbundance), .groups = "drop")

if (sort_mode %in% c("top_taxon", "top_taxon_desc")) {
  top_taxon_name <- normal_taxa_all[1]
  taxon_abund_group <- df_group %>%
    filter(!!sym(taxa_col) == top_taxon_name) %>%
    select(-!!sym(taxa_col)) %>%
    as.numeric()
  if (sort_mode == "top_taxon") {
    group_order <- colnames(df_group)[-1][order(taxon_abund_group)]
  } else {
    group_order <- colnames(df_group)[-1][order(taxon_abund_group, decreasing = TRUE)]
  }
  df_long_group <- df_long_group %>%
    mutate(Group = factor(Group, levels = group_order))
} else if (sort_mode == "cluster") {
  mat_group <- df_group %>%
    column_to_rownames(var = taxa_col) %>%
    as.matrix()
  dist_group <- dist(t(mat_group), method = "euclidean")
  hc_group <- hclust(dist_group, method = "ward.D2")
  group_order <- hc_group$labels[hc_group$order]
  df_long_group <- df_long_group %>%
    mutate(Group = factor(Group, levels = group_order))
} else {
  group_order <- unique(df_long_group$Group)
  df_long_group <- df_long_group %>%
    mutate(Group = factor(Group, levels = group_order))
}

taxon_order_group <- df_long_group %>%
  group_by(Taxon) %>%
  summarise(Total = sum(RelAbundance)) %>%
  arrange(desc(Total)) %>%
  pull(Taxon)
normal_g <- setdiff(taxon_order_group, c("Other", "Unclassified"))
special_g <- if ("Other" %in% taxon_order_group) c("Unclassified", "Other") else "Unclassified"
taxon_order_group <- c(normal_g, special_g)
taxon_order_group <- unique(taxon_order_group)
df_long_group$Taxon <- factor(df_long_group$Taxon, levels = taxon_order_group)

color_vec_group <- color_vec[levels(df_long_group$Taxon)]

p_group <- ggplot(df_long_group, aes(x = Group, y = RelAbundance, fill = Taxon)) +
  geom_bar(stat = "identity", position = "fill", width = 0.6, 
           color = border_color, linewidth = 0.2) +
  scale_y_continuous(labels = scales::percent, expand = expansion(mult = c(0, 0.05))) +
  scale_fill_manual(values = color_vec_group) +
  labs(x = "Group", y = "Relative Abundance", fill = plot_level) +
  theme_bw() +
  theme(
    text = element_text(family = "serif"),
    axis.text = element_text(color = "black"),
    axis.title = element_text(color = "black"),
    panel.grid = element_blank(),
    legend.text = element_text(size = 7),
    legend.key.size = unit(0.3, "cm"),
    plot.margin = margin(10, 10, 10, 10)
  ) +
  guides(fill = guide_legend(ncol = 1, reverse = FALSE))
ggsave("07_group_barplot.pdf", p_group, width = 8, height = 5)