// ========== 密码子表全局配置 & 工具函数 ==========
const TABLE_ID_NAME_MAP = {
    1:  "1 - 标准通用密码子表",
    2:  "2 - 脊椎动物线粒体密码子表",
    3:  "3 - 酵母线粒体密码子表",
    4:  "4 - 霉菌/原生动物/腔肠动物线粒体&支原体/螺原体密码子表",
    5:  "5 - 无脊椎动物线粒体密码子表",
    6:  "6 - 纤毛虫/松藻/六鞭毛虫核密码子表",
    9:  "9 - 棘皮动物/扁形动物线粒体密码子表",
    10: "10 - 游仆虫核密码子表",
    11: "11 - 细菌/古菌/植物质体密码子表",
    12: "12 - 替代酵母核密码子表",
    13: "13 - 海鞘线粒体密码子表",
    14: "14 - 替代扁形动物线粒体密码子表",
    15: "15 - 赭纤虫核密码子表",
    16: "16 - 绿藻线粒体密码子表",
    21: "21 - 吸虫线粒体密码子表",
    22: "22 - 斜生栅藻线粒体密码子表",
    23: "23 - 破囊壶菌线粒体密码子表"
};

const TABLE_ID_TYPE_MAP = {
    1: "standard",
    2: "transl_table=2",
    3: "transl_table=3",
    4: "transl_table=4",
    5: "transl_table=5",
    6: "transl_table=6",
    9: "transl_table=9",
    10: "transl_table=10",
    11: "transl_table=11",
    12: "transl_table=12",
    13: "transl_table=13",
    14: "transl_table=14",
    15: "transl_table=15",
    16: "transl_table=16",
    21: "transl_table=21",
    22: "transl_table=22",
    23: "transl_table=23"
};

const AA_ONE_TO_THREE = {
    "A":"Ala", "R":"Arg", "N":"Asn", "D":"Asp", "C":"Cys",
    "Q":"Gln", "E":"Glu", "G":"Gly", "H":"His", "I":"Ile",
    "L":"Leu", "K":"Lys", "M":"Met", "F":"Phe", "P":"Pro",
    "S":"Ser", "T":"Thr", "W":"Trp", "Y":"Tyr", "V":"Val",
    "TER":"TER"
};

function getTableName(tableId){
    return TABLE_ID_NAME_MAP[tableId] || "未知类型";
}

function getTableType(tableId){
    return TABLE_ID_TYPE_MAP[Number(tableId)] || "standard";
}

// 生成全部64个RNA密码子 (固定大写 U)
function getAll64Codons() {
    const bases = ["U","C","A","G"];
    const list = [];
    for(let b1 of bases)
        for(let b2 of bases)
            for(let b3 of bases)
                list.push(b1 + b2 + b3);
    return list;
}

function buildCodonMapFromRule(type) {
    const allCodons = getAll64Codons();
    const codonMap = {};

    if (typeof getGeneticCodeString !== "function") {
        allCodons.forEach(c => codonMap[c] = "UNK");
        return codonMap;
    }

    const ruleStr = getGeneticCodeString(type);
    if (!ruleStr || ruleStr === "true") {
        allCodons.forEach(c => codonMap[c] = "UNK");
        return codonMap;
    }

    const ruleList = ruleStr.replace(/\s+/g, "").split(",");
    allCodons.forEach(c => codonMap[c] = "UNK");

    for (const rule of ruleList) {
        if (!rule) continue;
        const eqIdx = rule.lastIndexOf("=");
        if (eqIdx <= 0) continue;

        const patternStr = rule.slice(0, eqIdx);
        let aaChar = rule.slice(eqIdx + 1);
        if (aaChar === "*") aaChar = "TER";

        if (patternStr.startsWith("/") && patternStr.endsWith("/")) {
            const regBody = patternStr.slice(1, -1);
            const reg = new RegExp(regBody, "i");

            for (const codon of allCodons) {
                const dnaLike = codon.replace(/U/g, "t");
                if (reg.test(dnaLike)) {
                    codonMap[codon] = aaChar;
                }
            }
        }
    }

    return codonMap;
}

function getCodonTable(tableId){
    const type = getTableType(tableId);
    return buildCodonMapFromRule(type);
}