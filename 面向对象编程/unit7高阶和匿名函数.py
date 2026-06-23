def caculate_area(radius):
    area = 3.14 * radius * radius
    return area
def calculate_circumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference
def caculate_and_print(radius):
    area = caculate_area(radius)
    circumference = calculate_circumference(radius)
    print(f"半径为 {radius} 的圆的面积是 {area:.2f}，周长是 {circumference:.2f}。")
radius = float(input("请输入圆的半径："))
print("正在计算...")
caculate_and_print(radius)