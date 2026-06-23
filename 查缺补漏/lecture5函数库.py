#import 导入mod

#模拟抛硬币
'''import random

coin = random.choice(['heads','tails'])
#接受一个列表，以相等概率随即返回一个值
print(coin)
'''


'''
from random import choice
coin = choice(['heads','tails'])#不用再加random前缀
'''



#random.randint(a,b)生成a到b之间包括端点的随机整数
#random.shuffle(x)将列表x元素顺序打乱


#统计库 statistics
'''
statistics.mean(x)列表x元素求平均

'''

















#import sys

# try:
#     print('hello,my name is',sys.argv[1])
# except IndexError:
#     print('参数太少')




# 终端 python+文件名+输入元素 
#字符之间加空格会识别为两个元素，用引号就不会


# if len(sys.argv) < 2 :
#     print('元素太少了')
# elif len(sys.argv) > 2 :
#     print('元素有点多')
# else :
#     print('hello,my name is',sys.argv[1])
#sys.argv 可以被当作列表来使用


#条件语句 退出程序方式 sys.exit(返回数据)

# if len(sys.argv) < 2 :
#     sys.exit('元素太少了')
# elif len(sys.argv) > 2 :
#     sys.exit('元素有点多')

# print('hello,my name is',sys.argv[1])






# 列表切片
#for _ in _list[1:]        表示取列表元素从第2个开始到结尾，组成新列表
# numbers=[a**2 for a in range(1,11)]
# for _ in numbers[2:7]:     包括2，但不包括7
#     print(_)

























# package 第三方包


'''
import cowsay
import sys

if len(sys.argv)==2:
    cowsay.cow('hello,'+sys.argv[1])

#牛在说话
'''
# if len(sys.argv)==2:
#     cowsay.trex('hello,'+sys.argv[1])    恐龙在说话


