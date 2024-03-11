#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2023/8/3 22:00
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : MergeTable.py
#
# Merge the tables. 

import tkinter as tk
import time
from tkinter import filedialog

def p_E(text):
    try:
        f = open("error.log")
    except:
        f = open("error.log","w")
    f.close()
    with open("error.log","a") as f:
        f.write(str(time.time())+str(text)+"\n")
        
def readTsv(filepath): #file -> dataframe
    with open(filepath) as f:
        tem = f.readlines()
    if "\t" in tem[0]:
        tem = [i.strip("\n").strip(" ").split("\t") for i in tem]
    else:
        tem = [i.strip("\n").strip(" ").split(",") for i in tem]
    frame = []
    for i in tem:
        if len(i) == len(tem[0]):
            frame.append(i)
        else:
            #print(i)
            p_E("\tLost data\t"+str(i))
    for row in range(len(frame)):
        for col in range(len(frame[row])):
            if not frame[row][col]:
                frame[row][col] = "-"
    return frame

def itemList(frame_lis,index_lis=[]): #read sample
    if len(frame_lis) != len(index_lis):
        index_lis = len(frame_lis)*[0]
    se = set()
    for i in range(len(frame_lis)):
        for j in range(len(frame_lis[i])):
            if j != 0:
                se.add(frame_lis[i][j][index_lis[i]])
    return list(se)

def traitList(frame_lis,index_lis=[]):#read trait
    if len(frame_lis) != len(index_lis):
        index_lis = len(frame_lis)*[0]
    ls = ["fid"]
    for i in range(len(frame_lis)):
        frame_lis[i][0].pop(index_lis[i])
        ls += (frame_lis[i][0])
    return ls

def frameFix(frame,index=0, tab_index=0):#read table info
    frame.pop(tab_index)
    d = {}
    for i in frame:
        fid = i.pop(index)
        d[fid] = i
    return d
    
def mergeFrame(frame_1, frame_2, index_1=0, index_2=0):
    len_1 = len(frame_1[0])-1
    len_2 = len(frame_2[0])-1
    itemlist = itemList([frame_1, frame_2],[index_1, index_2])
    traitlist = traitList([frame_1, frame_2],[index_1, index_2])
    d_1 = frameFix(frame_1,index_1, tab_index=0)
    d_2 = frameFix(frame_2,index_2, tab_index=0)
    frame = [traitlist]
    for i in itemlist:
        lis_1 = []
        try:
            lis_1 += d_1[i]
        except:
            lis_1 += ["-"]*len_1
        lis_2 = []
        try:
            lis_2 += d_2[i]
        except:
            lis_2 += ["-"]*len_2
        lis = [i]+lis_1+lis_2
        frame.append(lis)
    return frame


def printFrame(frame):
    with open("merge.txt","w") as f:
        for i in frame:
            f.write("\t".join(i)+"\n")
            
def main():
    global file_list
    for i in range(len(file_list)-1):
        try:
            try:
                f = open("merge.txt")
                frame_1 = readTsv("merge.txt")
                f.close()
            except:
                frame_1 = readTsv(file_list[i])
            frame_2 = readTsv(file_list[i+1])
            tem = mergeFrame(frame_1, frame_2)
            printFrame(tem)
        except:
            print(file_list[i]+" can not merge ")
            p_E("\t"+file_list[i]+" can not merge ")
            break
    print("finish!")
        
def inputfile():
    global file_list
    try:
        filepathes = filedialog.askopenfilenames()
        for i in filepathes:
            infilenames.insert("end",i+"\n")
        file_list += filepathes
    except:
        infilenames.insert("end","")
        file_list += ()

window = tk.Tk()
window.title("TableMerge v0.0.1")
window.geometry("600x300+600+300")
window.resizable(0,0)
lab_1 = tk.Label(window,text="Input file：",font=(None,15))
lab_1.grid(row=0,column=0)
    
file_list = ()
but_1 = tk.Button(window,text="Open",font=(None,15),command=inputfile)
but_1.grid(row=1,column=0)

infilenames = tk.Text(window,font=(None,10),height=10,width=40)
infilenames.grid(row=1,column=1)

but_2 = tk.Button(window,text="Merge!",font=(None,15),command=main)
but_2.grid(row=1,column=2)

L1 = tk.Label(window, text="\n\nAuthor: Hao Xue\nE-mail: studid@163.com")
L1.grid(row=2,column=1)
window.mainloop()

