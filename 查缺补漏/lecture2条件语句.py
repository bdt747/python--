# x = int(input("what's x ? "))
# y = int(input("what's y ? "))
# # if x < y :
# #     print("x is less than y.")
# # elif y > x :
# #     print("x is less than y.")
# # else :
# #     print("x is equal y.")
# # 这样提问比全是if的流程要少。
# if x != y :
#     print('x 不等于 y')
# else :
#     print('x 等于 y')
# # or and = != <= >=
# if x%2 == 1 :
#     print(f'{x}是奇数')
# else :
#     print(f'{x}是偶数')



# def main():
#     x = int(input("what's x ?"))
#     if is_even(x):
#         print("even")
#     else:
#         print("odd")



# def is_even(x):
#     # if x % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     #return (x % 2 == 0)
#     return True if x % 2 == 0 else False
# main()





name = input("what's your name?")

match name:
    case "zxc" | "z" | "x":
        print("1")
    case "zxx":
        print("2")
    case "zq":
        print('3')
    case _:
        print('who?')