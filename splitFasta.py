import sys
import os
print("Author: XueHao\nE-mail: studid@163.com\nplease wait!")

fastaFile = sys.argv[1]
splitNum = int(sys.argv[2])
path = os.path.basename(fastaFile)
print("READ sequence!")
with open(fastaFile) as f:
	ls = f.readlines()

print("LOAD sequence number!")
seqNum = 0
for i in ls:
	if ">" in i:
		seqNum += 1

print("sequence number: " + str(seqNum))

newNum = seqNum // splitNum
print(newNum)

flag = 0
fp = 0
for i in ls:
	if ">" == i[0]:
		flag += 1
		if flag % newNum - 1 == 0:
			if fp:
				#f.write(tem)
				flag = 1
				f.close()
			fp += 1
			print("process: " + str(fp))
			f = open(str(fp) + "_" + path, "w")
			#tem = ""
	#tem += i
	f.write(i)

	
f.close()
print("ok!")
