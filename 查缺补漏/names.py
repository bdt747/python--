'''

with open('name.txt','r') as flie_1:
    lines = flie_1.readlines() # 所有行,设为列表

for line in lines:
    print('hello,',line.rstrip())
'''


#省略版本，还可以省略r，这是隐含设定
# with open('name.txt','r') as flie_1:
#     for line in flie_1:
#         print('hello,',line.rstrip())






#对学生姓名排序
'''
names = []
with open('name.txt','r') as flie_1:
    for line in flie_1:
        names.append(line.rstrip())

for name in sorted(names,reverse=True):#默认False顺序排列
    print(f'hello,{name}')
'''













with open('names.csv') as aa:
    for line in aa:
        row = line.rstrip().split(',')
        print(f'{row[0]} is in {row[1]}')