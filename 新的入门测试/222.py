names=[ "Bob","Alice", "Charlie","Alice"]
print(names)
names.remove("Alice")
print(names)

# === 演示：如何核实列表是否为空 ===

# 方式1：利用布尔值（推荐）
empty_list = []
if not empty_list:
    print("方式1：列表是空的")

# 方式2：使用 len()
if len(empty_list) == 0:
    print("方式2：列表是空的")

# 方式3：直接比较
if empty_list == []:
    print("方式3：列表是空的")