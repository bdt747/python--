# while True :
#     print('meow \n'*3,end="")
# i = 0
# while i < 3:
#     print('meow')
#     i+=1
# for _ in [0,1,2]:#用下划线表示变量名并不重要
#     print('meow')
# for _ in range(3):
#     print('meow')
# print("meow\n"*3,end='')

#输入n，得到n次喵喵叫
# while True:
#     n=int(input("what's n?"))
#     if n<0 :
#         continue
#     else :
#         break
#     #if n>0:
#         #break
# for _ in range(n):
#     print('meow')




#函数调用输出喵
# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         x = int(input("请输入喵的次数："))
#         if x > 0:
#             return x

# def meow(n):
#     for _ in range(n):
#         print('meow')

# main()








#利用for循环逐步打印学生列表中的名字
# students = ['A','B','C']
# for student in students:
#     print(student)




#利用len函数搭配上述for循环
# students = ['A','B','C']
# for student in range(len(students)):
#     print(student+1,students[student])




#字典结构  键：值
# students={
#     'A':1,
#     'B':2,
#     'C':3,
#这样换行让数据变得明显
# print(students['A'])
# print(students['B'])
# print(students['C'])


# for student in students:
#     print(student)#遍历所有的键
#     print(student,students[student])#遍历所有键值




#列表搭配字典存储信息
# students = [
#     {'name':'zxx','phone':'123'},
#     {'name':'zq','phone':'234'}
# ]

# for student in students:
#     print(student['name'],student['phone'],sep=',')



# def main():
#     number = int(input("打印多少砖块："))
#     print("#\n"*number,end="")
# main()

















#循环嵌套
def main():
    kuan = int(input('请输入打印宽度：'))
    chang = int(input('请输入打印长度：'))
    changkuan(kuan,chang)

def changkuan(i,j):
    for _ in range(i):
        for _ in range(j):
            print("#",end="")
        print()

main()