// ===================== 【功能配置区 - 仅在此增删分类/工具】 =====================
const toolConfig = [
    {
        categoryName: "核酸序列处理",
        categoryIcon: "🧬",
        tools: [
            {
                toolName: "GenBank特征提取",
                toolDesc: "支持上传GB文件/粘贴GB文本，提取基因、CDS、mRNA、内含子等特征序列",
                toolIcon: "images/001.png",
                link: "function/001.genbank_feat_extract.html"
            },
            {
                toolName: "核酸到氨基酸序列翻译",
                toolDesc: "将蛋白编码基因序列翻译为氨基酸序列",
                toolIcon: "images/005.png",
                link: "function/005.CDS_translate.html"
            },
            {
                toolName: "DNA/RNA/氨基酸序列拼接",
                toolDesc: "核酸（DNA/RNA）和蛋白质序列清洗拼接",
                toolIcon: "images/006.png",
                link: "function/006.Seq_concat.html"
            },
            {
                toolName: "待添加功能",
                toolDesc: "预留空位",
                toolIcon: "🌳",
                link: "tool_03.html"
            }
        ]
    },
    {
        categoryName: "统计分析",
        categoryIcon: "📐",
        tools: [
            {
                toolName: "RSCU计算工具",
                toolDesc: "相对同义密码子使用度计算",
                toolIcon: "images/002.png",
                link: "function/002.RSCU.html"
            },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module1_01.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module1_02.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module1_03.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module1_04.html" }
        ]
    },
    {
        categoryName: "绘图与美化",
        categoryIcon: "📈",
        tools: [
            { toolName: "RSCU柱形图绘制", toolDesc: "支持单序列/多基因/多物种RSCU柱形图绘制", toolIcon: "images/003.png", link: "function/003.RSCU_plot.html" },
            { toolName: "tRNA二级结构图美化组图工具", toolDesc: "对MITOS或ViennaRNA RNAplot输出的tRNA二级结构图进行美化", toolIcon: "images/004.png", link: "function/004.Trna_structure_beautifier.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module2_03.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module2_04.html" }
        ]
    },
    {
        categoryName: "其他",
        categoryIcon: "📋",
        tools: [
            { toolName: "线粒体基因组分析流程", toolDesc: "预留空位", toolIcon: "⚙️", link: "module2_01.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module2_02.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module2_03.html" },
            { toolName: "待添加功能", toolDesc: "预留空位", toolIcon: "⚙️", link: "module2_04.html" }
        ]
    }
];
// =============================================================================