import random

def 猜数字游戏():
    """经典的猜数字游戏"""
    print("=" * 40)
    print("🎯 欢迎来到猜数字游戏！")
    print("=" * 40)

    # 难度选择
    print("\n请选择难度：")
    print("1. 简单 (1-50，10次机会)")
    print("2. 中等 (1-100，7次机会)")
    print("3. 困难 (1-200，5次机会)")

    while True:
        try:
            难度 = int(input("\n请输入选项 (1/2/3): "))
            if 难度 == 1:
                最大值, 最大次数 = 50, 10
                break
            elif 难度 == 2:
                最大值, 最大次数 = 100, 7
                break
            elif 难度 == 3:
                最大值, 最大次数 = 200, 5
                break
            else:
                print("❌ 请输入1、2或3！")
        except ValueError:
            print("❌ 请输入有效的数字！")

    # 生成随机数
    目标数字 = random.randint(1, 最大值)
    已猜次数 = 0
    历史记录 = []

    print(f"\n🤔 我已经想好了一个 1~{最大值} 之间的数字，你有 {最大次数} 次机会！")

    while 已猜次数 < 最大次数:
        剩余次数 = 最大次数 - 已猜次数
        print(f"\n📊 剩余次数: {剩余次数}")

        try:
            猜测 = int(input("请输入你的猜测: "))
        except ValueError:
            print("❌ 请输入有效的整数！")
            continue

        # 检查范围
        if 猜测 < 1 or 猜测 > 最大值:
            print(f"⚠️ 数字必须在 1~{最大值} 之间！")
            continue

        已猜次数 += 1
        历史记录.append(猜测)

        if 猜测 == 目标数字:
            print(f"\n{'=' * 40}")
            print(f"🎉 恭喜你猜对了！答案就是 {目标数字}")
            print(f"✨ 你用了 {已猜次数} 次猜中")
            print(f"{'=' * 40}")
            break
        elif 猜测 < 目标数字:
            print("📈 太小了，再大一点！")
        else:
            print("📉 太大了，再小一点！")

        # 提示温度
        if 已猜次数 >= 2:
            差值 = abs(目标数字 - 猜测)
            if 差值 <= 5:
                print("🔥 非常接近了！")
            elif 差值 <= 15:
                print("🌤️ 比较接近了")
            elif 差值 <= 30:
                print("❄️ 还有点远")
    else:
        print(f"\n💔 很遗憾，机会用完了！答案是 {目标数字}")

    # 显示历史记录
    if 历史记录:
        print(f"\n📋 你的猜测记录: {历史记录}")

    # 再来一局
    print("\n" + "=" * 40)
    重玩 = input("🔄 再来一局？(y/n): ").strip().lower()
    if 重玩 == 'y' or 重玩 == 'yes':
        print()
        猜数字游戏()
    else:
        print("👋 感谢游玩，再见！")


if __name__ == "__main__":
    猜数字游戏()
