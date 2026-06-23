#避免用户输入导致的语法错误

# while True:
#     try:
#         x = int(input("what's x? ")) # 如果值错误，等号不会被执行
#         break
#     except ValueError :
#         print('输入的不是整数。')

# print(f'x is {x}')




#try except else标准例子
# try:
#     x = int(input("what's x? "))
# except ValueError :
#     print('x is not an integer')
# else: # try成功执行才会执行这个
#     print(f'x is {x}')













#嵌套函数
'''
def main():
    x = get_int("what's x? ")
    print(f'x is {x}')

def get_int(prompt): # 这种函数更实用
    while True:
        try:
            x = int(input(prompt)) # 如果值错误，等号不会被执行
            return x
            #return int(input(prompt))也可以这样，但相对来说看起来不简洁
        except ValueError :
            print('输入的不是整数。')
            #pass 只是“什么也不做”的占位语句

main()
'''
