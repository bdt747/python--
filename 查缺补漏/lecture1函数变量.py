# print("hello,word")
# print("hello,word",end='    ')
# print('111')
# name=input("1123").strip().title()#删掉左右多余空格
# nnnn="1234l"
# print('he',name,nnnn,sep="1???")
# # sep 和 end命名参数
# print(f'hello,{name}')
# print('hello,'+str(name))
# first,last=name.split(' ')
# print(first,last)
# print(first)
# number_1 = float(input("请输入第一个数："))
# number_2 = float(input("请输入第二个数："))
# result = number_1 + number_2
# print((f"{result:.4f}\n") * 10)
# def main():
#     name=input('请输入你的名字：')
#     hello(name) # 定义函数里的变量并不能影响这个定义外
# def hello(to='word'):默认值是word
#     print('hello,',to)
# main()
def main():
    x = float(input('请输入第一个数：'))
    print('x 平方的值是',squard(x))
def squard(n):
    return n**2
main()