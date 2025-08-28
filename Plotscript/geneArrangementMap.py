#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Project : https://github.com/shueho/BioDataTools
# @Time    : 2023/8/4 21:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : GeneArrangementMap.py
#
# The linear arrangement of genes is distinguished according to different colors.

import sys
import os

print("Author: XueHao\nE-mail: studid@163.com")

HEAD = '''<svg version="1.1"
     baseProfile="full"
     width="3000" height="2000"
     xmlns="http://www.w3.org/2000/svg">\n'''

try:
    S = int(sys.argv[3]) #50
except:
    S = 50
COLOR = sys.argv[2]
with open(COLOR) as f:
    ls = f.readlines()
d = dict()
for i in ls:
    tem = i.strip().split("\t")
    for j in tem[1:]:
        d[j.strip()] = tem[0]

LIST = sys.argv[1]
with open(LIST) as f:
    ls = f.readlines()
ls = [i.strip().split("\t") for i in ls if i.strip()]


f = open("out.svg","w")
f.write(HEAD)
class Text:
    def __init__(self,x,y,string,f_size=25,fill="#000000",f="Times New Roman"):
        self.x = x
        self.y = y
        self.string = string
        self.f_size = f_size if len(string) < 3 else 20
        self.fill = fill
        self.f = f
    def pack(self):
        return '  <text x="{}" y="{}" font-size="{}" font-family="{}" text-anchor="middle" fill="{}">{}</text>'.format(self.x,self.y,self.f_size,self.f,self.fill,self.string)


class Rect:
    def __init__(self,x,y,fill,string="",width=60,height=40,stroke="#000000"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.string = string
    def pack(self):
        shape = '  <rect x="{}" y="{}" fill="{}" stroke="{}" width="{}" height="{}"/>\n'.format(self.x,self.y,self.fill,self.stroke,self.width,self.height)
        text = Text(self.x+self.width/2,self.y+3*self.height/4,self.string)
        return shape + text.pack() + "\n"

class Circle:
    def __init__(self,cx,cy,fill,string="",r=20,stroke="#000000"):
        self.cx = cx
        self.cy = cy
        self.fill = fill
        self.r = r
        self.stroke = stroke
        self.string = string
    def pack(self):
        shape = '  <circle cx="{}" cy="{}" fill="{}" r="{}" stroke="{}"/>\n'.format(self.cx,self.cy,self.fill,self.r,self.stroke)
        text = Text(self.cx,self.cy+self.r/2,self.string)
        return shape + text.pack() + "\n"



fx = 20
fy = 30
for i in ls:
    flag = None
    for j in i:
        #print(j)
        if not j:
            continue
        if j not in d:
            d[j] = "#ffffff"
        if len(j) == 1:
            if flag == 1:
                fx += 20
            tem = Circle(fx+20,fy+20,d[j],string=j)
            fx += 25
            flag = 1
        else:
            if flag == 2 or flag == None:
                fx -= 20
            tem = Rect(fx+20,fy,d[j],string=j)
            fx += 85        #fx += 80
            flag = 2
        f.write(tem.pack())
    fx = 20
    fy += S
    


f.write("</svg>")
f.close()

print("ok!")
