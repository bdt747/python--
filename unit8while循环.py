print("这是一个求平均数的程序")
user_input=input("请输入数字（输入exit退出）：")
total=0
count=0
while user_input!="exit":
    number=float(user_input)
    total+=number
    count+=1
    user_input=input("请输入数字（输入exit退出）：")
if count>0:
    print("平均数是：" + str(total/count))
else:
    print("没有输入任何数字")