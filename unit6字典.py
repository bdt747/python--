contacts={1:"Alice",2:"Bob",3:"Charlie"}#键是唯一的，不能存在重复的键
print(contacts[1])#输出联系人1的名字
contacts[4]="David"#添加联系人4
print(contacts)
del contacts[2]#删除联系人2
print(contacts)
contacts[3]="Eve"#修改联系人3的名字为Eve
print(contacts)
print(len(contacts))#输出联系人字典的长度
print(contacts.keys())#输出联系人字典的所有键
print(contacts.values())#输出联系人字典的所有值
print(contacts.items())#输出联系人字典的所有键值对
print(1 in contacts)#判断联系人1是否在字典中
print(contacts.get(2,"联系人不存在"))#获取联系人2的名字，如果不存在则返回"联系人不存在"