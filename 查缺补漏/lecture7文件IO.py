'''
# 一般三个列表输入输出，但是并没有保存
names = []

for _ in range(3):
    names.append (input("what's your name?"))

for name in sorted(names):
    print(f'hello,{name}')
'''

name = input("what's your name?")

with open('name.txt','a') as flie_1:
    flie_1.write(f'{name}\n')
    flie_1.close()
