print("Hello, World!")#这是打印，文本内容注意加引号
print("zxx,i love you")
#字符串连接
print("qq: \"123456789\"")#反斜杠可以转义特殊字符
print('qq: "123456789"')#双引号在单引号包裹下不需要转义
print('qq: \'123456789\'')#单引号在单引号包裹下需要转义
print("qq: '123456\n789'")#换行符\n
print("qq: '123456\t789'")#制表符\t
print("""11111
22222
33333""")#三引号可以换行
my_love="18595112719"
print("zxx的电话号码是"+my_love)#字符串连接
my_ex=my_love
my_love="100000000"
print(my_ex,my_love)#字符串是不可变类型，修改后会创建一个新的字符串对象
import math
print(math.pi)#math模块中的pi常量
"""
这是一个多行注释
可以用来解释代码的功能
"""