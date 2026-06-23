# """石头剪刀布小游戏 - 与电脑对战！"""
# import random

# choices = ["石头", "剪刀", "布"]
# player_score = 0
# computer_score = 0
# rounds = 0

# print("🎮 欢迎来到石头剪刀布游戏！")
# print("=" * 35)
# print("输入 0 退出游戏\n")

# while True:
#     # 玩家出拳
#     print("请出拳：1.石头  2.剪刀  3.布")
#     try:
#         player_input = input("你的选择 (1-3): ")
#     except EOFError:
#         break
    
#     if player_input == "0":
#         break
    
#     if player_input not in ["1", "2", "3"]:
#         print("❌ 输入无效，请输入 1、2 或 3\n")
#         continue
    
#     player_choice = choices[int(player_input) - 1]
#     computer_choice = random.choice(choices)
    
#     print(f"\n你出了：{player_choice}")
#     print(f"电脑出了：{computer_choice}")
    
#     # 判断胜负
#     if player_choice == computer_choice:
#         print("🤝 平局！")
#     elif (player_choice == "石头" and computer_choice == "剪刀") or \
#          (player_choice == "剪刀" and computer_choice == "布") or \
#          (player_choice == "布" and computer_choice == "石头"):
#         print("🎉 你赢了！")
#         player_score += 1
#     else:
#         print("💻 电脑赢了！")
#         computer_score += 1
    
#     rounds += 1
#     print(f"📊 当前比分：你 {player_score} - {computer_score} 电脑 (第 {rounds} 轮)\n")

# # 最终结果
# print("\n" + "=" * 35)
# print("🏁 游戏结束！")
# print(f"总轮数：{rounds}")
# print(f"最终比分：你 {player_score} - {computer_score} 电脑")
# if player_score > computer_score:
#     print("🎊 恭喜你获得最终胜利！")
# elif player_score < computer_score:
#     print("😅 电脑获胜，再接再厉！")
# else:
#     print("🤝 平局收场！")
