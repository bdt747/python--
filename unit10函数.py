#不要重复原则
def calculate(a,b):
    sector_area=a*b
    return sector_area
print(calculate(5,10))

def BMI(weight,height):
    bmi=weight/(height**2)
    print("有点胖了兄弟")
    return bmi
weight=float(input("请输入体重（kg）："))
height=float(input("请输入身高（m）："))

BMI(weight,height)