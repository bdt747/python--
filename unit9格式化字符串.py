message_content = """2026年新春佳节到，福气满门绕！
愿你在新的{0}年里：
身体健健康康，活力满满；
事业步步高升，再创辉煌；
财运亨通兴旺，好运连连；
心情阳光灿烂，笑口常开。

旧岁已展千重锦，新年再进百尺竿。
祝阖家欢乐，万事如意，新年大吉！ 🧧🎊

—— {1} 敬贺""".format("马", "张三")
print(message_content)
gpa_dict = {"语文": 85, "数学": 90, "英语": 88, "体育": 92}
for subject, score in gpa_dict.items():
    print("科目: {0}, 成绩: {1:.2f}".format(subject, score))