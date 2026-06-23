names=["Alice", "Bob", "Charlie", "David", "Eve"]
for i in range(len(names)):
    print(f" {names[i]},你好呀，欢迎来到Python的世界！我现在请你吃饭，快来吧！")

print(f"\n{names[1]}，因为今天工作繁忙，所以来不了\n")
names[1]="zxx"
for i in range(len(names)):
    print(f" {names[i]},你好呀，欢迎来到Python的世界！我现在请你吃饭，快来吧！")

print("\n炒股输了，心情不好，只能来两个人。\n")

while len(names)>2:
    removed_name=names.pop()
    print(f"很抱歉，{removed_name}，因为位置有限，所以不能请你吃饭了。\n")
for i in range(len(names)):
    print(f"\n{names[i]}，你还在名单上，欢迎来吃饭！")
while len(names)>0:
    removed_name=names.pop()
print("\n现在名单上没有人了。")