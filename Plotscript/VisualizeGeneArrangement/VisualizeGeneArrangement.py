#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2025/10/17 21:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : VisualizeGeneArrangement.py
#
# A visualization of gene arrangement showing coding direction and missing genes.

import sys
import os

COLOR = sys.argv[2]
GENE = sys.argv[1]
gap_g = int(sys.argv[3]) # 2
gap_y = int(sys.argv[4]) # 20
HW = sys.argv[5] if len(sys.argv) == 6 else "30,60,18"
HW = HW.split(",")
H = int(HW[0])
W1 = int(HW[1])
W2 = int(HW[2])

X = 100
Y = 100
def create_and_save_svg(body_content, filename="output.svg", width="100%", height="100%", viewBox="0 0 5000 1000"):
    svg_template = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{viewBox}">
{body_content}
</svg>'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_template)

def parse_color_table(file_path):
    color_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue 
            parts = line.strip().split('\t')
            if len(parts) < 2:
                continue
            color = parts[0].strip()
            flag = parts[1].strip()
            for gene in parts[2:]:
                gene = gene.strip()
                if gene:  
                    color_dict[gene] = (color, flag)
                    
    return color_dict
cd = parse_color_table(COLOR)

def generate_gene(text, x, y, miss=False):
    dash_ = "5,1" if miss else "none"  # 虚化边框
    flag = cd.get(text, ['#FFFFFF',3])[1]
    height = H
    width = W1 if flag == '3' else W2
    font_size = 20 if flag not in '24' else 15  
    font_style = "italic" if flag in ['3', '4'] else "normal"
    color = '#FFFFFF' if miss else cd.get(text, ['#FFFFFF'])[0]
    text_x = x + width/2
    text_y = y + height/2
    if flag in ['1', '3']:  
        transform_attr = ""
    else:  
        transform_attr = f' transform="rotate(-90, {x + width/2}, {y + height/2})"'
    
    svg_content = f'''  <rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" stroke="black" stroke-width="1" stroke-dasharray="{dash_}"/>
  <text x="{text_x}" y="{text_y}" font-size="{font_size}" font-family="Times New Roman" dy="0.35em" text-anchor="middle" font-weight="bold" font-style="{font_style}"{transform_attr}>{text}</text>\n'''
    return svg_content, width

def getStrain(lis):
    g = dict() 
    for i in lis:
        s,m,c = 0,0,0
        for j in i:
            if j not in "!:- ":
                g[i[i.find(j):].strip().replace(" ","")] = [s,m,c]
                break
            if j == "-":
                s = 1
            if j == ":":
                m = 1
            if j == "!":
                c = 1
    return g

def generate_gene_list(dic, y):
    X_ = X
    text = ""
    for i in dic:
        #print(i)
        if dic[i][2]:
            text += f'''  <text x="{X_+len(i)*13/2}" y="{y+H+(dic[i][0]-0.5)*20}" font-size="20" font-family="Times New Roman" font-weight="bold" dy="0.35em" fill="blue" text-anchor="middle" font-style="normal">{i}</text>
  <line x1="{X_}" y1="{y+H}" x2="{X_+len(i)*13}" y2="{y+H}" stroke="black" stroke-width="1" />'''
            X_ += len(i)*13+gap_g
            continue
        tem = generate_gene(i,X_,y+dic[i][0]*H,miss=dic[i][1])
        text += tem[0]
        X_ += tem[1]+gap_g
    return text

svg = ""
with open(GENE) as f:
    gs = f.readlines()
gs = [i.strip().split("\t") for i in gs if i.strip()]
Y_ = Y
for i in gs:
    if i[0][0] == "#":
        svg += f'''  <text x="{X}" y="{Y_}" font-size="30" font-family="Times New Roman" dy="0.35em" text-anchor="start" font-weight="bold" font-style="normal">{i[0].lstrip("#")}</text>\n'''
        #Y_ += 5 if i[0] == "#" else 30
        Y_ += H
    else:
        svg += f'''  <text x="{X}" y="{Y_}" font-size="25" font-family="Times New Roman" dy="0.35em" text-anchor="start" font-style="italic">{i[0]}</text>\n'''
        tem = getStrain(i[1:])
        Y_ += H*2/3
        svg += generate_gene_list(tem,Y_)
        Y_ += H*2 + gap_y
create_and_save_svg(svg)
