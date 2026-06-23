with open(r"D:\python练习\ceshi.txt","w",encoding="utf-8") as f:#使用with语句打开文件，自动关闭文件
    f.write("这是第一行\n")#写入文件内容，\n表示换行
    f.write("这是第二行\n")
    f.write("这是第三行\n")
with open(r"D:\python练习\ceshi.txt","a",encoding="utf-8") as f:
    f.write("这是追加的一行\n")#使用追加模式写入文件内容