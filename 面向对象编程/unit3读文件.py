f=open(r"D:\python练习\unit1打印部分.py","r",encoding="utf-8")#默认为读取模式
#print(f.read())#读取文件的全部内容，括号里加数字表示读取多少个字符
#print(f.readline())#读取文件的一行，括号里加数字表示读取多少个字符
lines=f.readlines()#读取文件的所有行并返回一个列表
for line in lines:
    print(line)
f.close()#关闭文件
