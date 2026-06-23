a=int(input("请输入一个数字（1或0）："))
if a==1 :
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(i)+"x"+str(j)+"="+str(i*j),end="\t")#end="\t"表示输出后不换行，使用制表符分隔
        print()#每行结束后换行
else:
    print("看来你不需要")