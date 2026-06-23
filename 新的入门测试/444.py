for i in range(1,20,2):
    print(i)
for j in range(3,31,3):
    print(j)
a=[]
for k in range(1,11):
    a.append(k**3)
    print(k**3)
print(a)
b=[k**3 for k in range(1,11)]
print(b)