import os


print("Author: XueHao\nE-mail: studid@163.com")
print("begin")
ls = list(os.popen("find -name transposed_report.tsv"))
ls = [i.strip() for i in ls if i.strip()]

fi = open("sumarry.tsv","w")
with open(ls[0]) as f:
    tem = f.readlines()
    fi.write("sample_ID\t"+tem[0])

def get_one(path):
    with open(path) as f:
        tem = f.readlines()
    fi.write(i.split("/")[-2]+"\t"+tem[1])

for i in ls:
    get_one(i)

fi.close()
print("OK!")
