try:
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    result = num1 / num2
except ValueError:
    print("输入无效，请确保输入的是整数。")
except ZeroDivisionError:
    print("错误：除数不能为零。")
except:
    print("发生了一个未知错误,请重新运行程序。")
else:
    print(f"{num1}除以{num2}的结果是：{result}")
finally:
    print("程序执行结束。")