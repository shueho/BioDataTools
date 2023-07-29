
import sys 
import os
print("Author: XueHao\nE-mail: studid@163.com\nplease wait!")
path = os.path.basename(sys.argv[1])
with open(path) as f:
	ls = f.readlines()

flag = 0
d = dict()
for i in ls:
	if ">" in i:
		flag += 1
		key_ = ">N_{:0>16} ".format(flag) + " ".join(i.strip().split(" ")[1:])
		d[key_] = ""
	else:
		d[key_] += i.strip()
f = open("out_"+path,"w")
for i in d:
	f.write(i+"\n"+d[i]+"\n")

f.close()
print("ok!")
